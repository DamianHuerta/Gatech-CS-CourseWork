#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O
"""

__author__ = """Damian Huerta"""
__collab__ = """I worked on this alone"""

"""
Function name: hangry
Parameters: file (str), num (int), food_type (str)
Returns: list

"""

def hangry(file,number,foodtype):
    fh = open(file,"r")
    mydict = {}
    cal = []
    food = []
    mylist = fh.readlines()
    fh.close()
    for g,w in enumerate(mylist):
        w = w.strip()
        w = w.lower()
        if  w == foodtype.lower():
            cal.append(int(mylist[g-1].strip()))
            if mylist[g-1] not in mydict.keys():
                mydict[int(mylist[g-1].strip())] = [mylist[g-2].strip()]
            else:
                mydict[mylist[g-1]].strip().append(mylist[g-2].strip())
    while True:
        if len(food) == number or len(cal) == 0:
            break
        else:
            upper = max(cal)
            index = cal.index(upper)
            food.append(mydict[upper][0])
            del cal[index]
            del mydict[upper][0]
    return food
    
        
  


"""
Function name: split_bill
Parameters: file (str), num_ppl (int), order (list), tip (float)
Returns: float

"""

def split_bill(file,people,order,tip):
    total= 0
    fh = open(file, "r")
    lines = fh.readlines()
    fh.close()
    for g,w in enumerate(lines):
        lines[g] = w.strip()
        lines[g] = lines[g].lower()
    for g,w in enumerate(order):
        if w.lower() in lines:
            index = lines.index(w.lower())
            total += float(lines[index+3][1:])
    total = total * (1.00 + tip)
    return round(total/people,2)
        


"""
Function name: food_dict
Parameters: file (str), foods(list)
Returns: dictionary

"""
def food_dict(file, foods):
    mydict = {}
    fh = open(file,"r")
    lines = fh.readlines()
    fh.close()
    for g,w in enumerate(lines):
        lines[g] = w.strip()
    for g,w in enumerate(foods):
        foods[g] = w.lower()
    for g,w in enumerate(lines):
        if w.lower() in foods:
            mydict[w]= (float(lines[g+3][1:]),int(lines[g+1]))
    return mydict



"""
Function name: budget_outfit
Parameters: file (.csv file)
Returns: dictionary

"""

def budget_outfit(file):
    categories = []
    total = 0
    price= []
    name = []
    prices = {}
    mydict = {}
    fh = open(file, "r")
    header = fh.readline()
    data = fh.readlines()
    for thing in data:
        thing = thing.strip()
        column = thing.split(',')
        prices[column[0]] = (column[2], float(column[1]))
    for thing in data:
        thing = thing.strip()s
        if column[2] not in categories:
            categories.append(column[2])
            price.append([])
            name.append([])
    for thing in prices:
        index = categories.index(prices[thing][0])
        price[index].append(prices[thing][1])
        name[index].append(thing)
    for g,w in enumerate(price):
        lower = min(w)
        total += lower
        index = w.index(lower)
        mydict[categories[g]] = name[g][index]
        mydict["total price"] = round(total,2)
    return mydict

        
        
                                 
        
        
        
        
    


        



"""
Function name: sort_by_rating
Parameters: file (.csv file), category (string), order (boolean)
Returns: None

"""

def sort_by_rating(file, category, order):
    fh = open(file, 'r')
    heading = fh.readline()
    heading = heading.split(",")
    lines = fh.readlines()
    fh.close()
    tuplist = []
    for line in lines:
        sep = line.split(",")
        if sep[2] == category:
            tuplist.append((float(sep[3].strip()),sep[0]))
    tuplist.sort()
    if order == True:
        fh2 = open("sorted_items.csv", 'w')
        fh2.write(heading[0] + ", " + heading[3])
        for thing in tuplist:
            fh2.write(str(thing[1]) +', ' + str(thing[0]) + "\n")
    
    else:
        fh2 = open("sorted_items.csv", 'w')
        fh2.write(heading[0] + ", " + heading[3])
        tuplist = tuplist[::-1]
        for thing in tuplist:
            fh2.write(str(thing[1]) + ', ' + str(thing[0]) + "\n")
    fh2.close()
            

    
