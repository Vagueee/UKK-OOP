import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font
from dotenv import load_dotenv
import os
import mysql.connector
import model
import main
load_dotenv()

class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.logged_in = False
        self.user_role = None

        # Canvas
        self.canvas = tk.Canvas(self.parent, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        model.backgroundimg(self)
        model.database(self)

        # Add Text
        self.canvas.create_text(480, 175, text="Login", anchor="center", font=("default", 28, "bold"))
        self.canvas.create_text(415, 225, text="Username", font=("default", 18))
        self.canvas.create_text(415, 255, text="Password", font=("default", 18))

        # Entry
        self.username_entry = tk.Entry(self.parent)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.parent, show="*")
        self.password_entry.pack()

        # Create Window
        self.canvas.create_window(545, 225, window=self.username_entry)
        self.canvas.create_window(545, 255, window=self.password_entry)

        # Login Button
        self.login_button = tk.Button(self.parent, text="Login", command=self.verify_login, font=font.Font(size=14, weight='bold'))
        self.canvas.create_window(480, 305, window=self.login_button, anchor="center")

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        query = f"SELECT * FROM tb_user WHERE username=%s AND password=%s"
        self.cursor.execute(query, (username, password))
        account = self.cursor.fetchone()

        if account != None:
            # If a match is found, get the user's role
            user_id = account[0]
            query = f"SELECT role FROM tb_user WHERE id_user=%s"
            self.cursor.execute(query, (user_id,))
            roles = self.cursor.fetchone()

            if roles != None:
                # If the user's role is admin, allow access to all features
                # Otherwise, limit access as appropriate for the user role
                role = roles[0]
                if role == "admin":
                    self.parent.destroy()
                    main.Main()
                    main.logged_in = True
                    main.user_role = 'admin'
                elif role == "kasir":
                    self.parent.destroy()
                    main.Main()
                    main.logged_in = True
                    main.user_role = 'kasir'
                elif role == "owner":
                    self.parent.destroy()
                    main.Main()
                    main.logged_in = True
                    main.user_role = 'owner'
            else:
                # If no role is found, show an error message
                messagebox.showerror(title="Login Failed", message="No role found for user")
        else:
            # If no match is found, show an error message
            messagebox.showerror(title="Login Failed", message="Wrong username or password")

if __name__ == '__main__':
    login = tk.Tk()
    login.title("Login")
    login.geometry("960x540+180+50")
    app = Login(login)
    app.pack()

    login.mainloop()