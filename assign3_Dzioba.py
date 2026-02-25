import tkinter as tk
from tkinter import messagebox

#Handler

def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()

    if not first or not last:
        messagebox.showerror("Error", "First Name and Last Name are required.")
        return

    message = (
        f"Welcome to tkinter, {first}, you entered:\n\n"
        f"First Name: {first}\n"
        f"Last Name: {last}\n"
        f"Email: {email}\n"
        f"Phone: {phone}"
    )

    messagebox.showinfo("Submitted Data", message)


def resetForm():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)


def quitApp():
    root.destroy()



#Main

root = tk.Tk()
root.title("Assignment 3 – Tkinter GUI")
root.geometry("500x300")

# LabelFrame

lblFrPerson = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
lblFrPerson.pack(padx=10, pady=10, fill="both", expand=True)

label_bg = "blue"
label_fg = "white"

#Entry Boxes
entry_style = {
    "bg": "black",
    "fg": "white",
    "insertbackground": "white",
    "highlightbackground": "white",
    "highlightcolor": "white",
    "highlightthickness": 1,
    "bd": 0
}

#Labels

lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg=label_bg, fg=label_fg)
lblFirst.grid(column=0, row=0, sticky="e", padx=5, pady=5)

entFirst = tk.Entry(lblFrPerson, **entry_style)
entFirst.grid(column=1, row=0, padx=5, pady=5)

lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg=label_bg, fg=label_fg)
lblLast.grid(column=0, row=1, sticky="e", padx=5, pady=5)

entLast = tk.Entry(lblFrPerson, **entry_style)
entLast.grid(column=1, row=1, padx=5, pady=5)

lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column=0, row=2, sticky="e", padx=5, pady=5)

entEmail = tk.Entry(lblFrPerson, **entry_style)
entEmail.grid(column=1, row=2, padx=5, pady=5)

lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column=0, row=3, sticky="e", padx=5, pady=5)

entPhone = tk.Entry(lblFrPerson, **entry_style)
entPhone.grid(column=1, row=3, padx=5, pady=5)

#Buttons

fraButtons = tk.Frame(lblFrPerson)
fraButtons.grid(column=0, row=4, columnspan=2, pady=15)

btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=5)

btnR = tk.Button(fraButtons, text="Reset", width=5, command=resetForm)
btnR.pack(side=tk.LEFT, padx=5)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=quitApp)
btnQ.pack(side=tk.LEFT, padx=5)

root.mainloop()
