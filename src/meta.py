# Log all the data for the project
def log_Data(fs, ss, ts):
	# First Sort Output
	print("Output 1: ");
	[print(l) for l in fs]

	# Second Sort Output
	print("\nOutput 2: ");
	[print(l) for l in ss];

	# Third Sort Output
	print("\nOutput 3: ");
	[print(l) for l in ts]

# Write the data to files for manual analysis,
# overwriting any existing files with the same name.
def write_Data(fs, ss, ts):
	# Master Sort Output 
	with open("out/output.txt", "w") as f:
		f.write("Output 1: \n");
		[f.write(l + "\n") for l in fs]
		f.write("\nOutput 2: \n");
		[f.write(l + "\n") for l in ss];
		f.write("\nOutput 3: \n")
		[f.write(l + "\n") for l in ts];


	# First Sort Output
	with open("out/output1.txt", "w") as f:
		f.write("Output 1: \n");
		[f.write(l + "\n") for l in fs]

	# Second Sort Output
	with open("out/output2.txt", "w") as f:
		f.write("Output 2: \n");
		[f.write(l + "\n") for l in ss];

	# Third Sort Output
	with open("out/output3.txt", "w") as f:
		f.write("Output 3: \n");
		[f.write(l + "\n") for l in ts];
