# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def damages_convert(damages_list):
  new_damages = []
  conversion = {"M": 1000000, "B": 1000000000}
  for item in damages_list:
    if "B" in item:
      item = item.strip("B")
      item = float(item)
      item = item * conversion.get("B")
      new_damages.append(item)
    elif "M" in item:
      item = item.strip("M")
      item = float(item)
      item = item * conversion.get("M")
      new_damages.append(item)
    else:
      new_damages.append(item)
  print(new_damages)
  return new_damages

# test function by updating damages
updated_damages = damages_convert(damages)
# 2 
# Create a Table
def hurricane_name_function(h_name, h_months, h_years, h_max_wind_speed, h_areas_affected, h_damage, h_deaths):
  new_dict = {}
  for a in range(len(h_name)):
    new_dict[a] = {
      "Name": h_name[a], 
      "Month": h_months[a], 
      "Year": h_years[a], 
      "Max Sustained Wind": h_max_wind_speed[a], 
      "Areas Affected": h_areas_affected[a], 
      "Damage": h_damage[a], 
      "Deaths": h_deaths[a]}
  print(new_dict)


# Create and view the hurricanes dictionary
years_dict = {}

for n, m, y, w, a, d, t in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  years_dict.update({y: [{"Name": n, "Month": m, "Year": y, "Max Sustained Wind": w, "Areas Affected": a, "Damage": d, "Deaths": t}]})


# 3
# Organizing by Year
for n, m, y, w, a, d, t in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  years_dict.update({y: [{"Name": n, "Month": m, "Year": y, "Max Sustained Wind": w, "Areas Affected": a, "Damage": d, "Deaths": t}]})
# create a new dictionary of hurricanes with year and key
print(years_dict)

# 4
# Counting Damaged Areas
areas_dict = {}

for area in areas_affected:
  for i in area:
    if i not in areas_dict:
      areas_dict[i] = 1
    else:
      areas_dict[i] += 1
  
# create dictionary of areas to store the number of hurricanes involved in
      
# 5 
# Calculating Maximum Hurricane Count

def max_areas_affected(areas_count):
  max_area_count = 0
  max_area = ""
  for area in areas_count:
    if areas_count[area] > max_area_count:
      max_area_count = areas_count[area]
      max_area = area
    return max_area_count, max_area
      
# find most frequently affected area and the number of hurricanes involved in
print(max_areas_affected(areas_dict))

# 6
# Calculating the Deadliest Hurricane
def find_most_deaths(hurricanes):
    max_deaths_hurricane = ""
    max_death_count = 0
    for hurr in hurricanes:
        if hurricanes[hurr]["Deaths"] > max_death_count:
            max_deaths_hurricane = hurr
            max_death_count = hurricanes[hurr]["Deaths"]
    return max_deaths_hurricane, max_death_count

# find highest mortality hurricane and the number of deaths
print(find_most_deaths(areas_dict))
  
# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key