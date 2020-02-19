text = 'brandname title'
text2 = 'new_balance'
print(text)
def slugify(string):
    string = string.split()
    for letter in string:
        if letter == ' ':
            letter = '_'
    return('_'.join(string).lower())
print(slugify(text))

def unslug(string):
    string = string.split('_')
    print(string)
    for letter in string:
        print(letter)
        if letter == '_':
            letter = ' '
    return(' '.join(string).lower())
print(slugify(text))
print(unslug(text2))