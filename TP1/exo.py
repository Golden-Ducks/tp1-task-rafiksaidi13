num = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

punct = ".…,;:’'\"-()[]{}“”"



d = [ 
    'Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.',
    'Five pizza were ready, but 3 bourak burned!',
    'We only had 8 chamiyya, no pizza, and one tea.',
    'Is 6 too much? I ate nine bourak lol.'
]

def norm(txt):
    cleaned_txt = ""
    txt = txt.lower()
    
    for c in txt:
        if c in punct:
            continue
        elif c in num:
            cleaned_txt += num[c]
        elif c == "?" or c == "!":
            cleaned_txt += " " + c
        else:
            cleaned_txt += c
    
    cleaned_txt = cleaned_txt.split()
    cleaned_txt = " ".join(cleaned_txt)
    
    return cleaned_txt

def tokenize(txt):
    return txt.split()


for sentence in d:
    normalized = norm(sentence)
    print(normalized)
    print(tokenize(normalized))


#     line 13
# Use string.punctuation bcz it's better than typing out specific marks manually
    
#     line 30
# building strings with += inside a loop is discouraged bcz strings are immutable
# use a list and then .join() for better performance
    
#     line 28
# btw, you can use .get() here to handle the dict lookup and the "else" in one line
    
#     line 37
# you can use a list comprehension here to clean and normalize everything in one go

# Next time,try to solve the logic yourself instead of just renaming someone else's work


