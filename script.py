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

#test function by updating damages
def update_damage_list(damage_list):
	updated_damage_list = []

	for each in damage_list:
		if each == "Damages not recorded":	# Adds "Damages not recorded" to Updated list with no changes 
			updated_damage_list.append(each)
		else:								# Converts Ms to 1,000,000 or Bs to 1,000,000,000 from item and appends to list
			if "M" in each :
				num = float(each[0:each.index("M")])
				updated_damage_list.append(num * 1000000) #  <------->   Update these to depend on conversion dict, Hunter
				


			elif "B" in each:
				num = float(each[0:each.index("B")])
				updated_damage_list.append(num * 1000000000)

	return updated_damage_list


print("\n\n UPdated damage list")
print(update_damage_list(damages))


# 2 
# Create a Table
def make_hurricane_table(names, months, years, max_sustained_winds, areas_affected, deaths):
	# Intended result: "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}

	hurricane_table_f = {}
	for n, m, y, msw, aa, d in zip(names, months, years, max_sustained_winds, areas_affected, deaths):
		 hurricane_table_f[n] = m, y, msw, aa, d
	return hurricane_table_f


# Create and view the hurricanes dictionary
hurricane_table = make_hurricane_table(names, months, years, max_sustained_winds, areas_affected, deaths)
for k, v in hurricane_table.items():
	print("\n")
	print("Hurricane {} happened in {}, {} had sustained winds of {}, affected {} and resulted in {} deaths.".format(k, v[0], v[1], v[2], v[3], v[4])) #<-------------------Update Formating on v[3]
#{  hurricane table
#'Cuba I': ('October', 1924, 165, ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 90), 
#'San Felipe II Okeechobee': ('September', 1928, 160, ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 4000), 
#'Bahamas': ('September', 1932, 160, ['The Bahamas', 'Northeastern United States'], 16), 'Cuba II': ('November', 1932, 175, ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 3103), 
#'CubaBrownsville': ('August', 1933, 160, ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 179), 
#'Tampico': ('September', 1933, 160, ['Jamaica', 'Yucatn Peninsula'], 184), 
#'Labor Day': ('September', 1935, 185, ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 408), 'New England': ('September', 1938, 160, ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 682), 
# 'Carol': ('September', 1953, 160, ['Bermuda', 'New England', 'Atlantic Canada'], 5), 
# 'Janet': ('September', 1955, 175, ['Lesser Antilles', 'Central America'], 1023), 
# 'Carla': ('September', 1961, 175, ['Texas', 'Louisiana', 'Midwestern United States'], 43), 
# 'Hattie': ('October', 1961, 160, ['Central America'], 319), 
# 'Beulah': ('September', 1967, 160, ['The Caribbean', 'Mexico', 'Texas'], 688), 
# 'Camille': ('August', 1969, 175, ['Cuba', 'United States Gulf Coast'], 259), 
# 'Edith': ('September', 1971, 160, ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 37), 
# 'Anita': ('September', 1977, 175, ['Mexico'], 11), 
# 'David': ('August', 1979, 175, ['The Caribbean', 'United States East coast'], 2068), 
# 'Allen': ('August', 1980, 190, ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 269), 
# 'Gilbert': ('September', 1988, 185, ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 318), 
# 'Hugo': ('September', 1989, 160, ['The Caribbean', 'United States East Coast'], 107), 
# 'Andrew': ('August', 1992, 175, ['The Bahamas', 'Florida', 'United States Gulf Coast'], 65), 
# 'Mitch': ('October', 1998, 180, ['Central America', 'Yucatn Peninsula', 'South Florida'], 19325), 
# 'Isabel': ('September', 2003, 165, ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 51), 
# 'Ivan': ('September', 2004, 165, ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 124), 
# 'Emily': ('July', 2005, 160, ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 17), 
# 'Katrina': ('August', 2005, 175, ['Bahamas', 'United States Gulf Coast'], 1836), 
# 'Rita': ('September', 2005, 180, ['Cuba', 'United States Gulf Coast'], 125), 
# 'Wilma': ('October', 2005, 185, ['Greater Antilles', 'Central America', 'Florida'], 87), 
# 'Dean': ('August', 2007, 175, ['The Caribbean', 'Central America'], 45), 
# 'Felix': ('September', 2007, 175, ['Nicaragua', 'Honduras'], 133), 
# 'Matthew': ('October', 2016, 165, ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 603), 
# 'Irma': ('September', 2017, 180, ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 138), 
# 'Maria': ('September', 2017, 175, ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 3057), 
# 'Michael': ('October', 2018, 160, ['Central America', 'United States Gulf Coast (especially Florida Panhandle)'], 74)}


# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def organize_by_year(hdict):
	new_dict = {}
	years_fnl = []
	
	for each in hdict.values(): # Update the list of years that had hurricane
		if each[1] not in years_fnl:
			years_fnl.append(each[1])
	#print(years_fnl)

	for y, k, v in zip(years_fnl, hdict.keys(), hdict.values()):
		if y not in new_dict.keys():
			new_dict[y] = dict([(k, v)])
	print(new_dict)
	return new_dict

#print(hurricane_table)
hurricane_table_by_year = organize_by_year(hurricane_table)


#{
#1924: {'Cuba I': ('October', 1924, 165, ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 90)}, 
# 1928: {'San Felipe II Okeechobee': ('September', 1928, 160, ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 4000)},
# 1932: {'Bahamas': ('September', 1932, 160, ['The Bahamas', 'Northeastern United States'], 16)}, 
# 1933: {'Cuba II': ('November', 1932, 175, ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 3103)}, 
# 1935: {'CubaBrownsville': ('August', 1933, 160, ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 179)}, 1938: {'Tampico': ('September', 1933, 160, ['Jamaica', 'Yucatn Peninsula'], 184)}, 
# 1953: {'Labor Day': ('September', 1935, 185, ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 408)}, 
# 1955: {'New England': ('September', 1938, 160, ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 682)}, 
# 1961: {'Carol': ('September', 1953, 160, ['Bermuda', 'New England', 'Atlantic Canada'], 5)}, 
# 1967: {'Janet': ('September', 1955, 175, ['Lesser Antilles', 'Central America'], 1023)}, 
# 1969: {'Carla': ('September', 1961, 175, ['Texas', 'Louisiana', 'Midwestern United States'], 43)}, 1971: {'Hattie': ('October', 1961, 160, ['Central America'], 319)}, 
# 1977: {'Beulah': ('September', 1967, 160, ['The Caribbean', 'Mexico', 'Texas'], 688)}, 
# 1979: {'Camille': ('August', 1969, 175, ['Cuba', 'United States Gulf Coast'], 259)}, 
# 1980: {'Edith': ('September', 1971, 160, ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 37)}, 
# 1988: {'Anita': ('September', 1977, 175, ['Mexico'], 11)}, 1989: {'David': ('August', 1979, 175, ['The Caribbean', 'United States East coast'], 2068)}, 
# 1992: {'Allen': ('August', 1980, 190, ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 269)}, 
# 1998: {'Gilbert': ('September', 1988, 185, ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 318)}, 
# 2003: {'Hugo': ('September', 1989, 160, ['The Caribbean', 'United States East Coast'], 107)}, 
# 2004: {'Andrew': ('August', 1992, 175, ['The Bahamas', 'Florida', 'United States Gulf Coast'], 65)}, 2005: {'Mitch': ('October', 1998, 180, ['Central America', 'Yucatn Peninsula', 'South Florida'], 19325)}, 
# 2007: {'Isabel': ('September', 2003, 165, ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 51)}, 
# 2016: {'Ivan': ('September', 2004, 165, ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 124)}, 
# 2017: {'Emily': ('July', 2005, 160, ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 17)}, 
# 2018: {'Katrina': ('August', 2005, 175, ['Bahamas', 'United States Gulf Coast'], 1836)}}

for p_id, p_info in hurricane_table_by_year.items():
    #print("\nPerson ID:", p_id)
    
    for key in p_info:
       # print(key + ':', p_info[key])
        print("\nIn {} was hurricane(s) {}".format(p_id, p_info.keys()))

# for k, v in hurricane_table_by_year.items():
# 	print("\nIn {} was hurricane(s) {}".format(k, v[0].keys
# 		))


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def times_hit_by_hurricane(hdict):
	areas_affected_list = [] #Is this necessary?
	areas_affected_dict = {}
	for i in areas_affected:
		for each in i:
			if each not in areas_affected_list:
				areas_affected_list.append(each) 


	for v in hurricane_table.values():
		for w in v[3]:
		
   		# Count the number of times each unique value appears and append tthe count to a dictionary. EX: {"Texas": 3, "Bahamas": 4, etc...}
			if w in areas_affected_dict:
				areas_affected_dict[w] = areas_affected_dict[w] + 1
			else:
				areas_affected_dict[w] = 1

 


	
	return areas_affected_dict 

	

times_hit = times_hit_by_hurricane(hurricane_table)




# 5 
# Calculating Maximum Hurricane Count

def hit_most_times(hitdict):
	
	a = max(hitdict, key=hitdict.get)
	all_values = hitdict.values()
	t = max(all_values)

	return a, t
	 

b, s = hit_most_times(times_hit) 
print(b + " was hit the most times with a count of " + str(s) + " times")

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
