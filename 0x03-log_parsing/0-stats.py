#!/usr/bin/python3
""""
a script that reads stdin line by line and computes metrics
"""


import sys

if __name__ == '__main__':
    total_file_size = [0]
    http_status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}

    def display_statistics():
        """Print statistics for file sizes and HTTP status codes."""
        print('Total File Size: {}'.format(total_file_size[0]))
        for status_code in sorted(http_status_counts.keys()):
            if http_status_counts[status_code]:
                print(f'{status_code}: {http_status_counts[status_code]}')

    def parse_log_line(line):
        """Parse a log line to extract file size and HTTP status code."""
        try:
            line = line[:-1]  # Remove the newline character
            words = line.split(' ')
            # File size is the last parameter on stdout
            total_file_size[0] += int(words[-1])
            # Status code comes before the file size
            http_status_code = int(words[-2])
            # Update the count for the status code
            if http_status_code in http_status_counts:
                http_status_counts[http_status_code] += 1
        except BaseException:
            pass

    line_number = 1
    try:
        for log_line in sys.stdin:
            parse_log_line(log_line)
            """Display statistics after processing every 10 lines."""
            if line_number % 10 == 0:
                display_statistics()
            line_number += 1
    except KeyboardInterrupt:
        display_statistics()
        raise
    display_statistics()
