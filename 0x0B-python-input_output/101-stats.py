#!/usr/bin/python3
"""
Script to compute metrics from log data
"""

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status code.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parses a line from the log data and updates the metrics.

    Args:
        line (str): Line from the log data.
        total_size (int): Current total file size.
        status_codes (dict): Dictionary containing the count of each status code.

    Returns:
        int: Updated total file size.
        dict: Updated status code counts.
    """
    parts = line.split()
    if len(parts) > 2:
        try:
            size = int(parts[-1])
            code = parts[-2]
            if code.isdigit() and int(code) in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[code] = status_codes.get(code, 0) + 1
                total_size += size
        except ValueError:
            pass
    return total_size, status_codes


def main():
    total_size = 0
    status_codes = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            total_size, status_codes = parse_line(line.strip(), total_size, status_codes)
            if count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
