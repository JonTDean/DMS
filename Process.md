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

	2. Date has two types `M-D-YYYY` and `M/D/YYYY`. The output should be of a single type denoting `M/D/YYYY`.


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

The way the data exists across the files is different. M and F exist in the psv and ssv files, represented as Male and Female respectively inside of csv.

Another thing to check for is the placement of `FavoriteColor` in accordance to `DOB`. In PSV/CSV `FavoriteColor` is prior to `DOB` and in SSV it is after.

Based on what is known our Line by line output standard should exist as:

``{last name}, {first name}, {gender}, {date of birth}, {favorite color}``
where DOB === M/D/YYYY

----

## Process 
At the moment I will design the functionality to be delimiter specific, since the pattern itself is delimiter specific. By attaching my logic to directly to the delimiter I'm indirectly attaching the logic directly to the pattern, which won't be a problem due to the static nature of the dataset itself. I.e. Firstnames are always strings, lastnames are always strings, etc. and the pattern in which they exist is always the same, allowing the logic to attach directly to the idemopotent pattern of the dataset.

The data is now cleaned up and I plan to create the sorting methods. 

Sort Output 1: 
- Sort 1
	1. Females First Males Last
	2. Sort each group by name order

		1.1 In order to do this I need to split

		1.2 the genders into two groups and

		1.3 then sort the groups by lastName Ascending

	3. The result should look like: 
		- Hingis Martina Female 4/2/1979 Green
		- Kelly Sue Female 7/12/1959 Pink
		- Kournikova Anna Female 6/3/1975 Red
		- Seles Monica Female 12/2/1973 Black
		- Abercrombie Neil Male 2/13/1943 Tan
		- Bishop Timothy Male 4/23/1967 Yellow
		- Bonk Radek Male 6/3/1975 Green
		- Bouillon Francis Male 6/3/1975 Blue
		- Smith Steve Male 3/3/1985 Red

- Sort 2
	1. Sort functionality
		
		1.1 Last Name (Asc): A to Z 
		
		1.2 Birth Date (Asc): Oldest to Youngest
			
		- So this one was a bit confusing on the wording however, the main principal they seem to want is to first sort by A to Z and *then* sort by oldest to youngest, not sort by A to Z *and* sort by oldest to youngest. Analyze and Solve.
				
	
	2. The results should look like:
		- Abercrombie Neil Male 2/13/1943 Tan
		- Kelly Sue Female 7/12/1959 Pink
		- Bishop Timothy Male 4/23/1967 Yellow
		- Seles Monica Female 12/2/1973 Black
		- Bonk Radek Male 6/3/1975 Green
		- Bouillon Francis Male 6/3/1975 Blue
		- Kournikova Anna Female 6/3/1975 Red
		- Hingis Martina Female 4/2/1979 Green
		- Smith Steve Male 3/3/1985 Red

- Sort 3
	1. Sort by last name

		1.1. Lastnames are Z to A

	2. The results should look like:
		- Smith Steve Male 3/3/1985 Red
		- Seles Monica Female 12/2/1973 Black
		- Kournikova Anna Female 6/3/1975 Red
		- Kelly Sue Female 7/12/1959 Pink
		- Hingis Martina Female 4/2/1979 Green
		- Bouillon Francis Male 6/3/1975 Blue
		- Bonk Radek Male 6/3/1975 Green
		- Bishop Timothy Male 4/23/1967 Yellow
		- Abercrombie Neil Male 2/13/1943 Tan