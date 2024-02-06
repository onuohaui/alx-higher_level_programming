#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """
    Print statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parse log line
    """
    parts = line.split()
    if len(parts) > 2:
        status_code = parts[-2]
        file_size = parts[-1]
        return (int(status_code), int(file_size))
    return None

def main():
    """
    Main function
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            log_data = parse_line(line)
            if log_data:
                status_code, file_size = log_data
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
