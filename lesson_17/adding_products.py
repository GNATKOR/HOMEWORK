import psycopg2

connection = psycopg2.connect(
    dbname="pcf",
    user="billy",
    password="Billy",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()
pcf_table = """CREATE TABLE product
        (id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        protein INTEGER CHECK(protein > 0),
        fats INTEGER CHECK(fats > 0),
        carbs INTEGER CHECK(carbs > 0))"""
try:
    cur.execute(pcf_table)
    connection.commit()
    print("TABLE product CREATED")
except psycopg2.errors.DuplicateTable:
    connection.rollback()
    print("TABLE product ALREADY EXISTS")
finally:
    product_name = input("Enter product name: ")
    product_protein = input("Enter the amount of proteins: ")
    product_fat = input("Enter the amount of fats: ")
    product_carbs = input("Enter the amount of carbs: ")

    insert = "INSERT INTO product (name, protein, fats, carbs) VALUES (%s, %s, %s, %s)"
    cur.execute(insert, (product_name, product_protein, product_fat, product_carbs))
    connection.commit()
    cur.close()
    connection.close()
    print("Connection closed.")
