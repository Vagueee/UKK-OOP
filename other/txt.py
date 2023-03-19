import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font
from dotenv import load_dotenv
import os
import mysql.connector
import main
load_dotenv()

def run_tambah():
    tambah = tk.TopLevel()
    tambah.title("Laundrive")
    tambah.geometry("960x540+180+50")
    tambah.resizable(False, False)
    frame = tk.Frame(tambah)
    frame.pack(fill="both", expand=False)

    # Image
    bg = os.getenv("bg_path")
    bg = f"{bg}"
    image = PhotoImage(file=bg)

    # Canvas
    canvas = tk.Canvas(tambah, width=960, height=540)
    canvas.pack(fill="both", expand=False)

    # Display
    canvas.create_image(0, 0, image=image, anchor="nw")

    # Connect to the database
    db_host = os.getenv("host")
    db_user = os.getenv("user")
    db_password = os.getenv("password")
    db_database = os.getenv("database")
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    # Create Cursor
    cursor = db.cursor()

    # Add Text
    canvas.create_text(480, 50, text="Tambah Outlet", anchor="center", font=("default", 24, "bold"))

    canvas.create_text(420, 100, text="Nama", font=("default", 14))
    nama_entry = tk.Entry(tambah)
    nama_entry.pack()
    canvas.create_text(420, 125, text="Alamat", font=("default", 14))
    alamat_entry = tk.Entry(tambah)
    alamat_entry.pack()
    canvas.create_text(420, 150, text="No. Telp", font=("default", 14))
    telp_entry = tk.Entry(tambah)
    telp_entry.pack()

    # Validate
    def validate(nama_entry, alamat_entry, telp_entry):
        try:
            str(nama_entry)
            str(alamat_entry)
            float(telp_entry)
            return True
        except ValueError:
            return False

    # Create Window
    canvas.create_window(540, 125, window=nama_entry)
    canvas.create_window(540, 150, window=alamat_entry)
    canvas.create_window(540, 200, window=telp_entry)

    def tambah():
        nama_val = nama_entry.get() 
        alamat_val = alamat_entry.get() 
        telp_val = telp_entry.get()

        if validate(nama_entry, alamat_entry, telp_entry):
            # Save the data to the database
            proc = "tambahoutlet"
            values = (nama_val, alamat_val, telp_val)
            cursor.callproc(proc, values)
            db.commit()
            tambah.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    # Create Buttons
    tambahs = tk.Button(tambah, text="Submit", command=tambah, font=font.Font(size=10, weight='bold'))

    # Display Buttons
    tambah_canvas = canvas.create_window( 480, 255, window=tambahs, anchor="center")