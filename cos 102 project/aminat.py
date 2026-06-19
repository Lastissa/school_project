keyWord = {
    "a" : 1,
    "e" : 2,
    "i" : 3,
    "o" : 4,
    "u" : 5
}

def engToJungle():
    word = input("enter english: ")
    translation = []
    for i in word:
        try: translation.append(str(keyWord[i.lower()]))
        except: 
            if len(i.strip()) ==0:translation.append(f"{i.lower()}")
            else:translation.append(f"{i.lower()}a")

    return "".join(translation)
        
        
while True:
    print(engToJungle())