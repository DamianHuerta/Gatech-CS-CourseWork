#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements
"""
__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked on this assignment alone"""

"""
Function name: quick_maths()
Parameters: a number (float), a number (float), an operation (string)
Return value: a float
"""

from math import ceil

def quick_maths(float1,float2,operation):
    if operation == "+":
        add= round(float1 + float2,2)
        return add
    elif operation == "-":
        sub= round(float1 - float2,2)
        return sub
    elif operation == "*":
        mult= round(float1 * float2,2)
        return mult
    elif operation == "/":
        divide= round(float1/float2,2)
        return divide
    elif operation == "%":
        remainder= round(float1%float2,2)
        return remainder
    else:
        return "That operation does not exist!"



"""
Function name: magic_ball()
Parameters: age (int), name (string), year in school (int)
Return value: an int
"""
def magic_ball(age, name, year):
    lucky= age+ len(name)+ year
    if lucky >= 30:
        return 3
    elif lucky >=10:
        return 2
    else:
        return 1



"""
Function name: give_fortune()
#Parameters: mood (a string), age (int), name (string), year in school (int)
#Return value: a fortune (a string)
"""

def give_fortune(mood, age, name, year):
    lucky= magic_ball(age, name, year)
    if mood== "happy" and lucky== 2:
        return "You're going to get 100 on everything!!"
    elif mood == "happy" and lucky == 3:
        return "You're going to get 100 on everything!!"
    elif mood == "happy" and lucky == 1:
        return "You're going to get As!"
    elif mood == "upset" and lucky == 3:
        return "It'll be okay!"
    elif mood == "upset" and lucky == 1:
        return "It's all up to you..."
    elif mood == "upset" and lucky == 2:
        return "It's all up to you..."

"""
Function name: feast()
Parameters: num_apples (int), num_grapes (int), num_oranges (int), activity level (string)
Return value: boolean
"""

def feast(apples, grapes, oranges, activity):
    total_cal= apples* 507 + grapes* 23 + oranges * 296
    if activity=="sedentary":
        cal= 2300
        if total_cal <= cal:
            return True
        else:
            return False
    elif activity == "moderate":
        cal = 2500
        if total_cal <= cal:
            return True
        else:
            return False
    elif activity=="active":
        cal = 2700
        if total_cal <= cal:
            return True
        else:
            return False




"""
Function name: fashion_advice()
Parameters: temperature (float), temperature_unit (string)
Return value: clothing advice (string)
"""

def fashion_advice(temp, temp_unit,):
    if temp_unit == "C":
        newtemp= (temp * (9/5)) + 32
    else:
        newtemp= temp
    if newtemp == 1301:
        return "programmer hat"
    elif newtemp >= 140:
        return "firefighter gear"
    elif newtemp >= 85:
        return "swimsuit"
    elif newtemp >= 60:
        return "t-shirt"
    elif newtemp >= 32:
        return "jacket"
    elif newtemp >= 0:
        return "puffy coat"
    else:
        return "snowsuit"



"""
Function name: cheap_travel()
Parameters: number_of_travellers (int), trip_length (float), transportation_method_A (string), transportation_method_B (string)
Return value: cheaper transportation method (string)
"""

def cheap_travel(num_travelers, length, method1, method2):
    if method1 == "bird":
        cost1 = ((.6 * length)+1.00)* num_travelers
    elif method1 == "uber":
        num_uber= ceil(num_travelers/4)
        cost1 = (num_uber* (1.00 * length)) + 2.00* num_uber
    elif method1 == "relay":
        cost1 = (.70*length)*num_travelers
    elif method1 == "marta":
        cost1 = num_travelers * 2.50
    if method2 == "bird":
        cost2 = ((.6 * length)+1.00)* num_travelers
    elif method2 == "uber":
        num_uber= ceil(num_travelers/4)
        cost2 = (num_uber* (1.00 * length)) + 2.00* num_uber
    elif method2 == "relay":
        cost2 = (.70*length)*num_travelers
    elif method2 == "marta":
        cost2 = num_travelers * 2.50
    if cost1 <= cost2:
        return method1
    else:
        return method2
        








    
