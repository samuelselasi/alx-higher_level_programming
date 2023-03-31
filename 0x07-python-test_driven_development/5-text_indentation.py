#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    txt = text[:]

    for char in ".?:":
        list_text = txt.split(char)
        txt = ""

        for elem in list_text:
            elem = elem.strip(" ")
            txt = elem + char if txt is "" else txt + "\n\n" + elem + char

    print(txt[:-3], end="")
