#!/usr/bin/python3
"""13. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text to a file,
    after each line containing a specific string
    """

    msg = ""
    with open(filename) as f:

        for line in f:
            msg += line

            if search_string in line:
                msg += new_string

    with open(filename, "w") as f:
        f.write(msg)
