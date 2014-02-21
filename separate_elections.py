import pandas as pd

def separate_elections(file_name, elections):
    """
    Takes a file_name and a list of 
    ('ElectionName', File name) pairs and
    creates a set of new separate files based
    on the pairs.
    """

    print('Reading the %s...' % file_name)
    votes = pd.read_csv(file_name)

    for election in elections:
        print('Seperating out %s...' % election[0])
        filter = votes['ElectionName'] == election[0]
        filtered = votes[filter]
        print('Writing to %s...' % election[1])
        filtered.to_csv(election[1])




if __name__ == '__main__':

    elections = [
        'MUNICIPAL AND SCHOOL DISTRICT PRIMARY',
        'MUNICIPAL AND SCHOOL DISTRICT GENERAL',
        '2012 STATE PRIMARY', 
        '2012 STATE GENERAL'
    ]

    files = [
        'data/elections/2012_state_primary.csv',        
        'data/elections/2012_state_general.csv',       
        'data/elections/2013_municipal_primary.csv', 
        'data/elections/2013_municipal_general.csv'        
    ]

    results = 'data/raw/Election_Results_By_Precinct.csv'

    separate_elections(results, zip(elections, files))
