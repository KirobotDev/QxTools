import tkinter as tk

root = tk.Tk()
root.title("QxTools")
root.geometry("800x600")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="QxTools",
    font=("Arial", 28, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=(50, 10))

subtitle = tk.Label(
    root,
    text="Bienvenue sur QxTools !, Cliquez sur le bouton ci-dessous pour accéder au GitHub.",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#cfcfcf",
    justify="center"
)
subtitle.pack(pady=10)

github_button = tk.Button(
    root,
    text="GitHub",
    font=("Arial", 13, "bold"),
    bg="#2ea043",
    fg="white",
    activebackground="#238636",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=lambda: webbrowser.open("https://github.com/KirobotDev/QxTools")
)
github_button.pack(pady=30)

footer = tk.Label(
    root,
    text="© 2026 KirobotDev",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="#808080"
)
footer.pack(side="bottom", pady=15)

root.mainloop()
