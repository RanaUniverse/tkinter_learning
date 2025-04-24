from tkinter import Tk, Label

root = Tk()

root.title("Welcome To Rana Universe")
width = 700
height = 300
size = f"{width}x{height}"
root.geometry(size)

bg_color = "#FFFFFF"
root.configure(background=bg_color)


# First label
labeled_text = "Rana Universe"
label = Label(
    root,
    text=labeled_text,
    bg=bg_color,
    fg="green",
    font=("Helvetica", 30, "bold"),
    padx=10,
    pady=10,
)
label.pack()

# Second label
second_label = Label(
    root,
    text="Welcome to the second line!",
    bg=bg_color,
    fg="blue",
    font=("Helvetica", 20),
    padx=10,
    pady=10,
)
second_label.pack()

# Second label
second_label = Label(
    root,
    text="This is 3rd Line",
    bg=bg_color,
    fg="blue",
    font=("Helvetica", 20),
    padx=10,
    pady=10,
)
second_label.pack()


root.mainloop()
