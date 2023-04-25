from BorderPatrolSimulation.Settings.Constants import *
import customtkinter as ctk
import tkinter as tk


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.setup()
        self.run()

    def setup(self):

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.minsize(500, 500)
        self.title("Border patrol simulation")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        save_entry = ctk.CTkEntry(master=self, placeholder_text="CTkEntry")
        save_entry.grid(row=0, column=0, padx=20, pady=20, sticky="nwne")
        save_button = ctk.CTkButton(master=self, command=MainWindow.button_function, text="SAVE")
        save_button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        load_entry = ctk.CTkEntry(master=self, placeholder_text="CTkEntry")
        load_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        load_button = ctk.CTkButton(master=self, command=MainWindow.button_function, text="LOAD")
        load_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        start_button = ctk.CTkButton(master=self, command=MainWindow.start_simulation, text="START")
        start_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        # self.geometry("1000x500")
        # tuple color for a light mode color and dark mode color
        # button = ctk.CTkButton(master=self, text="CTkButton",
        # command=MainWindow.button_function(), fg_color=("red", "darkred"))
        # button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def run(self):
        self.mainloop()

    @staticmethod
    def button_function():
        print("button pressed")

    @staticmethod
    def start_simulation():
        if not import_settings():
            raise ImportError("Can not import settings properly!")
        from BorderPatrolSimulation.Simulation.Simulation import Simulation
        s = Simulation()
        print("ASD")

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")
