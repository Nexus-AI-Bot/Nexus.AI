import mysql.connector
import os

password_temp_1 = input("Enter db password here: ")

class Economy:
    def __init__(self, client):
        self.client = client
        
    def query(self, user_id):
        # Connect to the MySQL database on DigitalOcean
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        # Check if the user ID is in the database
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        
        if result is not None:
            # If the user ID is in the database, return the associated balance
            balance = result[0]
        else:
            # If the user ID is not in the database,c reate a new account with a balance of 0
            cursor.execute("INSERT INTO accounts (user_id, balance) VALUES (%s, 0)", (user_id,))
            db.commit()
            balance = 0
        
        cursor.close()
        db.close()
        
        return balance
    
    def add(self, user_id, amount):
        # Connect to the MySQL database on DigitalOcean
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        # Add the specified amount to the user's balance
        cursor = db.cursor()
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE user_id = %s", (amount, user_id))
        db.commit()
        cursor.close()
        db.close()
        
        # Notify the user that their balance has been updated
        message = f"You've been given {amount} coins. Your new balance is {self.query(user_id)} coins."
        return message
        
    def delete(self, user_id, amount):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        balance = self.query(user_id)

        if balance == 0:
            return "404"

        balance -= amount
        cursor = db.cursor()
        cursor.execute("UPDATE accounts SET balance = %s WHERE user_id = %s", (balance, user_id))
        db.commit()
        cursor.close()
        return f"Removed {amount} from {balance}"
    
    def add_pet(self, user_id, pet_name):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO pets (user_id, pet_name) VALUES (%s, %s)", (user_id, pet_name))
        db.commit()
        cursor.close()

    def delete_pet(self, user_id, pet_name):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("DELETE FROM pets WHERE user_id = %s AND pet_name = %s", (user_id, pet_name))
        db.commit()
        cursor.close()

    def check_user_pet(self, user_id):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("SELECT pet_name FROM pets WHERE user_id = %s", (user_id,))
        result = cursor.fetchall()
        cursor.close()

        if result is None:
            return []

        return [pet[0] for pet in result]
    
    def query_pay(self, key):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("SELECT value FROM pay WHERE id = %s", (key,))
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None

        return str(result[0])


    def add_pay(self, key, value):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO pay (id, value) VALUES (%s, %s) ON DUPLICATE KEY UPDATE value = VALUES(value)", (key, str(value)))
        db.commit()
        cursor.close()


    def delete_pay(self, key):
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        cursor = db.cursor()
        cursor.execute("DELETE FROM pay WHERE id = %s", (key,))
        db.commit()
        cursor.close()
