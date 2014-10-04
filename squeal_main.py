"""

By ZhiChao Luo
#1000431856
As Assighment 3: Squeal
CSC 108

"""
"""
Process SQuEaL queries from the keyboard and print the results.
"""

import db_io
import squeal

def main():
    """ () -> NoneType
    Ask for queries from the keyboard; stop when empty line is received. For
    each query, process it and use db_io.print_csv to print the results.
    """
    # Write your main function body here.
    # An infinite while loop continues until a blank line is entered
    while True:
        #ask user for input
        choose_query = input('')
        #if an empty line is entered, break the loop
        if choose_query == '':
            break
        
        index_of_from = choose_query.index('from')
        
        #Saperate the titles given by the user from the user input
        list_of_titles = choose_query[7:index_of_from-1].split(',')
        list_of_where_names = []
        #If the optional query where is used, saperates the title which is used in the where query
        if 'where' in choose_query :
            index_of_where = choose_query.index('where')
            #Saperate the table names given by the user from the user input
            list_of_tables_names = choose_query[index_of_from+5:index_of_where-1\
                                                ].split(',')
            #Saperate the title names from where query
            #given by the user from the user input
            if '=' in choose_query:
                list_of_where_names = choose_query[index_of_where+6:].split('=')
            elif '>' in choose_query:
                list_of_where_names = choose_query[index_of_where+6:].split('>')
        else:
            #Saperate the table names given by the user from the user input
            list_of_tables_names = choose_query[index_of_from+5:].split(',')
        
        #Creating a list for storing the tables which the user is required to use
        
        list_of_tables = []
        
        #Put the correct tables with the names user given into the list_of_tables list.
        for items in list_of_tables_names:
            list_of_tables.append(db_io.read_table(items+'.csv'))
            
        #if the title names given is a '*', then use all the titles in the tables
        if list_of_titles[0] == '*' :
            list_of_titles = []
            for items in list_of_tables :
                for key in items.keys():
                    list_of_titles.append(key)
        
        #product_table represents the table or cartesian product 
        #of two tables from the user's input
        product_table = {}
        if len (list_of_tables) == 1:
            product_table = list_of_tables[0]
        else:
            product_table = squeal.cartesian_product(list_of_tables[0],\
                                                     list_of_tables[1])
        #Check if the second value in the where query is a value or a column name
        value_or_column_name = 'value'
        for key in  product_table.keys():
            if 'where' in choose_query and key == list_of_where_names[1]:
                value_or_column_name = 'column'
        #procesed_table represents the processed table after operation
        #from the user's where query, which is optional
        processed_table = {}
        
        #If where query is entered, added the missing title, (which is the 
        #title after the = operation in the user input) into the product
        if 'where' in choose_query and value_or_column_name == 'column':
            processed_table[list_of_where_names[1]] = \
                product_table[list_of_where_names[1]]
        
        #Eliminate all the titles which the user did not request in the query
        for key in product_table.keys() :
            if key in list_of_titles:
                processed_table[key] = product_table[key]
        
        #Get keys from the processed_table for further use
        processed_table_keys = []
        #A variable use to save the length of a row
        row_length = 0
        
        #If where query is used by the user, then operate the where query
        if 'where' in choose_query :
            #Loop each row in the table and check for duplicate in the given titles
            for row_count in range(len(processed_table[list_of_where_names[0]])) :
                row_length = len(processed_table[list_of_where_names[0]])
                
                #If the information in the given titles from the where query
                #are the same, then mark the row as "DELETEDROW"
                if '=' in choose_query and value_or_column_name == 'column':
                    if processed_table[list_of_where_names[0]][row_count] != \
                       processed_table[list_of_where_names[1]][row_count] :
                        for key in list(processed_table.keys()) :
                            processed_table[key][row_count] = "DELETEDROW"
                #are greater than the other, then mark the row as "DELETEDROW"
                elif '>' in choose_query and value_or_column_name == 'column':
                    if processed_table[list_of_where_names[0]][row_count] <= \
                       processed_table[list_of_where_names[1]][row_count] :
                        for key in list(processed_table.keys()) :
                            processed_table[key][row_count] = "DELETEDROW"
                if '=' in choose_query and value_or_column_name == 'value':
                    if processed_table[list_of_where_names[0]][row_count] != \
                       list_of_where_names[1] :
                        for key in list(processed_table.keys()) :
                            processed_table[key][row_count] = "DELETEDROW"
                elif '>' in choose_query and value_or_column_name == 'value':
                    if processed_table[list_of_where_names[0]][row_count] <= \
                       list_of_where_names[1]:
                        for key in list(processed_table.keys()) :
                            processed_table[key][row_count] = "DELETEDROW"   
            #Delete the title after = operator given in the where query
            if value_or_column_name == 'column' and list_of_where_names[0] \
               != list_of_where_names[1] :
                del processed_table[list_of_where_names[1]]
                position_changes = 0
            
            #Check all the keys in the processed_table
            for key in list(processed_table.keys()) :
                position_changes = 0
                for row_count in range(row_length) :
                    #Delete all the rows with the letter 'DELETEDROW'
                    if processed_table[key][row_count-position_changes] \
                       == "DELETEDROW" :
                        del processed_table[key][row_count-position_changes]
                        position_changes = position_changes + 1
        #Print the table
        db_io.print_csv(processed_table)
    
    #db_io.print_csv(squeal.cartesian_product(data['movies'],data['oscars']))
    
if __name__ == '__main__':
    main()
