#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
import datetime, pathlib, os, csv


# In[104]:


class Exercise:
    def __init__(self, name, weight, reps, sets):
        """
        Initialises an Exercise object with the parameters.
        
        Parameters:
        - name(str): The name of the exercise.
        - weight(int): The weight used for the exercise.
        - reps(int): The number of repititions performed.
        - sets(int): The number of sets completed
        """
        self.name = name
        self.weight = weight
        self.reps = reps
        self.sets = sets
        
class FitnessTracker:
    def __init__(self):
        """
        Initialise a Fitness Tracker object with an empty list to store exercises into
        """
        self.exercises = {
            "Name":[],
            "Set":[],
            "Reps":[],
            "Weight":[]
        }
    def add_exercise(self, name, weight, reps, sets):
        """
        Adds a new exercise to the trackers with the following parameters
        
        Parameters:
        - name(str): The name of the exercise.
        - weight(int): The weight used for the exercise.
        - reps(int): The number of repititions performed.
        - sets(int): The number of sets completed
        """

        exercise = Exercise(name, weight,reps, sets)
        for i in range(len(exercise.name)):
            self.exercises["Name"].append(exercise.name[i])
            self.exercises["Set"].append(exercise.sets[i])
            self.exercises["Reps"].append(exercise.reps[i])
            self.exercises["Weight"].append(exercise.weight[i])
    
    def display_exercises(self):
        """
        Displays the list of exercises tracked. 
        If no exercises are present, a message indicating no exercises are available to print
        """
        if not self.exercises["Name"]:
            print("No Exercises to display")
        else:
            exercise_df = pd.DataFrame(self.exercises)
            print(exercise_df)
        
    def clear_exercises(self):
        keys = list(self.exercises.keys())
        self.exercises.clear()
        self.exercises = {key: [] for key in keys}
        
    def export_to_csv(self):
        exercise_df = pd.DataFrame(self.exercises)
        
        csv_file = "data/exercise_tracker_glob.csv"
        
        if not os.path.exists(csv_file):
            with open(csv_file, "w", newline="") as file: 
                writer = csv.writer(file)
                writer.writerow(["Date", "Name", "Set", "Reps", "Weight"])
                print("CSV File Successfully Created")
                etg_df = pd.read_csv(csv_file, delim_whitespace=True)
        else:
            csv_file = "data/exercise_tracker_glob.csv"
            etg = pd.read_csv(csv_file).dropna(how="any")
            etg_df = pd.DataFrame(etg)
            
        todays_date = datetime.date.today().strftime("%d/%m/%Y")
        exercise_df["Date"] = todays_date
        column_order = ["Date", "Name", "Set", "Reps", "Weight"]
        output_df = exercise_df[column_order]
        
        merge_df = [etg_df, exercise_df]
        csv_df = pd.concat(merge_df, ignore_index = True)
        csv_df.to_csv("data/exercise_tracker_glob.csv", index = False)
                


# In[102]:




