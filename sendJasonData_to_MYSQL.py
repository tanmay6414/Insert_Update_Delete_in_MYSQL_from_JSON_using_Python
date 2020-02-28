#Python code for insering jason file data into mysql server

#basic import module
#Module to be install 
#1. pip install mysql-connector-python



"""
Database operation need to perform first

create database jsonToSQL;
use jsonToSQL;
CREATE TABLE sendtosql (id varchar(3),name varchar(50),country varchar(50),house varchar(50),reign varchar(50));

"""






import mysql.connector
from mysql.connector import errorcode
import  json

#PATH to jason file
file = "C:/Users/TANNY/Desktop/College/Chammu/json_to_Mysql/test.json"
#read json file
srushti=open(file).read()
tanmay = json.loads(srushti)


# do validation and checks before insert
def vstring(val):
    if val != None:
        if type(val) is int:
            ta=str(val).encode('utf-8')
            return ta
        else:
            return val


# connect to MySQL
def connect():
    
    config = {
              'user': 'root',
              'password': 'root',
              'host': '127.0.0.1',
              'database': 'jsonToSQL',
              'raise_on_warnings': True
            }
    try:
        # Establish a MySQL connection
        #give proper connection to your database
        database = mysql.connector.connect(**config)
        return database
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


database=connect()
cursor = database.cursor()


def insert():

    search = "select max(id) from sendtoSQL;"
    cursor.execute(search)
    myresult = cursor.fetchall()
    for i in myresult:
        a=i[0]


    # parse json data to SQL insert
    search=0
    for i, item in enumerate(tanmay):
        id = vstring(item.get("ID", None))
        name = vstring(item.get("Name", None))
        country = vstring(item.get("Country", None))
        house = vstring(item.get("House", None))
        reign = vstring(item.get("Reign", None))

        if a==None:
            search=1
            cursor.execute("INSERT INTO sendtoSQL (id,	name, country, house, reign) VALUES (%s, %s,%s,%s,%s)", (id,name,country,house,reign))
        else:
            if int(a)<int(id):
                search=1
                cursor.execute("INSERT INTO sendtoSQL (id,  name, country, house, reign) VALUES (%s, %s,%s,%s,%s)", (id,name,country,house,reign))


    #to commite changes
    database.commit()
    if search==1:
        print("\n\nOperation perform successfully...!!!!\n\n")
    else:
        print("\n\nDatabase are up to date \nPlease try with new data....\n\n")







def updateValue():
    up=int(input("\n\nEnter id which has to be updated : "))
    print("What you want to update??\n1. Name\t2. Country\t3. House\t4.Regin")
    ch=int(input("\nEnter your choice : "))
    if ch==1:
        upname=input("Enter name which you want to update : ")
        q="UPDATE sendtoSQL SET name='"+ upname+"' WHERE id ="+str(up)
        cursor.execute(q)
    elif ch==2:
        upname=input("Enter country which you want to update : ")
        q="UPDATE sendtoSQL SET country='"+ upname+"' WHERE id ="+str(up)
        cursor.execute(q)
    elif ch==3:
        upname=input("Enter house number which you want to update : ")
        q="UPDATE sendtoSQL SET house='"+ upname+"' WHERE id ="+str(up)
        cursor.execute(q)
    elif ch==4:
        upname=input("Enter reign which you want to update : ")
        q="UPDATE sendtoSQL SET reign='"+ upname+"' WHERE id ="+str(up)
        cursor.execute(q)
    else:
        print("Select correct choise....")
    database.commit()



def delete():
    up=int(input("\n\nEnter id which has to be deleted : "))
    q="DELETE FROM sendtoSQL WHERE id='"+str(up)+"'"
    cursor.execute(q)
    database.commit()






                
    


while 1:
    print("\n\nWhat you want to do?\n1. Insert from existing json file\t2. Update database information\t3. Delete specific row from database")
    ch1=int(input("Enter your choise : "))
    if ch1==1:
        insert()
    elif ch1==2:
        updateValue()
    elif ch1==3:
        delete()
    else:
        print("Please insert correct choise......!!!")
database.close()

