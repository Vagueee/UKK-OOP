import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_paket(self):
    self.paket = tk.Toplevel()
    self.paket.title("Laundrive")
    self.paket.geometry("960x540+180+80")
    self.paket.resizable(False, False)
    self.frame = tk.Frame(self.paket)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.paket, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Paket", anchor="center", font=("default", 28, "bold"))

    model.create_crud_button(self, frame=self.paket, x=355, y=110, text="Tambah Data", command=tambah_paket)
    model.create_crud_button(self, frame=self.paket, x=480, y=110, text="Edit Data", command=edit_paket)
    model.create_crud_button(self, frame=self.paket, x=600, y=110, text="Delete Data", command=delete_paket)

    model.create_treeview(
        self, 
        frame=self.paket, 
        proc='paketselect', 
        columns=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        headings=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        texts=('ID', 'Outlet', 'Jenis', 'Nama Paket', 'Harga'))

def tambah_paket():
    pass

def edit_paket():
    pass

def delete_paket():
    pass