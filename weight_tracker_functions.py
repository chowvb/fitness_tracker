#!/usr/bin/env python
# coding: utf-8
import pathlib, os, csv, datetime
import pandas as pd


# Create a class to store all variables to be used in. 
class WeightTracker:

    def check_csv(self):
        """
        This funciton checks whether there is a .csv file present to store data into, 
        If there is no file present then one shall be created.
        If the .csv file is located within the correct directory then it will be read and converted into a dataframe.
        """
        csv_file = "fitness_tracker/data/weight_tracker.csv"
        if not os.path.exists(csv_file):
            with open(csv_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date","Weight"])
            print("CSV file successfully created")
        else:
            print("\nCSV file loaded")
            df = pd.read_csv(csv_file).dropna(how="any")
            df.to_csv(csv_file,index=False)
        
    def update_csv(self, weight):
        """
        Update_csv, creates a dictionary which includes the current date and the recorded weight inputted from the user.
        self = self
        weight = inputted value from the user from the CLI when main.py is executed
        """
        csv_file = "fitness_tracker/data/weight_tracker.csv"
        weight_df = pd.read_csv(csv_file)
        
        new_data = {
            "Date": [],
            "Weight": []
        }
        
        # Obtain todays date from the operating system
        todays_date = datetime.date.today().strftime("%d/%m/%Y")

        # Append the dictionary with todays date and the inputted weight that is passed through from main.py
        new_data["Date"].append(todays_date)
        new_data["Weight"].append(weight)

        # Create a dataframe with the date and weight 
        new_data_df = pd.DataFrame(new_data)

        # Join the new data with the data read from the .csv file as a new dataframe
        updated_weight_df = pd.concat([weight_df, new_data_df], ignore_index=True)

        # Save the new dataframe to a .csv file (Removes contents but the contents are stored in weight_df and re-added)
        updated_weight_df.to_csv("fitness_tracker/data/weight_tracker.csv",index=False)
    
    def view_weight(self):
        """
        Prints the .csv file out into the CLI
        """
        csv_file = "fitness_tracker/data/weight_tracker.csv"
        weight_df = pd.read_csv(csv_file)
        print("\n",weight_df)
    
    def remove_entry(self, row):
        """
        This funciton is to be used to remove a specified row of the .csv file if an incorrect input is made. 
        self = self 
        row = Row number inputted by the user (A dataframe preview is printed with the row numbers in main.py to allow 
        the user to identify which row they wish to remove))
        """

        # Read csv file
        csv_file ="fitness_tracker/data/weight_tracker.csv"
        df = pd.read_csv(csv_file)

        # Drop the row number specified in the included function argument
        df_dropped = df.drop(row)

        # Rewrite and save the new csv file 
        df_dropped.to_csv(csv_file,index=False)
        print("Row Deleted Successfully\n")

    def open_database(self):
        """
        Open the database in the default programm that is used to read the csv file. 
        """
        # Identify the path location 
        file_dir = pathlib.Path("fitness_tracker/data/weight_tracker.csv")

        # Open the file using the os module
        os.startfile(file_dir)

