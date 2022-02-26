
import psycopg2
conn = psycopg2.connect(user="postgres", password="12345", database="cart", host="localhost", port="5432")
print("Successfully connected to cart!")


cursor = conn.cursor()
cursor.execute("select * from shopcart")
conn.commit()
result=cursor.fetchall()
val1=result[0]
val2=result[1]
val3=result[2]

vv=val1[0]
print(vv)
vv2=val2[0]
print(vv2)
vv3=val3[0]
print(vv3)

conn.close()

con = psycopg2.connect(user="postgres", password="12345", database="invoice", host="localhost", port="5432")
print("Successfully connected to invoice!")
cursor=con.cursor()
cursor.execute(f"INSERT INTO BILL(barcodeno) VALUES({vv});")
con.commit()
print("successfully inserted")

con.close()






