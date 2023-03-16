'''#a = 34
b = 34
if a == 34 and b == 34:
    print (a + b)
  ##  planets[3] = "Red Planet"
## print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Output: ['Mercury', 'Venus']

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
new_planet = input('Dame el planeta que falta')
planets.append(new_planet)
planet_index = planets.index(new_planet)
print(planet_index)

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))

# Displays Earth

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth

wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError

planet.update({'name': 'Makemake'})

# name is now set to Makemake

planet['name'] = 'Makemake'

# name is now set to Makemake

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709

planet = { 'name': 'Mars',
'moons': 2}
print (f'{planet["name"]} has {planet["moons"]} moons')

planet = { 'name': 'Mars',
'moons': 2}
planet ['circumference (km)'] = {'polar':6752,
'equatorial': 6792}
print (f'{planet["name"]} has {planet["moons"]} moons and a polar circumference of {planet["circumference (km)"]["polar"]}')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# Output:
# There was 10.8cm in the last quarter

planet_moons = {'mercury': 0,
'venus': 0,
'earth': 1,
'mars': 2,
'jupiter': 79,
'saturn': 82,
'uranus': 27,
'neptune': 14,
'pluto': 5,
'haumea': 2,
'makemake': 1,
'eris': 1}
moons = planet_moons.values()
total_planet = len(planet_moons.keys())
total_moons = 0
for value in moons:
    total_moons = total_moons + value
average = total_moons / total_planet
print(f'Every planet has an average of {average} moons')

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
destination = 'Earth'
destination2 = 'Moon'
distance = 0
distance2 = 0
distance = distance_from_earth(destination)
print (distance)

distance2 = distance_from_earth(destination2)
print (distance2)

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
total_days = days_to_complete(238855, 75)
total_days = round(total_days)
print (total_days)

def 
calculadora(num1,num2):

suma = 
num1 + num2

return 
suma

a = int(input('Dame el numero 1: '))

b = int(input('Dame el numero 2: '))

suma = calculadora(a,b)

print(suma)

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

a= arrival_time()
print (a)

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")
a = arrival_time("Mars")
print(a)

def variable_length(*args):
    print(args)
    >>> variable_length()
()
>>> variable_length("one", "two")
('one', 'two')
>>> variable_length(None)
(None,)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
a = sequence_time(4 , 14 ,18, 40, 13, 12, 10)
print (a)

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)'''

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

