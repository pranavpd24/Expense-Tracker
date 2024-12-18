# importing important libraries
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#defining fie
CSV_FILE="expenses.csv"

#intializing the csv file

def intialize_csv():
    try:
        with open(CSV_FILE,"x",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass
    
#adding expenses
def add_Expense(amount, category, description):
    with open(CSV_FILE, "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow([datetime.now().strftime("%d-%m-%Y"), amount, category, description])
    print("Expense added successfully")

#Viewing expenses
def view_Expense():
    try:
        df=pd.read_csv(CSV_FILE)
        print("\nAll Expenses: ")
        print(df.to_string(index=False))
    except FileNotFoundError:
        print("No Expenses added. Add an expense to start.")


#Viewing Expenses for Duration
def view_durationExpenses(start_date, end_date):
    try:
        df=pd.read_csv(CSV_FILE, parse_dates=["Date"], dayfirst=True)
        filtered=df[(df["Date"]>=pd.to_datetime(start_date,dayfirst=True))& (df["Date"]<=pd.to_datetime(end_date,dayfirst=True))]
        if not filtered.empty:
            print(f"\nExpenses form {start_date} to {end_date}")
            print(filtered.to_string(index=False))
        else:
            print(f"No Expenses found between {start_date} and {end_date}")
    except FileNotFoundError:
        print("No expense found. Add expenses to start")
    except ValueError:
        print("Invalid date format. Please use 'dd-mm-yyyy'.")


#Viewing Expenses by category
def view_expense_byCategory(category):
    try:
        df=pd.read_csv(CSV_FILE)
        filtered=df[df["Category"].str.lower()==category.lower()]
        if not filtered.empty:
            print(f"\nExpenses for category {category}: ")
            print(filtered.to_string(index=False))
        else:
            print(f"No Expenses found for the category {category}.")
    except FileNotFoundError:
        print("No Expenses added. Add an expense to start.")

#Generating whole report
def generate_report():
    try:
        df=pd.read_csv(CSV_FILE)
        category_sums=df.groupby("Category")["Amount"].sum()
        plt.pie(category_sums, labels=category_sums.index, autopct="%1.1f%%",startangle=140)
        plt.title("Expense Distribution by Category")
        plt.show()
    except FileNotFoundError:
        print("No Expenses added. Add an expense to start.")
    except ValueError:
        print("No data to generate a report")

def main_menu():
    intialize_csv()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Expenses by start date and end date")
        print("5. Generate Expense Report")
        print("6. Exit")

        choice=input("Enter your choice(1-5): ")
        if choice=="1":
            try:
                amount=float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Travel): ")
                description = input("Enter description: ")
                add_Expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please Try again.")
        elif choice=="2":
            view_Expense()
        elif choice=="3":
            category=input("Enter category to filter by: ")
            view_expense_byCategory(category)
        elif choice=="4":
            print("Enter Dates in 'dd-mm-yyyy' format.")
            start_date=input("Enter Starting Date: ")
            end_date=input("Entern End Date: ")
            view_durationExpenses(start_date, end_date)
        elif choice=="5":
            generate_report()
        elif choice=="6":
            print("Exiting Expense Tracker. Good BYE!!!")
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__=="__main__":
    main_menu()
            
    




