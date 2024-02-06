#!/usr/bin/python3
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0
line_count = 0

def print_stats():
    """Print accumulated statistics"""
    print("File size: {}".format(file_size))
    for status, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(status, count))

try:
    for line in sys.stdin:
        data = line.split()
        line_count += 1

        try:
            size = int(data[-1])
            status = int(data[-2])
            file_size += size

            if status in status_codes:
                status_codes[status] += 1

        except (ValueError, IndexError):
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
print_stats()
