import pandas as pd
import csv

categories = {
    1: "FOOD",
    2: "HOME",
    3: "WORK",
    4: "FUN",
    5: "MISC"
}

def request_for_user_expenses():
    data = []

    print (f"SELECT THE CATEGORY,{categories}")
   
    # Prompts for the users data
    item_purchased = input("Enter expense name: ")
    item_category = int(input("Enter the category number of the item: "))
    item_price = float(input("Enter expense price ($): "))
    data.append([item_purchased, categories.get(item_category), item_price])  # Appending the inputs
    return  data


# Function for the opening of the csv file and appending 'a' the provided data. 
# Method used is the write method for the file
def open_file_and_add_new_entries(filename, rows):
    with open(filename, "a", newline="") as file:
        csvwriter = csv.writer(file)
        # Rows will take the data return value from the other function request_for_user_expenses()
        return csvwriter.writerows(rows)

def read_the_file():
    amount_spent_by_category = {}
    filename = "expenses_tracker_app.csv"
    data = pd.read_csv(filename)
    values = data["AMOUNT"].tolist()
    category = data["CATEGORY"].tolist()
    for i in range(len(category)):
        amount_spent_by_category[category[i]] = values[i]

        number_of_entries = amount_spent_by_category.keys()

    return ( sum(values) )
    

# This function utilizes all the above defined function above 
def main():
    # Definition of all the necessary variable
    monthly_budget = 1000
    filename = "expenses_tracker_app.csv"

    # The 'n' variable registers the number of entries our user has to work with.
    # It also controls the number of iteraitions our for loop has to work with
    n = int(input("Please enter the number of expense entries: "))

    # Conditional statement to ensure our user picks the right number of entries and control errors
    if n >= 1:
        # Trying to get the entire sum of all the items entered into the file.
        values = read_the_file()

        for _ in range(n):
            lenght,user_expenses = request_for_user_expenses()
            
            # Conditional to manage the total expenses and inform the user of results
            if 0 <= values <= monthly_budget:
                open_file_and_add_new_entries(filename, user_expenses)
                print("Expense entry added successfully.","\n")
                print(f"Total expenses: {read_the_file()}","\n")
                print(f"Remaining budget: {monthly_budget - read_the_file()}","\n")
                print(f"You have made {lenght} number of entries")
            
            else:
                print("Expense entry added successfully.","\n")
                print(f"Total expenses: {read_the_file()}","\n")
                print(f"Remaining budget: {monthly_budget - read_the_file()}","\n")
                print("Exceeded monthly budget. Entry not added.", "\n")
        
    else:
        print("Invalid number entered. Please enter a number greater than zero.","\n")
        
    # Read the expense data from the CSV file
    data = pd.read_csv(filename)
    
    # Print the data
    print(data)

if __name__ == '__main__':
    main()
