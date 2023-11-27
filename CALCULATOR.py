import tkinter as tk
from tkinter import PhotoImage
import time


class ResistorCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Resistor Color Calculator")

        self.band_color = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey",
                           "White", "Gold", "Silver"]

        self.tol_color = ["Brown +-%1", "Red +-%2", "Green +-%0.5", "Blue +-%0.25", "Violet +-%0.1", "Grey +-%0.05",
                          "Gold +-%5", "Silver +-%10"]
        self.bands = []
        for i in range(4):
            initial_value = self.tol_color[0] if i == 3 else self.band_color[0]
            self.bands.append(tk.StringVar(value=initial_value))

        self.label_band1 = tk.Label(master, text="1. Digit : ")
        self.label_band1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.band1_menu = tk.OptionMenu(master, self.bands[0], *self.band_color)
        self.band1_menu.grid(row=0, column=1, sticky="w")

        self.label_band2 = tk.Label(master, text="2. Digit : ")
        self.label_band2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.band2_menu = tk.OptionMenu(master, self.bands[1], *self.band_color)
        self.band2_menu.grid(row=1, column=1, sticky="w")

        self.label_band3 = tk.Label(master, text="3. Band Multiplier : ")
        self.label_band3.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.band3_menu = tk.OptionMenu(master, self.bands[2], *self.band_color)
        self.band3_menu.grid(row=2, column=1, sticky="w")

        self.label_band4 = tk.Label(master, text="4. Band Tolerance : ")
        self.label_band4.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.band4_menu = tk.OptionMenu(master, self.bands[3], *self.tol_color)
        self.band4_menu.grid(row=3, column=1, sticky="w")

        self.calculate_button = tk.Button(master, text=" CALCULATE ", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="", bg="black", fg="white")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.resistor_photo = PhotoImage(file="Resistor.png")

        self.photo_label = tk.Label(master, image=self.resistor_photo)
        self.photo_label.grid(row=0, column=2, rowspan=4, padx=10, pady=10, sticky="nsew")

        # Saat ve Tarih Label'ları
        self.clock_label = tk.Label(master, font=('times new roman', 20))
        self.clock_label.grid(row=4, column=2, pady=10, sticky="nsew")

        self.update_clock()

        # Sütun ve satır boyutlarını yapılandırma
        for i in range(3):
            tk.Grid.columnconfigure(master, i, weight=1)
        for i in range(7):
            tk.Grid.rowconfigure(master, i, weight=1)

        # Saat ve Tarih Güncelleme Fonksiyonu
        self.update_clock()

    def calculate(self):
        color_codes = [self.band_color.index(band.get().split()[0]) for band in self.bands]
        tolerance = self.band4_menu.cget("text").split()[1] if self.band4_menu.cget("text") else ""
        res_val = self.calculate_result(color_codes, tolerance)
        self.result_label.config(text=f"Resistor Value : {res_val} ohm")

    def calculate_result(self, color_codes, tolerance):
        resistor_value = (color_codes[0] * 10 + color_codes[1]) * 10 ** color_codes[2]
        return f"{resistor_value} ohm, {tolerance} tolerance"



    def update_clock(self):
        time_str = time.strftime("%H:%M:%S\n%d/%m/%Y")

        self.clock_label.config(text=time_str)
        self.master.after(1000, self.update_clock)


root = tk.Tk()
app = ResistorCalculator(root)
root.geometry("960x400")  # İlk pencere boyutu
root.mainloop()
