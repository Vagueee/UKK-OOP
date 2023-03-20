import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_karyawan(self):
    self.karyawan = tk.Toplevel()
    self.karyawan.title("Laundrive")
    self.karyawan.geometry("960x540+180+80")
    self.karyawan.resizable(False, False)
    self.frame = tk.Frame(self.karyawan)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.karyawan, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Karyawan", anchor="center", font=("default", 28, "bold"))

    model.create_crud_button(self, frame=self.karyawan, x=355, y=110, text="Tambah Data", command=tambah_karyawan)
    model.create_crud_button(self, frame=self.karyawan, x=480, y=110, text="Edit Data", command=edit_karyawan)
    model.create_crud_button(self, frame=self.karyawan, x=600, y=110, text="Delete Data", command=delete_karyawan)

    model.create_treeview(
        self, 
        frame=self.karyawan, 
        proc='karyawanselect', 
        columns=('id', 'outlet', 'nama', 'username', 'role'), 
        headings=('id', 'outlet', 'nama', 'username', 'role'), 
        texts=('ID', 'Outlet', 'Nama', 'Username', 'Role'))

def tambah_karyawan():
    pass

def edit_karyawan():
    pass

def delete_karyawan():
    pass