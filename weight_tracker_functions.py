#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pathlib, os, csv, datetime
import pandas as pd


# In[7]:


class WeightTracker:
    def check_csv(self):
        csv_file = "data/weight_tracker.csv"
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
        csv_file = "data/weight_tracker.csv"
        weight_df = pd.read_csv(csv_file)
        
        new_data = {
            "Date": [],
            "Weight": []
        }
        
        todays_date = datetime.date.today().strftime("%d/%m/%Y")
        new_data["Date"].append(todays_date)
        new_data["Weight"].append(weight)
        new_data_df = pd.DataFrame(new_data)
        updated_weight_df = pd.concat([weight_df, new_data_df], ignore_index=True)
        updated_weight_df.to_csv("data/weight_tracker.csv",index=False)
    
    def view_weight(self):
        csv_file = "data/weight_tracker.csv"
        weight_df = pd.read_csv(csv_file)
        print("\n",weight_df)
    
    def remove_entry(self, row):
        csv_file ="data/weight_tracker.csv"
        df = pd.read_csv(csv_file)
        df_dropped = df.drop(row)
        df_dropped.to_csv(csv_file,index=False)
        print("Row Deleted Successfully\n")

    def open_database(self):
        file_dir = pathlib.Path("data/weight_tracker.csv")
        os.startfile(file_dir)
    


