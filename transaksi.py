import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_transaksi(self):
    self.transaksi = tk.Toplevel()
    self.transaksi.title("Laundrive")
    self.transaksi.geometry("960x540+180+80")
    self.transaksi.resizable(False, False)
    self.frame = tk.Frame(self.transaksi)
    self.frame.pack(fill="both", expand=False)

    # Canvas
    self.canvas = tk.Canvas(self.transaksi, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    # Display
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    self.canvas.create_text(480, 50, text="Data Transaksi", anchor="center", font=("default", 28, "bold"))

    model.crud_button(self, frame=self.transaksi, x=355, y=110, text="Tambah Data", command=tambah_transaksi)
    model.crud_button(self, frame=self.transaksi, x=480, y=110, text="Edit Data", command=edit_transaksi)
    model.crud_button(self, frame=self.transaksi, x=600, y=110, text="Delete Data", command=delete_transaksi)

    model.treeview(
        self, 
        frame=self.transaksi, 
        proc='transaksiselect', 
        columns=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        headings=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        texts=('ID', 'Kode Invoice', 'Outlet', 'Karyawan', 'Pelanggan', 'Tanggal', 'Batas Waktu', 'Waktu Bayar', 'Status', 'Dibayar'))

def tambah_transaksi():
    pass

def edit_transaksi():
    pass

def delete_transaksi():
    pass