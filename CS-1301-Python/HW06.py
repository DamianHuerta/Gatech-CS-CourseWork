#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - Try/Except and Dictionaries 
"""

__author__ = """Damian Huerta"""
__collab__ = """I worked on this homework alone"""

"""
Function name: number_letter_sort
Parameters: string
Returns: tuple
"""


def number_letter_sort(astr):
    digits = ""
    letters= ""
    for thing in astr:
        try:
            a = int(thing)
            digits += str(thing)
        except:
            letters += thing
    return (digits, letters)



"""
Function name: add_divide
Parameters: list of ints, int
Returns: float
"""

def add_divide(alist, integer):
    total = 0
    for g,w in enumerate(alist):
        if g%integer == 0:
            try:   
                total = total/w
            except:
                total += 1
        else:
            total += w
    return round(total,2)
        
"""      
Function name: trip_planner
Parameters: list of tuples
Returns: dictionary with each value as a dictionary
"""

def trip_planner(alist):
    dictionary = {}
    used = []
    for thing in alist:
        dictionary[thing[0]] = {}
    for thing in alist:
        if thing[1] not in used:
            dictionary[thing[0]][thing[1]] =  thing[2]
            used.append(thing[1])
        else:
            dictionary[thing[0]][thing[1]] += thing[2]

    return dictionary

  

"""
Function name: average_rating 
Parameters: dictionary containing NYC neighborhoods as keys and their values
being a nested dictionary whose keys are tourist locations and values are a
list of integer ratings
Returns: dictionary 
"""
def average_rating(dictionary):
    average = 0
    for g,w in dictionary.items():
        for d,h in w.items():
            average = sum(h)/len(h)
            dictionary[g][d] = round(average,2)
    return dictionary 

"""
Function name: get_restaurants 
Parameters: a dictionary containing restaurants as keys and their values being
a list of the items that they serve 
Returns: a dictionary containing the items as keys and their values being a
list  
"""

def get_restaurants(dictionary):
    new = {}
    used = []
    for g,w in dictionary.items():
        for other in w:
            if other not in used:
                new[other] = []
                used.append(other)
    for thing in used:
        for g,w in dictionary.items():
            if thing in dictionary[g]:
                new[thing].append(g)
    return new
        



"""
Function name: catch_flight
Parameters: dictionary, tuple containing two strings
Returns: dictionary
"""
def catch_flight(dictionary,tup):
    new = {}
    for g,w in dictionary.items():
        new[g] = 0
    for g,w in dictionary.items():
        for d,h in enumerate(w):
            if float(dictionary[g][d][1:]) >= float(tup[0][1:]) and float(dictionary[g][d][1:]) <= float(tup[1][1:]):
                new[g] += 1
    return new



