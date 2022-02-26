#create table 
#connection with postgresql
#script 
# two options 1 add 2 edit
#2 fns using query  -> called when user enters choice



import psycopg2
conn = psycopg2.connect(user="postgres", password="12345", database="product", host="localhost", port="5432")
print("Successfully connected!")
cursor = conn.cursor()


cursor.execute("CREATE TABLE PRODUCT(BARCODE_NO BIGINT PRIMARY KEY , NAME VARCHAR(30) NOT NULL, PRICE DECIMAL NOT NULL, WEIGHT DECIMAL NOT NULL)")
print("Table successfully created!")
conn.commit()

print("Records Successfully Inserted!")
conn.close()