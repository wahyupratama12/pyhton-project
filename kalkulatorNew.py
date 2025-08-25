import tkinter as tk

def klik(tulisan):
    layar.insert(tk.END, tulisan)

def hapus():
    layar.delete(0, tk.END)

def hapus_satu():
    layar.delete(len(layar.get())-1, tk.END)

def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(tk.END, str(hasil))
    except:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "Error")

def persen():
    try:
        nilai = float(layar.get()) / 100
        layar.delete(0, tk.END)
        layar.insert(tk.END, str(nilai))
    except:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "Error")

root = tk.Tk()
root.title("Kalkulator iPhone Style")
root.configure(bg="#000000")  # Latar belakang hitam

# Tampilan layar
layar = tk.Entry(root, font=("Arial", 30), bg="#000000", fg="white", borderwidth=0, justify="right", insertbackground="white")
layar.grid(row=0, column=0, columnspan=4, pady=15, padx=10, sticky="nsew")

# Style warna
warna_angka = "#751F1F"
warna_operator = "#CF7900"
warna_fungsi = "#D4D4D2"
fg_operator = "white"
fg_fungsi = "black"

def buat_tombol(text, row, col, bg, fg, cmd, colspan=1, rowspan=1):
    btn = tk.Button(root, text=text, bg=bg, fg=fg, font=("Arial", 20), command=cmd,
                    bd=0, relief="flat", activebackground=bg, activeforeground=fg)
    btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

# Atur grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Baris fungsi
buat_tombol("C", 1, 0, warna_fungsi, fg_fungsi, hapus)
buat_tombol("±", 1, 1, warna_fungsi, fg_fungsi, lambda: klik("-"))
buat_tombol("%", 1, 2, warna_fungsi, fg_fungsi, persen)
buat_tombol("÷", 1, 3, warna_operator, fg_operator, lambda: klik("/"))

# Baris angka 7 8 9
buat_tombol("7", 2, 0, warna_angka, "white", lambda: klik("7"))
buat_tombol("8", 2, 1, warna_angka, "white", lambda: klik("8"))
buat_tombol("9", 2, 2, warna_angka, "white", lambda: klik("9"))
buat_tombol("×", 2, 3, warna_operator, fg_operator, lambda: klik("*"))

# Baris angka 4 5 6
buat_tombol("4", 3, 0, warna_angka, "white", lambda: klik("4"))
buat_tombol("5", 3, 1, warna_angka, "white", lambda: klik("5"))
buat_tombol("6", 3, 2, warna_angka, "white", lambda: klik("6"))
buat_tombol("−", 3, 3, warna_operator, fg_operator, lambda: klik("-"))

# Baris angka 1 2 3
buat_tombol("1", 4, 0, warna_angka, "white", lambda: klik("1"))
buat_tombol("2", 4, 1, warna_angka, "white", lambda: klik("2"))
buat_tombol("3", 4, 2, warna_angka, "white", lambda: klik("3"))
buat_tombol("+", 4, 3, warna_operator, fg_operator, lambda: klik("+"))

# Baris angka 0 dan .
buat_tombol("0", 5, 0, warna_angka, "white", lambda: klik("0"), colspan=2)
buat_tombol(".", 5, 2, warna_angka, "white", lambda: klik("."))
buat_tombol("=", 5, 3, warna_operator, fg_operator, hitung)

root.mainloop()
