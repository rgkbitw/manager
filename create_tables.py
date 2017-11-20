import sqlite3 as sql
conn = sql.connect('test.db')

print('Connected  to the database !')

# chemicals table:

chemicals = '''CREATE TABLE CHEMICAL
    ( ITEM_ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      FORMULA TEXT NOT NULL,
      PHASE TEXT NOT NULL,
      TEMP TEXT NOT NULL,
      PRICE INT NOT NULL,
      QUANTITY INT NOT NULL,
      IS_HAZARDOUS TEXT NOT NULL
    );'''


# Non-glass ware table

nonglassware = '''CREATE TABLE NONGLASSWARE
    ( ITEM_ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      PRICE INT NOT NULL,
      QUANTITY INT NOT NULL
    );'''

# Glassware table:
glasware = '''CREATE TABLE GLASSWARE
    ( ITEM_ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      CAPACITY INT NULL,
      PRICE INT NOT NULL,
      QUANTITY INT NOT NULL
    );'''

# Experiments and their usage of chemicals:

#experiment table:
experiment = '''CREATE TABLE EXPERIMENT
    ( ITEM_ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      BRIEF TEXT NOT NULL
    );'''


#LOG TABLE:
log = '''CREATE TABLE LOG
    ( ITEM_ID INT PRIMARY KEY NOT NULL,
      LOG_FOR TEXT NOT NULL,
      TYPE TEXT NOT NULL,
      TIME TEXT NOT NULL,
      AUTHOR TEXT NOT NULL
    );'''

conn.execute(chemicals)
print("Done chemicals")
conn.execute(nonglassware)
print('Done nonglassware')
conn.execute(glasware)
print('Done glassware')
conn.execute(experiment)
print('done experiment')
conn.execute(log)
print('Done log')

print('Done Sucessfully !')

conn.close()
