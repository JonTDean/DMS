# Thought Process

## What is the problem? and how do I solve this?

1. Read the incoming data

		- The first file is a csv
		- The second file is a psv
		- The third file is a ssv

2. Process the incoming data
	
	1. Our data looks like the following where %S is representative of the string format
		- %S can be either <" | "> <" , "> or <" "> 
		
		```python
		("DATA_A %s DATA_B" % (" | " OR " , " OR " "))
		```

	2. Date has two types `MM-DD-YYYY` and `MM/DD/YYYY`. The output should be of a single type denoting `MM/DD/YYYY`.


	3. Our data is not uniform and differs based on the delimiter value.

		- PSV
			- `LastName | FirstName | MiddleInitial | Gender | FavoriteColor | DateOfBirth`

		- CSV 
			- `LastName, FirstName, Gender, FavoriteColor, DateOfBirth`

		- SSV
			- `LastName FirstName MiddleInitial Gender DateOfBirth FavoriteColor`

3. Transform and multiplex the data 

Due to the different (x)sv files having different data patterns, the approach I will be choosing will be to break down the design of each string and extract the patterns that exist. 

Ex: [0] === lastname && [1] === firstname exist in all cases

Things change starting at the 3rd index [2]. In the case of our csv file, we lose the middle initial existing at [2]. 

The way the data exists across the files is different. M and F exist in the psv and ssv files, represented as Male and Female respectively inside of comma.

Another thing to check for is the placement of `FavoriteColor` in accordance to `DOB`. In PSV/CSV it is prior and in SSV it is last.

----

### Process 
At the moment I will design the functionality to be delimiter specific, since the pattern itself is delimiter specific. By attaching my logic to directly to the delimiter I'm indirectly attaching the logic directly to the pattern, which won't be a problem due to the static nature of the dataset itself. I.e. Firstnames are always strings, lastnames are always strings, etc. and the pattern in which they exist is always the same, allowing the logic to attach directly to the idemopotent pattern of the dataset.
