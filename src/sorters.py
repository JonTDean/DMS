# Sort 1 - 
# (FM->LN Ascend) Sort
def firstSort(lst):
	return sorted(
		lst, # Sort by -> Gender			  Last Name 
		key=lambda line: (line.split(" ")[2], line.split(" ")[0]),
	);

# Sort 2 -
# 
# def secondSort(lst):

# Sort 3 -
# Madness Sort
# def thirdSort(lst):
