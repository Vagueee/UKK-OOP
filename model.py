import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
from dotenv import load_dotenv
from tkinter import Menu, PhotoImage, messagebox, Canvas, font, ttk, filedialog, StringVar
from tkcalendar import DateEntry
from typing import Tuple
from weasyprint import HTML, CSS
import jinja2
import csv
import os
import mysql.connector
load_dotenv()

# def backgroundimg(self):
#     # Image
#     bg = os.getenv("bg_path")
#     bg = f"{bg}"
#     self.image = PhotoImage(file=bg)

# def btnimg(self):
#     # Icon button
#     ot = os.getenv("ic_outlet")
#     self.otimg = PhotoImage(file=ot)
#     pkt = os.getenv("ic_paket")
#     self.pktimg = PhotoImage(file=pkt)
#     kar = os.getenv("ic_karyawan")
#     self.karimg = PhotoImage(file=kar)
#     plg = os.getenv("ic_pelanggan")
#     self.plgimg = PhotoImage(file=plg)
#     tr = os.getenv("ic_transaksi")
#     self.trimg = PhotoImage(file=tr)


def database(self):
    # Connect to the database
    self.db_host = os.getenv("host")
    self.db_user = os.getenv("user")
    self.db_password = os.getenv("password")
    self.db_database = os.getenv("database")
    self.db = mysql.connector.connect(
        host=self.db_host,
        user=self.db_user,
        password=self.db_password,
        database=self.db_database
    )

    # Create Cursor
    self.cursor = self.db.cursor()


def bargraph(
    self,
    title: str,
    x: str,
    y: str,
    style: str,
    proc: str,
):
    # Get values
    self.cursor.callproc(proc)
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchall()

    figure = plt.figure(figsize=(7, 4))
    plt.style.use(style)
    axes = figure.add_subplot(1, 1, 1)
    axes.bar(
        range(len(data)),
        [datas[0] for datas in data],
        tick_label=[datas[1] for datas in data]
    )
    axes.set_title(title)
    axes.set_xlabel(x)
    axes.set_ylabel(y)
    plt.ion()

    return figure


def create_card(
    self,
    x: int,
    y: int,
    width: int = 150,
    height: int = 200,
) -> ttk.Frame:
    card_frame = ttk.Frame(
        self.main,
        width=width,
        height=height,
        relief="groove"
    )
    self.canvas.create_window(x, y, anchor='n', window=card_frame)
    return card_frame


def create_button(
    self,
    frame: ttk.Frame,
    image: PhotoImage,
    text: str,
    command: callable,
):
    label = ttk.Label(frame, image=image)
    button = ttk.Button(
        frame,
        text=text,
        command=command,
    )
    label.pack()
    button.pack()


def create_crud_button(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    text: str,
    command: callable,
    disabled: bool = False,
    font_size: int = 14,
    font_weight: str = 'bold',
):
    self.button = ttk.Button(
        frame,
        text=text,
        command=command,
    )
    # Disabled if no id value
    self.button["state"] = "disabled" if disabled else "normal"

    self.canvas.create_window(x, y, window=self.button, anchor='center')
    return self.button


def switch(buttons: list, selection: Tuple):
    # Disable button logic
    for button in buttons:
        button["state"] = "normal" if button["state"] == "disabled" else "normal"


def create_laporan_button(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    text: str,
    command: callable,
    font_size: int = 10,
    font_weight: str = 'bold',
):
    self.button = ttk.Button(
        frame,
        text=text,
        command=command,
    )

    self.canvas.create_window(x, y, window=self.button, anchor='center')
    return self.button


def search_entry(
    self,
    frame: ttk.Frame,
    txtvar: str,
    x: int,
    y: int,
):
    entry = ttk.Entry(frame, textvariable=txtvar)
    entry.pack()
    self.canvas.create_window(x, y, window=entry)

    return entry


def search(
    self,
    proc: str,
    search: str,
    treeview: ttk.Treeview,
):
    self.cursor.callproc(proc, (search,))
    result = self.cursor.stored_results()

    for searched in result:
        searched = searched.fetchall()

    if len(searched) > 0:
        treeview.delete(*treeview.get_children())
        for i in searched:
            treeview.insert(parent='', index='end', values=i)
    else:
        treeview.delete(*treeview.get_children())


