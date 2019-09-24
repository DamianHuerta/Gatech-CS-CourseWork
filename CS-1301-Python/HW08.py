#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW08 - API/JSON
"""

__author__ = """Damian Huerta-Ortega"""
__collab__ = """I worked on this homework alone"""
import requests as r
from pprint import pprint


"""
Function name: min_pop_countries
Parameters: region (str), num (int)
Returns: list of tuples

"""

def min_pop_countries(region, number):
    url = "https://restcountries.eu/rest/v2/region/"
    fullurl = url + region
    mylist= []
    mylist2 = []
    final = []
    try:
        req  = r.get(fullurl)
        data = req.json()

        for thing in data:
            tup = (thing["name"],thing["population"])
            mylist.append(thing["name"])
            mylist2.append(thing["population"])
        while True:
            if len(final) == number or len(mylist) == 0:
                break
            up = max(mylist2)
            index = mylist2.index(up)
            tup = (mylist[index],mylist2[index])
            final.append(tup)
            del mylist[index]
            del mylist2[index]
        return final
    except:
        return region + " is not a valid region"

    

"""
Function name: can_visit
Parameters: country_code (str), langList (list of strings)
Returns: boolean

"""

def can_visit(code, langlist):
    url = "https://restcountries.eu/rest/v2/alpha/"
    fullurl = url + code
    mylist = []
    count = 0
    req = r.get(fullurl)
    data= req.json()
    lang = data["languages"]
    for thing in lang:
        mylist.append(thing["name"])
    for thing in langlist:
        if thing in mylist:
            count += 1
    if count > 0:
        return True
    else:
        return False

#print(can_visit("SAU", ['Estonian', 'Finnish', 'Greek', 'Indonesian', 'Hungarian', 'Slovak', 'Slovenian', 'French', 'Russian', 'English', 'Portuguese', 'Ukrainian', 'Mandarin', 'Bulgarian', 'Turkish', 'Serbian', 'Italian', 'Danish', 'Croatian', 'Korean', 'German', 'Mandarin', 'Czech', 'Romanian', 'Arabic', 'Georgian', 'Persian', 'Polish', 'Japanese', 'Lithuanian', 'Spanish', 'Swedish', 'Hebrew', 'Dutch', 'Thai', 'French', 'Portuguese', 'Vietnamese', 'Norwegian', 'Spanish', 'Latvian', 'Mandarin', 'Uzbek']))




"""
Function name: valid_directions
Parameters: pathList (list of strings)
Returns: dictionary

"""

def valid_directions(path):
    mydict = {}
    url = "https://restcountries.eu/rest/v2/alpha/"
    for g,w in enumerate(path):
        fullurl= url + w
        req= r.get(fullurl)
        data= req.json()
        if g+1 == len(path):
            mydict[data["nativeName"]] = data["currencies"][0]['symbol']
        elif path[g+1] in data["borders"]:
            mydict[data["nativeName"]] = data["currencies"][0]['symbol']
        else:
            return {}
    return mydict

#print(valid_directions(["FRA", "CHN", "ESP", "SAU"]))


"""
Function name: network_faves
Parameters:  network_id (int), show_list (list of show ids)
Returns: list of shows

"""

def network_faves(net,shows):
    url = "https://api.themoviedb.org/3/network/"+ str(net) +"?api_key=e58e9cfe66b118df3d1d5d9683a19063"
    req = r.get(url)
    data= req.json()
    network = data["name"]
    pop = []
    show = []
    final=[]
    nets= []
    #upper = 0
    used = []
    for code in shows:
        try:
            url = "https://api.themoviedb.org/3/tv/"+ str(code)+"?api_key=e58e9cfe66b118df3d1d5d9683a19063&language=en-US"
            req = r.get(url)
            data = req.json()

            realnet = data['networks']

            for thing in realnet:
                nets.append(thing["name"])
            if network in nets:
                pop.append(data["popularity"])
                show.append(data["name"])
            realnet = []
            nets= []
        except:
            continue
    while True:
        if len(final) == 3 or len(pop) == 0:
            break
        up = max(pop)
        upper = up
        index = pop.index(up)
        final.append(show[index])
        del show[index]
        del pop[index]
    return final

        
        
        
        
        

        
        
        

"""
Function name: valid_movies
Parameters: country_list (list of country codes), movie_list (list of movie ids)
Returns: dictionary

"""

def valid_movies(country,movies):
    diction = {}
    languages = []
    for code in country:
            diction[code] = []
    for code in movies:
        url = "https://api.themoviedb.org/3/movie/" + str(code) +"/translations?api_key=e58e9cfe66b118df3d1d5d9683a19063"
        req = r.get(url)
        data = req.json()
        trans = data["translations"]
        url2= "https://api.themoviedb.org/3/movie/" +str(code)+"?api_key=e58e9cfe66b118df3d1d5d9683a19063&language=en-US"
        req2 = r.get(url2)
        data2 = req2.json()
        name = data2["original_title"]
        for thing in trans:
            languages.append(thing["english_name"])
        #print(languages)
        for code in country:
            result = can_visit(code,languages)
            if result == True:
                diction[code].append(name)
        languages = []
    return diction


        


"""
Function name: superb_chemistry
Parameters: movie_list (list) actor_list (list)
Returns: list

"""
def superb_chemistry(movies,actors):
    films= []
    yes = []
    peeps = []
    acts = []
    for actor in actors:
        full = "https://api.themoviedb.org/3/person/"+ str(actor) +"?api_key=e58e9cfe66b118df3d1d5d9683a19063&language=en-US"
        req = r.get(full)
        data = req.json()
        peep = data["name"]
        peeps.append(data["name"])
        for pos,movie in enumerate(movies):
            full = "https://api.themoviedb.org/3/movie/"+ str(movie) + "/credits?api_key=e58e9cfe66b118df3d1d5d9683a19063"
            req = r.get(full)
            data = req.json()
            cast = data["cast"]
            for thing in cast:
                acts.append(thing["name"])
            if pos + 1 == len(movies) and peep in acts:
                yes.append(peep)
                acts = []
            elif peep in acts:
                continue
                acts = []
            else:
                acts= []
                break
    return yes




#print(superb_chemistry( [272, 155, 49026] , [2524, 1810] ))
