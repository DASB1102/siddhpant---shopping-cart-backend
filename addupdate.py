#SHOP OWNER - script
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
        print(error)


def update():
    temp_id=int(input("Enter barcode for which do you want to update: "))
    print("Present info product: ")
    try:
        sql_query6="SELECT * FROM product_details WHERE BARCODE_NO=%s"
        cursor.execute(sql_query6,(temp_id,))
        outcome=cursor.fetchone()
        print(f"name : {outcome[1]}\nprice: {outcome[2]}\nweight :{outcome[3]}")
    except (Exception,psycopg2.DatabaseError) as error:
                print(error)
    while True:
        print("\n1-Name\n2-Price\n3-Weight\n4-Back")
        choice2=int(input("Enter your choice: "))  # for update choice
        if choice2==1:
            try :
                sql_query2="UPDATE product_details SET NAME = %s WHERE BARCODE_NO=%s"
                up_name=input("Enter new name: ")
                params2=(up_name,temp_id)
                cursor.execute(sql_query2,params2)
                conn.commit()
                print("Updated successfully!!")
            except (Exception,psycopg2.DatabaseError) as error:
                print(error)

        elif choice2==2:
            try : 
                sql_query3="UPDATE product_details SET PRICE=%s WHERE BARCODE_NO=%s"
                up_price=float(input("Enter new price: "))
                params3=(up_price,temp_id)
                cursor.execute(sql_query3,params3)
                conn.commit()
                print("Updated successfully!!")
            except (Exception,psycopg2.DatabaseError) as error:
                print(error)
            
        elif choice2==3:
            try :
                sql_query4="UPDATE product_details SET QUANTITY=%s WHERE BARCODE_NO=%s"
                up_weight=float(input("Enter new weight: "))
                params4=(up_weight,temp_id)
                cursor.execute(sql_query4,params4)
                conn.commit()
                print("Updated successfully!!")
            except (Exception,psycopg2.DatabaseError) as error:
                print(error)

        elif choice2==4:
            break
        else:
            print("Invalid choice")

def deleteProduct():
    temp_id2=int(input("Enter barcode for which do you want to update: "))
    print("Present info product: ")
    try:
        sql_query5="SELECT * FROM product_details WHERE BARCODE_NO=%s"
        cursor.execute(sql_query5,(temp_id2,))
        result=cursor.fetchone()
        print(f"name : {result[1]}\nprice: {result[2]}\nweight :{result[3]}")
    except (Exception,psycopg2.DatabaseError) as error:
                print(error)

    flag=int(input("Enter 1 to delete permanently"))
    if flag==1:
        try:
            sql_query6="DELETE FROM product_details WHERE BARCODE_NO=%s"
            cursor.execute(sql_query6,(temp_id2,))
            conn.commit()
            print("Deleted successfully!!")
        except (Exception,psycopg2.DatabaseError) as error:
                print(error)



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