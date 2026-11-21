import random
import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

POCET_HODNOT = 60  # min. 50 podľa zadania

def generuj_hodnoty(n=POCET_HODNOT):
    return [round(random.uniform(0, 40), 1) for _ in range(n)]

def zorad(hodnoty):
    return sorted(hodnoty)

def priemer(hodnoty):
    return sum(hodnoty) / len(hodnoty)

def celsius_na_fahrenheit(c):
    return c * 1.8 + 32

class Aplikacia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prevod teploty °C → °F")
        self.geometry("900x700")

        self.povodne = generuj_hodnoty()
        self.vypocitane = [celsius_na_fahrenheit(c) for c in self.povodne]

        ovladanie = tk.Frame(self)
        ovladanie.pack(pady=10)

        tk.Label(ovladanie, text="Zadaj teplotu v °C:").grid(row=0, column=0, padx=5)
        self.vstup = tk.Entry(ovladanie, width=10)
        self.vstup.grid(row=0, column=1, padx=5)
        tk.Button(ovladanie, text="Vypočítať", command=self.vypocitaj).grid(
            row=0, column=2, padx=5
        )
        tk.Button(ovladanie, text="Nové hodnoty", command=self.nove_hodnoty).grid(
            row=0, column=3, padx=5
        )

        self.vysledok = tk.Label(self, text="Výsledok: -", font=("Arial", 12, "bold"))
        self.vysledok.pack()

        self.statistiky = tk.Label(self, text="", justify="left")
        self.statistiky.pack(pady=5)

        self.fig = Figure(figsize=(8, 4.5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.obnov()

    def vypocitaj(self):
        text = self.vstup.get().replace(",", ".").strip()
        try:
            c = float(text)
        except ValueError:
            messagebox.showerror("Chyba", "Zadaj platné číslo.")
            return
        f = celsius_na_fahrenheit(c)
        self.vysledok.config(text=f"Výsledok: {c:.1f} °C = {f:.1f} °F")

    def nove_hodnoty(self):
        self.povodne = generuj_hodnoty()
        self.vypocitane = [celsius_na_fahrenheit(c) for c in self.povodne]
        self.obnov()

    def obnov(self):
        zoradene = zorad(self.povodne)
        self.statistiky.config(
            text=(
                f"Počet hodnôt: {len(self.povodne)}   "
                f"Min: {min(self.povodne):.1f} °C   "
                f"Max: {max(self.povodne):.1f} °C   "
                f"Priemer: {priemer(self.povodne):.1f} °C\n"
                f"Najmenších 5 (zoradené): {zoradene[:5]}"
            )
        )

        self.ax.clear()
        x = range(1, len(self.povodne) + 1)
        self.ax.plot(x, self.povodne, marker="o", label="Pôvodné hodnoty (°C)")
        self.ax.plot(x, self.vypocitane, marker="s", label="Vypočítané hodnoty (°F)")
        self.ax.set_xlabel("Číslo merania")
        self.ax.set_ylabel("Teplota")
        self.ax.set_title("Porovnanie pôvodných a vypočítaných hodnôt")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()


if __name__ == "__main__":
    Aplikacia().mainloop()
