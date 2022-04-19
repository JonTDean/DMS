# Standardize the date string so I don't have to 
# rewrite this x times.
def output_String(last_name, first_name, gender, dob, fc):
	return f"{last_name} {first_name} {gender} {dob} {fc}";

# Convert an initial to it's full capitalized name.
def gender_Dict(gender):
	return {
		"m": "Male",					#if
		"f": "Female",					#elseif		
	}.get(gender.lower(), "Other");		#else

# Convert Date time to it's appropriate format
def date_Convert(dt):
	if "-" in dt:						# Check for MM-DD-YYYY format
		return dt.replace("-", "/");	# Convert to MM/DD/YYYY format
	else:
		return dt;						# Return MM/DD/YYYY format