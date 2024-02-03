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

    # Initialize an index and a flag to indicate if a punctuation mark was found
    i = 0
    punct = False

    while i < len(text):
        # Print the character
        print(text[i], end="")
        
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            punct = True
        elif punct and text[i] == ' ':
            # Skip printing the space after a punctuation
            pass
        else:
            punct = False
        
        # If a punctuation mark was found and the current character is not a space,
        # print two new lines
        if punct and text[i] != ' ':
            print("\n")
            punct = False
        
        i += 1
