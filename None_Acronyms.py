acronyms={'LOL': 'laugh at loud', 'IDK':"I don't know"}
definition = acronyms.get('BTW')
if definition:
    print(definition)
else:
    print("Key doesn't exist")
    