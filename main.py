def read_file(filename):
	with open(f'data/{filename}.txt', 'r') as f:
		return f.read()
	
csv = read_file('comma');
psv = read_file('pipe');
ssv = read_file('space');

print(csv);
print(psv);
print(ssv);