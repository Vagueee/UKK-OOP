from model import *
import login
import outlet
import paket
import karyawan
import pelanggan
import transaksi


class Main(ttk.Frame):
    def __init__(self, role, name):
        self.main = tk.Tk()
        self.main.title("Laundrive")
        self.main.geometry("960x540+180+50")
        self.main.resizable(False, False)
        self.main.protocol("WM_DELETE_WINDOW", lambda: on_closing(self))
        self.main.call('source', 'azure.tcl')
        self.main.call('set_theme', 'dark')
        self.frame = ttk.Frame(self.main)
        self.frame.pack(fill="both", expand=False)
        self.canvas = tk.Canvas(self.main, width=960, height=540)
        self.canvas.pack(fill="both", expand=True)

        database(self)
        roles = role
        names = name

        menubar = tk.Menu(self.main)
        self.main.config(menu=menubar)

        menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=menu)
        menu.add_command(
            label="Data Outlet", command=lambda: outlet.start_outlet(self, role=roles))
        menu.add_command(
            label="Data Paket", command=lambda: paket.start_paket(self, role=roles))
        menu.add_command(label="Data Karyawan", command=lambda: karyawan.start_karyawan(
            self, role=roles))
        menu.add_command(label="Data Pelanggan", command=lambda: pelanggan.start_pelanggan(
            self, role=roles))
        menu.add_command(label="Data Transaksi", command=lambda: transaksi.start_transaksi(
            self, role=roles))
        menu.add_separator()
        menu.add_command(label="Log Out", command=lambda: logout(self))
        menu.add_command(label="Exit", command=lambda: on_closing(self))

        self.canvas.create_text(480, 50, text="Laundrive", anchor="center", font=(
            "Verdana", 28, "bold"), fill="#b5b3b3")
        self.canvas.create_text(20, 20, text=names, anchor="w", font=(
            "Verdana", 14), fill="#b5b3b3")

        graph = bargraph(self, title="Pendapatan Total Laundry",
                         x="Waktu (Tanggal)", y="Pendapatan (Rp.)", style="bmh", proc="pendapatan")
        canvas = FigureCanvasTkAgg(graph, self.main)
        graph_canvas = canvas.get_tk_widget()
        self.canvas.create_window(480, 300, window=graph_canvas)


def logout(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        relog = tk.Tk()
        relog.title("Re Login")
        relog.geometry("960x540+180+50")
        self.role = None,
        self.name = None,
        plt.close("all")
        self.main.destroy()
        login.Login(relog)


def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        plt.close("all")
        self.main.destroy()
