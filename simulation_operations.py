import os
from tkinter import ttk, messagebox

def prepare_simulation(app):
    """Prepara la simulazione."""
    selected = app.program_listbox.curselection()
    if not selected:
        messagebox.showerror("Errore", "Seleziona un programma da simulare.")
        return
    program_name = app.program_listbox.get(selected)
    program_path = os.path.join("programs", program_name)
    
    app.clear_left_frame()
    ttk.Label(app.left_frame, text=f"Simulazione Programma: {program_name}").pack(pady=10)

    ttk.Button(app.left_frame, text="Esegui Simulazione Completa", command=lambda: simulate_program(app, program_path)).pack(pady=5)
    ttk.Button(app.left_frame, text="Esegui Passo Singolo", command=lambda: step_simulation(app, program_path)).pack(pady=5)
    ttk.Button(app.left_frame, text="Annulla Simulazione", command=app.show_main_buttons).pack(pady=5)

def simulate_program(app, program_path):
    """Simula il programma."""
    try:
        with open(program_path, 'r') as file:
            gcode_commands = file.readlines()

        app.show_graph()
        app.ax.clear()

        # Eseguire la simulazione completa
        for line in gcode_commands:
            if line.startswith('G1'):
                # Esempio di simulazione del comando G1
                app.ax.plot([0, 1, 2], [0, 1, 0])
            elif line.startswith('G2'):
                # Esempio di simulazione del comando G2
                app.ax.plot([0, 1, 2], [0, 1, 1])
            elif line.startswith('G3'):
                # Esempio di simulazione del comando G3
                app.ax.plot([0, 1, 2], [0, 1, 2])

        app.canvas.draw()
        app.show_message(f"Simulazione del programma {program_path} completata.", "info")
    except Exception as e:
        app.show_message(f"Errore durante la simulazione: {e}", "error")

def step_simulation(app, program_path):
    """Esegue un passo della simulazione."""
    try:
        if not hasattr(app, 'simulation_state'):
            with open(program_path, 'r') as file:
                app.simulation_state = file.readlines()
            app.simulation_index = 0
            app.show_graph()
            app.ax.clear()

        if app.simulation_index < len(app.simulation_state):
            line = app.simulation_state[app.simulation_index].strip()
            app.simulation_index += 1
            if line.startswith('G1'):
                # Esempio di simulazione del comando G1
                app.ax.plot([0, 1, 2], [0, 1, 0])
            elif line.startswith('G2'):
                # Esempio di simulazione del comando G2
                app.ax.plot([0, 1, 2], [0, 1, 1])
            elif line.startswith('G3'):
                # Esempio di simulazione del comando G3
                app.ax.plot([0, 1, 2], [0, 1, 2])
            app.canvas.draw()
            app.show_message(f"Eseguito passo {app.simulation_index} della simulazione.", "info")
        else:
            app.show_message("Simulazione completata.", "info")
    except Exception as e:
        app.show_message(f"Errore durante la simulazione: {e}", "error")

def cancel_simulation(app):
    """Annulla la simulazione."""
    if hasattr(app, 'simulation_state'):
        del app.simulation_state
        del app.simulation_index
    app.hide_graph()
    app.show_main_buttons()