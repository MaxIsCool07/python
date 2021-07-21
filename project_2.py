def remove_word(input_1:str, input_2:str) -> str:
    """
        Remove all occurences of input_1 in input_2.

        Keyword arguments:
        input_1 -- string to be removed
        input_2 -- string contains input_1
        Return:
        output -- string remaining in input_2 after removing input_1
    """
    output = input_2
    while(input_1 in output):
        index = output.index(input_1)
        output = output[0:index] + output[index+len(input_1):]
    return output 

print(remove_word('ab', 'abcabc'))