def create_treeview(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    proc: str,
    columns: tuple,
    headings: tuple,
    texts: tuple,
):
    self.treeview = ttk.Treeview(frame)
    self.treeview.pack(padx=20, pady=20)
    self.treeview['columns'] = columns

    # Width window (seharusnya pake winfo.width())
    framewidth = 900
    width = int(framewidth / len(columns))

    # Create column
    self.treeview.column("#0", width=0,  stretch=True)
    for each in columns:
        self.treeview.column(each, anchor='center',
                             width=width, minwidth=width, stretch=True)

    # Create header
    self.treeview.heading("#0", text="", anchor="center")
    for heading, text in zip(headings, texts):
        self.treeview.heading(heading, text=text, anchor='center')

    # Get data from database
    self.cursor.callproc(proc)
    result = self.cursor.stored_results()

    for each in result:
        i = each.fetchall()
        # Insert into treeview
        for row in i:
            self.treeview.insert(parent='', index='end', values=row)

    self.canvas.create_window(x, y, anchor='n', window=self.treeview)
    return self.treeview


def create_tambah_entry(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
):
    entry = ttk.Entry(frame)
    entry.pack()
    self.canvas.create_window(x, y, window=entry)
    return entry


def create_edit_entry(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    index: int,
    state: str,
    treeview: ttk.Treeview,
    procid: str,
):
    # Get id from row
    editing = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(editing, 'values')

    # Get values by id
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchone()

    entry = ttk.Entry(frame, state=state)
    entry.insert(0, data[index])
    entry.pack()
    self.canvas.create_window(x, y, window=entry)
    return entry


def create_tambah_dropdown(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    procdrop: str,
):
    # Get values for dropdown
    self.cursor.callproc(procdrop)
    result = self.cursor.stored_results()

    # Get values from stored procedure
    for values in result:
        values = values.fetchall()

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown


def create_tambah_dropdown_sorted(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    procdrop: str,
    sortby: str,
):
    # Get values for dropdown
    self.cursor.callproc(procdrop, (sortby,))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    for values in result:
        values = values.fetchall()

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown


def create_edit_dropdown(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    index: int,
    target_index: int,
    state: str,
    treeview: ttk.Treeview,
    procid: str,
    procdrop: str,
):
    # Get id from row
    editing = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(editing, 'values')

    # Get values by id
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchone()

    # Get values for dropdown
    self.cursor.callproc(procdrop)
    drop = self.cursor.stored_results()

    # Get values from stored procedure
    values = None
    for each in drop:
        values = each.fetchall()

    # Get selected value by id
    selected = None
    for each in values:
        # print(each, data)
        if data[index] == each[target_index]:
            selected = each
            break

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17, state=state)
    dropdown.current(values.index(selected))
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown


def create_tambah_enumdropdown(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    procenum: str,
):
    # Get enum values for dropdown
    self.cursor.callproc(procenum)
    result = self.cursor.stored_results()

    # Split values by , and replace ' with space
    for value in result:
        values = value.fetchone()[1][5:-1].split(',')
        values = [i.replace("'", "") for i in values]

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown


def create_edit_enumdropdown(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    index: int,
    state: str,
    treeview: ttk.Treeview,
    procid: str,
    procenum: str,
):
    # Get id from row
    editing = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(editing, 'values')

    # Get values by id
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchone()

    # Get enum values for dropdown
    self.cursor.callproc(procenum)
    drop = self.cursor.stored_results()

    # Split values by , and replace ' with space
    for value in drop:
        values = value.fetchone()[1][5:-1].split(',')
        values = [i.replace("'", "") for i in values]

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17, state=state)
    dropdown.current(values.index(data[index]))
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown


def create_tambah_date(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    width: int = 12,
    background: str = 'darkblue',
    foreground: str = 'white',
    borderwidth: int = 2,
):
    tanggal = DateEntry(frame, width=width, background=background,
                        foreground=foreground, borderwidth=borderwidth)
    tanggal.configure(width=17)
    tanggal.pack()
    self.canvas.create_window(x, y, window=tanggal)
    return tanggal


