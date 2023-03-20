import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_outlet(self):
    self.outlet = tk.Toplevel()
    self.outlet.title("Laundrive")
    self.outlet.geometry("960x540+180+80")
    self.outlet.resizable(False, False)
    self.frame = tk.Frame(self.outlet)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.outlet, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Outlet", anchor="center", font=("default", 28, "bold"))

    model.create_crud_button(self, frame=self.outlet, x=355, y=110, text="Tambah Data", command=lambda: tambah_outlet(self))
    model.create_crud_button(self, frame=self.outlet, x=480, y=110, text="Edit Data", command=lambda: edit_outlet(self))
    model.create_crud_button(self, frame=self.outlet, x=600, y=110, text="Delete Data", command=lambda: delete_outlet(self))

    self.treeview = model.create_treeview(
        self, 
        frame=self.outlet, 
        proc='outletselect', 
        columns=('id', 'nama', 'alamat', 'tlp'), 
        headings=('id', 'nama', 'alamat', 'tlp'), 
        texts=('ID', 'Nama', 'Alamat', 'No. Telp'))

def tambah_outlet(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = tk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Tambah Outlet", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 125, text="Alamat", font=("default", 14))
    self.canvas.create_text(420, 150, text="No. Telp", font=("default", 14))

    nama = model.create_entry(self, self.tambah, x = 540, y = 100)
    alamat = model.create_entry(self, self.tambah, x = 540, y = 125)
    telp = model.create_entry(self, self.tambah, x = 540, y = 150)

    def tambah():
        nama_val = nama.get()
        alamat_val = alamat.get()
        telp_val = telp.get()

        model.validate_number(values=(telp_val))
        model.tambah(
            self, 
            frame=self.tambah,
            destroy=self.outlet, 
            redirect=lambda: start_outlet(self), 
            entries=(nama_val, alamat_val, telp_val), 
            proc="outlettambah")

    model.create_submit_button(self, x = 480, y = 200, frame=self.tambah, command=tambah)

def edit_outlet(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = tk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Edit Outlet", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 125, text="Alamat", font=("default", 14))
    self.canvas.create_text(420, 150, text="No. Telp", font=("default", 14))

    nama = model.create_entry(self, self.edit, x = 540, y = 100)
    alamat = model.create_entry(self, self.edit, x = 540, y = 125)
    telp = model.create_entry(self, self.edit, x = 540, y = 150)

    def edit():
        pass

    model.create_submit_button(self, x = 480, y = 200, frame=self.tambah, command=edit)

def delete_outlet(self):
    model.delete(
        self, 
        treeview=self.treeview, 
        proc="outletdelete")