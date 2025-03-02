import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def load_existing_programs(app):
    """Carica i programmi esistenti nella lista."""
    app.program_listbox.delete(0, tk.END)
    programs_dir = "programs"
    if not os.path.exists(programs_dir):
        os.makedirs(programs_dir)
    files = os.listdir(programs_dir)
    for file in files:
        if file.endswith(".gcode"):
            app.program_listbox.insert(tk.END, file)

def create_new_program(app):
    """Crea un nuovo programma."""
    app.clear_left_frame()
    ttk.Label(app.left_frame, text="Crea Nuovo Programma").pack(pady=10)

    ttk.Label(app.left_frame, text="Nome Programma:").pack(pady=5)
    program_name_entry = ttk.Entry(app.left_frame)
    program_name_entry.pack(pady=5)

    ttk.Label(app.left_frame, text="Contenuto G-code:").pack(pady=5)
    gcode_text = tk.Text(app.left_frame, height=10)
    gcode_text.pack(pady=5)

    def save_new_program():
        program_name = program_name_entry.get()
        gcode_content = gcode_text.get("1.0", tk.END).strip()
        if not program_name or not gcode_content:
            messagebox.showerror("Errore", "Nome programma e contenuto G-code sono obbligatori.")
            return
        program_path = os.path.join("programs", f"{program_name}.gcode")
        with open(program_path, 'w') as file:
            file.write(gcode_content)
        app.show_message(f"Programma {program_name} salvato con successo.")
        app.show_main_buttons()

    ttk.Button(app.left_frame, text="Salva", command=save_new_program).pack(pady=5)
    ttk.Button(app.left_frame, text="Annulla", command=app.show_main_buttons).pack(pady=5)

def edit_selected_program(app):
    """Modifica il programma selezionato."""
    try:
        selected = app.program_listbox.curselection()
        if not selected:
            messagebox.showerror("Errore", "Seleziona un programma da modificare.")
            return
        program_name = app.program_listbox.get(selected)
        program_path = os.path.join("programs", program_name)

        app.clear_left_frame()
        ttk.Label(app.left_frame, text=f"Modifica Programma: {program_name}").pack(pady=10)

        ttk.Label(app.left_frame, text="Contenuto G-code:").pack(pady=5)
        gcode_text = tk.Text(app.left_frame, height=10)
        gcode_text.pack(pady=5)

        with open(program_path, 'r') as file:
            gcode_text.insert(tk.END, file.read())

        def save_edited_program():
            gcode_content = gcode_text.get("1.0", tk.END).strip()
            if not gcode_content:
                messagebox.showerror("Errore", "Il contenuto G-code non può essere vuoto.")
                return
            with open(program_path, 'w') as file:
                file.write(gcode_content)
            app.show_message(f"Programma {program_name} salvato con successo.")
            app.show_main_buttons()

        ttk.Button(app.left_frame, text="Salva", command=save_edited_program).pack(pady=5)
        ttk.Button(app.left_frame, text="Annulla", command=app.show_main_buttons).pack(pady=5)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la modifica del programma: {e}")

def save_new_program(app):
    """Salva il nuovo programma."""
    # Questa funzione è già implementata all'interno di create_new_program
    pass

def cancel_new_program(app):
    """Annulla la creazione del nuovo programma."""
    app.show_main_buttons()

def save_edited_program(app, program_path):
    """Salva il programma modificato."""
    # Questa funzione è già implementata all'interno di edit_selected_program
    pass