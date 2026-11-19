import os
import csv

required_headers = [
    "timestamp",
    "severity",
    "event_type",
    "username",
    "source_ip"
]

max_file_size = 50 * 1024 * 1024

def read_csv(file_path):
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
                if header_names == None:
                    raise ValueError("File is Empty")
                for string in header_names:
                    string = string.strip()
                unique_headers = set(header_names)
                if not (read_file.fieldnames == required_headers):
                    raise ValueError("Expected Fields Not Located in File")
                
                for row in read_file:
                    if None in row:
                        raise ValueError("Extra Fields Present in CSV File")
                    missing = [k for k, v in row.items() if k is not None and v is None]
                    if missing:
                       raise ValueError("Missing Field Present in CSV File")
                
                    csv_dict.append(row)
                return csv_dict

        except FileNotFoundError:
            raise FileNotFoundError

        except PermissionError:
            raise PermissionError

        except UnicodeDecodeError:
            raise UnicodeDecodeError

        
    if not lower_file.endswith(".csv"):
        raise ValueError("Unsupported File Type")