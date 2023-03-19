import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font
from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()

def backgroundimg(self):
    # Image
    bg = os.getenv("bg_path")
    bg = f"{bg}"
    self.image = PhotoImage(file=bg)
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")

def btnimg(self):
    ot = os.getenv("ic_outlet")
    self.otimg = PhotoImage(file=ot)
    kar = os.getenv("ic_karyawan")
    self.karimg = PhotoImage(file=kar)
    tr = os.getenv("ic_transaksi")
    self.trimg = PhotoImage(file=tr)
    plg = os.getenv("ic_pelanggan")
    self.plgimg = PhotoImage(file=plg)

def database(self):
    # Connect to the database
    self.db_host = os.getenv("host")
    self.db_user = os.getenv("user")
    self.db_password = os.getenv("password")
    self.db_database = os.getenv("database")
    self.db = mysql.connector.connect(
        host=self.db_host,
        user=self.db_user,
        password=self.db_password,
        database=self.db_database
    )

    # Create Cursor
    self.cursor = self.db.cursor()

def create_card(
        self,
        x: int,
        y: int,
        width: int = 150,
        height: int = 200,
    ) -> tk.Frame:
        card_frame = tk.Frame(
            self.main,
            width=width,
            height=height,
            bd=2,
            relief="groove",
            highlightthickness=2,
            highlightbackground="black"
        )
        self.canvas.create_window(x, y, anchor='n', window=card_frame)
        return card_frame

def create_button(
    self,
    frame: tk.Frame,
    image: PhotoImage,
    text: str,
    command: callable,
    font_size: int = 10,
    font_weight: str = 'bold',
    width: int = 20,
    height: int = 2,
    ):
    label = tk.Label(frame, image=image)
    button = tk.Button(
        frame,
        text=text,
        command=command,
        font=font.Font(size=font_size, weight=font_weight),
        width=width,
        height=height,
    )
    label.pack()
    button.pack()