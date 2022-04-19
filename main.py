from src import files, sorters, meta;

# Store all of the cleaned string lines
# into this array for further data analysis.
cleaned_List = [];

# Run the parsing process, this extracts
# the data from each file and cleans it.
# Applying the appropriate string 
# transformations to the data.
files.extract_Data(cleaned_List);

print(cleaned_List);

# Run sorts and store them
# # First Sort Output
fs = sorters.first_Sort(cleaned_List);
# # Second Sort Output
ss = sorters.second_Sort(cleaned_List);
# # Third Sort Output
ts = sorters.third_Sort(cleaned_List);

# Log all the data for the project
meta.log_Data(fs, ss, ts);

# Write the data to files for manual analysis
meta.write_Data(fs, ss, ts);