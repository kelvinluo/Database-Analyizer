"""

By ZhiChao Luo
#1000431856
As Assighment 3: Squeal
CSC 108

""""""Module db_io: functions for I/O on tables and databases.

A table file has a .csv extension.

We define "table" to mean this:

    dict of {str: list of str}

Each key is a column name from the table and each value is the list of strings
in that column from top row to bottom row.

We define "database" to mean this:

    dict of {str: table}

Each key is the name of the .csv file without the extension.  Each value is
the corresponding table as defined above.
"""

import glob
    
def print_csv(table):
    """ (table) -> NoneType
    Print a representation of table in the same format as a table file.
    """
    columns = list(table.keys())
    print(','.join(columns))
    for i in range(len(table[columns[0]])) :
        cur_column = []
        for column in columns:
            cur_column.append(table[column][i])
        print(','.join(cur_column))




# Write your read_table and read_database functions below.
# Use glob.glob('*.csv') to return a list of csv filenames from
#   the current directory.

def read_table(file):
    '''(file open for reading) -> table
    
    return a table by changing the given csv file into a dictionary
    with titles as keys to each columns
       
    '''
    #open the file of the given file name
    get_file = open(file,'r')
    #Read the information of the file
    text = get_file.read()
    #Saperate each rows
    get_table = text.split('\n')
    
    #Saperate the test informations by commas
    for counter in range (len(get_table)) :
        get_table[counter] = get_table[counter].split(',')
    get_table = get_table[0:-1]
    
    #creat a new ditionary to store the table
    new_table = {}
    
    #Let the first variable of each colume as the key to the following rows
    #Where create a table in the proper format
    for counter in range(len(get_table[0])) :
        list_of_data = []
        for counter2 in range (1,len(get_table)):
            list_of_data.append(get_table[counter2][counter])
        new_table[get_table[0][counter]] = list_of_data
    return new_table

def read_database():
    '''() -> database
    
    Get all csv files from the current path and make them into tables with
    proper format.
    Return a database as a dictionary where use the name of each files as the key
    and each key leads to their own tables
    
    '''
    #Get all the file names for the current path
    file_name = glob.glob('*.csv')
    data_base = {}
    #Check each files with their own specific file name
    for items in file_name :
        data_base[items.replace('.csv','')] = read_table(items)
    return data_base