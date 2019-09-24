#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""

__author__ = """Damian Huerta"""
__collab__ = """I worked on this homework alone with the exception of emailing a TA for a test case question"""




"""
Function name: crazy_scrabble
Parameters: string, int, boolean 
Return value: int
"""

def crazy_scrabble(string, integer, boolean):
    count = integer
    used = ""
    newcount = 0
    for letter in string:
        if letter in used:
            newcount -= 1
            
        if letter in "kmpxyz":
            newcount += 7
            used += letter
        elif letter in "cs":
            newcount += 4
            used += letter
        elif letter in "aeiou":
            newcount -= 2
            used += letter
        else:
            newcount +=1
            used += letter
    if len(string) > 6:
        newcount += 3        
    if boolean and newcount > 0:
            newcount= newcount* 2
    totalpoints= count + newcount
    if totalpoints < 0:
        return 0
    else:
        return totalpoints




"""
Function name: decode
Parameters: string
Return value: string
"""

def decode(string):
    reverse= ""
    count = 0
    message= ""
    for let in string:
        if count < 13:
            if let.isupper():
                message += let
                count +=1
            elif let.isdigit():
                message += let
                count += 1
            elif let == " ":
               message += let
               count +=1
            else:
                continue
    for letter in message:
        reverse = letter + reverse

    return reverse


"""
Function name: average
Parameters: int
Return value: float or string
"""

def average(integer):
    grade = ""
    total_grade= 0
    counter= 1
    if integer == 0:
        return"Not enough grades to calculate average."
    while counter <= integer:
        grade = input("Please enter a test grade: ")
        total_grade += float(grade)
        average = total_grade/counter
        counter += 1
        if average < 70:
            return round(average, 1)
    return round(average,1)




"""
Function name: contains_substring 
Parameters: string, string 
Return value: bool 
"""

def contains_substring(string1, string2):
    substring = string2
    if len(string2) > len(string1):
        return False
    elif string2 == "":
        return False
    elif string1.find(substring) >=0:
        return True
    else:
        return False
    




"""
Function name: most_similar
Parameters: string, string, string 
Return value: string 
"""

def most_similar(string1, string2, string3):
    word= list(string1)
    count1= 0
    count2= 0
    similar1=0
    similar2=0
    for letter in string2:
        if letter == word[count1]:
            similar1 += 1
            count1 +=1
        else:
            count1 +=1
    for letter in string3:
        if letter == word[count2]:
            similar2 += 1
            count2 +=1
        else:
            count2 += 1
    if similar1 > similar2:
        return string2
    elif similar2 > similar1:
        return string3
    elif similar1 == similar2:
        return string2
        
        




"""
Function name: extract_word
Parameters: string, string, string 
Return value: string 
"""

def extract_word(string1, string2, string3):
    word = string1
    a = string2
    b = string3
    place1= word.find(a)
    place2= word.find(b)
    if place1 > place2:
        return ""
    else:
        answer= word[place1+1:place2]
        return answer



