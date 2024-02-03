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

    # Add two newlines after each punctuation mark
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')

    # Split the text by newlines and strip leading spaces from each line
    lines = text.split('\n')
    for line in lines:
        print(line.strip(), end="")
        if line is not lines[-1]:  # Add a newline after each line except the last
            print()
