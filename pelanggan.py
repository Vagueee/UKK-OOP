import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_pelanggan(self):
    self.pelanggan = tk.Toplevel()
    self.pelanggan.title("Laundrive")
    self.pelanggan.geometry("960x540+180+80")
    self.pelanggan.resizable(False, False)
    self.frame = tk.Frame(self.pelanggan)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.pelanggan, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Pelanggan", anchor="center", font=("default", 28, "bold"))

    treeview = model.create_treeview(
        self, 
        frame=self.pelanggan, 
        proc='pelangganselect', 
        columns=('id', 'nama', 'alamat', 'jenis_kelamin', 'tlp'), 
        headings=('id', 'nama', 'alamat', 'jenis_kelamin', 'tlp'), 
        texts=('ID', 'Nama', 'Alamat', 'Jenis Kelamin', 'No. Telp'))

    tambah_button = model.create_crud_button(self, frame=self.pelanggan, x=355, y=110, text="Tambah Data", command=lambda: tambah_pelanggan(self))
    edit_button = model.create_crud_button(self, frame=self.pelanggan, x=480, y=110, disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_pelanggan(self))
    delete_button = model.create_crud_button(self, frame=self.pelanggan, x=600, y=110, disabled=len(treeview.selection()) == 0, text="Delete Data", command=lambda: delete_pelanggan(self))

    treeview.bind("<ButtonRelease-1>", lambda event: model.switch([edit_button, delete_button], selection=treeview.selection()))

def tambah_pelanggan(self):
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

    self.canvas.create_text(480, 50, text="Tambah Pelanggan", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 125, text="Alamat", font=("default", 14))
    self.canvas.create_text(420, 150, text="Jenis Kelamin", font=("default", 14))
    self.canvas.create_text(420, 175, text="No. Telp", font=("default", 14))

    nama = model.create_tambah_entry(self, self.tambah, x = 545, y = 100)
    alamat = model.create_tambah_entry(self, self.tambah, x = 545, y = 125)
    jenis_kelamin = model.create_tambah_enumdropdown(self, self.tambah, x = 545, y = 150, procenum="pelangganjk")
    telp = model.create_tambah_entry(self, self.tambah, x = 545, y = 175)

    def tambah():
        nama_val = nama.get()
        alamat_val = alamat.get()
        jenis_kelamin_val = jenis_kelamin.get()
        telp_val = telp.get()

        validate = model.validate_number(values=(telp_val))
        if validate == True:
            model.tambah(
                self, 
                frame=self.tambah,
                destroy=self.pelanggan, 
                redirect=lambda: start_pelanggan(self), 
                entries=(nama_val, alamat_val, jenis_kelamin_val, telp_val), 
                proc="pelanggantambah")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    model.create_submit_button(self, x = 480, y = 225, frame=self.tambah, command=tambah)

def edit_pelanggan(self):
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

    self.canvas.create_text(480, 50, text="Edit Pelanggan", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 150, text="Nama", font=("default", 14))
    self.canvas.create_text(420, 100, text="Alamat", font=("default", 14))
    self.canvas.create_text(420, 125, text="Jenis Kelamin", font=("default", 14))
    self.canvas.create_text(420, 175, text="No. Telp", font=("default", 14))

    nama = model.create_edit_entry(self, self.edit, x = 545, y = 100, index=1, treeview=self.treeview, procid="pelangganselectbyid")
    alamat = model.create_edit_entry(self, self.edit, x = 545, y = 125, index=2, treeview=self.treeview, procid="pelangganselectbyid")
    jenis_kelamin = model.create_edit_enumdropdown(self, self.edit, x = 545, y = 150, index=3, treeview=self.treeview, procid="pelangganselectbyid", procenum="pelangganjk")
    telp = model.create_edit_entry(self, self.edit, x = 545, y = 175, index=4, treeview=self.treeview, procid="pelangganselectbyid")

    def edit():
        id_val = model.get_id(self, treeview=self.treeview, procid="pelangganselectbyid")
        nama_val = nama.get()
        alamat_val = alamat.get()
        jenis_kelamin_val = jenis_kelamin.get()
        telp_val = telp.get()

        validate = model.validate_number(values=(telp_val))
        if validate == True:
            model.edit(
                self,
                frame=self.edit,
                destroy=self.paket,
                redirect=lambda: start_pelanggan(self),
                entries=(id_val, nama_val, alamat_val, jenis_kelamin_val, telp_val),
                procedit="paketedit")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    model.create_submit_button(self, x = 480, y = 225, frame=self.edit, command=edit)

def delete_pelanggan(self):
    model.delete(
        self, 
        treeview=self.treeview, 
        proc="pelanggandelete")