def analyze_log_file(log_file_path):
    result = {}
    try:
        with open(log_file_path, "r", encoding='utf-8') as file:
            for line in file:
                try:
                    parts = line.split('"')
                    after_request = parts[2].strip().split()
                    status_code = after_request[0]
                    if status_code.isdigit():
                        result[status_code] = result.get(status_code, 0) + 1
                except (IndexError, ValueError):
                    continue
    except FileNotFoundError:
        print("log file not found")
    except IOError:
        print("log file read error")
    return result
stats = analyze_log_file("apache_logs.txt")
print(stats)
