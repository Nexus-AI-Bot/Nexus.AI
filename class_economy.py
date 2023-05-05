import mysql.connector
import os

password_temp_1 = os.environ.get("PASSWORD_DB")

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
            port=25060
        )
        
        # Check if the user ID is in the database
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        
        if result is not None:
            # If the user ID is in the database, return the associated balance
            balance = result[0]
        else:
            # If the user ID is not in the database, create a new account with a balance of 0
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
            port=25060
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
        # Connect to the MySQL database on DigitalOcean
        db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060
        )
        
        # Reduce the user's balance by the specified amount
        cursor = db.cursor()
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE user_id = %s", (amount, user_id))
        db.commit()
        cursor.close()
        db.close()
        
        # Notify the user that their balance has been updated
        message = f"You've lost {amount} coins. Your new balance is {self.query(user_id)} coins."
