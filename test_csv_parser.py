from parsers.csv_parser import read_csv

# Test 1: Read a normal CSV file
file_path = "parsers/Sample_Logs/csv_tests/empty_fields.csv"

try:
    records = read_csv(file_path)

    print("Number of records:", len(records))

    for record in records:
        print(record)

except Exception as error:
    print("An error occurred:", error)
