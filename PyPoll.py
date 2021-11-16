# The dat we need to retrieve
# Open the election results and read the file.
# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# A complete list of candidates who recieved votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote