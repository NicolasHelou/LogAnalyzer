import os
import csv

required_headers = {
    "timestamp",
    "severity",
    "event_type",
    "username",
    "source_ip"
}

max_file_size = 50 * 1024 * 1024

def read_csv(file_path):
    if not lower_file.endswith(".csv"):
        raise ValueError("Unsupported File Type")
    file_size = os.path.getsize(file_path)
    if file_size > max_file_size:
        raise ValueError("File Size Too Large")
    
    lower_file = file_path.lower()
    if lower_file.endswith(".csv"):
        try:
            with open(file_path, "r", encoding="utf-8", newline="") as file:
                csv_dict = []
                read_file = csv.DictReader(file)
                header_names = read_file.fieldnames
                csv_headers = []
                if header_names == None:
                    raise ValueError("File is Empty")
                for string in header_names:
                    string = string.strip()
                    csv_headers.append(string)
                if any(not string for string in csv_headers):
                    raise ValueError("CSV Contains an Empty Header")

                unique_headers = set(csv_headers)
                if len(csv_headers) != len(unique_headers):
                    raise ValueError("CSV Contains Duplicate Headers")
                read_file.fieldnames = csv_headers
                missing_fields = required_headers - set(unique_headers) 
                if missing_fields:
                    missed = ", ".join(sorted(missing_fields))
                    raise ValueError(f"Expected Field(s) Not Located in File: {missed}")
                
                for row in read_file:
                    if None in row:
                        raise ValueError("Extra Fields Present in CSV File")
                    missing = [k for k, v in row.items() if k is not None and v is None]
                    if missing:
                       raise ValueError(f"Missing Field Present in CSV row: {', '.join(missing)}")
                
                    csv_dict.append(row)
                return csv_dict

        except FileNotFoundError:
            raise FileNotFoundError

        except PermissionError:
            raise PermissionError

        except UnicodeDecodeError:
            raise UnicodeDecodeError

        
