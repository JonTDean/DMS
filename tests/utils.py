import random;

clean_List = [
	'Smith Steve Male 3/3/1985 Red',
	'Bonk Radek Male 6/3/1975 Green', 
	'Bouillon Francis Male 6/3/1975 Blue', 
	'Abercrombie Neil Male 2/13/1943 Tan', 
	'Bishop Timothy Male 4/23/1967 Yellow', 
	'Kelly Sue Female 7/12/1959 Pink', 
	'Kournikova Anna Female 6/3/1975 Red', 
	'Hingis Martina Female 4/2/1979 Green',
 	'Seles Monica Female 12/2/1973 Black'
];

# 
def shuffle_Clean_List():				# Randomize the index pos
	return sorted(clean_List, key=lambda _: random.random())