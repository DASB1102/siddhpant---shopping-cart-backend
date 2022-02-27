import psycopg2




#connection with cart : barcode fetch
def cartFetch(table_name):
    conn = psycopg2.connect(user="postgres", password="12345", database="cart", host="localhost", port="5432")
    print("Successfully connected to cart!")
    cursor = conn.cursor()
    try:
        sql_query="""SELECT BARCODE_NO,QTY FROM "%s"; """
        cursor.execute(sql_query,(table_name,))
        result=cursor.fetchall()
        print(result)
        return result           #returns barcode,qty as list of tuples
    except (Exception,psycopg2.DatabaseError) as error:
            print(error)
    conn.close()

#connection with product : fetch details of barcode given from cart
def fetchProductDetails(barcode_list): 
    prod_info=[]
    conn2 = psycopg2.connect(user="postgres", password="12345", database="product", host="localhost", port="5432")
    print("Successfully connected to product!")
    cursor = conn2.cursor()
    try:
        sql_query2="SELECT * FROM product_details WHERE BARCODE_NO=%s"
        for barcode in barcode_list:
            cursor.execute(sql_query2,(barcode,))
            result=cursor.fetchone()
            #print(result)
            prod_info.append(result)
        return prod_info           
    except (Exception,psycopg2.DatabaseError) as error:
            print(error)
    conn2.close()



#connection with invoice : Creation of table ,Addition of product 

def final_invoice(prod_info,qty_list,invoice_no):
    #connection with invoice 
    conn3 = psycopg2.connect(user="postgres", password="12345", database="invoice", host="localhost", port="5432")
    print("Successfully connected to invoice!")
    cursor = conn3.cursor()

    barcode_list=[]
    name_list=[]
    price_list=[]
    weight_list=[]

    #seperating product details 
    len=0
    for i in prod_info:
        barcode_list.append(i[0])
        name_list.append(i[1])
        price_list.append(i[2])
        weight_list.append(i[3])
        len+=1
    #print("--products details seperated--")
    
    #creation of table having name as invoice number 
    try:
        create_query="""CREATE TABLE "%s" (BARCODE_NO BIGINT PRIMARY KEY ,
                NAME VARCHAR(30) NOT NULL, 
                PRICE_in_rs DECIMAL NOT NULL, 
                WEIGHT_in_gms DECIMAL NOT NULL,
                QTY_pcs INT NOT NULL);"""
        cursor.execute(create_query,(invoice_no,))
        conn3.commit()
        print(f"Invoice {invoice_no} successfully created!")
    
    except (Exception,psycopg2.DatabaseError) as error:
            print(error)

    #Addition of products buyed
    try:
        sql_query3="""INSERT INTO "%s"(BARCODE_NO,NAME,PRICE_in_rs,WEIGHT_in_gms,QTY_pcs) VALUES(%s,%s,%s,%s,%s);"""
        #sql_query4="""INSERT INTO "%s"(QTY_pcs) VALUES(%s);"""
        for i in range(0,len):
            cursor.execute(sql_query3,(invoice_no,barcode_list[i],name_list[i],price_list[i],weight_list[i],qty_list[i]))
            conn3.commit()
    
        print(f"INVOICE NO : {invoice_no} IS CREATED SUCCESSFULLY!!")

    except (Exception,psycopg2.DatabaseError) as error:
            print(error)
    conn3.close()
    




if __name__ == "__main__":
    invoice_no=1
    t1=cartFetch(1001)
    barcode_list=[]
    qty_l=[]
    for i in t1:
        barcode_list.append(i[0])
        qty_l.append(i[1])
    print(qty_l)
    #print(barcode_list)

    prod_info=fetchProductDetails(barcode_list)
    print(prod_info)

    final_invoice(prod_info,qty_l,invoice_no)
    #invoice_no+=1
