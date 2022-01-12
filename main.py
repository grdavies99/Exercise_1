

with open('gettysburg.txt') as f:
    data = f.read().strip()

# print(data.replace(" ",""))

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
    

print("numbers: " + str(CountNumbers(data)) )
print("Consonants: " + str(CountConsonants(data)))
print("Vowels: " + str(CountVowels(data)))
print("Uppercase Letters: "+ str(CountUperrcase(data)))
print("Lowercase Letters: "+ str(CountLowercase(data)))
