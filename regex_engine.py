# function that check if there is match 
def is_match(regex_char, input_char):
    if len(regex_char) == 0:
        return True
    elif regex_char == input_char or regex_char == '.' and input_char:
        return True
    else:
        return False

# call is_match function for each character
def check_string_match(regex, string):
    # converting the strings into chars lists
    regex_chars = [char for char in regex]
    string_chars = [char for char in string]
    # if the input is empty handle it
    regex_char = regex_chars.pop(0) if regex_chars else ''
    input_char = string_chars.pop(0) if string_chars else ''
    # call the function 'is_match' and get te result
    match = is_match(regex_char, input_char)
    # if there´s no match return false
    if not match:
        return False
    # when is a match, the regex and string was consumed so return true
    elif match and (not regex_chars and not string_chars):
        return True
    # else recall this function
    return check_string_match(regex_chars, string_chars)

# get the input and split it by '|' and pass it to the function
regex, string = input().split("|")
match_result = check_string_match(regex, string)
print(match_result)
