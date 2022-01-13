text = input("Enter name of text file: ")



with open(text) as f:
    data = f.read().strip()

def CountConsonants(info):
    cons = 0
    for char in info:
        if char in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
            cons += 1
    return cons

def CountVowels(info):
    vowels = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for char in info.lower():
            if char == "a":
                vowels["a"] += 1
            if char == "e":
                vowels["e"] += 1
            if char == "i":
                vowels["i"] += 1
            if char == "o":
                vowels["o"] += 1
            if char == "u":
                vowels["u"] += 1
    return vowels

def CountNumbers(info):
    numbers = 0
    for char in info:
        if char in "0123456789":
            numbers += 1
    return numbers

def CountUperrcase(info):
    upper = 0
    for char in info:
        if char.isupper():
            upper += 1
    return upper

def CountLowercase(info):
    Lower = 0
    for char in info:
        if char.islower():
            Lower += 1
    return Lower

def RemoveBreaks(info):
    info = info.replace("\n", " ")
    return info    

# print(len(RemoveBreaks(data).split(" ")))

print("\nStatistics for " + text + ":\n")
print("Characters: " + str(len(data)))
print("Upper case: "+ str(CountUperrcase(data)))
print("Lower case: "+ str(CountLowercase(data)))
print("Digits: " + str(CountNumbers(data)) )
print("White spaces: " + str(data.count(" ")))
print("Vowels: " + str(CountVowels(data)))
print("Consonants: " + str(CountConsonants(data)))
print("Sentences: " + str(data.count(".")))
print("Average words per sentence: " + str(round(len(RemoveBreaks(data).split(" "))/data.count("."),1)))
