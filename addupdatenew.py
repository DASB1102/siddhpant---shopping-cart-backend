from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#creation of engine
engine = create_engine("postgresql://postgres:12345@localhost:5432/product")
print("Successfully connected!")

#creation of session
db = scoped_session(sessionmaker(bind=engine)) 

def add():

    id=int(input("Enter id of product: "))
    name=input("Enter name: ")
    price=int(input("Enter price: "))
    qty=int(input("Enter quantity: "))
    db.execute(f"INSERT INTO PRODUCT(ID, NAME, PRICE,QUANTITY) VALUES({id},'{name}',{price},{qty});")
    db.commit()
    print("Added successfully!")

def update():

    temp_id=int(input("Enter id for which do you want to update: "))
    print("Present info product: ")
    result=db.execute(f"SELECT * FROM PRODUCT WHERE ID={temp_id}")
    for i in result:
        print(i)
    while True:
        print("\n1-Name\n2-Price\n3-Quantity\n4-Back")
        choice2=int(input("Enter your choice: "))  # for update choice

        if choice2==1:
            up_name=input("Enter new name :")
            db.execute(f"UPDATE PRODUCT SET NAME='{up_name}' WHERE ID={temp_id}" )
            db.commit()
            print("Updated successfully!!")

        elif choice2==2:
            up_price=int(input("Enter new price: "))
            db.execute(f"UPDATE PRODUCT SET PRICE={up_price} WHERE ID={temp_id}" )
            db.commit()
            print("Updated successfully!!")

        elif choice2==3:
            up_qty=int(input("Enter new quantity: "))
            db.execute(f"UPDATE PRODUCT SET QUANTITY={up_qty} WHERE ID={temp_id}" )
            db.commit()
            print("Updated successfully!!")

        elif choice2==4:
            break

        else:
            print("Invalid choice")

def deleteProduct():

    temp_id2=int(input("Enter id for which do you want to update: "))
    print("Present info product: ")
    result=db.execute(f"SELECT * FROM PRODUCT WHERE ID={temp_id2}")
    for i in result:
        print(i)
    flag=int(input("Enter 1 to delete permanently: "))

    if flag==1:
        db.execute(f"DELETE FROM PRODUCT WHERE ID={temp_id2}")
        db.commit()
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

db.close()