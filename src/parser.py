# from main import output_String;

from posixpath import split


def output_String(last_name, first_name, gender, dob, fc):
	return f"{last_name} {first_name} {gender} {dob} {fc}";

def parse_PSV(data, arr):
		split_Line = data.split(" | ")	# Split each line by the pipe

		# Append the output string
		# to the cleaned data list
		arr.append(
			output_String(			
				split_Line[0],			# Last Name
				split_Line[1],			# First Name
				split_Line[3],			# gender
				split_Line[5],			# dob
				split_Line[4]			# favorite_color
			)
		);
	
def parse_CSV(data, arr):
	split_Line = data.split(", ")	# Split each line by the pipe

	# Append the output string
	# to the cleaned data list
	arr.append(
		output_String(			
			split_Line[0],			# Last Name
			split_Line[1],			# First Name
			split_Line[2],			# gender
			split_Line[4],			# dob
			split_Line[3]			# favorite_color
		)
	);

def parse_SSV(data, arr):
	split_Line = data.split(" ")	# Split each line by the pipe

	# Append the output string
	# to the cleaned data list
	arr.append(
		output_String(			
			split_Line[0],			# Last Name
			split_Line[1],			# First Name
			split_Line[3],			# gender
			split_Line[4],			# dob
			split_Line[5]			# favorite_color
		)
	);