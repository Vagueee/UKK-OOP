from model import *
import main

class Login(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.call('source', 'azure.tcl')
        self.parent.call('set_theme', 'dark')
        self.parent.resizable(False, False)
        self.canvas = tk.Canvas(self.parent, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        database(self)

        self.canvas.create_text(480, 175, text="Login", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
        self.canvas.create_text(405, 225, text="Username", font=("Verdana", 18, "bold"), fill="#b5b3b3")
        self.canvas.create_text(405, 270, text="Password", font=("Verdana", 18, "bold"), fill="#b5b3b3")

        self.username_entry = ttk.Entry(self.parent)
        # self.username_entry.insert(0, 'Username')
        # self.username_entry.bind("<FocusIn>", lambda args: self.username_entry.delete('0', 'end'))
        self.username_entry.pack()
        self.password_entry = ttk.Entry(self.parent, show="*")
        # self.password_entry.insert(0, 'Password')
        # self.password_entry.bind("<FocusIn>", lambda args: self.password_entry.delete('0', 'end'))
        self.password_entry.pack()

        self.canvas.create_window(555, 225, window=self.username_entry)
        self.canvas.create_window(555, 270, window=self.password_entry)

        self.login_button = ttk.Button(self.parent, text="Login", command=self.verify_login)
        self.canvas.create_window(480, 320, window=self.login_button, anchor="center")

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        query = f"SELECT * FROM tb_user WHERE username=%s AND password=%s"
        self.cursor.execute(query, (username, password))
        account = self.cursor.fetchone()

        if account != None:
            # If a match is found, get the user's role
            user_id = account[0] # ID
            username = account[2] # Name
            query = f"SELECT role FROM tb_user WHERE id_user=%s"
            self.cursor.execute(query, (user_id,))
            roles = self.cursor.fetchone()

            if roles != None:
                # If the user's role is admin, allow access to all features
                # Otherwise, limit access as appropriate for the user role
                role = roles[0]
                if role == "Admin":
                    self.parent.destroy()
                    main.Main(role=role, username=username)
                elif role == "Kasir":
                    self.parent.destroy()
                    main.Main(role=role, username=username)
                elif role == "Owner":
                    self.parent.destroy()
                    main.Main(role=role, username=username)
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