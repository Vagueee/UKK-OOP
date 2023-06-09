from model import *


def start_transaksi(self, role):
    self.transaksi = tk.Toplevel()
    self.transaksi.title("Laundrive")
    self.transaksi.geometry("960x540+180+80")
    self.transaksi.resizable(False, False)
    self.transaksi.protocol("WM_DELETE_WINDOW", lambda: on_closing(self))
    self.frame = ttk.Frame(self.transaksi)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.transaksi, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)
    self.role = role

    menubar = tk.Menu(self.transaksi)
    self.transaksi.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menu.add_command(
        label="Exit", command=self.transaksi.destroy)

    self.canvas.create_text(480, 50, text="Data Transaksi", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self,
        frame=self.transaksi,
        x=480,
        y=150,
        proc='transaksiselect',
        columns=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan',
                 'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'),
        headings=('id', 'kode_invoice', 'outlet', 'karyawan', 'pelanggan',
                  'tgl', 'batas_waktu', 'waktu_bayar', 'status', 'dibayar'),
        texts=('ID', 'Kode Invoice', 'Outlet', 'Karyawan', 'Pelanggan', 'Tanggal', 'Batas Waktu', 'Waktu Bayar', 'Status', 'Dibayar'))

    if self.role != "Owner":
        tambah_button = create_crud_button(
            self, frame=self.transaksi, x=60, y=110, text="Tambah Data", command=lambda: tambah_transaksi(self))
        edit_button = create_crud_button(self, frame=self.transaksi, x=165, y=110, disabled=len(
            treeview.selection()) == 0, text="Edit Data", command=lambda: edit_transaksi(self))
        detail_button = create_crud_button(self, frame=self.transaksi, x=265, y=110, disabled=len(
            treeview.selection()) == 0, text="Detail Data", command=lambda: detail_transaksi(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch(
            [edit_button, detail_button], selection=treeview.selection()))

    else:
        detail_button_owner = create_crud_button(self, frame=self.transaksi, x=60, y=110, disabled=len(
            treeview.selection()) == 0, text="Detail Data", command=lambda: detail_transaksi(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch(
            [detail_button_owner], selection=treeview.selection()))

    var_search = StringVar()
    search_bar = search_entry(
        self, frame=self.transaksi, txtvar=var_search, x=480, y=110)
    search_bar.bind("<Key>", lambda event: search(
        self, proc="transaksisearch", search=var_search.get(), treeview=treeview))

    csv_button = create_laporan_button(
        self, frame=self.transaksi, x=800, y=110, text="Export CSV", command=lambda: csv_transaksi(self))
    xls_button = create_laporan_button(
        self, frame=self.transaksi, x=900, y=110, text="Export Excel", command=lambda: xls_transaksi(self))


def csv_transaksi(self):
    default_filename = 'data.csv'
    initial_dir = '.'
    filetypes = [('CSV files', '*.csv')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(
        defaultextension='.csv', initialfile=default_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        exportcsv(
            filename=filename,
            treeview=self.treeview)


def xls_transaksi(self):
    default_filename = 'data.xlsx'
    initial_dir = '.'
    filetypes = [('Excel', '*.xslx')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(
        defaultextension='.xslx', initialfile=default_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        exportxls(
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

    self.canvas.create_text(480, 50, text="Tambah Transaksi", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(410, 100, text="Outlet",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 140, text="Karyawan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 180, text="Pelanggan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 220, text="Tanggal",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 260, text="Batas Waktu",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 300, text="Waktu Bayar",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 340, text="Biaya Tambahan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 380, text="Diskon",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 420, text="Status",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 460, text="Dibayar",
                            font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_tambah_dropdown(
        self, self.tambah, x=570, y=100, procdrop="dropdownoutlet")
    karyawan = create_tambah_dropdown(
        self, self.tambah, x=570, y=140, procdrop="dropdownkasir")
    pelanggan = create_tambah_dropdown(
        self, self.tambah, x=570, y=180, procdrop="dropdownpelanggan")
    tanggal = create_tambah_date(self, self.tambah, x=570, y=220)
    batas_waktu = create_tambah_date(self, self.tambah, x=570, y=260)
    waktu_bayar = create_tambah_date(self, self.tambah, x=570, y=300)
    biaya_tambahan = create_tambah_entry(self, self.tambah, x=570, y=340)
    diskon = create_tambah_entry(self, self.tambah, x=570, y=380)
    status = create_tambah_enumdropdown(
        self, self.tambah, x=570, y=420, procenum="transaksistatus")
    dibayar = create_tambah_enumdropdown(
        self, self.tambah, x=570, y=460, procenum="transaksidibayar")

    def tambahdata():
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
            redirect=lambda: tambah_detail_transaksi(
                self, outlet_val=outlet_val),
            entries=(outlet_val, karyawan_val, pelanggan_val, tanggal_val, batas_waktu_val,
                     waktu_bayar_val, biaya_tambahan_val, diskon_val, status_val, dibayar_val),
            proc="transaksitambah")

    create_submit_button(self, x=480, y=500,
                         frame=self.tambah, command=tambahdata)


def tambah_detail_transaksi(self, outlet_val):
    self.tambahdet = tk.Toplevel()
    self.tambahdet.title("Laundrive")
    self.tambahdet.geometry("960x540+180+80")
    self.tambahdet.resizable(False, False)
    self.frame = ttk.Frame(self.tambahdet)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambahdet, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Detail Transaksi",
                            anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(410, 100, text="Paket",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 140, text="Kuantitas",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 180, text="Keterangan",
                            font=("Verdana", 14), fill="#b5b3b3")

    paket = create_tambah_dropdown_sorted(
        self, self.tambahdet, x=570, y=100, procdrop="dropdownpaket", sortby=outlet_val)
    qty = create_tambah_entry(self, self.tambahdet, x=570, y=140)
    keterangan = create_tambah_entry(self, self.tambahdet, x=570, y=180)

    def tambahdata():
        self.cursor.execute(
            'SELECT id_transaksi FROM tb_transaksi ORDER BY id_transaksi DESC LIMIT 1;')
        id_val = self.cursor.fetchone()

        paket_val = paket.get()
        qty_val = qty.get()
        keterangan_val = keterangan.get()

        tambah(
            self,
            frame=self.tambahdet,
            destroy=self.transaksi,
            redirect=lambda: start_transaksi(self, role=self.role),
            entries=(id_val[0], paket_val, qty_val, keterangan_val),
            proc="detailtambah")

    create_submit_button(self, x=480, y=220,
                         frame=self.tambahdet, command=tambahdata)


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

    self.canvas.create_text(480, 50, text="Tambah Transaksi", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(410, 100, text="Outlet",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 140, text="Karyawan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 180, text="Pelanggan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 220, text="Tanggal",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 260, text="Batas Waktu",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 300, text="Waktu Bayar",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 340, text="Biaya Tambahan",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 380, text="Diskon",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 420, text="Status",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(410, 460, text="Dibayar",
                            font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_edit_dropdown(self, self.edit, x=570, y=100, index=2, target_index=0, state='disabled',
                                  treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownoutlet")
    karyawan = create_edit_dropdown(self, self.edit, x=570, y=140, index=3, target_index=0, state='disabled',
                                    treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownkasir")
    pelanggan = create_edit_dropdown(self, self.edit, x=570, y=180, index=4, target_index=0, state='disabled',
                                     treeview=self.treeview, procid="transaksiselectbyid", procdrop="dropdownpelanggan")
    tanggal = create_edit_date(self, self.edit, x=570, y=220, index=5,
                               state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    batas_waktu = create_edit_date(self, self.edit, x=570, y=260, index=6,
                                   state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    waktu_bayar = create_edit_date(self, self.edit, x=570, y=300, index=7,
                                   state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    biaya_tambahan = create_edit_entry(self, self.edit, x=570, y=340, index=8,
                                       state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    diskon = create_edit_entry(self, self.edit, x=570, y=380, index=9,
                               state='disabled', treeview=self.treeview, procid="transaksiselectbyid")
    status = create_edit_enumdropdown(self, self.edit, x=570, y=420, index=10, state='normal',
                                      treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksistatus")
    dibayar = create_edit_enumdropdown(self, self.edit, x=570, y=460, index=11, state='normal',
                                       treeview=self.treeview, procid="transaksiselectbyid", procenum="transaksidibayar")

    def editdata():
        id_val = get_id(self, treeview=self.treeview,
                        procid="transaksiselectbyid")
        status_val = status.get()
        dibayar_val = dibayar.get()

        edit(
            self,
            frame=self.edit,
            destroy=self.transaksi,
            redirect=lambda: start_transaksi(self, role=self.role),
            entries=(id_val, status_val, dibayar_val),
            procedit="transaksiedit")

    create_submit_button(self, x=480, y=500, frame=self.edit, command=editdata)


def detail_transaksi(self):
    self.detail = tk.Toplevel()
    self.detail.title("Laundrive")
    self.detail.geometry("700x540+260+80")
    self.detail.resizable(False, False)
    self.frame = ttk.Frame(self.detail)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.detail, width=400, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    detail = self.treeview.selection()[0]
    values = self.treeview.item(detail, 'values')
    proc = "detailselectbyid"
    self.cursor.callproc(proc, (values[0],))
    result = self.cursor.stored_results()

    data = None
    for rows in result:
        data = rows.fetchone()

    self.canvas.create_text(120, 60, text="Laundrive", anchor="n", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(20, 140, text=f"Kode Invoice \n{data[0]}", anchor="w", font=(
        "Verdana", 12), fill="#b5b3b3")

    self.canvas.create_text(20, 220, text=f"Klien \n\n{data[2]}", anchor="w", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(20, 260, text=f"{data[4]}", anchor="w", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(20, 280, text=f"{data[3]}", anchor="w", font=(
        "Verdana", 12), fill="#b5b3b3", width=300)
    self.canvas.create_text(680, 220, text=f"Outlet\n\n{data[5]}", anchor="e", font=(
        "Verdana", 12), fill="#b5b3b3", justify="right")
    self.canvas.create_text(680, 260, text=f"{data[7]}", anchor="e", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(680, 270, text=f"{data[6]}", anchor="ne", font=(
        "Verdana", 12), fill="#b5b3b3", width=300, justify="right")

    self.canvas.create_text(20, 420, text=f"Paket \n\n{data[8]}", anchor="w", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(220, 420, text=f"Keterangan \n\n{data[9]}", anchor="center", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(480, 420, text=f"Kuantitas \n\n{data[10]}", anchor="center", font=(
        "Verdana", 12), fill="#b5b3b3")
    self.canvas.create_text(680, 420, text=f"Total Harga\n\nRp. {int(data[14])}", anchor="e", font=(
        "Verdana", 12), fill="#b5b3b3", justify="right")

    def pdf_invoice(data):
        default_filename = 'invoice.pdf'
        initial_dir = '.'
        filetypes = [('PDF', '*.pdf')]
        # Prompt the user to choose a filename and location
        filename = filedialog.asksaveasfilename(
            defaultextension='.pdf', initialfile=default_filename, initialdir=initial_dir, filetypes=filetypes)
        if filename:
            exportpdf(
                filename=filename,
                inv=data[0],
                tgl=data[1],
                namapel=data[2],
                alamatpel=data[3],
                telppel=data[4],
                namaout=data[5],
                alamatout=data[6],
                telpout=data[7],
                paket=data[8],
                desk=data[9],
                kuan=data[10],
                harga=data[11],
                pajak=data[12],
                diskon=data[13],
                total=data[14],
            )

    pdf_button = create_laporan_button(
        self, frame=self.detail, x=60, y=30, text="PDF", command=lambda: pdf_invoice(data))


def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.main.destroy()
