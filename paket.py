from model import *

def start_paket(self, role):
    self.paket = tk.Toplevel()
    self.paket.title("Laundrive")
    self.paket.geometry("960x540+180+80")
    self.paket.resizable(False, False)
    self.frame = ttk.Frame(self.paket)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.paket, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)
    self.role = role

    self.canvas.create_text(480, 50, text="Data Paket", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self, 
        frame=self.paket, 
        x= 480,
        y= 150,
        proc='paketselect', 
        columns=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        headings=('id', 'outlet', 'jenis', 'nama', 'harga'), 
        texts=('ID', 'Outlet', 'Jenis Paket', 'Nama Paket', 'Harga'))

    csv_button = create_laporan_button(self, frame=self.paket, x=60, y=110 ,text="CSV", command=lambda: csv_paket(self))
    xls_button = create_laporan_button(self, frame=self.paket, x=160, y=110 ,text="Excel", command=lambda: xls_paket(self))

    if self.role == "Admin":
        tambah_button = create_crud_button(self, frame=self.paket, x=360, y=110, text="Tambah Data", command=lambda: tambah_paket(self))
        edit_button = create_crud_button(self, frame=self.paket, x=480, y=110, disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_paket(self))
        delete_button = create_crud_button(self, frame=self.paket, x=600, y=110 , disabled=len(treeview.selection()) == 0, text="Delete Data", command=lambda: delete_paket(self))

        treeview.bind("<ButtonRelease-1>", lambda event: switch([edit_button, delete_button], selection=treeview.selection()))

def csv_paket(self):
    default_filename = 'data.csv'
    initial_dir = '.'
    filetypes = [('CSV files', '*.csv')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(defaultextension='.csv', initialfile=default_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        exportcsv(
        filename=filename,
        treeview=self.treeview)

def xls_paket(self):
    default_filename = 'data.xlsx'
    initial_dir = '.'
    filetypes = [('Excel', '*.xslx')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(defaultextension='.xslx', initialfile=default_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        exportxls(
        filename=filename,
        treeview=self.treeview)

def tambah_paket(self):
    self.tambah = tk.Toplevel()
    self.tambah.title("Laundrive")
    self.tambah.geometry("960x540+180+80")
    self.tambah.resizable(False, False)
    self.frame = ttk.Frame(self.tambah)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.tambah, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Tambah Paket", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Outlet", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Jenis Paket", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="Nama Paket", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 220, text="Harga", font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_tambah_dropdown(self, self.tambah, x = 545, y = 100, procdrop="dropdownoutlet")
    jenis = create_tambah_enumdropdown(self, self.tambah, x = 545, y = 140, procenum="paketjenis")
    nama = create_tambah_entry(self, self.tambah, x = 545, y = 180)
    harga = create_tambah_entry(self, self.tambah, x = 545, y = 220)

    def tambahdata():
        outlet_val = outlet.get()
        jenis_val = jenis.get()
        nama_val = nama.get()
        harga_val = harga.get()

        validate = validate_number(values=(harga_val))
        if validate == True:
            tambah(
                self, 
                frame=self.tambah,
                destroy=self.paket, 
                redirect=lambda: start_paket(self), 
                entries=(outlet_val, jenis_val, nama_val, harga_val), 
                proc="pakettambah")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x = 480, y = 265, frame=self.tambah, command=tambahdata)

def edit_paket(self):
    self.edit = tk.Toplevel()
    self.edit.title("Laundrive")
    self.edit.geometry("960x540+180+80")
    self.edit.resizable(False, False)
    self.frame = ttk.Frame(self.edit)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.edit, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Edit Paket", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Outlet", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Jenis Paket", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="Nama Paket", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 220, text="Harga", font=("Verdana", 14), fill="#b5b3b3")

    outlet = create_edit_dropdown(self, self.edit, x = 545, y = 100, index=1, target_index=1, state='normal', treeview=self.treeview, procid="paketselectbyid", procdrop="dropdownoutlet")
    jenis = create_edit_enumdropdown(self, self.edit, x = 545, y = 140, index=2, state='normal', treeview=self.treeview, procid="paketselectbyid", procenum="paketjenis")
    nama = create_edit_entry(self, self.edit, x = 545, y = 180, index=3, state='normal', treeview=self.treeview, procid="paketselectbyid")
    harga = create_edit_entry(self, self.edit, x = 545, y = 220, index=4, state='normal', treeview=self.treeview, procid="paketselectbyid")

    def editdata():
        id_val = get_id(self, treeview=self.treeview, procid="paketselectbyid")
        outlet_val = outlet.get()
        jenis_val = jenis.get()
        nama_val = nama.get()
        harga_val = harga.get()

        validate = validate_number(values=(harga_val))
        if validate == True:
            edit(
                self,
                frame=self.edit,
                destroy=self.paket,
                redirect=lambda: start_paket(self),
                entries=(id_val, outlet_val, jenis_val, nama_val, harga_val),
                procedit="paketedit")
        else:
            messagebox.showerror("Error", "Please enter a valid entry")

    create_submit_button(self, x = 480, y = 265, frame=self.edit, command=editdata)


def delete_paket(self):
    delete(
        self, 
        treeview=self.treeview, 
        proc="paketdelete")