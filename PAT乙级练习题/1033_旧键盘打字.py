error_chars = input()
input_chars = input()

result = ""
for i in input_chars:
    if i.isdigit():
        if i in error_chars:
            continue
    elif i.isalpha():
        if i.upper() in error_chars:
            continue
        elif i.isupper() and '+' in error_chars:
            continue
    elif i in error_chars:
        continue
    result += str(i)

if len(result) != 0:
    print(result)
else:
    print()
