#!/usr/bin/python3
"""14. Log parsing"""

import sys


if __name__ == "__main__":

    def status_codes(size, status_codes):
        """A function that prints status codes till CTRL + C"""

        print("File size: {}".format(size))
        for key in sorted(status_codes):
            print("{}: {}".format(key, status_codes[key]))

    size = 0
    possible_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    i = 0

    try:
        for line in sys.stdin:
            if i == 10:
                status_codes(size, possible_codes)
                i = 1

            else:
                i += 1

            line = line.split()
            try:
                size += int(line[-1])

            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if possible_codes.get(line[-2], -1) == -1:
                        possible_codes[line[-2]] = 1

                    else:
                        possible_codes[line[-2]] += 1

            except IndexError:
                pass

        status_codes(size, possible_codes)

    except KeyboardInterrupt:
        status_codes(size, possible_codes)
        raise
