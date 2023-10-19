#!/usr/bin/python3
""""
a script that reads stdin line by line and computes metrics
"""


def process_logs():
    """
    Parse and process log entries to calculate file size
    and status code counts.
    """
    stdin = __import__('sys').stdin
    line_count = 0
    total_file_size = 0
    status_code_counts = {}
    status_codes = ('200', '301', '400', '401', '403', '404', '405', '500')

    try:
        for line in stdin:
            line_count += 1
            line_parts = line.split()
            try:
                total_file_size += int(line_parts[-1])
                if line_parts[-2] in status_codes:
                    try:
                        status_code_counts[line_parts[-2]] += 1
                    except KeyError:
                        status_code_counts[line_parts[-2]] = 1
            except (IndexError, ValueError):
                pass
            if line_count == 10:
                generate_report(total_file_size, status_code_counts)
                line_count = 0

        generate_report(total_file_size, status_code_counts)

    except KeyboardInterrupt as e:
        generate_report(total_file_size, status_code_counts)
        raise


def generate_report(file_size, status_codes):
    """
    Generates a report with the total file size
    and counts of each status code.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    process_logs()
