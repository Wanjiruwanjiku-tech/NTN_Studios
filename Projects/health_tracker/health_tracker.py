import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime




# File to Update
DATA_FILE = 'data.csv'

# Ensure the file exists. If not use pandas to create a new csv file
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['date', 'disease', 'cases', 'location'])
    df.to_csv(DATA_FILE, index=False)

# Main function
def main():
    while True:
        print("\nCommunity Health Tracker")
        print("1. Add Report")
        print("2. View Summary")
        print("3. Trends")
        print("4. Exit")

        # User input
        choice = input("Choose an option(1-4): ")

        if choice == '1':
            pass
        if choice == '2':
            pass
        if choice == '3':
            pass
        if choice == '4':
            print("Goodbye...")
            break

# The Main function to run
if __name__ == "__main__":
    main()