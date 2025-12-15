def filtre_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                try:
                    ip = line.split()[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1
                except IndexError:
                    continue
        try:
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                for ip, count in ip_counts.items():
                    outfile.write(f"{ip} - {count}\n")
        except IOError:
            print("File write error")
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("File read error")
allowed_ips = ["83.149.9.216", "66.249.73.135", "218.30.103.62"]
filtre_ips("apache_logs.txt", "filtered_ips.txt", allowed_ips)