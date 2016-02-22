# Langley Voters List Scripts

## Langley Voters Mailing List Updater

This script updates a mailing list of Langley voters with information from a voters list.

The output is the same list of people from the mailing list, with the following changes:

1. If a person is not in the voters list, don't include them.

2. If a person has an updated Langley address in the voters list, include them with the updated address.

3. If a person has an updated non-Langley address in the voters list, don't include them.

### File Formats

The lists are in CSV format. The columns for the mailing list are:

    NUM,LAST,FIRST,INITIAL,ADDRESS,CITY,POSTAL CODE,First Name Only,POSTAL FIX

The columns for the voters list are:

    Voter #,Last Name,First Name,Address,City,Postal

The columns for the output list are the same as for the mailing list, with the addition of a "moved" column denoting whether the person had moved (within Langley).

## Langley Voters Phone List Updater

This script takes a voters list and a phone list, and returns a list of the phone numbers of people who are in the voters list.

The script respects the do-not-call columns in the phone list.

### File Formats

The lists are in CSV format. The columns for the voters list are the same as above:

    Voter #,Last Name,First Name,Address,City,Postal

The phone list is in NationBuilders format, but the script only uses these columns:

    full_name, phone_number, work_phone_number, mobile_number

The output is sent to stdout, and has the following columns:

    First Name, Last Name, full_name, phone_number, work_phone_number, mobile_number
