import sqlite3 as sql
#library to get data

def get_data(table,required_prop,property,value):
    # make the query of type:
    '''SELECT required prop FROM table
       WHERE propery == value
    '''

    #make a query
    query ='SELECT * FROM '+ str(table) #+ 'WHERE '+ str(property) + '=' + str(value) + ';'

    # conn to  the database
    conn = sql.connect('test.db')
    return conn.execute(query).fetchall()



def add_data(table):
    #add the data to the database
    #expects an array
    '''INSERT INTO table(ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES(1, 'Paul', 32, 'California', 20000.00)
    '''
