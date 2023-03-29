from model import *


def start_karyawan(self, role):
    self.karyawan = tk.Toplevel()
    self.karyawan.title("Laundrive")
    self.karyawan.geometry("960x540+180+80")
    self.karyawan.resizable(False, False)
    self.karyawan.protocol("WM_DELETE_WINDOW", lambda: on_closing(self))
    self.frame = ttk.Frame(self.karyawan)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.karyawan, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)
    self.role = role

    menubar = tk.Menu(self.karyawan)
    self.karyawan.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menu.add_command(
        label="Exit", command=self.karyawan.destroy)

    self.canvas.create_text(480, 50, text="Data Karyawan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self,
        frame=self.karyawan,
        x=480,
        y=150,
        proc='karyawanselect',
        columns=('id', 'outlet', 'nama', 'username', 'role'),
        headings=('id', 'outlet', 'nama', 'username', 'role'),
        texts=('ID', 'Outlet', 'Nama', 'Username', 'Role')
    )

    if self.role == "Admin":
        tambah_button = create_crud_button(
            self, frame=self.karyawan, x=60, y=110, text="Tambah Data", command=lambda: tambah_karyawan(self))
        edit_button = create_crud_button(self, frame=self.karyawan, x=165, y=110, disabled=len(
            treeview.selection()) == 0, text="Edit Data", command=lambda: edit_karyawan(self))
        delete_button = create_crud_button(self, frame=self.karyawan, x=265, y=110, disabled=len(
            treeview.selection()) == 0, text="Delete Data", command=lambda: delete_karyawan(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch(
            [edit_button, delete_button], selection=treeview.selection()))

    var_search = StringVar()
    search_bar = search_entry(
        self, frame=self.karyawan, txtvar=var_search, x=480, y=110)
    search_bar.bind("<Key>", lambda event: search(
        self, proc="karyawansearch", search=var_search.get(), treeview=treeview))

    csv_button = create_laporan_button(
        self, frame=self.karyawan, x=800, y=110, text="CSV", command=lambda: csv_karyawan(self))
    xls_button = create_laporan_button(
        self, frame=self.karyawan, x=900, y=110, text="Excel", command=lambda: xls_karyawan(self))


def csv_karyawan(self):
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


def xls_karyawan(self):
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


def tambah_karyawan(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Karyawan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(415, 100, text="Outlet",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 140, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 180, text="Username",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 220, text="Password",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 260, text="Role",
                            font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_tambah_dropdown(
        self, self.tambah, x=550, y=100, procdrop="dropdownoutlet")
    nama = create_tambah_entry(self, self.tambah, x=550, y=140)
    username = create_tambah_entry(self, self.tambah, x=550, y=180)
    password = create_tambah_entry(self, self.tambah, x=550, y=220)
    role = create_tambah_enumdropdown(
        self, self.tambah, x=550, y=260, procenum="karyawanrole")

    def tambahdata():
        outlet_val = outlet.get()
        nama_val = nama.get()
        username_val = username.get()
        password_val = password.get()
        role_val = role.get()

        tambah(
            self,
            frame=self.tambah,
            destroy=self.karyawan,
            redirect=lambda: start_karyawan(self),
            entries=(outlet_val, nama_val, username_val,
                     password_val, role_val),
            proc="karyawantambah")

    create_submit_button(self, x=480, y=300,
                         frame=self.tambah, command=tambahdata)


def edit_karyawan(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = ttk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Edit Karyawan", anchor="center", font=(
        "Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(415, 100, text="Outlet",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 140, text="Nama",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 180, text="Username",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 220, text="Password",
                            font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(415, 260, text="Role",
                            font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_edit_dropdown(self, self.edit, x=550, y=100, index=1, target_index=0, state='normal',
                                  treeview=self.treeview, procid="karyawanselectbyid", procdrop="dropdownoutlet")
    nama = create_edit_entry(self, self.edit, x=550, y=140, index=2,
                             state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    username = create_edit_entry(self, self.edit, x=550, y=180, index=3,
                                 state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    password = create_edit_entry(self, self.edit, x=550, y=220, index=4,
                                 state='normal', treeview=self.treeview, procid="karyawanselectbyid")
    role = create_edit_enumdropdown(self, self.edit, x=550, y=260, index=5, state='normal',
                                    treeview=self.treeview, procid="karyawanselectbyid", procenum="karyawanrole")

    def editdata():
        id_val = get_id(self, treeview=self.treeview,
                        procid="karyawanselectbyid")
        outlet_val = outlet.get()
        nama_val = nama.get()
        username_val = username.get()
        password_val = password.get()
        role_val = role.get()

        edit(
            self,
            frame=self.edit,
            destroy=self.karyawan,
            redirect=lambda: start_karyawan(self),
            entries=(id_val, outlet_val, nama_val,
                     username_val, password_val, role_val),
            procedit="karyawanedit")

    create_submit_button(self, x=480, y=300, frame=self.edit, command=editdata)


def delete_karyawan(self):
    delete(
        self,
        treeview=self.treeview,
        proc="karyawandelete")


def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.main.destroy()
