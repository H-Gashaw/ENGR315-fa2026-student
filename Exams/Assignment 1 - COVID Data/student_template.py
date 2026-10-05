import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path='data/covid/us-counties.csv'):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

data = parse_nyt_data()
for row in data:
    date = row[0]
    county = row[1]
    state = row[2]
    cases = row[4]
    deaths = row[5]
    if row[1] == 'Harrisonburg city' or row[1] == 'Rockingham' and row[2] == 'Virginia' :
        print(row)
    #if cases > 0:
    #    print("Date: {date}, County: {county}, State: {state}, Cases: {cases}, Deaths: {deaths}")
    
previous_cases = {}
largest_new_cases = None
largest_date = None
largest_location = None

for row in sorted(data, key=lambda row: row[0]):
    date = row[0]
    county = row[1]
    state = row[2]
    cases = row[4]
    location = (county, state)

    if location in previous_cases:
        new_cases = cases - previous_cases['Harrisonburg city', 'Virginia' or 'Rockingham', 'Virginia']

        if largest_new_cases is None or new_cases > largest_new_cases:
            largest_new_cases = new_cases
            largest_date = date
            largest_location = location

    previous_cases['Harrisonburg city', 'Virginia' or 'Rockingham', 'Virginia'] = cases

if largest_new_cases is not None:
    print("Largest number of new cases:", largest_new_cases)
    print("Date:", largest_date)
    print("County and state:", largest_location)
else:
    print("Not enough data to calculate a daily increase.")



print("Largest number of new cases:", largest_new_cases)
print("Date:", largest_date)

        