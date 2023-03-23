from model import *

def start_transaksi(self):
    self.transaksi = tk.Toplevel()
    self.transaksi.title("Laundrive")
    self.transaksi.geometry("960x540+180+80")
    self.transaksi.resizable(False, False)
    self.frame = ttk.Frame(self.transaksi)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.transaksi, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Data Transaksi", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self, 
        frame=self.transaksi, 
        x= 480,
        y= 150,
        proc='transaksiselect', 
        columns=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        headings=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan', 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'), 
        texts=('ID', 'Kode Invoice', 'Outlet', 'Karyawan', 'Pelanggan', 'Tanggal', 'Batas Waktu', 'Waktu Bayar', 'Status', 'Dibayar'))

    csv_button = create_laporan_button(self, frame=self.transaksi, x=100, y=110 ,text="Export as CSV", command=lambda: csv_transaksi(self))

    tambah_button = create_crud_button(self, frame=self.transaksi, x=355, y=110, text="Tambah Data", command=lambda: tambah_transaksi(self))
    edit_button = create_crud_button(self, frame=self.transaksi, x=480, y=110, disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_transaksi(self))
    detail_button = create_crud_button(self, frame=self.transaksi, x=600, y=110, disabled=len(treeview.selection()) == 0, text="Detail Data", command=lambda: detail_transaksi(self))

    treeview.bind("<ButtonRelease-1>", lambda event: switch([edit_button, detail_button], selection=treeview.selection()))

def csv_transaksi(self):
    Verdana_filename = 'data.csv'
    initial_dir = '.'
    filetypes = [('CSV files', '*.csv')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(Verdanaextension='.csv', initialfile=Verdana_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        importcsv(
        filename=filename,
        treeview=self.treeview)

def tambah_transaksi(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Transaksi", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(415, 100, text="Outlet", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 140, text="Karyawan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 180, text="Pelanggan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 220, text="Tanggal", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 260, text="Batas Waktu", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 300, text="Waktu Bayar", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 340, text="Biaya Tambahan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 380, text="Diskon", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 420, text="Status", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 460, text="Dibayar", font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_tambah_dropdown(self, self.tambah, x = 550, y = 100, procdrop="dropdownoutlet")
    karyawan = create_tambah_dropdown(self, self.tambah, x = 550, y = 140, procdrop="dropdownkasir")
    pelanggan = create_tambah_dropdown(self, self.tambah, x = 550, y = 180, procdrop="dropdownpelanggan")
    tanggal = create_tambah_date(self, self.tambah, x = 550, y = 220)
    batas_waktu = create_tambah_date(self, self.tambah, x = 550, y = 260)
    waktu_bayar = create_tambah_date(self, self.tambah, x = 550, y = 300)
    biaya_tambahan = create_tambah_entry(self, self.tambah, x = 550, y = 340)
    diskon = create_tambah_entry(self, self.tambah, x = 550, y = 380)
    status = create_tambah_enumdropdown(self, self.tambah, x = 550, y = 420, procenum="transaksistatus")
    dibayar = create_tambah_enumdropdown(self, self.tambah, x = 550, y = 460, procenum="transaksidibayar")

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

        tambah(
            self, 
            frame=self.tambah,
            destroy=self.tambah, 
            redirect=lambda: tambah_detail_transaksi(self), 
            entries=(outlet_val, karyawan_val, pelanggan_val, tanggal_val, batas_waktu_val, waktu_bayar_val, biaya_tambahan_val, diskon_val, status_val, dibayar_val), 
            proc="transaksitambah")

    create_submit_button(self, x = 480, y = 500, frame=self.tambah, command=tambah)

def tambah_detail_transaksi(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Detail Transaksi", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Paket", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Keterangan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="Kuantitas", font=("Verdana", 14), fill="#b5b3b3")

    paket = create_tambah_dropdown(self, self.tambah, x = 545, y = 100, procdrop="dropdownpaket")
    keterangan = create_tambah_entry(self, self.tambah, x = 545, y = 140)
    qty = create_tambah_entry(self, self.tambah, x = 545, y = 180)

    def tambah():
        self.cursor.execute('call detailidtransaksi();')
        id_val = self.cursor.fetchone()

        paket_val = paket.get()
        keterangan_val = keterangan.get()
        qty_val = qty.get()

        tambah(
            self, 
            frame=self.tambah,
            destroy=self.transaksi, 
            redirect=lambda: start_transaksi(self), 
            entries=(id_val[0], paket_val, keterangan_val, qty_val), 
            proc="detailtambah")

    create_submit_button(self, x = 480, y = 220, frame=self.tambah, command=tambah)


def edit_transaksi(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = ttk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Transaksi", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(415, 100, text="Outlet", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 140, text="Karyawan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 180, text="Pelanggan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 220, text="Tanggal", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 260, text="Batas Waktu", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 300, text="Waktu Bayar", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 340, text="Biaya Tambahan", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 380, text="Diskon", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 420, text="Status", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 460, text="Dibayar", font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_edit_dropdown(self, self.edit, x = 550, y = 100, index=2, target_index=0, state='disabled', treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownoutlet")
    karyawan = create_edit_dropdown(self, self.edit, x = 550, y = 140, index=3, target_index=0, state='disabled', treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownkasir")
    pelanggan = create_edit_dropdown(self, self.edit, x = 550, y = 180, index=4, target_index=0, state='disabled', treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownpelanggan")
    tanggal = create_edit_date(self, self.edit, x = 550, y = 220, index=5, state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    batas_waktu = create_edit_date(self, self.edit, x = 550, y = 260, index=6, state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    waktu_bayar = create_edit_date(self, self.edit, x = 550, y = 300, index=7, state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    biaya_tambahan = create_edit_entry(self, self.edit, x = 550, y = 340, index=8, state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    diskon = create_edit_entry(self, self.edit, x = 550, y = 380, index=9, state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    status = create_edit_enumdropdown(self, self.edit, x = 550, y = 420, index=10, state='normal', treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksistatus")
    dibayar = create_edit_enumdropdown(self, self.edit, x = 550, y = 460, index=11, state='normal', treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksidibayar")

    def edit():
        id_val = get_id(self, treeview=self.treeview, procid="transaksiselectbyid")
        status_val = status.get()
        dibayar_val = dibayar.get()

        edit(
            self,
            frame=self.edit,
            destroy=self.transaksi,
            redirect=lambda: start_transaksi(self),
            entries=(id_val, status_val, dibayar_val),
            procedit="transaksiedit")

    create_submit_button(self, x = 480, y = 500, frame=self.edit, command=edit)

def detail_transaksi(self):
    self.detail = tk.Toplevel()
    self.detail.title("Laundrive")
    self.detail.geometry("400x540+260+80")
    self.detail.resizable(False, False)
    self.frame = ttk.Frame(self.detail)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.detail, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    detail = self.treeview.selection()[0]
    values = self.treeview.item(detail, 'values')
    proc = "detailselectbyid"
    self.cursor.callproc(proc, (values[0],))
    result = self.cursor.stored_results()

    data = None
    for rows in result:
        data = rows.fetchall()[0]
    
    self.canvas.create_text(200, 100, text=f"Id Paket : {data[0]}", anchor="center", font=("Verdana", 12))
    self.canvas.create_text(200, 140, text=f"Kuantitas : {data[1]}", anchor="center", font=("Verdana", 12))
    self.canvas.create_text(200, 180, text=f"Keterangan : {data[2]}", anchor="center", font=("Verdana", 12))
    self.canvas.create_text(200, 220, text=f"Total Harga : {data[3]}", anchor="center", font=("Verdana", 12))