# Langley Voters Mailing List Updater

This script updates a mailing list of Langley voters with information from a voters list.

The output is the same list of people from the mailing list, with the following changes:

1. If a person is not in the voters list, don't include them.

2. If a person has an updated Langley address in the voters list, include them with the updated address.

3. If a person has an updated non-Langley address in the voters list, don't include them.

## File Formats

The lists are in CSV format. The columns for the mailing list are:

    NUM,LAST,FIRST,INITIAL,ADDRESS,CITY,POSTAL CODE,First Name Only,POSTAL FIX

The columns for the voters list are:

    Voter #,Last Name,First Name,Address,City,Postal

The columns for the output list are the same as for the mailing list, with the addition of a "moved" column denoting whether the person had moved (within Langley).
