# Sort 1 - 
# GENDER female === 1 male === -1
# LN Ascending
# (FM->LN (ASC)) Sort
def firstSort(lst):
	return sorted(
		lst, # Sort by -> Gender			  Last Name 
		key=lambda line: (line.split(" ")[2], line.split(" ")[0]),
	);

# Sort 2 -
# Birth Date, Ascending 
# Last Name, Ascending
# (DOB_YYYY (ASC) -> THEN (LN (ASC))) Sort 
def secondSort(lst):
	return sorted(
		sorted(
			lst,
			key=lambda line: line.split(" ")[0],			# Sort by Last Name
		),
		key=lambda line: line.split(" ")[3].split("/")[2],	# Sort by DOB -> YYYY
	);

# Sort 3 -
# Lastnames are Z to A
# (LN DESC) Sort
def thirdSort(lst):
	return sorted(
		lst,
		key=lambda line: line.split(" ")[0],				# Sort by Last Name Descending
		reverse=True,
	);
