import psycopg2

conn = psycopg2.connect(user="postgres", password="12345", database="product", host="localhost", port="5432")
print("Successfully connected!")
cursor = conn.cursor()

def add():
    barcode_no=int(input("Enter barcode number of product: "))
    name=input("Enter name: ")
    price=float(input("Enter price: "))
    weight=float(input("Enter weight: "))
    try:
        sql_query="INSERT INTO product_details VALUES (%s,%s,%s,%s);"
        params=(barcode_no,name,price,weight)
        cursor.execute(sql_query,params)
        conn.commit()
        print("Added successfully!")
    except (Exception,psycopg2.DatabaseError) as error:
        print("please donot provide null value or same barcode number")

def update():
    temp_id=int(input("Enter id for which do you want to update: "))
    print("Present info product: ")
    while True:
        print("\n1-Name\n2-Price\n3-Quantity\n4-Back")
        print("")
        choice2=int(input("Enter your choice: "))  # for update choice
        if choice2==1:
            up_name=input("Enter new name: ")
            cursor.execute(f"UPDATE PRODUCT SET NAME='{up_name}' WHERE ID={temp_id}" )
            conn.commit()
            print("Updated successfully!!")
        elif choice2==2:
            up_price=int(input("Enter new price: "))
            cursor.execute(f"UPDATE PRODUCT SET PRICE={up_price} WHERE ID={temp_id}" )
            conn.commit()
            print("Updated successfully!!")
        elif choice2==3:
            up_qty=int(input("Enter new quantity: "))
            cursor.execute(f"UPDATE PRODUCT SET QUANTITY={up_qty} WHERE ID={temp_id}" )
            conn.commit()
            print("Updated successfully!!")
        elif choice2==4:
            break
        else:
            print("Invalid choice")

def deleteProduct():
    temp_id2=int(input("Enter id for which do you want to update: "))
    print("Present info product: ")
    cursor.execute(f"SELECT * FROM PRODUCT WHERE ID={temp_id2}")
    result=cursor.fetchone()
    print(result)
    flag=int(input("Enter 1 to delete permanently"))
    if flag==1:
        cursor.execute(f"DELETE FROM PRODUCT WHERE ID={temp_id2}")
        conn.commit()
        print("Deleted successfully!!")


if __name__ == "__main__":
    while True:
        print("\n1-To Add Item\n2-To Update Item\n3-To Delete Item\n4-To exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add()
        elif choice==2:
            update()
        elif choice==3:
             deleteProduct()
        elif choice==4:
            break
        else:
            print("Invalid choice")
        choice=''

conn.close()