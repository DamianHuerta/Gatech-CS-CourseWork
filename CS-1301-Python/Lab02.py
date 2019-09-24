#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
Lab02 - Data Analysis
"""

__author__ = """Damian Huerta"""
__collab__ = """I worked on this alone."""

"""
Function name: sleepy_students
Parameters: int
Returns: float

"""

def sleepy_students(num):
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    count = 0
    sleep = 0
    for line in data:
        line = line.strip()
        column = line.split(",")
        if int(column[2]) >= num:
            count += 1
            sleep += float(column[12])
    return round(sleep/count,2)
            
            

"""
Function name: family_pets
Parameters: int
Returns: string

"""
def family_pets(num):
    pets = []
    count = []
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    for line in data:
        line = line.strip()
        column = line.split(",")
        if int(column[3]) == num:
            bud = column[13].split(";")
            for pet in bud:
                if pet in pets:
                    index = pets.index(pet)
                    count[index] +=1
                else:
                    pets.append(pet)
                    count.append(1)
    upper = max(count)
    index2 = count.index(upper)
    return pets[index2]


    
        

"""
Function name: coffee_by_major
Parameters: string
Returns: float

"""
def coffee_by_major(mystr):
    total = 0
    count = 0
    major = 0
    count2 = 0
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    for stuff in data:
        stuff = stuff.strip()
        column = stuff.split(",")
        total += float(column[9])
        count += 1
    avgtot = total/count
    for stuff in data:
        column = stuff.split(",")
        if mystr.lower() in column[4].lower().split(";"):
            count2 += 1
            major += float(column[9])
    if count2 == 0:
        return None
    else:
        majoravg = major/count2
        return round(majoravg - avgtot,2)

"""
Function name: music_vs_movie
Parameters: string, string
Returns: float

"""
def music_vs_movie(mystr,mystr2):
    movie = 0
    music = 0
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    for line in data:
        line  = line.strip()
        column = line.split(",")
        if mystr.lower() in column[8].lower():
            movie += 1
            if mystr2.lower() in column[7].lower():
                music += 1
    if movie == 0 or music == 0:
        return None
    return round((music/movie)*100,2)

#print(music_vs_movie("rawr","xD"))
    


"""
Function name: tally
Parameters: string
Returns: dictionary

"""
def tally(mystr):
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    mydict = {}

    if mystr == "age":
        index = 0
    elif mystr == "outofstate":
        index = 1
    elif mystr == "siblings":
        index = 3
    elif mystr == "major":
        index = 4
    elif mystr == "minor":
        index = 5
    elif mystr == "restaurant":
        index = 6
    elif mystr == "numlangs":
        index = 10
    else:
        return mydict
    for line in data:
        line = line.strip()
        column = line.split(",")
        if column[index] not in mydict.keys():
            mydict[column[index]] = 1
        else:
            mydict[column[index]] += 1
    return mydict
    
       

"""
Function name: languages_by_major
Parameters: a string representing a major
Returns: return a dictionary of all the languages spoken by students of that major mapped to
how many people speak it

Complete the following questions about your function:
What question about the data does your function aim to answer?
What are all the languages spoken by a specific major and how many people speak each language?

How does your function answer the question? (e.g., what calculations does it make,
what data does it extract from the CSV, etc.)
It will extract all the languages from people with a specific major. The calculations it will
make involve adding one each time to the value of that language (key) a language is repeated.
If the language is not in the dictionary it will be added as a key with a value of 1

Describe the parameters - what are they and what types are they?
My parameter is a string that represents a specific major

Describe the output - what does it represent and what type is it?
the output is a dictionary. In this dictionary, the keys are languages spoken by students
in the specific major that is input as a parameter and the value is the number of students
who speak the language in that major.


"""
def languages_by_major(mystr):
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    mydict = {}
    for line in data:
        line = line.strip()
        column = line.split(",")
        if mystr.lower() in column[4].lower():
            languages = column[11].split(";")
            for lang in languages:
                if lang not in mydict.keys():
                    mydict[lang.capitalize()] = 1
                else:
                    mydict[lang.capitalize()] += 1
    return mydict

#print(languages_by_major("CS"))

"""
Function name: diverse_major
Parameters: none
Returns: str

Complete the following questions about your function:
What question about the data does your function aim to answer?

My functions answers the following questions:
Which major speaks the most languages?
How many languages does this major speak?
What languages does this major speak?

How does your function answer the question? (e.g., what calculations does it make,
what data does it extract from the CSV, etc.)
It answers the question by running through all majors and checking how many languages each
major speaks then finding the max. It does this by making a nested list that corresponds to
a major at that same index in a different list. Inside the nestsed list is all the languages
that specific major speaks. Then we make a new list that also corresponds to the specific
index of the other two lists. Inside this list are the lengths of the respective nested lits
that have all the languages. The max of this is taken to know which major speaks the most languages
It finally returns a string that says which major speaks the most languages, how many languages
that major speaks and what those languages are

Describe the parameters - what are they and what types are they?

There are no parameters

Describe the output - what does it represent and what type is it?
Its output is a string that has information about the most diverse speaking major

"""
def diverse_major():
    fh = open("data.csv","r")
    header = fh.readline()
    data = fh.readlines()
    majors = []
    lang = []
    how = []
    for line in data:
        line = line.strip()
        column = line.split(",")
        double = column[4].split(";")
        for major in double:
            if major.strip() not in majors:
                hi = major.strip()
                majors.append(hi)
                lang.append([])
    for g,major in enumerate(majors):
        for line in data:
            line = line.strip()
            column = line.split(",")
            if major.lower() in column[4].lower():
                talk = column[11].split(";")
                for langs in talk:
                    if langs not in lang[g]:
                        lang[g].append(langs)
    for thing in lang:
        how.append(len(thing))
    upper = max(how)
    index2 = how.index(upper)
    tongues = ""
    for thing in lang[index2]:
        tongues += "\n" + thing
    return "{} is the most diverse-speaking major! {} majors speak {} different languages.\n\nHere are all the languages they speak:\n {}".format(majors[index2],majors[index2],str(upper),tongues)


