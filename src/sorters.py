# Sort 1 - 
# (FM->LN Ascend) Sort
def firstSort(lst):
	return sorted(
		lst, # Sort by -> Gender			  Last Name 
		key=lambda line: (line.split(" ")[2], line.split(" ")[0]),
	);

# Sort 2 -
# by birth date, ascending 
# then by last name ascending 
# 
def secondSort(lst):
	return sorted(
		lst,
		key=lambda line: (line.split(" ")[3], line.split(" ")[0]),
	);

# Sort 3 -
# 1. Lastnames are Z to A
# 2. Firstnames are A to Z
# 3. DOBs are Youngest to Oldest
def thirdSort(lst):
	return sorted(
		lst,
		key=lambda line: line.split(" ")[0],
		reverse=True,
	);
