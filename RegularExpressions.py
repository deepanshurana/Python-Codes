import re

patterns = ['term1', 'term2']

text = 'This is string with term1, but not the other!'
text1 = 'term1'
for pattern in patterns:
    print("I am searching for: ", pattern)

    if (re.search(pattern, text)):  # Returns match type, or match object.
        print("MATCH.")

    else:
        print("NO MATCH.")

# return of re.search() is more than a boolean or none. It returns a MatchType
# Object. It contains information about the object.

match = re.search('term1', text)
print(type(match))
print(type(match.start()))  # starting index position of search.
print(match.start())

match2 = re.search('term1', text1)
print(match2.start())

"""
You can also split the term using re module.
"""
splitTerm = "@"
email = 'user@gmail.com'
match3 = re.split(splitTerm, email)
print(match3)

# to find all the instances of the pattern, use .findall()

match4 = re.findall('match', 'Test phrase, match in Match Middle MATCH.')
print(match4)


# creating a helper function.

def multiReFind(pattern, phrase):
    for i in pattern:
        print("Searching for pattern {}".format(i))
        print(re.findall(i, phrase), end='\n')


testPhrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd'
testPatterns = ['sd*']  # s followed by 0 or more ds.
multiReFind(testPatterns, testPhrase)

testPatterns2 = ['sd+']  # s followed by 1 or more ds.
multiReFind(testPatterns2, testPhrase)

testPatterns3 = ['sd{3}']  # s followed by 3 ds.
multiReFind(testPatterns3, testPhrase)

testPatterns4 = ['sd{1,3}']  # s followed by 1 or 3 ds.
multiReFind(testPatterns4, testPhrase)

testPatterns5 = ['s[sd]+']  # s followed by one or more s and ds.
multiReFind(testPatterns5, testPhrase)

testPhrase2 = "This is a string! But it has punctuation. How can we remove it?"
testPattern6 = ['[^?.!]+']  # ^-> exclude terms. use "+" for one or more occurance.
multiReFind(testPattern6, testPhrase2)

testPatterns7 = ['[a-z]+']  # to fetch all lowercase letters.(string)
multiReFind(testPatterns7, testPhrase2)

testPatterns8 = ['[A-Z]+']  # to fetch all uppercase letters.
multiReFind(testPatterns8, testPhrase2)

testPhrase3 = 'This is a string with numbers 123124 and a symbol #hashtag'

testPatterns9 = [r'\d+']  # to fetch all the digits.
multiReFind(testPatterns9, testPhrase3)

testPatterns10 = [r'\D+']  # to fetch all the non-digits.
multiReFind(testPatterns10, testPhrase3)

testPatterns11 = [r'\W+']  # fetch all the alpha numeric chrs.
multiReFind(testPatterns11, testPhrase3)
