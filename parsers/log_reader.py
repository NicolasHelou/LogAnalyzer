import os
import pathlib

def read_log_file(file_path):
    if file_path.endswith(".log") or file_path.endswith(".txt") or file_path.endswith(".LOG") or file_path.endswith(".TXT"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                entries = []
                for line in lines:
                    cleaned_line = line.strip()
                    if not cleaned_line:
                        continue
                    entries.append(cleaned_line)
                return entries
        
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
           
        except PermissionError:
            raise PermissionError("Permission not granted")

        except UnicodeDecodeError:
            raise UnicodeDecodeError("File cannot be decoded using UTF-8")
    
    if not file_path.endswith(".log", ".txt"):
        raise ValueError("Unsupported file type")