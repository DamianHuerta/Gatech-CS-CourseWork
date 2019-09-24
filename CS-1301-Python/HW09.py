#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked on this alone"""

"""
Function name: shows_r
Parameters: lists of tuples
Returns: int

"""
def shows_r(mylist):
    if len(mylist) == 0:
        return 0
    else:
        if mylist[0][0] * mylist[0][1] <= 22:
            count = 1 + shows_r(mylist[1:])
            return count
        else:
            count = shows_r(mylist[1:])
            return count



"""
Function name: shows_i
Parameters: lists of tuples
Returns: int

"""
def shows_i(mylist):
    count = 0
    for thing in mylist:
        if thing[0]*thing[1] <= 22:
            count += 1
        else:
            continue
    return count

"""
Function name: wheres_waldo_r
Parameters: string
Returns: int

"""

def wheres_waldo_r(mystring):
    if "waldo" in mystring:
        if len(mystring) <5:
            return -1
        elif mystring[0:5] == "waldo":
            return 0
        else:
            return 1 + wheres_waldo_r(mystring[1:])
    else:
        return -1
            
            
        
        
         
        

"""
Function name: wheres_waldo_i
Parameters: string
Returns: int

"""
def wheres_waldo_i(mystring):
    count = -1
    for g,letter in enumerate(mystring):
        if mystring[g] == "w" and len(mystring) >= 5 and mystring[g:g+5] == "waldo":
            count = g
            return g
        else:
            continue
    return count
    
"""
Function name: count_patterns_r
Parameters: string with at least 3 characters
Returns: int

"""
def count_patterns_r(mystr):
    if len(mystr) < 3:
        return 0
    else:
        count = count_patterns_r(mystr[1:])
        pat = mystr[0:3]
        if pat[0] == pat[2] and pat[0] != pat[1]:
            count += 1
        return count
            
    

"""
Function name: count_patterns_i
Parameters: string with at least 3 characters
Returns: int

"""
def count_patterns_i(mystr):
    count = 0
    for g,w in enumerate(mystr):
        if g > 0 and g <= len(mystr)-2 and mystr[g-1] == mystr[g+1] and mystr[g]!=mystr[g+1]:
            count+=1
    return count

"""
Function name: string_stats_r
Parameters: string
Returns: dictionary

"""
def string_stats_r(mystr):
    if len(mystr) == 0:
        return {"uppercase": 0, "lowercase": 0, "numbers": 0, "spaces": 0, "other":0}
    else:
        letter = mystr[0]
        if letter.isupper():
            mydict = string_stats_r(mystr[1:])
            mydict["uppercase"]+=1
            return mydict
        elif letter.islower():
            mydict = string_stats_r(mystr[1:])
            mydict["lowercase"] +=1
            return mydict
        elif letter.isdigit():
            mydict = string_stats_r(mystr[1:])
            mydict["numbers"]+=1
            return mydict
        elif letter == " ":
            mydict = string_stats_r(mystr[1:])
            mydict["spaces"] += 1
            return mydict
        else:
            mydict = string_stats_r(mystr[1:])
            mydict["other"] += 1
            return mydict
        
    

"""
Function name: string_stats_i
Parameters: string
Returns: dictionary

"""
def string_stats_i(mystr):
    mydict = {"uppercase": 0, "lowercase": 0, "numbers": 0, "spaces": 0, "other":0}
    for letter in mystr:
        if letter.isupper():
            mydict["uppercase"]+=1
        elif letter.islower():
            mydict["lowercase"] +=1
        elif letter.isdigit():
            mydict["numbers"]+=1
        elif letter == " ":
            mydict["spaces"] += 1
        else:
            mydict["other"] += 1
    return mydict

#print(string_stats_i( "sPoNgE BoB iS mY #1 fAn!"))

