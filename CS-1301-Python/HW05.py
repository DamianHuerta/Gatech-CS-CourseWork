#!/usr/bin/env python3
import calendar
import statistics

"""
Georgia Institute of Technology - CS1301
HW05 - Tuples and Modules
"""

__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked on this alone"""

"""
Function name: favorite day
Parameters: dates (list of tups), weekday (int), day (int)
Returns: reduced dates (list of tups)
"""

def favorite_day(dates,weekday,day):
    new = []
    for thing in dates:
        if calendar.weekday(thing[1],thing[0],day) == weekday:
            new.append(thing)
        else:
            continue
    return new
        
  


"""
Function name: organize_grades
Parameters: grades (list of tups), courses (list of strs)
Returns: results (list of tups)
"""

def organize_grades(grades,courses):
    classes= courses
    random = []
    rip = []

    for thing in classes:
        random.append([])
    for thing in grades:
        a = classes.index(thing[1])
        random[a].append(thing[0])
    for g,w in enumerate(random):
        random[g] = statistics.stdev(random[g])
    for g,w in enumerate(classes):
        a= round(random[g],2), classes[g]
        rip.append(a)
    return rip
    
        
    
       

"""
Function name: format_date
Parameters: dateList (list)	
Returns: newDateList (list)
"""

def format_date(dates):
    for d,h in enumerate(dates):
        day = h[0]
        month = h[1]
        year = h[2]
        dates[d] = (month, day, year)
    return dates
         
            

"""
Function name: todo_tuple
Parameters:  todo (list)
Returns: final_list (list)
"""

def todo_tuple(ugh,yay):
    gen = []
    lower = []
    last = []
    empty = ()
    for done in yay:
        lower.append(done.lower())
    for g in ugh:
        for w in g:
            if w.lower() not in lower:
                empty += (w,)
        if len(empty) != 0:
            last.append(empty)
        empty = ()
    return last
                
                
                
        

"""
Function name: no_missing_attributes
Parameters: attributeList (list of tuples)
Returns: newAttributeList (list of tuples)
"""

def no_missing_attributes(alist):
    newlist = []
    empty = ()
    for stuff in alist:
        if len(stuff) == 2:
            user = stuff[0]+ str(stuff[1])
            final = (stuff[0],stuff[1],user)
            newlist.append(final)
                

        else:
            for rosa in stuff:
                empty += (rosa,)
            newlist.append(empty)
            empty = ()
    return newlist

    




