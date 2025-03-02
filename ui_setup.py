import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def setup_ui(app):
    """Configura l'interfaccia utente principale."""
    app.main_frame = ttk.Frame(app.root)
    app.main_frame.pack(fill="both", expand=True)

    app.left_frame = ttk.Frame(app.main_frame)
    app.left_frame.pack(side="left", fill="y")

    app.right_frame = ttk.Frame(app.main_frame)
    app.right_frame.pack(side="right", fill="both", expand=True)

    app.message_label = ttk.Label(app.right_frame, text="", wraplength=400)
    app.message_label.pack(pady=10)

def initialize_graph(app):
    """Inizializza il grafico."""
    app.figure, app.ax = plt.subplots()
    app.canvas = FigureCanvasTkAgg(app.figure, master=app.right_frame)
    app.canvas.get_tk_widget().pack(fill="both", expand=True)
    app.toolbar = NavigationToolbar2Tk(app.canvas, app.right_frame)
    app.toolbar.update()
    app.canvas.draw()

def plot_initial_graph(app):
    """Traccia il grafico iniziale."""
    app.ax.clear()
    app.ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    app.ax.set_title("Grafico Iniziale")
    app.ax.set_xlabel("Asse X")
    app.ax.set_ylabel("Asse Y")
    app.canvas.draw()

def clear_left_frame(app):
    """Pulisce il frame sinistro."""
    for widget in app.left_frame.winfo_children():
        widget.destroy()

def show_graph(app):
    """Mostra il grafico."""
    app.canvas.get_tk_widget().pack(fill="both", expand=True)
    app.toolbar.pack()

def hide_graph(app):
    """Nasconde il grafico."""
    app.canvas.get_tk_widget().pack_forget()
    app.toolbar.pack_forget()