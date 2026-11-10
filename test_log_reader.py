from parsers.log_reader import read_log_file

# Test 1: Read the sample security log
file_path = "parsers/Sample_Logs/csv_tests/normal_events.csv"

try:
    entries = read_log_file(file_path)

    print("Number of entries:", len(entries))

    for entry in entries:
        print(entry)

except Exception as error:
    print("An error occurred:", error)