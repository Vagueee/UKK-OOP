import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas, font, ttk
from dotenv import load_dotenv
import os
import mysql.connector
import model
load_dotenv()

def start_outlet(self):
    self.outlet = tk.Toplevel()
    self.outlet.title("Laundrive")
    self.outlet.geometry("960x540+180+80")
    self.outlet.resizable(False, False)
    self.frame = tk.Frame(self.outlet)
    self.frame.pack(fill="both", expand=False)

    # Canvas
    self.canvas = tk.Canvas(self.outlet, width=960, height=540)
    self.canvas.pack(fill="both", expand=True)

    model.backgroundimg(self)
    model.database(self)

    # Display
    self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    self.canvas.create_text(480, 50, text="Data Outlet", anchor="center", font=("default", 28, "bold"))