def read_file(filename):
	with open(f'data/{filename}.txt', 'r') as f:
		return f.read()
	
psv = read_file('pipe').split('\n');
csv = read_file('comma').split('\n');
ssv = read_file('space').split('\n');

# Start on PSV first beacuse its first in the file

# Start on CSV

# Start on SSV Start on the SSV last because 
# we want to call the ssv parser when 
# neither tabs nor commas are present

