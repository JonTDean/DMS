from operator import itemgetter
from sorters import firstSort
from src import files;

# Store all of the cleaned string lines
# into this array for further data analysis.
cleaned_List = [];

# Run the parser process
files.extract_Data(cleaned_List);

# First Sort Output
print("Output 1: ");
fs = firstSort(cleaned_List);
print(fs);

# Second Sort Output

# Third Sort Output