#!/usr/bin/env python

import sys, csv, operator

OUTPUT_FIELD_NAMES = ['First Name', 'Last Name', 'full_name', 'phone_number', 'work_phone_number', 'mobile_number']

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: {} phone_file voters_file".format(sys.argv[0]))
        
    phone_filename = sys.argv[1]
    voters_filename = sys.argv[2]

    with open(phone_filename) as phone_file, \
         open(voters_filename) as voters_file:

        phone_csv = csv.DictReader(phone_file)
        voters_csv = csv.DictReader(voters_file)
        output_csv = csv.DictWriter(sys.stdout, OUTPUT_FIELD_NAMES)

        output_csv.writeheader()

        sorted_phone_csv = sorted(phone_csv, key=operator.itemgetter('last_name', 'first_name'))

        for phone_row in sorted_phone_csv:
            for voters_row in voters_csv:
                cmp = compare_names(phone_row, voters_row)
                if cmp == 1:
                    next
                elif cmp == 0:
                    phones = get_allowed_phone_numbers(phone_row)
                    if phones:
                        voters_row.update(phones)
                        output_row = {k:voters_row[k] for k in OUTPUT_FIELD_NAMES}
                        output_csv.writerow(output_row)
                    break
                elif cmp == -1: # not in list
                    break

# below, row1 is from phone_file, row2 is from voters_file

def get_allowed_phone_numbers(row1):
    if row1['do_not_call'] == 'TRUE' or row1['do_not_contact'] == 'TRUE' or row1['federal_donotcall'] == 'TRUE':
        return None

    result = {k:row1[k] for k in OUTPUT_FIELD_NAMES if k in row1}
    if row1['mobile_opt_in'] == 'FALSE' or row1['is_mobile_bad'] == 'TRUE':
        result['mobile_number'] = ''
    if not result['phone_number'] and not result['work_phone_number'] and not result['mobile_number']:
        return None

    return result

def compare_names(row1, row2):
    name1 = row1['last_name'].lower() + next(iter(row1['first_name'].lower().split()), '')
    name2 = row2['Last Name'].lower() + next(iter(row2['First Name'].lower().split()), '')
    if name1 < name2:
        return -1
    elif name1 > name2:
        return 1
    else:
        return 0

# row could be either from phone_file or voters_file
def printable_row(row):
    if 'first_name' in row:
        return ", ".join((row['first_name'], row['last_name'] ))
    else:
        return ", ".join((row['First Name'], row['Last Name']))

if __name__ == "__main__":
    main()
