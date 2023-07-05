Fitness Tracker Development Notes: 

Key Features: 
- Mobile App/
- Track Workouts:
	- Exercise 
	- Weight
	- Reps
	- Sets
- Body Weight Tracker:
	- Add Daily Weight
Data Storage:
- MySQL?
- CSV?
- json?


Notes: 

- Track Workouts:
	- Simple:
	- Complex:
- Body Weight Tracker: 
	- Add Current Weight
	- Retreive Date

30/06/2023 - Notes

- Desired output format 
Exercise Name: "Squat"
Set 1: "{weight}kg for {reps} reps"
Set 2: etc 
Set 3: etc
etc 

01/07/2023 - Notes

- Desired CSV Output 
Exercise	Sets	Weight	Reps	
Squat		1	100	3
Squat		2	120	2
Squat		3	100	5

---Adding Weight Tracking Feature---

- Check .csv file exists 
- Load or create the csv file as a dataframe. 
- Add new entry into the dataframe 
	- Date
	- Weight
- Remove data entry function
- View data frame
- Perform data analysis, (Not Yet Implemented)
	- Changes from previous entry
	- Data visualisation? graph?

To do:
- Add function to open the dataframe in excel (source code can be found in the 4_pane_application for the calorie tracker)



02/07/2023 - Notes 
- Moved the operation interface into a main file 

05/07/2023 - Notes
-Changed the funcitonality of the exercise tracker functions to store data into a DataFrame rather than individual lists. 
- Functions Altered:
	- display_exercises(self)
		- Altered the code to convert the data stored in the Exercises class and Fitness Tracker class from 		a dictionary to a DataFrame and printed it to display the list of added exercises. 
	- export_to_csv(self)
		- takes converts the dictionary of stored data into a dataframe. Either creates a new csv file if 		one is not present or opens the existing csv file (deleting any N/A datapoints). Funciton retrieves 		todays date and insets the date into the DataFrame inputted from the user (not the csv file). This 		DataFrame is the concatenated with the data from the csv file, the new DataFrame is then saved 			under the csv file name. 
- For future features 
	- Include an operator to open the csv file. 
	- Create a data analysis operator that seperates all of the different exercises and analyse progress and 	produce some data visualisations
