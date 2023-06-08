import mysql.connector
import json

password_temp_1 = input("Enter friend db password: ")


class Friend:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="db-mysql-lon1-35653-do-user-13900096-0.b.db.ondigitalocean.com",
            user="doadmin",
            password=password_temp_1,
            database="defaultdb",
            port=25060,
        )
        self.cursor = self.db.cursor()

    def add(self, username, likes):
        query = "INSERT INTO friend (Username, Likes) VALUES (%s, %s)"
        values = (username, json.dumps(likes))
        self.cursor.execute(query, values)
        self.db.commit()
        print("Friend added successfully.")

    def delete(self, username, like):
        likes = self.query_likes(username)
        if like in likes:
            likes.remove(like)
            self.update_likes(username, likes)
            print("Like deleted successfully.")
        else:
            print("Like not found for the specified username.")

    def update(self, username, likes):
        self.update_likes(username, likes)
        print("Likes updated successfully.")

    def query_likes(self, username):
        query = "SELECT Likes FROM friend WHERE Username = %s"
        values = (username,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            likes = json.loads(result[0])
            return likes if likes else []
        else:
            print("Friend not found.")
            return []

    def update_likes(self, username, likes):
        query = "UPDATE friend SET Likes = %s WHERE Username = %s"
        values = (json.dumps(likes), username)
        self.cursor.execute(query, values)
        self.db.commit()

    def query_username(self, username):
        query = "SELECT * FROM friend WHERE Username = %s"
        values = (username,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return result[0], json.loads(result[1])
        else:
            return None

    def query_same_likes(self, likes):
        query = "SELECT Username, Likes FROM friend"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        matching_usernames = []
        for row in result:
            username = row[0]
            db_likes = json.loads(row[1])
            if any(like in db_likes for like in likes):
                matching_usernames.append(username)
        if matching_usernames:
            return matching_usernames
        else:
            print("No friends found with at least one similar like.")
            return []

