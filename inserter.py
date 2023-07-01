import mysql.connector
from random import randint
from time import sleep

# Connect to MySQL
cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3333,
            user="root",
            password="new_password",
            database="experimental_data"
            )

# Create a cursor object
cursor = cnx.cursor()

data = [randint(0, 100) for i in range(0, 300)]

# Update the table
for idx, row in enumerate(data):
    print(f"inserting {idx} point")
    sleep(5)
    insert_query = f"INSERT Into delay_times (time) VALUES ({row})"
    cursor.execute(insert_query)
    cnx.commit()


# Close the cursor and connection
cursor.close()
cnx.close()
