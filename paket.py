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
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Paket", anchor="center", font=("default", 28, "bold"))

    model.create_crud_button(self, frame=self.paket, x=355, y=110, text="Tambah Data", command=lambda: tambah_paket(self))
    model.create_crud_button(self, frame=self.paket, x=480, y=110, text="Edit Data", command=lambda: edit_paket(self))
    model.create_crud_button(self, frame=self.paket, x=600, y=110, text="Delete Data", command=lambda: delete_paket(self))

    model.create_treeview(
        self, 
        frame=self.paket, 
        proc='paketselect', 
        columns=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        headings=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        texts=('ID', 'Outlet', 'Jenis Paket', 'Nama Paket', 'Harga'))

def tambah_paket(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = tk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    model.database(self)

    self.canvas.create_text(480, 50, text="Tambah Outlet", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Jenis Paket", font=("default", 14))
    self.canvas.create_text(420, 150, text="Nama Paket", font=("default", 14))
    self.canvas.create_text(420, 175, text="Harga", font=("default", 14))

    outlet = model.create_tambah_dropdown(self, self.tambah, x = 545, y = 100, procdrop="dropdownoutlet")
    jenis = model.create_tambah_enumdropdown(self, self.tambah, x = 545, y = 125, procenum="paketjenis")
    nama = model.create_tambah_entry(self, self.tambah, x = 545, y = 150)
    harga = model.create_tambah_entry(self, self.tambah, x = 545, y = 175)

    def tambah():
        outlet_val = outlet.get()
        jenis_val = jenis.get()
        nama_val = nama.get()
        harga_val = harga.get()

        validate = model.validate_number(values=(harga_val))
        if validate == True:
            model.tambah(
                self, 
                frame=self.tambah,
                destroy=self.paket, 
                redirect=lambda: start_paket(self), 
                entries=(outlet_val, jenis_val, nama_val, harga_val), 
                proc="pakettambah")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    model.create_submit_button(self, x = 480, y = 225, frame=self.tambah, command=tambah)

def edit_paket(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = tk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    model.database(self)

    self.canvas.create_text(480, 50, text="Edit Outlet", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Jenis Paket", font=("default", 14))
    self.canvas.create_text(420, 150, text="Nama Paket", font=("default", 14))
    self.canvas.create_text(420, 175, text="Harga", font=("default", 14))

    outlet = model.create_edit_dropdown(self, self.edit, x = 545, y = 100, index=1, treeview=self.treeview, procid="paketselectbyid", procdrop="dropdownoutlet")
    jenis = model.create_edit_enumdropdown(self, self.edit, x = 545, y = 125, index=2, treeview=self.treeview, procid="paketselectbyid", procenum="paketjenis")
    nama = model.create_edit_entry(self, self.edit, x = 545, y = 150, index=3, treeview=self.treeview, procid="paketselectbyid")
    harga = model.create_edit_entry(self, self.edit, x = 545, y = 175, index=4, treeview=self.treeview, procid="paketselectbyid")

    def edit():
        id_val = model.get_id(self, treeview=self.treeview, procid="paketselectbyid")
        outlet_val = outlet.get()
        jenis_val = jenis.get()
        nama_val = nama.get()
        harga_val = harga.get()

        validate = model.validate_number(values=(harga_val))
        if validate == True:
            model.edit(
                self,
                frame=self.edit,
                destroy=self.paket,
                redirect=lambda: start_paket(self),
                entries=(id_val, outlet_val, jenis_val, nama_val, harga_val),
                procedit="paketedit")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    model.create_submit_button(self, x = 480, y = 225, frame=self.edit, command=edit)


def delete_paket(self):
    model.delete(
        self, 
        treeview=self.treeview, 
        proc="paketdelete")