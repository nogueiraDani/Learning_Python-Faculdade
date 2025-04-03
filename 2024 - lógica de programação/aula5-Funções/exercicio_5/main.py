def validate_string(text, x=0, y=0):
    if x <= len(text) <= y:
        return True
    else:
        return False


result = validate_string('Dani', 1, 5)
print(result)
