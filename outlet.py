from model import *


def start_outlet(self, role):
    self.outlet = tk.Toplevel()
    self.outlet.title("Laundrive")
    self.outlet.geometry("960x540+180+80")
    self.outlet.resizable(False, False)
    # self.outlet.protocol("WM_DELETE_WINDOW", lambda: on_closing(self))
    self.frame = ttk.Frame(self.outlet)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.outlet, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)
    self.role = role

    menubar = tk.Menu(self.outlet)
    self.outlet.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menu.add_command(
        label="Exit", command=self.outlet.destroy)

    self.canvas.create_text(480, 50, text="Data Outlet", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self,
        frame=self.outlet,
        x=480,
        y=150,
        proc='outletselect',
        columns=('id', 'nama', 'alamat', 'tlp'),
        headings=('id', 'nama', 'alamat', 'tlp'),
        texts=('ID', 'Nama', 'Alamat', 'No. Telp'))

    if self.role == "Admin":
        tambah_button = create_crud_button(
            self, frame=self.outlet, x=60, y=110, text="Tambah Data", command=lambda: tambah_outlet(self))
        edit_button = create_crud_button(self, frame=self.outlet, x=165, y=110, disabled=len(
            treeview.selection()) == 0, text="Edit Data", command=lambda: edit_outlet(self))
        delete_button = create_crud_button(self, frame=self.outlet, x=265, y=110, disabled=len(
            treeview.selection()) == 0, text="Delete Data", command=lambda: delete_outlet(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch(
            [edit_button, delete_button], selection=treeview.selection()))

    var_search = StringVar()
    search_bar = search_entry(
        self, frame=self.outlet, txtvar=var_search, x=480, y=110)
    search_bar.bind("<Key>", lambda event: search(
        self, proc="outletsearch", search=var_search.get(), treeview=treeview))

    csv_button = create_laporan_button(
        self, frame=self.outlet, x=800, y=110, text="Export CSV", command=lambda: csv_outlet(self))
    xls_button = create_laporan_button(
        self, frame=self.outlet, x=900, y=110, text="Export Excel", command=lambda: xls_outlet(self))


def csv_outlet(self):
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


def xls_outlet(self):
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


def tambah_outlet(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Outlet", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(405, 100, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(405, 140, text="Alamat",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(405, 180, text="No. Telp",
                            font=("Verdana", 14), fill="#b5b3b3")

    nama = create_tambah_entry(self, self.tambah, x=545, y=100)
    alamat = create_tambah_entry(self, self.tambah, x=545, y=140)
    telp = create_tambah_entry(self, self.tambah, x=545, y=180)

    def tambahdata():
        nama_val = nama.get()
        alamat_val = alamat.get()
        telp_val = telp.get()

        validate = validate_number(values=(telp_val))
        if validate == True:
            tambah(
                self,
                frame=self.tambah,
                destroy=self.outlet,
                redirect=lambda: start_outlet(self),
                entries=(nama_val, alamat_val, telp_val),
                proc="outlettambah")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x=480, y=220,
                         frame=self.tambah, command=tambahdata)


def edit_outlet(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = ttk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Edit Outlet", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(405, 100, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(405, 140, text="Alamat",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(405, 180, text="No. Telp",
                            font=("Verdana", 14), fill="#b5b3b3")

    nama = create_edit_entry(self, self.edit, x=545, y=100, index=1,
                             state='normal', treeview=self.treeview, procid="outletselectbyid")
    alamat = create_edit_entry(self, self.edit, x=545, y=140, index=2,
                               state='normal', treeview=self.treeview, procid="outletselectbyid")
    telp = create_edit_entry(self, self.edit, x=545, y=180, index=3,
                             state='normal', treeview=self.treeview, procid="outletselectbyid")

    def editdata():
        id_val = get_id(self, treeview=self.treeview,
                        procid="outletselectbyid")
        nama_val = nama.get()
        alamat_val = alamat.get()
        telp_val = telp.get()

        validate = validate_number(values=(telp_val))
        if validate == True:
            edit(
                self,
                frame=self.edit,
                destroy=self.outlet,
                redirect=lambda: start_outlet(self),
                entries=(id_val, nama_val, alamat_val, telp_val),
                procedit="outletedit")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x=480, y=220, frame=self.edit, command=editdata)


def delete_outlet(self):
    delete(
        self,
        treeview=self.treeview,
        proc="outletdelete")


def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.outlet.destroy()
