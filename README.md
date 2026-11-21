# Prevod teploty °C → °F

Aplikácia v Pythone (Tkinter + matplotlib).

- Vygeneruje 60 náhodných teplôt (°C)
- Operácie nad poľom: zoradenie, min, max, priemer
- Výpočet: F = C · 1.8 + 32
- Graf porovnáva pôvodné a vypočítané hodnoty
- GUI: tlačidlá, vstupné pole, popisy; prevod ľubovoľného čísla

## Spustenie
```
pip install -r requirements.txt
python main.py
```

## Vytvorenie .exe (Windows)
```
pyinstaller --onefile --windowed main.py
```
Výsledok: `dist/main.exe`
