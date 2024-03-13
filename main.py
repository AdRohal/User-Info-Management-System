import sqlite3

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                address TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def get_user_input(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        return first_name, last_name, age, address, phone_number, email

    def add_user(self):
        user_data = self.get_user_input()
        self.cursor.execute('''
            INSERT INTO users (first_name, last_name, age, address, phone_number, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', user_data)
        self.conn.commit()
        print("✅ User information added successfully!")

    def show_users(self):
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()

        if not users:
            print("❌ No users found in the database.")
        else:
            print("👥 Users in the database:")
            for user in users:
                print(
                    f"ID: {user[0]}, Name: {user[1]} {user[2]}, Age: {user[3]}, Address: {user[4]}, Phone: {user[5]}, Email: {user[6]}")

    def delete_user(self):
        user_id = int(input("Enter the ID of the user you want to delete: "))
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
        print("🗑️ User deleted successfully!")

    def main(self):
        while True:
            print("\n1. Add User")
            print("2. Show Users")
            print("3. Delete User")
            print("4. Quit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.show_users()
            elif choice == '3':
                self.delete_user()
            elif choice == '4':
                print("👋 Exiting program.")
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    db = UserDatabase()
    db.main()
