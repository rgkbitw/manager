import requests
import sqlite3 as sql

from main import counts
print(counts)

# Reference to the tables:

ref=\
    {'CHEMICAL':['ITEM_ID','NAME','FORMULA','PHASE','TEMP','PRICE','QUANTITY','IS_HAZARDOUS'],
     'GLASSWARE':['ITEM_ID','NAME','CAPACITY','PRICE','QUANTITY'],
     'NONGLASSWARE':['ITEM_ID','NAME','PRICE','QUANTITY'],
     'EXPERIMENT':['ITEM_ID','NAME','BRIEF'],
     'LOG':['ITEM_ID','TYPE','TIME','AUTHOR']
     }


# Insert in any table:
# args: any number of arguments : first should be table number followed by the attribs
# returns : adds to table if success else return None
def insert(*args):
    global counts
    table=args[0]
    if table not in ref.keys():
        print("ABORTED !!")
        return None
    else:
        if len(args[1:])!=len(ref[table]):
            print("ATTRIBUTES NOT ENOUGH!")
            return None
        else:
            index=list(ref.keys()).index(table)
            # Everything is okay
            con = sql.connect('test.db')
            try:
                cur = con.cursor()
                print("Did this")
                quert= 'INSERT INTO '+ table+ ' ('+ ",".join(ref[table]) + ") VALUES(" + ",".join('?'*len(ref[table])) + ")"
                print(quert)
                print(counts[index],*args[2:])
                t= tuple(args[1:])
                print(t)
                cur.execute(quert,t)
                print("did this too")
                con.commit()
                print("Did this ttoooo")
                msg = "Record successfully added"
                counts[index]+=1
            except:
                print("Rolling back why ??")
                con.rollback()
                print("error in insert operation")

            finally:
                con.close()
                print("Done !")


for i in range(1,100):
    print("Adding to the database:",i)
    insert('EXPERIMENT',i,'EXperiment NO:'+str(i),' Done!')
