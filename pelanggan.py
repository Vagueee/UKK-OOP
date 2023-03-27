from model import *


def start_pelanggan(self, role):
    self.pelanggan = tk.Toplevel()
    self.pelanggan.title("Laundrive")
    self.pelanggan.geometry("960x540+180+80")
    self.pelanggan.resizable(False, False)
    self.frame = ttk.Frame(self.pelanggan)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.pelanggan, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)
    self.role = role

    menubar = tk.Menu(self.pelanggan)
    self.pelanggan.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menu.add_command(
        label="Exit", command=self.pelanggan.destroy)

    self.canvas.create_text(480, 50, text="Data Pelanggan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self,
        frame=self.pelanggan,
        x=480,
        y=150,
        proc='pelangganselect',
        columns=('id', 'nama', 'alamat', 'jenis_kelamin', 'tlp'),
        headings=('id', 'nama', 'alamat', 'jenis_kelamin', 'tlp'),
        texts=('ID', 'Nama', 'Alamat', 'Jenis Kelamin', 'No. Telp'))

    csv_button = create_laporan_button(
        self, frame=self.pelanggan, x=60, y=110, text="CSV", command=lambda: csv_pelanggan(self))
    xls_button = create_laporan_button(
        self, frame=self.pelanggan, x=160, y=110, text="Excel", command=lambda: xls_pelanggan(self))

    if self.role != "Owner":
        tambah_button = create_crud_button(
            self, frame=self.pelanggan, x=360, y=110, text="Tambah Data", command=lambda: tambah_pelanggan(self))
        edit_button = create_crud_button(self, frame=self.pelanggan, x=480, y=110, disabled=len(
            treeview.selection()) == 0, text="Edit Data", command=lambda: edit_pelanggan(self))
        delete_button = create_crud_button(self, frame=self.pelanggan, x=600, y=110, disabled=len(
            treeview.selection()) == 0, text="Delete Data", command=lambda: delete_pelanggan(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch(
            [edit_button, delete_button], selection=treeview.selection()))


def csv_pelanggan(self):
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


def xls_pelanggan(self):
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


def tambah_pelanggan(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Pelanggan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Alamat",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="Jenis Kelamin",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 220, text="No. Telp",
                            font=("Verdana", 14), fill="#b5b3b3")

    nama = create_tambah_entry(self, self.tambah, x=545, y=100)
    alamat = create_tambah_entry(self, self.tambah, x=545, y=140)
    jenis_kelamin = create_tambah_enumdropdown(
        self, self.tambah, x=545, y=180, procenum="pelangganjk")
    telp = create_tambah_entry(self, self.tambah, x=545, y=220)

    def tambahdata():
        nama_val = nama.get()
        alamat_val = alamat.get()
        jenis_kelamin_val = jenis_kelamin.get()
        telp_val = telp.get()

        validate = validate_number(values=(telp_val))
        if validate == True:
            tambah(
                self,
                frame=self.tambah,
                destroy=self.pelanggan,
                redirect=lambda: start_pelanggan(self),
                entries=(nama_val, alamat_val, jenis_kelamin_val, telp_val),
                proc="pelanggantambah")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x=480, y=265,
                         frame=self.tambah, command=tambahdata)


def edit_pelanggan(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = ttk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Edit Pelanggan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Alamat",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Jenis Kelamin",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 220, text="No. Telp",
                            font=("Verdana", 14), fill="#b5b3b3")

    nama = create_edit_entry(self, self.edit, x=545, y=100, index=1,
                             state='normal', treeview=self.treeview, procid="pelangganselectbyid")
    alamat = create_edit_entry(self, self.edit, x=545, y=140, index=2,
                               state='normal', treeview=self.treeview, procid="pelangganselectbyid")
    jenis_kelamin = create_edit_enumdropdown(self, self.edit, x=545, y=180, index=3, state='normal',
                                             treeview=self.treeview, procid="pelangganselectbyid", procenum="pelangganjk")
    telp = create_edit_entry(self, self.edit, x=545, y=220, index=4,
                             state='normal', treeview=self.treeview, procid="pelangganselectbyid")

    def editdata():
        id_val = get_id(self, treeview=self.treeview,
                        procid="pelangganselectbyid")
        nama_val = nama.get()
        alamat_val = alamat.get()
        jenis_kelamin_val = jenis_kelamin.get()
        telp_val = telp.get()

        validate = validate_number(values=(telp_val))
        if validate == True:
            edit(
                self,
                frame=self.edit,
                destroy=self.paket,
                redirect=lambda: start_pelanggan(self),
                entries=(id_val, nama_val, alamat_val,
                         jenis_kelamin_val, telp_val),
                procedit="paketedit")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x=480, y=265, frame=self.edit, command=editdata)


def delete_pelanggan(self):
    delete(
        self,
        treeview=self.treeview,
        proc="pelanggandelete")
