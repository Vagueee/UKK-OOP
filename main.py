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

        database(self)

        self.canvas.create_text(480, 50, text="Laundrive", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")

        menubar = tk.Menu(self.main)
        self.main.config(menu=menubar)

        menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Data", menu=menu)
        menu.add_command(label="Data Outlet", command=lambda: outlet.start_outlet(self))
        menu.add_command(label="Data Paket", command=lambda: paket.start_paket(self))
        menu.add_command(label="Data Karyawan", command=lambda: karyawan.start_karyawan(self))
        menu.add_command(label="Data Pelanggan", command=lambda: pelanggan.start_pelanggan(self))
        menu.add_command(label="Data Transaksi", command=lambda: transaksi.start_transaksi(self))
        menu.add_separator()
        menu.add_command(label="Exit", command=self.main.destroy)

        graph = graphic(self, proc="pendapatan")
        canvas = FigureCanvasTkAgg(graph, self.main)
        graph_canvas = canvas.get_tk_widget()

        self.canvas.create_window(480, 300, window=graph_canvas)

        # ot_frame = create_card(self, x = 260, y = 160)
        # pkt_frame = create_card(self, x = 360, y = 300)
        # kar_frame = create_card(self, x = 480, y = 160)
        # plg_frame = create_card(self, x = 600, y = 300)
        # tr_frame = create_card(self, x = 700, y = 160)

        # # Button + label
        # create_button(
        #     self,
        #     frame=ot_frame,
        #     image=self.otimg,
        #     text="Data Outlet",
        #     command=lambda: outlet.start_outlet(self)
        # )
        
        # create_button(
        #     self,
        #     frame=pkt_frame,
        #     image=self.pktimg,
        #     text="Data Paket",
        #     command=lambda: paket.start_paket(self)
        # )

        # create_button(
        #     self,
        #     frame=kar_frame,
        #     image=self.karimg,
        #     text="Data Karyawan",
        #     command=lambda: karyawan.start_karyawan(self)
        # )

        # create_button(
        #     self,
        #     frame=plg_frame,
        #     image=self.plgimg,
        #     text="Data Pelanggan",
        #     command=lambda: pelanggan.start_pelanggan(self)
        # )

        # create_button(
        #     self,
        #     frame=tr_frame,
        #     image=self.trimg,
        #     text="Data Transaksi",
        #     command=lambda: transaksi.start_transaksi(self)
        # )
