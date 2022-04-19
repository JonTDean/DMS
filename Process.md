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


