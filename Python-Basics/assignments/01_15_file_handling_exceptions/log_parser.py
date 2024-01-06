import os
import re

class LogFileParser:
    def __init__(self, log_file_path):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        self.log_file_path = os.path.join(script_directory, log_file_path)
        self.log_entries = []


    def parse_log_file(self):
        with open(self.log_file_path, 'r') as file:
            for line in file:
                match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+): (.+)', line)
                
                if match:
                    timestamp, log_level, message = match.groups()
                    self.log_entries.append({'timestamp': timestamp, 'level': log_level, 'message': message})

    def display_log_entries(self):
        for entry in self.log_entries:
            print(f"Timestamp: {entry['timestamp']}, Level: {entry['level']}, Message: {entry['message']}")

# Example Usage
log_parser = LogFileParser("logfile.txt")
log_parser.parse_log_file()
log_parser.display_log_entries()
