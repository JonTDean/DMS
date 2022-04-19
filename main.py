from src import parser;

cleaned_Data = [];

# Read data from specified file
def read_File(filename):
	with open(f'data/{filename}.txt', 'r') as f:
		return f.read();
	
# Convert the read data into a list
# of strings that are indexed by <"\n">
# each line represents the next index essentially
def line_List(filename):
	return read_File(filename).split('\n');

# Clean and parse data from the
# data folder located at the root.
def parser_Engine():

	# Start on Pipe Separated Values first 
	[parser.parse_PSV(line ,cleaned_Data) for line in line_List('pipe')];
	
	# Start on CSV next
	[parser.parse_CSV(line, cleaned_Data) for line in line_List('comma')];
	
	# Start on SSV Start on the SSV last
	[parser.parse_SSV(line, cleaned_Data) for line in line_List('space')];

parser_Engine();

# print("CLEANED DATA: \n", cleaned_Data);
[print(l) for l in cleaned_Data];