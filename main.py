import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font
from dotenv import load_dotenv
import model
import outlet
import paket
import karyawan
import pelanggan
import transaksi
load_dotenv()

class Main(tk.Frame):
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Laundrive")
        self.main.geometry("960x540+180+50")
        self.main.resizable(False, False)
        self.frame = tk.Frame(self.main)
        self.frame.pack(fill="both", expand=False)
        self.logged_in = None
        self.user_role = None
        self.canvas = tk.Canvas(self.main, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        model.backgroundimg(self)
        model.btnimg(self)

        self.canvas.create_text(480, 50, text="Laundrive", anchor="center", font=("default", 28, "bold"))

        self.ot_frame = model.create_card(self, x = 260, y = 160)
        self.pkt_frame = model.create_card(self, x = 360, y = 300)
        self.kar_frame = model.create_card(self, x = 480, y = 160)
        self.plg_frame = model.create_card(self, x = 600, y = 300)
        self.tr_frame = model.create_card(self, x = 700, y = 160)

        # Button + label
        model.create_button(
            self,
            frame=self.ot_frame,
            image=self.otimg,
            text="Data Outlet",
            command=lambda: outlet.start_outlet(self)
        )
        
        model.create_button(
            self,
            frame=self.pkt_frame,
            image=self.pktimg,
            text="Data Paket",
            command=lambda: paket.start_paket(self)
        )

        model.create_button(
            self,
            frame=self.kar_frame,
            image=self.karimg,
            text="Data Karyawan",
            command=lambda: karyawan.start_karyawan(self)
        )

        model.create_button(
            self,
            frame=self.plg_frame,
            image=self.plgimg,
            text="Data Pelanggan",
            command=lambda: pelanggan.start_pelanggan(self)
        )

        model.create_button(
            self,
            frame=self.tr_frame,
            image=self.trimg,
            text="Data Transaksi",
            command=lambda: transaksi.start_transaksi(self)
        )
