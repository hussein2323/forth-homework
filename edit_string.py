def reverse_string(s):
    return s[::-1]

def string_length(s):
    return len(s)

def delete_spaces(s):
    return s.replace(" ", "")

def check_string(s):
    if s.isalpha():
        return "Only letters"
    elif s.isdigit():
        return "Only digits"
    elif s.isalnum():
        return "Letterstand digits"
    else:
        return "Containstspecial characters"