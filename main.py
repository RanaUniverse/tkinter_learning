from tkinter import Tk, Label

root = Tk()

root.title("Welcome To Rana Universe")
width = 700
height = 300
size = f"{width}x{height}"
root.geometry(size)

bg_color = "#FFFFFF"
root.configure(background=bg_color)

labeled_text = "Rana Universe"
label = Label(
    root,
    text=labeled_text,
    bg="#FFFFFF",
    fg="green",
    font=("Helvetica", 30, "bold"),
    padx=10,
    pady=10,
)

# label.pack()
label.pack(side='left', fill='y', expand=True, padx=10, pady=10)
root.mainloop()
