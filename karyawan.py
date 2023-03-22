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
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Karyawan", anchor="center", font=("default", 28, "bold"))

    treeview = model.create_treeview(
        self, 
        frame=self.karyawan, 
        proc='karyawanselect', 
        columns=('id', 'outlet', 'nama', 'username', 'role'), 
        headings=('id', 'outlet', 'nama', 'username', 'role'), 
        texts=('ID', 'Outlet', 'Nama', 'Username', 'Role')
    )

    tambah_button = model.create_crud_button(self, frame=self.karyawan, x=355, y=110 , text="Tambah Data", command=lambda: tambah_karyawan(self))
    edit_button = model.create_crud_button(self, frame=self.karyawan, x=480, y=110 , disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_karyawan(self))
    delete_button = model.create_crud_button(self, frame=self.karyawan, x=600, y=110 , disabled=len(treeview.selection()) == 0, text="Delete Data", command=lambda: delete_karyawan(self))

    treeview.bind("<ButtonRelease-1>", lambda event: model.switch([edit_button, delete_button], selection=treeview.selection()))

def tambah_karyawan(self):
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

    self.canvas.create_text(480, 50, text="Tambah Karyawan", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 150, text="Username", font=("default", 14))
    self.canvas.create_text(420, 175, text="Password", font=("default", 14))
    self.canvas.create_text(420, 200, text="Role", font=("default", 14))

    outlet = model.create_tambah_dropdown(self, self.tambah, x = 545, y = 100, procdrop="dropdownoutlet")
    nama = model.create_tambah_entry(self, self.tambah, x = 545, y = 125)
    username = model.create_tambah_entry(self, self.tambah, x = 545, y = 150)
    password = model.create_tambah_entry(self, self.tambah, x = 545, y = 175)
    role = model.create_tambah_enumdropdown(self, self.tambah, x = 545, y = 200, procenum="karyawanrole")

    def tambah():
        outlet_val = outlet.get()
        nama_val = nama.get()
        username_val = username.get()
        password_val = password.get()
        role_val = role.get()

        model.tambah(
            self, 
            frame=self.tambah,
            destroy=self.karyawan, 
            redirect=lambda: start_karyawan(self), 
            entries=(outlet_val, nama_val, username_val, password_val, role_val), 
            proc="karyawantambah")

    model.create_submit_button(self, x = 480, y = 250, frame=self.tambah, command=tambah)

def edit_karyawan(self):
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

    self.canvas.create_text(480, 50, text="Edit Karyawan", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 150, text="Username", font=("default", 14))
    self.canvas.create_text(420, 175, text="Password", font=("default", 14))
    self.canvas.create_text(420, 200, text="Role", font=("default", 14))

    outlet = model.create_edit_dropdown(self, self.edit, x = 545, y = 100, index=1, target_index=0, state='normal', treeview=self.treeview, procid="karyawanselectbyid", procdrop="dropdownoutlet")
    nama = model.create_edit_entry(self, self.edit, x = 545, y = 125, index=2, state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    username = model.create_edit_entry(self, self.edit, x = 545, y = 150, index=3, state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    password = model.create_edit_entry(self, self.edit, x = 545, y = 175, index=4, state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    role = model.create_edit_enumdropdown(self, self.edit, x = 545, y = 200, index=5, state='normal', treeview=self.treeview, procid="karyawanselectbyid", procenum="karyawanrole")

    def edit():
        id_val = model.get_id(self, treeview=self.treeview, procid="karyawanselectbyid")
        outlet_val = outlet.get()
        nama_val = nama.get()
        username_val = username.get()
        password_val = password.get()
        role_val = role.get()

        model.edit(
            self,
            frame=self.edit,
            destroy=self.karyawan,
            redirect=lambda: start_karyawan(self),
            entries=(id_val, outlet_val, nama_val, username_val, password_val, role_val),
            procedit="karyawanedit")

    model.create_submit_button(self, x = 480, y = 250, frame=self.edit, command=edit)


def delete_karyawan(self):
    model.delete(
        self, 
        treeview=self.treeview, 
        proc="karyawandelete")