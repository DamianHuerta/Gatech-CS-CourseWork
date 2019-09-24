def move_vowels(astr):
    myword= ""
    vowels= ""
    for letter in astr:
        if letter in "aeiou":
            vowels += letter
        else:
            myword += letter
    return myword + vowels


