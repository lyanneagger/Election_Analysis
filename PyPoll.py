<<<<<<< HEAD
# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print (row)

    # To do: perform analysis
    print(election_data)
    

#Using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:

    #Write three counties to the file
=======
# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to ssave the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print (row)

    # To do: perform analysis
    print(election_data)
    

#Using the with statement open the file as a text file
with open(file_to_save,"w") as txt_file:

    #Write three counties to the file
>>>>>>> cc542b727e9f253a528602af6cb979e09c06ef29
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")