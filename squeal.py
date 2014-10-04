"""

By ZhiChao Luo
#1000431856
As Assighment 3: Squeal
CSC 108

"""""" Module squeal: table and database manipulation functions.

The meanings of "table" and "database" are as described in db_io.py.
"""

# Write your Cartesian product function and all your other helper functions
# here.

def cartesian_product(table_one,table_two):
    '''(table, table) -> table
    Return a new table that is the cartesian product of the two 
    arguments which are both SQuEaL tables. Do not mutate the original tables.
    
    >>>cartesian_product({1:[1,2],2:[3,4]},{3:[5,6],4:[7,8]})
    {1:[1,1,2,2],2:[3,3,4,4],3:[5,6,5,6],4:[7,8,7,8]}
    >>>cartesian_product({a:[a,b],b:[c,d]},{c:[e,f],d:[g,i]})
    {a:[a,a,b,b],b:[c,c,d,d],c:[e,f,e,f],d:[g,i,g,i]}
    '''
    #These two listss are used to store the keys from the two tables
    table_one_keys = []
    table_two_keys = []
    #Create an empty ditionary to store the new table    
    new_table = {}
    
    #Get keys from the table and put them into a list
    for key in table_one :
        table_one_keys.append(key)
        new_table[key] = []
    
    #Get keys from the table and put them into a list
    for key in table_two :
        table_two_keys.append(key)
        new_table[key] = []
    
    #Duplicate each row from the first table for the number of rows from the
    #second table
    for counter1 in range (len(table_one_keys)) :
        for counter2 in range(len(table_one[table_one_keys[0]])) :
            for counter3 in range(len(table_two[table_two_keys[0]])) :
                new_table[table_one_keys[counter1]].\
                    append(table_one[table_one_keys[counter1]][counter2])
    
    #Expand each columns from the second table for the number of rows from the
    #second table with the same columns
    for counter1 in range(len(table_two_keys)) :
        for counter2 in range(len(table_one[table_one_keys[0]])) :
            for items in table_two[table_two_keys[counter1]] :
                new_table[table_two_keys[counter1]].append(items)
                
    return new_table