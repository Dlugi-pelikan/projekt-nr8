import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox as msb

root = Tk()
root.title("Funkcja kwadratowa")
root.geometry('450x300')

def wykres():
    try:
        a = float(fA.get());
        b = float(fB.get());
        c = float(fC.get());
        p = float(fP.get());
        k = float(fK.get());
    except ValueError:
        msb.showwarning("Błąd", "Wprowadzone wartości muszą być liczbami.")
        return

    X = []
    c= round(min(p, k))
    for x in range( int(round(min(p, k))), int(round(max(p,k))) *10):
        X.append(x*0.1)
    Y = []
    for x in X:
        Y.append(a*(x*x)+ b*x + c)

    plt.plot(X, Y)
    plt.title('Wykres f(x) = ' + str(a) + '*x² + ' + str(b) + 'x + ' + str(c))
    plt.grid(True)
    plt.show()
    return

tk.Label(root, text = "Podaj współczynniki ax² + bx + c: ", font = ("Calibri", 14)).grid(row=0, columnspan=9, sticky=N + E + S + W)
tk.Label(root, text = "a: ",font = ("Calibri", 14)).grid(row=1, column = 1, sticky=N + E + S + W)
tk.Label(root, text = "b: ",font = ("Calibri", 14)).grid(row=2, column = 1, sticky=N + E + S + W)
tk.Label(root, text = "c: ",font = ("Calibri", 14)).grid(row=3, column = 1, sticky=N + E + S + W)
fA = tk.Entry(root, font = ("Calibri", 12))
fA.grid(row=1, column = 2, sticky=N + E + S + W)
fB = tk.Entry(root, font = ("Calibri", 12))
fB.grid(row=2, column = 2, sticky=N + E + S + W)
fC = tk.Entry(root, font = ("Calibri", 12))
fC.grid(row=3, column = 2, sticky=N + E + S + W)

tk.Label(root).grid(row = 4, sticky=N + E + S + W)
tk.Label(root, text = "Podaj początek i koniec przedziału dla wykresu funkcji:", font = ("Calibri", 14), anchor="e").grid(row=5, columnspan=12, sticky=N + E + S + W)
tk.Label(root, text = "początek: ", font = ("Calibri", 14)).grid(row=6, column = 1, sticky=N + E + S + W)
tk.Label(root, text = "koniec: ", font = ("Calibri", 14)).grid(row=7, column = 1, sticky=N + E + S + W)
fP = tk.Entry(root, text = "0", font = ("Calibri", 12))
fP.grid(row=6, column = 2, sticky=N + E + S + W)
fK = tk.Entry(root, text = "10", font = ("Calibri", 12))
fK.grid(row=7, column = 2, sticky=N + E + S + W)

tk.Label(root).grid(row = 8, sticky=N + E + S + W)
button = tk.Button(root, text = "generuj wykres", command=wykres)
button.grid(row = 9, sticky=N + E + S + W, columnspan = 9)

root.mainloop()