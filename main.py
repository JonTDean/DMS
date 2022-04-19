from src import files;

# Store all of the cleaned string lines
# into this array for further data analysis.
cleaned_List = [];

# Run the parser process
files.extract_Data(cleaned_List);

# Output the data to the console
print("CLEANED DATA:");
[print(line) for line in cleaned_List];
print("---------------------------------");

# Sort 1 - 
# # 1. Females First Males Last
# # 2. Sort each group by name order
# # # In order to do this I need to split
# # # the genders into two groups and
# # # then sort the groups by lastName Ascending
# # # joining the result to be: 
# # # # Hingis Martina Female 4/2/1979 Green
# # # # Kelly Sue Female 7/12/1959 Pink
# # # # Kournikova Anna Female 6/3/1975 Red
# # # # Seles Monica Female 12/2/1973 Black
# # # # Abercrombie Neil Male 2/13/1943 Tan
# # # # Bishop Timothy Male 4/23/1967 Yellow
# # # # Bonk Radek Male 6/3/1975 Green
# # # # Bouillon Francis Male 6/3/1975 Blue
# # # # Smith Steve Male 3/3/1985 Red
print("Output 1: ");

# Sort 2 - by birth date, ascending then by last name ascending Sort 3 - by last name, descending
print("Output 2: ");
print("Output 3: ");