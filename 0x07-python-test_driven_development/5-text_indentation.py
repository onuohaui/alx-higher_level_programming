#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: string
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')

    lines = text.split('\n')
    for line in lines:
        print(line.strip(), end="")
        if line is not lines[-1]:
            print()
