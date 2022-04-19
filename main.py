from src import files, sorters;

# Store all of the cleaned string lines
# into this array for further data analysis.
cleaned_List = [];

# Run the parser process
files.extract_Data(cleaned_List);

# First Sort Output
print("Output 1: ");
fs = sorters.firstSort(cleaned_List);
print(fs);

# Second Sort Output
print("Output 2: ");
ss = sorters.secondSort(cleaned_List);
# print(ss);
[print(l) for l in ss];

# Third Sort Output