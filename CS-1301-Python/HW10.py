#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Object-Oriented Programming
"""

__author__ = """Damian Huerta-Ortega"""
__collab__ = """I did this homework alone"""

class Account:
    
    """
    Function name: __init__
    Parameters: self, username, password, screen_plan, profiles
    """
    def __init__(self,username,password,screen_plan,profiles= []):
        self.username = username
        self.password = password
        self.screen_plan = screen_plan
        self.profiles = profiles

    """
    Function name: add_profile
    Parameters: self, profiles
    Returns: str
    """
    def add_profile(self,profiles):
        indicator = False
        for gen in profiles:
            if gen in self.profiles:
                indicator = True
                continue
            else:
                self.profiles.append(gen)
        if indicator == True:
            return "Duplicate profiles"
        else:
            return "All profiles successfully added"

    """
    Function name: remove_profile
    Parameters: self, profiles
    Returns: str
    """
    def remove_profile(self,profiles):
        for gen in profiles:
            if gen not in self.profiles:
                return "Some profiles not found"
            else:
                index = self.profiles.index(gen)
                del self.profiles[index]
        return "All profiles successfully removed"

    """
    Function name: split_cost
    Parameters: self
    Returns: float
    """
    def split_cost(self):
        if self.screen_plan >2:
            cost = (15.99 * 12)/len(self.profiles)
        elif self.screen_plan == 2:
            cost = (12.99 * 12)/len(self.profiles)
        else:
            cost = (8.99*12)/len(self.profiles)
        return cost
    
    def __repr__(self):
        """ This method provides a string representation of the object. Do not modify! """
        return("An Account object under username {} with {} profiles.".format(self.username, len(self.profiles)))

class Profile:

    """
    Function name: __init__
    Parameters: self, name, age, watch_list
    """
    def __init__(self,name,age,watch_list= []):
        self.name = name
        self.age = age
        self.watch_list = watch_list

    
    """
    Function name: can_watch
    Parameters: self, show
    Returns: boolean
    """
    def can_watch(self,show):
        rate = show.rating
        if rate in "TV-YTV-G":
            return True
        elif rate in "TV-Y7TV-PG" and self.age >=7:
            return True
        elif rate == "TV-14" and self.age >=14:
            return True
        elif rate =="TV-MA" and self.age >= 17:
            return True
        else:
            return False


    """
    Function name: recommend
    Parameters: self, other_profile, recommendations
    Returns: int
    """
    def recommend(self, other_profile, recommendations):
        mylist = []
        for show in recommendations:
            if self.can_watch(show) and other_profile.can_watch(show):
                if show not in self.watch_list and show not in other_profile.watch_list:
                    mylist.append(show)
                else:
                    continue
            else:
                continue
        for show in mylist:
            other_profile.watch_list.append(show)
        return len(mylist)


    """
    Function name: shows_by_rating
    Parameters: self
    Returns: dict
    """
    def shows_by_rating(self):
        #mydict = {"TV-Y":[],"TV-G":[],"TV-Y7":[],"TV-PG":[],"TV-14":[],"TV-MA":[]}
        mydict = {}
        shows = self.watch_list
        
        for show in shows:
            rating = show.rating
            
            if rating  == "TV-Y" :
                if "TV-Y" not in mydict.keys():
                    mydict["TV-Y"] = [show]
                else:
                    mydict["TV-Y"].append(show)
            elif rating == "TV-G":
                if "TV-G" not in mydict.keys():
                    mydict["TV-G"] = [show]
                else:
                    mydict["TV-G"].append(show)
            elif rating == "TV-Y7":
                if "TV-Y7" not in mydict.keys():
                    mydict["TV-Y7"] = [show]
                else:
                    mydict["TV-Y7"].append(show)
            elif rating == "TV-PG":
                if "TV-PG" not in mydict.keys():
                    mydict["TV-PG"] = [show]
                else:
                    mydict["TV-PG"].append(show)
            elif rating == "TV-14":
                if "TV-14" not in mydict.keys():
                    mydict["TV-14"] = [show]
                else:
                    mydict["TV-14"].append(show)
            else:
                if "TV-MA" not in mydict.keys():
                    mydict["TV-MA"] = [show]
                else:
                    mydict["TV-MA"].append(show)
        return mydict
        
    """
    Function name: __eq__
    Parameters: self, other
    Returns: boolean
    """
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    
    def __repr__(self):
        """ This method provides a string representation of the object. Do not modify! """
        return "A Profile for {}, age {}.".format(self.name, self.age)
    
class Show:

    """
    Function name: __init__
    Parameters: self, name, seasons, episodes, runtime, rating
    """
    def __init__(self,name, seasons, episodes,runtime,rating):
        self.name = name
        self.seasons = seasons
        self.episodes = episodes
        self.runtime = runtime
        self.rating = rating


    """
    Function name: __eq__
    Parameters: self, other
    Returns: boolean
    """
    def __eq__(self,other):
        return self.name == other.name and self.seasons == other.seasons and self.episodes == other.episodes and self.runtime == other.runtime and self.rating == other.rating

    
    """
    Function name: __gt__
    Parameters: self, other
    Returns: boolean
    """
    def __gt__(self,other):
        return (self.runtime * self.episodes * self.seasons) > (other.runtime * other.episodes * other.seasons)

    
    """
    Function name: __lt__
    Parameters: self, other
    Returns: boolean
    """
    def __lt__(self, other):
        return (self.runtime * self.episodes * self.seasons) < (other.runtime * other.episodes * other.seasons)

   
    """
    Function name: crossover
    Parameters: self, other
    Returns: a Show object
    """
    def crossover(self,other):
        first = self.name.split()[0]
        last = other.name.split()[-1]
        seasons = self.seasons + other.seasons
        episodes = self.episodes + other.episodes
        runtime = self.runtime + other.runtime
        return Show(first + " " + last,seasons,episodes,runtime,self.rating)
    
    def __repr__(self):
        """ This method provides a string representation of the object. Do not modify! """
        return "A Show called {}, rated {}, with {} seasons of {} {}-minute-long episodes each.".format(self.name, self.rating, self.seasons, self.runtime,self.episodes)#h
hi =Account("petra","secret",4)
hi2 = Account("jane_villanueva","secret!",2,["Jane's profile","Rafael's profile"])
print(hi2.add_profile(["Jane's profile","Rafael's profile"]))
print(hi2.profiles)
print(hi2.add_profile(["Alba's profile","Jane's profile","Rafael's profile"]))
print(hi2.profiles)
hi = Show("Arthur",22,10,25,"TV-G")
sup = Profile("Mateo",5,[hi])
print(type(sup.watch_list[0]))
