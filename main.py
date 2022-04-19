from operator import itemgetter
from src import files;

# Store all of the cleaned string lines
# into this array for further data analysis.
cleaned_List = [];

# Run the parser process
files.extract_Data(cleaned_List);


print("Output 1: ");

firstSort(cleaned_List);

# # Sort 2 - by birth date, ascending then by last name ascending Sort 3 - by last name, descending
# print("Output 2: ");
# print("Output 3: ");