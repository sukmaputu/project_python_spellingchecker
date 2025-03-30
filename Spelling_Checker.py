from tkinter import *
from textblob import TextBlob

def check_spelling():
    input_text = entry.get()  # Ambil teks dari input field
    blob = TextBlob(input_text)
    corrected_text = blob.correct()  # Koreksi teks
    output_label.config(text=f"Corrected Text: {corrected_text}")  # Tampilkan hasil

# Inisialisasi GUI
root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

# Label Judul
title_label = Label(root, text="Spelling Checker", font=("Arial", 24, "bold"), bg="#dae6f6")
title_label.pack(pady=20)

# Input Field
entry = Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=10)

# Button untuk Mengecek Ejaan
check_button = Button(root, text="Check Spelling", font=("Arial", 14), command=check_spelling)
check_button.pack(pady=10)

# Output Label
output_label = Label(root, text="", font=("Arial", 14), bg="#dae6f6", fg="green")
output_label.pack(pady=20)

root.mainloop()
