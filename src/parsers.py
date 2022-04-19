from src.transformers import date_Convert, gender_Dict, output_String

split_Line = lambda data, delim: data.split(delim)

def parse_PSV(data, arr):
		split_Line = data.split(" | ")	# Split each line by the pipe

		# Append the output string
		# to the cleaned data list
		arr.append(
			output_String(			
				split_Line[0],					# Last Name
				split_Line[1],					# First Name
				gender_Dict(split_Line[3]),		# Converted Gender
				date_Convert(split_Line[5]),	# Converted dob
				split_Line[4]					# favorite_color
			)
		);
	
def parse_CSV(data, arr):
	split_Line = data.split(", ")	# Split each line by the comma

	# Append the output string
	# to the cleaned data list
	arr.append(
		output_String(			
			split_Line[0],						# Last Name
			split_Line[1],						# First Name
			split_Line[2],						# Converted gender
			split_Line[4],						# Converted dob
			split_Line[3]						# favorite_color
		)
	);

def parse_SSV(data, arr):
	split_Line = data.split(" ")	# Split each line by the space

	# Append the output string
	# to the cleaned data list
	arr.append(
		output_String(			
			split_Line[0],						# Last Name
			split_Line[1],						# First Name
			gender_Dict(split_Line[3]),			# Converted gender
			date_Convert(split_Line[4]),		# Converted dob
			split_Line[5]						# favorite_color
		)
	);