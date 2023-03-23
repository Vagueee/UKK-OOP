from model import *
import outlet
import paket
import karyawan
import pelanggan
import transaksi

class Main(ttk.Frame):
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Laundrive")
        self.main.geometry("960x540+180+50")
        self.main.resizable(False, False)
        self.main.call('source', 'azure.tcl')
        self.main.call('set_theme', 'dark')
        self.frame = ttk.Frame(self.main)
        self.frame.pack(fill="both", expand=False)
        self.canvas = tk.Canvas(self.main, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        btnimg(self)

        self.canvas.create_text(480, 50, text="Laundrive", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")

        self.ot_frame = create_card(self, x = 260, y = 160)
        self.pkt_frame = create_card(self, x = 360, y = 300)
        self.kar_frame = create_card(self, x = 480, y = 160)
        self.plg_frame = create_card(self, x = 600, y = 300)
        self.tr_frame = create_card(self, x = 700, y = 160)

        # Button + label
        create_button(
            self,
            frame=self.ot_frame,
            image=self.otimg,
            text="Data Outlet",
            command=lambda: outlet.start_outlet(self)
        )
        
        create_button(
            self,
            frame=self.pkt_frame,
            image=self.pktimg,
            text="Data Paket",
            command=lambda: paket.start_paket(self)
        )

        create_button(
            self,
            frame=self.kar_frame,
            image=self.karimg,
            text="Data Karyawan",
            command=lambda: karyawan.start_karyawan(self)
        )

        create_button(
            self,
            frame=self.plg_frame,
            image=self.plgimg,
            text="Data Pelanggan",
            command=lambda: pelanggan.start_pelanggan(self)
        )

        create_button(
            self,
            frame=self.tr_frame,
            image=self.trimg,
            text="Data Transaksi",
            command=lambda: transaksi.start_transaksi(self)
        )
