#!/usr/bin/env python

import sys, csv

OUTPUT_FIELD_NAMES = ['NUM', 'LAST', 'FIRST', 'INITIAL', 'ADDRESS', 'CITY', 'POSTAL CODE',
                      'First Name Only', 'POSTAL FIX', 'moved']

def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: {} mailing_file voters_file output_file".format(sys.argv[0]))
        
    mailing_filename = sys.argv[1]
    voters_filename = sys.argv[2]
    output_filename = sys.argv[3]

    with open(mailing_filename) as mailing_file, \
         open(voters_filename) as voters_file, \
         open(output_filename, 'w') as output_file:

        mailing_csv = csv.DictReader(mailing_file)
        voters_csv = csv.DictReader(voters_file)
        output_csv = csv.DictWriter(output_file, OUTPUT_FIELD_NAMES)

        output_csv.writeheader()

        for mailing_row in mailing_csv:
            for voters_row in voters_csv:
                cmp = compare_names(mailing_row, voters_row)
                if cmp == 1:
                    next
                elif cmp == 0:
                    new_address = address_to_use(mailing_row, voters_row)
                    if new_address is not None:
                        output_csv.writerow(new_address)
                    break
                elif cmp == -1: # not in list
                    break

# below, row1 is from mailing_file, row2 is from voters_file
                            
def compare_names(row1, row2):
    name1 = row1['LAST'] + row1['FIRST']
    name2 = row2['Last Name'] + row2['First Name']
    if name1 < name2:
        return -1
    elif name1 > name2:
        return 1
    else:
        return 0

def address_to_use(row1, row2):
    if addresses_eq(row1, row2):
        row1.update({
            'moved': '0'
        })
        return row1
    else:
        if in_langley_p(row2):
            return voter_to_mailing(row1, row2)
        else:
            return None

def voter_to_mailing(row1, row2):
    row1.update({
        'ADDRESS': row2['Address'],
        'CITY': row2['City'].split(',')[0],
        'POSTAL CODE': row2['Postal'],
        'POSTAL FIX': "{} {}".format(row2['Postal'][0:3], row2['Postal'][3:7]),
        'First Name Only': row2['First Name'].split()[0],
        'moved': '1'
    })
    return row1
        
def addresses_eq(row1, row2):
    return row1['ADDRESS'] == row2['Address']

def in_langley_p(row2):
    return 'LANGLEY' in row2['City']

# row could be either from mailing_file or voters_file
def printable_row(row):
    if 'FIRST' in row:
        return ", ".join((row['FIRST'], row['LAST'], row['ADDRESS'], row['CITY'], row['moved']))
    else:
        return ", ".join((row['First Name'], row['Last Name'], row['Address'], row['City']))

if __name__ == "__main__":
    main()
