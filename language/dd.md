A CSV Data Cleaner is a program that reads a CSV file, checks the data for errors or inconsistencies, and cleans it up so it can be used properly.

For example, imagine a CSV file containing expense records with missing amounts, duplicate entries, or inconsistent category names.

The program would work like this:

1. CSV: Read data from a `.csv` file, such as an expense report.
2. Data validation: Check whether the data is valid, such as ensuring amounts are numbers and dates follow the correct format.
3. Transformations: Standardize the data, such as converting category names to lowercase or removing unnecessary spaces.
4. Missing data: Detect empty fields and decide whether to fill them with a default value, skip the record, or flag it for correction.
5. Save the cleaned data: Export the corrected data into a new CSV file.

Example

Before cleaning:

| Name | Amount | Category |
| --- | --- | --- |
| Food | 500 | food |
| Transport |  | Transport |
| Food | 500 | food |

After cleaning:

| Name | Amount | Category |
| --- | --- | --- |
| Food | 500 | Food |
| Transport | Missing | Transport |

The program could standardize category names and flag the missing amount. It could also detect the duplicate record, but should only remove it if you decide that it is genuinely a duplicate.

In simple terms: You are building a Python program that takes messy CSV data, checks it, fixes what it safely can, and produces a cleaner file.