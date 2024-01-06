with open('logfile.txt', 'r') as f:
    log_file_lines = f.readlines()

for i in log_file_lines:
    print(i)