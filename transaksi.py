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
    self.canvas = tk.Canvas(self.transaksi, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    self.canvas.create_text(480, 50, text="Data Transaksi", anchor="center", font=("default", 28, "bold"))

    treeview = model.create_treeview(
        self, 
        frame=self.transaksi, 
        proc='transaksiselect', 
        columns=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        headings=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        texts=('ID', 'Kode Invoice', 'Outlet', 'Karyawan', 'Pelanggan', 'Tanggal', 'Batas Waktu', 'Waktu Bayar', 'Status', 'Dibayar'))

    tambah_button = model.create_crud_button(self, frame=self.transaksi, x=355, y=110, text="Tambah Data", command=lambda: tambah_transaksi(self))
    edit_button = model.create_crud_button(self, frame=self.transaksi, x=480, y=110, disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_transaksi(self))
    detail_button = model.create_crud_button(self, frame=self.transaksi, x=600, y=110, disabled=len(treeview.selection()) == 0, text="Detail Data", command=lambda: detail_transaksi(self))

    treeview.bind("<ButtonRelease-1>", lambda event: model.switch([edit_button, detail_button], selection=treeview.selection()))

def tambah_transaksi(self):
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

    self.canvas.create_text(480, 50, text="Tambah transaksi", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Karyawan", font=("default", 14))
    self.canvas.create_text(420, 150, text="Pelanggan", font=("default", 14))
    self.canvas.create_text(420, 175, text="Tanggal", font=("default", 14))
    self.canvas.create_text(420, 200, text="Batas Waktu", font=("default", 14))
    self.canvas.create_text(420, 225, text="Waktu Bayar", font=("default", 14))
    self.canvas.create_text(420, 250, text="Biaya Tambahan", font=("default", 14))
    self.canvas.create_text(420, 275, text="Diskon", font=("default", 14))
    self.canvas.create_text(420, 300, text="Status", font=("default", 14))
    self.canvas.create_text(420, 325, text="Dibayar", font=("default", 14))

    outlet = model.create_tambah_dropdown(self, self.tambah, x = 545, y = 100, procdrop="dropdownoutlet")
    karyawan = model.create_tambah_dropdown(self, self.tambah, x = 545, y = 125, procdrop="dropdownkasir")
    pelanggan = model.create_tambah_dropdown(self, self.tambah, x = 545, y = 150, procdrop="dropdownpelanggan")
    tanggal = model.create_tambah_date(self, self.tambah, x = 545, y = 175)
    batas_waktu = model.create_tambah_date(self, self.tambah, x = 545, y = 200)
    waktu_bayar = model.create_tambah_date(self, self.tambah, x = 545, y = 225)
    biaya_tambahan = model.create_tambah_entry(self, self.tambah, x = 545, y = 250)
    diskon = model.create_tambah_entry(self, self.tambah, x = 545, y = 275)
    status = model.create_tambah_enumdropdown(self, self.tambah, x = 545, y = 300, procenum="transaksistatus")
    dibayar = model.create_tambah_enumdropdown(self, self.tambah, x = 545, y = 300, procenum="transaksidibayar")

    def tambah():
        outlet_val = outlet.get()
        karyawan_val = karyawan.get()
        pelanggan_val = pelanggan.get()
        tanggal_val = tanggal.get_date()
        batas_waktu_val = batas_waktu.get_date()
        waktu_bayar_val = waktu_bayar.get_date()
        biaya_tambahan_val = biaya_tambahan.get()
        diskon_val = diskon.get()
        status_val = status.get()
        dibayar_val = dibayar.get()

        model.tambah(
            self, 
            frame=self.tambah,
            destroy=self.transaksi, 
            redirect=lambda: start_transaksi(self), 
            entries=(outlet_val, karyawan_val, pelanggan_val, tanggal_val, batas_waktu_val, waktu_bayar_val, biaya_tambahan_val, diskon_val, status_val, dibayar_val), 
            proc="transaksitambah")

    model.create_submit_button(self, x = 480, y = 375, frame=self.tambah, command=tambah)

def edit_transaksi(self):
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

    self.canvas.create_text(480, 50, text="Tambah Transaksi", anchor="center", font=("default", 28, "bold"))
    self.canvas.create_text(420, 100, text="Outlet", font=("default", 14))
    self.canvas.create_text(420, 125, text="Karyawan", font=("default", 14))
    self.canvas.create_text(420, 150, text="Pelanggan", font=("default", 14))
    self.canvas.create_text(420, 175, text="Tanggal", font=("default", 14))
    self.canvas.create_text(420, 200, text="Batas Waktu", font=("default", 14))
    self.canvas.create_text(420, 225, text="Waktu Bayar", font=("default", 14))
    self.canvas.create_text(420, 250, text="Biaya Tambahan", font=("default", 14))
    self.canvas.create_text(420, 275, text="Diskon", font=("default", 14))
    self.canvas.create_text(420, 300, text="Status", font=("default", 14))
    self.canvas.create_text(420, 325, text="Dibayar", font=("default", 14))

    outlet = model.create_edit_dropdown(self, self.edit, x = 545, y = 100, index=2, target_index=0, treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownoutlet")
    karyawan = model.create_edit_dropdown(self, self.edit, x = 545, y = 125, index=3, target_index=0, treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownkasir")
    pelanggan = model.create_edit_dropdown(self, self.edit, x = 545, y = 150, index=4, target_index=0, treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownpelanggan")
    tanggal = model.create_edit_date(self, self.edit, x = 545, y = 175, index=5, treeview=self.treeview, procid="transaksiselectbyid")
    batas_waktu = model.create_edit_date(self, self.edit, x = 545, y = 200, index=6, treeview=self.treeview, procid="transaksiselectbyid")
    waktu_bayar = model.create_edit_date(self, self.edit, x = 545, y = 225, index=7, treeview=self.treeview, procid="transaksiselectbyid")
    biaya_tambahan = model.create_edit_entry(self, self.edit, x = 545, y = 250, index=8, treeview=self.treeview, procid="transaksiselectbyid")
    diskon = model.create_edit_entry(self, self.edit, x = 545, y = 275, index=9, treeview=self.treeview, procid="transaksiselectbyid")
    status = model.create_edit_enumdropdown(self, self.edit, x = 545, y = 300, index=10, treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksistatus")
    dibayar = model.create_edit_enumdropdown(self, self.edit, x = 545, y = 325, index=11, treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksidibayar")

    def edit():
        id_val = model.get_id(self, treeview=self.treeview, procid="transaksiselectbyid")
        status_val = status.get()
        dibayar_val = dibayar.get()

        model.edit(
            self,
            frame=self.edit,
            destroy=self.transaksi,
            redirect=lambda: start_transaksi(self),
            entries=(id_val, status_val, dibayar_val),
            procedit="transaksiedit")

    model.create_submit_button(self, x = 480, y = 375, frame=self.edit, command=edit)

def detail_transaksi():
    pass