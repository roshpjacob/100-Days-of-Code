# The job is to create a function that can add new countries to this list.
# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.
# 
# add_new_country("Brazil", 5, ["Sao Paulo", "Rio d

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(ctr, vis, lst):
    dct = {"country": ctr, "visits": vis, "cities": lst}
    travel_log.append(dct)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
