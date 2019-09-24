#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements
"""
__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked on the homework alone"""

from math import ceil

"""
Function name: cookie_cost()
Parameters: N/A
Return value: N/A
"""

def cookie_cost():
    choco= input('How many chocolate cookies would you like? ')
    oat= input('How many oatmeal cookies would you like? ')
    peanut= input('How many peanut butter cookies would you like? ')
    cost = round(float(choco) * 4 + float(oat) * 2.75 + float(peanut) * 3.5, 2)
    print('{} chocolate cookies, {} oatmeal cookies, and {} peanut butter cookies would cost ${}.'.format(choco, oat, peanut, cost))
    



"""
Function name: shortcut()
Parameters: N/A
Return value: N/A
"""

def shortcut():
    width= input('What is the width of Tech Green? ')
    length= input('What is the length of Tech Green? ')
    diag= round((float(width)**2 + float(length)**2)**.5, 2)
    print('Tech Green with length {} on one side and {} on the other side has a diagonal length of {}.'.format(float(width), float(length), diag))



"""
Function name: eating_out()
Parameters: N/A
Return value: N/A
"""

def eating_out():
    times_out= (input('How many times do you plan yo eat out this week? '))
    job_A= round((int(times_out)* 10.75)/ 7.25)
    job_B= round((int(times_out)* 10.75)/8)
    print('To eat out {} times this week, you would have to work {} hours at job A or {} hours at job B.'.format(times_out, job_A, job_B))

          

"""
Function name: textbooks()
Parameters: N/A
Return value: N/A
"""

def textbooks():
    txtbook= int(input('How many textbooks do you have?'))
    shelves= ceil((txtbook*1.5)/ 15)
    case= ceil(shelves/5)
    print('You need {} shelves to store {} textbooks, so you need to buy {} bookcases.'.format(shelves, txtbook, case))
    


"""
Function name: split_bill()
Parameters: pizza_cost, tax_percent
Return value: total_cost
"""

def split_bill(pizza_cost, tax_percent):
    people= int(input('What is the total number of people?'))
    cost= float(pizza_cost* (1+tax_percent))
    tip= float(input('What percent would you like to tip?'))
    costtip= cost*tip + cost
    perperson= round(costtip/people,2)
    total_cost= float(perperson)
    return total_cost


    

 


