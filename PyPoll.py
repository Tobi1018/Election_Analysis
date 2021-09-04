# The data we need t retrieve.
# 1. The total number of votes cast
# 2. A complete list of canditates who received votes
# 3. The percentage of votes each canditates won
# 4. The totals number of votes each canditates won
# 5. The winner of the election based on popular votes.

# Import the datetime class from the datetime module
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(csv)


#Assigne a variable fo the file to load and the path
file_to_load = 'Election_Analysis/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')


#To do: perform analysis

#Close the file

election_data.close()

# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load =os.path.join("Election_Analysis/election_results.csv")
#Assign a variable to save the file to a path.
file_to_load =os.path.join("Election_Analysis", "election_analysis.txt")

#("analysis", "election_analysis.txt")
#Election_Analysis\election_analysis.txt"
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader =csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)