def create_edit_date(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    index: int,
    state: str,
    treeview: ttk.Treeview,
    procid: str,
    width: int = 12,
    background: str = 'darkblue',
    foreground: str = 'white',
    borderwidth: int = 2,
):
    # Get id from row
    editing = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(editing, 'values')

    # Get values by id
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchone()

    tanggal = DateEntry(frame, width=width, background=background,
                        foreground=foreground, borderwidth=borderwidth)
    tanggal.configure(width=17, state=state)
    tanggal.set_date(data[index])
    tanggal.pack()
    self.canvas.create_window(x, y, window=tanggal)
    return tanggal


def create_submit_button(
    self,
    frame: ttk.Frame,
    x: int,
    y: int,
    command: callable,
    text: str = 'Submit',
    font_size: int = 10,
    font_weight: str = 'bold',
):
    self.button = ttk.Button(frame, text=text, command=command)
    self.canvas.create_window(x, y, window=self.button, anchor="center")


def validate_number(
    values: Tuple,
) -> bool:
    # Validation for numeric entry
    for each in values:
        if each.isdigit():
            return True
        else:
            return False


def get_id(
    self,
    treeview: ttk.Treeview,
    procid: str
):
    # Get id from row
    selecting = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(selecting, 'values')

    # Get values by id
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    # Get values from stored procedure
    data = None
    for each in result:
        data = each.fetchall()[0]

    # Return id
    return data[0]


def tambah(
    self,
    frame: ttk.Frame,
    destroy: tk.Toplevel,
    redirect: callable,
    entries: Tuple,
    proc: str,
):
    values = entries
    self.cursor.callproc(proc, values)
    self.db.commit()
    self.cursor.close()
    frame.destroy()
    destroy.destroy()
    redirect()


def edit(
    self,
    frame: ttk.Frame,
    destroy: tk.Toplevel,
    redirect: callable,
    entries: Tuple,
    procedit: str
):
    values = entries
    self.cursor.callproc(procedit, values)
    self.db.commit()
    self.cursor.close()
    frame.destroy()
    destroy.destroy()
    redirect()


def delete(
    self,
    treeview: ttk.Treeview,
    proc: str,
):
    # Get id from row
    deleting = treeview.selection()[0]
    # Get values in the same row
    values = treeview.item(deleting, 'values')

    # Delete values by id
    self.cursor.callproc(proc, (values[0],))
    self.db.commit()
    treeview.delete(deleting)


def exportcsv(
    filename: str,
    treeview: ttk.Treeview,
):
    # Write csv file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        header = []
        for col in treeview["columns"]:
            header.append(treeview.heading(col)["text"])
        writer.writerow(header)
        # Write data rows
        for item in treeview.get_children():
            row = []
            for col in treeview["columns"]:
                row.append(treeview.set(item, col))
            writer.writerow(row)


def exportxls(
    filename: str,
    treeview: ttk.Treeview,
):
    # Get the data from the Treeview
    data = []
    for item in treeview.get_children():
        values = treeview.item(item, 'values')
        data.append(values)

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=[col for col in treeview['columns']])

    # Write the DataFrame to an Excel file
    df.to_excel(filename, index=False)


def exportpdf(
    filename: str,
    inv: str,
    tgl: str,
    namapel: str,
    alamatpel: str,
    telppel: str,
    namaout: str,
    alamatout: str,
    telpout: str,
    paket: str,
    desk: str,
    kuan: int,
    harga: int,
    pajak: int,
    diskon: int,
    total: int,
):
    context = {
        'kodeinvoice': inv,
        'tanggal': tgl,
        'nama_pel': namapel,
        'alamat_pel': alamatpel,
        'telp_pel': telppel,
        'nama_out': namaout,
        'alamat_out': alamatout,
        'telp_out': telpout,
        'paket': paket,
        'deskripsi': desk,
        'kuantitas': kuan,
        'harga': harga,
        'pajak': pajak,
        'diskon': diskon,
        'total': int(total)
    }

    pdf_loader = jinja2.FileSystemLoader('.')
    pdf_env = jinja2.Environment(loader=pdf_loader)

    html = pdf_env.get_template('invoice_template.html')
    bootstrap = './css/bootstrap.css'
    css = './css/style.css'
    pdf = html.render(context)

    HTML(string=pdf).write_pdf(filename, stylesheets=[bootstrap, css])

    # config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    # options = {
    # 'enable-local-file-access': True,
    # 'encoding': 'UTF-8',
    # 'quiet': '',
    # 'debug-javascript': True
    # }

    # pdfkit.from_string(pdf, filename, options=options, configuration=config, css=css)
