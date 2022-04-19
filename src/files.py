from src import parsers;

# Read data from specified file
def read_File(filename):
    with open(f'data/{filename}.txt', 'r') as f:
        return f.read()

# Convert the read data into a list
# of strings that are indexed by <"\n">
# each line represents the next index essentially
def line_List(filename):
    return read_File(filename).split('\n')

# Clean and parse data from the
# data folder located at the root.
def extract_Data(arr):
    # Start on Pipe Separated Values first
    [parsers.parse_PSV(line, arr) for line in line_List('pipe')]
    # Start on CSV next
    [parsers.parse_CSV(line, arr) for line in line_List('comma')]
    # Start on SSV Start on the SSV last
    [parsers.parse_SSV(line, arr) for line in line_List('space')]