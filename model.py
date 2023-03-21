import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from typing import Tuple
from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()

def backgroundimg(self):
    # Image
    bg = os.getenv("bg_path")
    bg = f"{bg}"
    self.image = PhotoImage(file=bg)

def btnimg(self):
    ot = os.getenv("ic_outlet")
    self.otimg = PhotoImage(file=ot)
    pkt = os.getenv("ic_paket")
    self.pktimg = PhotoImage(file=pkt)
    kar = os.getenv("ic_karyawan")
    self.karimg = PhotoImage(file=kar)
    tr = os.getenv("ic_transaksi")
    self.trimg = PhotoImage(file=tr)
    plg = os.getenv("ic_pelanggan")
    self.plgimg = PhotoImage(file=plg)

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

def create_card(
    self,
    x: int,
    y: int,
    width: int = 150,
    height: int = 200,
    ) -> tk.Frame:
        card_frame = tk.Frame(
            self.main,
            width=width,
            height=height,
            bd=2,
            relief="groove",
            highlightthickness=2,
            highlightbackground="black"
        )
        self.canvas.create_window(x, y, anchor='n', window=card_frame)
        return card_frame

def create_button(
    self,
    frame: tk.Frame,
    image: PhotoImage,
    text: str,
    command: callable,
    font_size: int = 10,
    font_weight: str = 'bold',
    width: int = 20,
    height: int = 2,
    ):
    label = tk.Label(frame, image=image)
    button = tk.Button(
        frame,
        text=text,
        command=command,
        font=font.Font(size=font_size, weight=font_weight),
        width=width,
        height=height,
    )
    label.pack()
    button.pack()

def create_crud_button(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    text: str,
    command: callable,
    font_size: int = 14,
    font_weight: str = 'bold',
    ):
    button = tk.Button(
        frame,
        text=text,
        command=command,
        font=font.Font(size=font_size, weight=font_weight)
    )
    self.canvas.create_window(x, y, window=button, anchor='center')

def create_treeview(
    self,
    frame: tk.Frame,
    proc: str,
    columns: tuple,
    headings: tuple,
    texts: tuple,
    width: int = 90,
    minwidth: int = 90,
    ):
    self.treeview = ttk.Treeview(frame)
    self.treeview.pack()
    self.treeview['columns'] = columns
    self.treeview.column("#0", width=0,  stretch=False)
    for each in columns:
        self.treeview.column(each, anchor='center', width=width, minwidth=minwidth)

    self.treeview.heading("#0", text="", anchor="center")
    for heading, text in zip(headings, texts):
        self.treeview.heading(heading, text=text, anchor='center')

    self.cursor.callproc(proc)
    result = self.cursor.stored_results()

    for each in result:
        i = each.fetchall()
        for row in i:
            self.treeview.insert(parent='', index='end', values=row)

    self.canvas.create_window(480, 140, anchor='n', window=self.treeview)
    return self.treeview
    
# def create_toplevel(
#     title: str,
#     ) -> tk.Frame:
#     toplevel = tk.Toplevel()
#     toplevel.title(title)
#     toplevel.geometry("960x540+180+80")
#     toplevel.resizable(False, False)
#     frame = tk.Frame(toplevel)
#     frame.pack(fill="both", expand=False)
#     canvas = tk.Canvas(toplevel, width=960, height=540)
#     canvas.pack(fill="both", expand=True)

#     return frame

def create_tambah_entry(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    ):
    entry = tk.Entry(frame)
    entry.pack()
    self.canvas.create_window(x, y, window=entry)
    return entry

def create_edit_entry(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    index: int,
    treeview: ttk.Treeview,
    procid: str,
    ):
    editing = treeview.selection()[0]
    values = treeview.item(editing, 'values')
    
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    data = None
    for each in result:
        print(each)
        data = each.fetchone()
    
    entry = tk.Entry(frame)
    entry.insert(0, data[index])
    entry.pack()
    self.canvas.create_window(x, y, window=entry)
    return entry

def create_tambah_dropdown(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    procdrop: str,
    ):
    self.cursor.callproc(procdrop)
    result = self.cursor.stored_results()

    for values in result:
        values = values.fetchall()

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown

def create_edit_dropdown(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    index: int,
    treeview: ttk.Treeview,
    procid: str,
    procdrop: str,
    ):
    editing = treeview.selection()[0]
    values = treeview.item(editing, 'values')
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    data = None
    for each in result:
        data = each.fetchall()[0]

    self.cursor.callproc(procdrop)
    drop = self.cursor.stored_results()

    for values in drop:
        values = values.fetchall()


    i = None
    for each in values:
        if data[index] == each[index]:
            i = each
            break

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.current(values.index(i))
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown

def create_tambah_enumdropdown(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    procenum: str,
    ):
    self.cursor.callproc(procenum)
    result = self.cursor.stored_results()

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
    frame: tk.Frame,
    x: int,
    y: int,
    index: int,
    treeview: ttk.Treeview,
    procid: str,
    procenum: str,
    ):
    editing = treeview.selection()[0]
    values = treeview.item(editing, 'values')
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()

    data = None
    for each in result:
        data = each.fetchall()[0]

    self.cursor.callproc(procenum)
    drop = self.cursor.stored_results()

    for value in drop:
        values = value.fetchone()[1][5:-1].split(',')
        values = [i.replace("'", "") for i in values]

    dropdown = ttk.Combobox(frame, values=values, state="readonly")
    dropdown.configure(width=17)
    dropdown.current(values.index(data[index]))
    dropdown.pack()
    self.canvas.create_window(x, y, window=dropdown)
    return dropdown

def create_submit_button(
    self,
    frame: tk.Frame,
    x: int,
    y: int,
    command: callable,
    text: str = 'Submit',
    font_size: int = 10,
    font_weight: str = 'bold',
    ):
    self.button = tk.Button(frame, text=text, command=command, font=font.Font(size=font_size, weight=font_weight))
    self.canvas.create_window(x, y, window=self.button, anchor="center")

def validate_number(
    values: Tuple,
    ) -> bool:
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
    selecting = treeview.selection()[0]
    values = treeview.item(selecting, 'values')
    
    self.cursor.callproc(procid, (values[0],))
    result = self.cursor.stored_results()
    
    data = None
    for each in result:
        data = each.fetchall()[0]
    
    return data[0]

def tambah(
    self,
    frame: tk.Frame,
    destroy: tk.Toplevel,
    redirect: callable,
    entries: Tuple,
    proc: str,
    ):
    values = entries
    self.cursor.callproc(proc, values)
    self.db.commit()
    frame.destroy()
    destroy.destroy()
    redirect()

def edit(
    self,
    frame: tk.Frame,
    destroy: tk.Toplevel,
    redirect: callable,
    entries: Tuple,
    procedit: str
    ):
    values = entries
    self.cursor.callproc(procedit, values)
    self.db.commit()
    frame.destroy()
    destroy.destroy()
    redirect()

def delete(
    self,
    treeview: ttk.Treeview,
    proc: str,
    ):
    deleting = treeview.selection()[0]
    values = treeview.item(deleting, 'values')

    self.cursor.callproc(proc, (values[0],))
    self.db.commit()
    treeview.delete(deleting)
