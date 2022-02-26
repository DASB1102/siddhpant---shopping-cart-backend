# Databases : 1-product 2-cart 3-invoice / Table :  product_details

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password=12345, host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database product;'''

#Creating a database
cursor.execute(sql)
print("PRODUCT created successfully...")

#Preparing query to create a database
sql2 = '''CREATE database cart;'''

#Creating a database
cursor.execute(sql2)
print("CART created successfully...")

#Preparing query to create a database
sql3 = '''CREATE database invoice;'''

#Creating a database
cursor.execute(sql3)
print("INVOICE created successfully...")

#Closing the connection
conn.close()

conn2 = psycopg2.connect(user="postgres", password="12345", database="product", host="localhost", port="5432")
print("Successfully connected to product !")
cursor2 = conn2.cursor()


cursor2.execute("CREATE TABLE product_details (BARCODE_NO BIGINT PRIMARY KEY , NAME VARCHAR(30) NOT NULL, PRICE DECIMAL NOT NULL, WEIGHT DECIMAL NOT NULL)")
print("PRODUCT_DETAILS successfully created!")
conn2.commit()

conn2.close()



