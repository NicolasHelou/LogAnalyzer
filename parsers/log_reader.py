import os
import pathlib

max_file_size = 50 * 1024 * 1024

def read_log_file(file_path):
    lowercase = file_path.lower()
    if not lowercase.endswith(".log") and not lowercase.endswith(".txt"):
        raise ValueError("Unsupported file type")
    file_size = os.path.getsize(file_path)
    if file_size > max_file_size:
        raise ValueError("File Size Too Large")
    if lowercase.endswith(".log") or lowercase.endswith(".txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                entries = []
                for line in file:
                    cleaned_line = line.strip()
                    if not cleaned_line:
                        continue
                    entries.append(cleaned_line)
                return entries
        
        except FileNotFoundError:
            raise FileNotFoundError
           
        except PermissionError:
            raise PermissionError

        except UnicodeDecodeError:
            raise UnicodeDecodeError
    
