# Election Audit Analysis

## Overview of Project

### Purpose

This analysis uses Python to determine candidate votes in total and per county, then prints the results to a single text file for ease of use and reading.




## Election-Audit Results

- A total of 369,711 votes were cast in this congressional election.
- Denver County had 82.8% of the total votes (306,055 votes).<br>
  Jefferson County had 10.5% of the total votes (38.855 votes).<br>
  Arapahoe County had 6.7% of the total votes (24,801 votes).
- Denver County had the largest number of votes.
- Diana DeGette had 73.8% of the total votes (272,892 votes).<br>
  Charles Casper Stockham had 23.0% of the total votes (85,213 votes).<br>
  Raymon Anthony Doane had 3.1% of the total votes (11,606 votes).
- Diana DeGette won the election with 73.8% of the total vote (272,892 votes).


## Election-Audit Summary

This script can easily be used to audit any election with only a few minor changes. Once the data is saved into a csv file, the path to load the data file would change:<br>
`file_to_load = os.path.join("Resources", "election_results.csv")`.<br>
 Similarly, the path to save the results would change based on the file path:<br> `file_to_save = os.path.join("analysis","election_analysis.txt")`.<br>
The script could also scale to different levels, replacing "county" results with city, district, or state results to bring in other election results, whether they be congressional, local council, mayoral, or gubernatorial races.