from model import *

def start_outlet(self):
    self.outlet = tk.Toplevel()
    self.outlet.title("Laundrive")
    self.outlet.geometry("960x540+180+80")
    self.outlet.resizable(False, False)
    self.frame = ttk.Frame(self.outlet)
    self.frame.pack(fill="both", expand=False)
    self.canvas = tk.Canvas(self.outlet, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    database(self)

    self.canvas.create_text(480, 50, text="Data Outlet", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")

    treeview = create_treeview(
        self, 
        frame=self.outlet, 
        x= 480,
        y= 150,
        proc='outletselect', 
        columns=('id', 'nama', 'alamat', 'tlp'), 
        headings=('id', 'nama', 'alamat', 'tlp'), 
        texts=('ID', 'Nama', 'Alamat', 'No. Telp'))
    
    csv_button = create_laporan_button(self, frame=self.outlet, x=100, y=110 ,text="Export as CSV", command=lambda: csv_outlet(self))

    tambah_button = create_crud_button(self, frame=self.outlet, x=355, y=110, text="Tambah Data", command=lambda: tambah_outlet(self))
    edit_button = create_crud_button(self, frame=self.outlet, x=480, y=110, disabled=len(treeview.selection()) == 0, text="Edit Data", command=lambda: edit_outlet(self))
    delete_button = create_crud_button(self, frame=self.outlet, x=600, y=110, disabled=len(treeview.selection()) == 0, text="Delete Data", command=lambda: delete_outlet(self))

    treeview.bind("<ButtonRelease-1>", lambda event: switch([edit_button, delete_button], selection=treeview.selection()))

def csv_outlet(self):
    Verdana_filename = 'data.csv'
    initial_dir = '.'
    filetypes = [('CSV files', '*.csv')]
    # Prompt the user to choose a filename and location
    filename = filedialog.asksaveasfilename(Verdanaextension='.csv', initialfile=Verdana_filename, initialdir=initial_dir, filetypes=filetypes)
    if filename:
        importcsv(
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

    self.canvas.create_text(480, 50, text="Tambah Outlet", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Nama", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Alamat", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="No. Telp", font=("Verdana", 14), fill="#b5b3b3")

    nama = create_tambah_entry(self, self.tambah, x = 540, y = 100)
    alamat = create_tambah_entry(self, self.tambah, x = 540, y = 140)
    telp = create_tambah_entry(self, self.tambah, x = 540, y = 180)

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

    create_submit_button(self, x = 480, y = 220, frame=self.tambah, command=tambahdata)

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

    self.canvas.create_text(480, 50, text="Edit Outlet", anchor="center", font=("Verdana", 28, "bold"), fill="#b5b3b3")
    self.canvas.create_text(420, 100, text="Nama", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 140, text="Alamat", font=("Verdana", 14), fill="#b5b3b3")
    self.canvas.create_text(420, 180, text="No. Telp", font=("Verdana", 14), fill="#b5b3b3")

    nama = create_edit_entry(self, self.edit, x = 540, y = 100, index=1, state='normal', treeview=self.treeview, procid="outletselectbyid")
    alamat = create_edit_entry(self, self.edit, x = 540, y = 140, index=2, state='normal', treeview=self.treeview, procid="outletselectbyid")
    telp = create_edit_entry(self, self.edit, x = 540, y = 180, index=3, state='normal', treeview=self.treeview, procid="outletselectbyid")

    def editdata():
        id_val = get_id(self, treeview=self.treeview, procid="outletselectbyid")
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

    create_submit_button(self, x = 480, y = 220, frame=self.edit, command=editdata)

def delete_outlet(self):
    delete(
        self, 
        treeview=self.treeview, 
        proc="outletdelete")