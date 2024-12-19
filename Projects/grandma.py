while True:
    word = input ("what do you think grandma likes?")
    if word == "she likes words without a b":
        print("right! grandma only likes words without a b!")
        break
    if "b" in word:
        print(f"grandma dosen't like {word}!")
    else:
        print (f"grandma likes {word}!")

    print("")