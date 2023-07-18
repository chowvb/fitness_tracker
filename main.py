import weight_tracker_functions as wtf
import exercise_tracker_functions as etf

def main():
    """
    main() doesn't take any extra parameters, prints out in the CLI (command line interface) a series of 
    operators and what their functions are. The CLI application is run on a while loop until the quit 
    operator is selected. 

    option 1 -> runs the weight tracker applicaiton functions, with another CLI user operator input 
    option 2 -> runs the exercise tracking application function defined within this script however, 
    it calls upon functions and variables in the exercise_tracker_functions.

    The User will input one of the displayed operators in the to progress to the next CLI line.
    """
    main_loop = False 
    
    while not main_loop:
        print(
            """
            (1): Weight Tracker
            (2): Exercise Tracker
            (q): Quit
            """)
        option = input("Please input an operator: ")
        
        if option == "1":
            weight_function()
        if option == "2":
            exercise_function()
        if option == "q":
            main_loop = True


def exercise_function():
    """
    Initiates the FitnessTracker Class called from the module fitness_tracker_functions. 
    Prints into the command line a options for the operator to input a number or (b) for back to the main loop


    """
    tracker = etf.FitnessTracker()
    Loop = False
    while not Loop: 
        print("""
        (1): Add Exercise To Workout
        (2): Display Exercises In Workout
        (3): Clear Exercise List
        (4): Export to CSV
        (b): Back
        """)
        option = input("Choose an Option:")
        if option == "1":
            # CLI then asks for the User to input the required variables for the .csv file.
            # these inputs are then passed into the .add_exercise as parameters in the exercise_tracker_funcitons
            name = input("Exercise Name: ")
            sets = int(input("Sets:"))
            name_list = []
            sets_list = []
            reps_list = []
            weight_list = []

            for count in range(sets):
                weight = int(input("Weight(kg):"))
                reps = int(input("For Reps: "))
                name_list.append(name)
                sets_list.append(count + 1)
                reps_list.append(reps)
                weight_list.append(weight)
            tracker.add_exercise(name_list, weight_list, reps_list, sets_list)

        if option == "2":
            tracker.display_exercises()

        if option == "3":
            tracker.clear_exercises()

        if option == "b":
            Loop = True

        if option == "4":
            tracker.export_to_csv() 

def weight_function():
    """
    Runs the weight tracking feature of the application, the module was imported as wtf
    """
    loop = False
    tracker = wtf.WeightTracker()
    tracker.check_csv()

    while not loop:
        print("""
        (1): View Weight Tracker
        (2): Add Todays Weight
        (3): Remove A Data Entry
        (4): Open Database 
        (b): Back
        """)
        
        option = input("Please Chose an Option: ")

        if option == "1":
            tracker.view_weight()

        if option == "2":
            weight_input = input("Input Todays Weight: ")
            tracker.update_csv(weight_input)

        if option == "3":
            data_preview = pd.read_csv("data/weight_tracker.csv")
            first_row = 0
            last_row = len(data_preview)-1
            print(data_preview)
            option_3_loop = False
            while not option_3_loop:
                row_to_remove = int(input("Please input the row to be removed: "))
                if first_row <= row_to_remove <= last_row:
                    row = row_to_remove
                    option_3_loop = True
                else:
                    print("Incorrect Input")
            tracker.remove_entry(row)
            tracker.view_weight()

        if option == "4":
            tracker.open_database()

        if option == "b":
            loop = True


main()
