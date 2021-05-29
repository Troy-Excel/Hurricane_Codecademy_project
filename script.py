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
conversion = {"M": 1000000,
              "B": 1000000000}


def damage_update():
  for damage_index, damage in enumerate(damages):
    if 'M' in damage:
      damage = float(damage[:-1])  * conversion['M']
      damages[damage_index] = damage
    elif 'B' in damage:
      damage = float(damage[:-1]) * conversion['B']
      damages[damage_index] = damage
    else:
      damages[damage_index] = damage
  return damages
damage_update()


name_dict = {}
def name_as_key():
  for name_index, name in enumerate(names):
    name_dict[name] =  {
    'Name': names[name_index],
    'Month': months[name_index],
    'Year': years[name_index],
    'Max Sustained Wind' : max_sustained_winds[name_index],
    'Areas Affected' : areas_affected[name_index],
    'Damage' : damages[name_index],
    'Deaths' : deaths[name_index]
    }
  return name_dict
name_as_key()
print()
print('Hurricane data by Hurricane name:')
print(name_dict)


# 3
# Organizing by Year

year_dict = {}
def year_as_key():
  list_name_dict = []
  for name_dict_key, name_dict_value in name_dict.items():
    list_name_dict.append(name_dict_value)
  for year_index, year in enumerate(years):
      year_dict[year] = list_name_dict[year_index]    
       
  return year_dict
year_as_key()
print()
print('Hurricane data by year:')
print(year_dict)








#create a list w/ unique elements for areas affected.
area_count_dict = {}
flat_areas = [area for areas in areas_affected for area in areas]
unique_areas = list(set(flat_areas))


#create a functions that counts each area affected by comparing to flat_areas list
def area_count_function():
  for unique_area_index, unique_area in enumerate(unique_areas):
    area_count_dict[unique_area] = sum(x.count(unique_area) for x in flat_areas)
  return area_count_dict
area_count_function()    
print()
print('Number of times each unique area was impacted by a hurricane:')
print(area_count_dict)





# 5 
# Calculating Maximum Hurricane Count

count_list = []
def max_count_function():
  max_count = 0
  name_max = ''
  for area_count_key, area_count_value in area_count_dict.items():
    if area_count_value > max_count:
      max_count = area_count_value
      name_max = area_count_key
  count_list.append(max_count)
  count_list.append(name_max)
max_count_function()
print()
print('The area most impacted by hurricanes:', count_list)    




# 6
# Calculating the Deadliest Hurricane
max_death_list = []
def max_deaths_function():
  max_deaths = 0
  for death_index, death in enumerate(deaths):
    if death > max_deaths:
      max_deaths = death
      max_deaths_index = death_index
  max_death_list.append(max_deaths)
  max_death_list.append(max_deaths_index)
max_deaths_function()
print()
print("Hurricane with the most deaths is:", max_death_list[0], 'death,. for Hurricane', names[max_death_list[1]])
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
mortality_key = []  
mortality_value = []              
mortality_rating_dict = {}
mort_by_rating_list = []
mort_by_rating_index = []
mort_by_rating_dict = {1:[], 2:[], 3:[], 4:[]}
for mortality_scale_key, mortality_scale_value in mortality_scale.items():
  mortality_key.append(mortality_scale_key)
  mortality_value.append(mortality_scale_value)
death_rating_list = []
def mort_rating_function():
  for death_index, death in enumerate(deaths):
    if death <= mortality_value[1]:
      death_rating_list.append(1)
    if death <= mortality_value[2]:
      death_rating_list.append(2)
    if death <= mortality_value[3]:
      death_rating_list.append(3)
    if death <= mortality_value[4]:
      death_rating_list.append(4)
  for name_index, name in enumerate(names):
    mortality_rating_dict[name] = death_rating_list[name_index]
  for mortality_rating_dict_index, mortality_rating_dict_value in mortality_rating_dict.items():
    if mortality_rating_dict_value == 1:
      mort_by_rating_dict[1].append(mortality_rating_dict_index)
    if mortality_rating_dict_value == 2:
      mort_by_rating_dict[2].append(mortality_rating_dict_index)
    if mortality_rating_dict_value == 3:
      mort_by_rating_dict[3].append(mortality_rating_dict_index)
    if mortality_rating_dict_value == 4:
      mort_by_rating_dict[4].append(mortality_rating_dict_index)
      

  return mortality_rating_dict 
mort_rating_function()  
print()
print('Hurricanes by death scale:')
print(mort_by_rating_dict)










# find highest damage inducing hurricane and its total cost
max_damage_list = []
def max_damages_function():
  max_damages = 0
  for damage_index, damage in enumerate(damages):
    if type(damage) != str and damage > max_damages:
      max_damages = damage
      max_damage_index = damage_index
  max_damage_list.append(max_damages)
  max_damage_list.append(max_damage_index)
max_damages_function()
print()
print("Hurricane with the most damage is:", max_damage_list[0], 'dollars in damage, for Hurricane', names[max_damage_list[1]])

# 9
damage_scale = {0: 0,
              1: 100000000,
              2: 1000000000,
              3: 10000000000,
              4: 50000000000}
damage_scale_key = list(damage_scale.keys())
damage_scale_value = list(damage_scale.values())
damage_scale_list = []
damage_scale_dict = {}
damage_by_scale_dict = {1: [], 2: [], 3: [], 4:[]}
def damage_scale_function():

  for damage_index, damage in enumerate(damages):
    if type(damage) != str and damage <= damage_scale_value[1]:
      damage_scale_list.append(1)
    elif type(damage) != str and damage <= damage_scale_value[2]:
      damage_scale_list.append(2)
    elif type(damage) != str and damage <= damage_scale_value[3]:
      damage_scale_list.append(3)
    elif type(damage) != str and damage <= damage_scale_value[4]:
      damage_scale_list.append(4)
    else:
      damage_scale_list.append(damage)
  for damage_scale_list_index, damage_scale_list_value in enumerate     (damage_scale_list):
    if type(damage_scale_list_value) != str and damage_scale_list_value ==    1:
      damage_scale_dict[names[damage_scale_list_index]] = 1
    if type(damage_scale_list_value) != str and damage_scale_list_value == 2:
      damage_scale_dict[names[damage_scale_list_index]] = 2
    if type(damage_scale_list_value) != str and damage_scale_list_value == 3:
      damage_scale_dict[names[damage_scale_list_index]] = 3
    if type(damage_scale_list_value) != str and damage_scale_list_value == 4:
      damage_scale_dict[names[damage_scale_list_index]] = 4
  for damage_scale_dict_key, damage_scale_dict_value in damage_scale_dict.items():
    if damage_scale_dict_value == 1:
      damage_by_scale_dict[1].append(damage_scale_dict_key)
    if damage_scale_dict_value == 2:
      damage_by_scale_dict[2].append(damage_scale_dict_key)    
    if damage_scale_dict_value == 3:
      damage_by_scale_dict[3].append(damage_scale_dict_key)
    if damage_scale_dict_value == 4:
      damage_by_scale_dict[4].append(damage_scale_dict_key)
damage_scale_function()
print()
print("Hurricanes by damages scale:")
print(damage_by_scale_dict) 
  

 

  
# categorize hurricanes in new dictionary with damage severity as key

# Rating Hurricanes by Damage
