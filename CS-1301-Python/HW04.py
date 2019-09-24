#!/usr/bin/env python3
import string
"""
Georgia Institute of Technology - CS1301
HW04 - Strings and Lists
"""

__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked alone"""

"""
Function name: remove_upper 
Parameters: string 	
Returns: string
"""


def remove_upper(astr):
    notupper= ""
    newphrase= ""
    no_space= astr.split()
    for word in no_space:
        if word[0].islower():
            for letter in word:
                if letter.isdigit():
                    notupper += "c"
                else:
                    notupper += letter
            newphrase = newphrase + notupper + " "
            notupper= ""
        else:
            continue
    return newphrase.strip()
                    

"""
Function name: username_validator
Parameters:  aStr (str)
Returns: new_username (str)
"""

def username_validator(astr):
    validated= ""
    final= ""
    count = 0
    count2 = 0
    for char in astr:
        if char not in (string.ascii_letters + string.digits + "." + "-"):
            validated += "-"
        elif char in string.digits:
            count += 1
            if count <= 3:
                validated += char
            else:
                continue
        else:
            validated += char
    for char in validated:
        if char.isupper():
            count2 += 1
        else:
            continue
    if count2 > 0:
        return validated
    else:
        return validated.capitalize()
        
        

        

"""
Function name: letter_count
Parameters:  aList (list), num (int), char (str)
Returns: newList (list)
"""

def letter_count(alist, num, char):
    newlist = []
    count = 0
    for word in alist:
        for letter in word:
            if letter.lower() == char.lower():
                count += 1
            else:
                continue
        if count == num:
            newlist.append(word)
        count = 0
    return newlist
        


"""
Function name: flatten_list
Parameters:  aList (list)
Returns: final_list (list)
"""

def flatten_list(alist):
    finallist= []
    for i in alist:
        if type(i) == list:
            for j in i:
                finallist.append(j)
        else:
            finallist.append(i)
    return finallist
           

"""
Function name: add_vowels
Parameters: list of strings
Return value: string
"""

def add_vowels(alist):
    astr = ""
    for string in alist:
        a = string.find("a")
        newstring = string[0:a]
        for letter in newstring:
            if letter in "eiouEIOU":
                astr += letter
                break
        if newstring.find("e") == -1 and newstring.find("i") == -1 and newstring.find("o") == -1 and newstring.find("u")==-1:
            astr += "a"                
        
         
    return astr

            

"""
Function name: total_cost
Parameters: list, boolean
Return value: list
"""

def total_cost(alist, boolean):
    cost= 0
    pizza =[]
    used = []
    organize = []
    
    if alist == []:
        return []
    if boolean == True:
        for string in alist:
            a= string.find("$")
            b= string[a+1:]
            cost += float(b)
        
        pizza.append(cost)
        return pizza
    else:
        for i in alist:
            space = i.find("$")
            thing = i[0:space-1]
            if thing not in used:
                used.append(thing)
                gen = thing, float(i[space+1:])
                organize.append(list(gen))
                
         
                
            else:
                money = i[space+1:]
                for (g,w) in enumerate(used):
                        if thing == w:
                           organize[g][1] = organize[g][1]+ float(money) 
                           
                        
    return organize

