import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_pelanggan(self):
    self.pelanggan = tk.Toplevel()
    self.pelanggan.title("Laundrive")
    self.pelanggan.geometry("960x540+180+80")
    self.pelanggan.resizable(False, False)
    self.frame = tk.Frame(self.pelanggan)
    self.frame.pack(fill="both", expand=False)

    # Canvas
    self.canvas = tk.Canvas(self.pelanggan, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    # Display
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    self.canvas.create_text(480, 50, text="Data Pelanggan", anchor="center", font=("default", 28, "bold"))