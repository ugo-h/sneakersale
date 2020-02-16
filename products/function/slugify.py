text = 'brandname title'
print(text)
def slugify(string):
    string = string.split()
    for letter in string:
        if letter == ' ':
            letter = '_'
    return('_'.join(string).lower())
print(slugify(text))