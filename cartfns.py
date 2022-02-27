import psycopg2
from datetime import datetime



conn = psycopg2.connect(user="postgres", password="12345", database="cart", host="localhost", port="5432")
print("Successfully connected!")
cursor = conn.cursor()

def createTable():
    start=True              # flag for creating table
    if start==True:
        unix_time = int(datetime.now().timestamp())
        table_name=unix_time
        try: 
            create_query="""CREATE TABLE "%s"(BARCODE_NO BIGINT PRIMARY KEY,QTY INT NOT NULL)"""
            cursor.execute(create_query,(table_name,))
            conn.commit()
            print(f"cart no : {table_name} created successfully")
            return table_name
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)


def addProduct(barcode_no,qty,table_name):
    try:
        sql_query="""INSERT INTO "%s" VALUES (%s,%s);"""
        params=(table_name,barcode_no,qty)
        cursor.execute(sql_query,params)
        conn.commit()
        print("Added successfully!")
    except (Exception,psycopg2.DatabaseError) as error:
            print(error)


def delProduct(barcode_no,table_name):
    try:
        sql_query="""DELETE FROM "%s" WHERE BARCODE_NO=%s;"""
        params=(table_name,barcode_no)
        cursor.execute(sql_query,params)
        conn.commit()
        print("Removed successfully!")
    except (Exception,psycopg2.DatabaseError) as error:
            print(error)


#EXTRA : IF NEEDED 
def delTable(table_name):
    stop=True           # flag when shopping ends 
    if stop==True:
        try:
            sql_query="""DROP TABLE "%s" ;"""
            params=(table_name,)
            cursor.execute(sql_query,params)
            conn.commit()
            print(f"cart no : {table_name} deleted successfully!")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)

#tn=createTable()
#delProduct(2920292022088,tn)



