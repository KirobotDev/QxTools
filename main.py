import os
import time
import questionary
import winreg

def projet():
    os.system("cls")

     # def install_qx():
    #     folder = os.path.join(os.environ["USERPROFILE"], "qx_tool")
    #     os.makedirs(folder, exist_ok=True)

    #     script_path = os.path.join(folder, "qx.py")

    #     with open(script_path, "w", encoding="utf-8") as f:
    #         f.write(open(__file__, "r", encoding="utf-8").read())

    #     bat_path = os.path.join(folder, "qx.bat")

    #     with open(bat_path, "w", encoding="utf-8") as f:
    #         f.write(f'@echo off\npython "{script_path}" %*')

    #     key = winreg.OpenKey(
    #         winreg.HKEY_CURRENT_USER,
    #         "Environment",
    #         0,
    #         winreg.KEY_ALL_ACCESS
    #     )

    #     try:
    #         path_value, _ = winreg.QueryValueEx(key, "Path")
    #     except:
    #         path_value = ""

    #     if folder not in path_value:
    #         winreg.SetValueEx(
    #             key,
    #             "Path",
    #             0,
    #             winreg.REG_EXPAND_SZ,
    #             path_value + ";" + folder
    #         )


    choix = questionary.select(
        "Choisis",
        [
            # "Install Qx CLI",
            "Web Structure",
            "Base Structure",
            "Ai Structure", 
            "Tkinter Structure",
            "Quit"
        ]
    ).ask()
    
    if choix == "Web Structure":
        os.system("cls")
        sur = input("Ette vous sur de votre choix ? (Oui ou Non) : ").lower()
            
        if sur == "oui":
            os.system("cls")
            print(f"Bonjour sais entrains d'ètre crée ;) ")
            time.sleep(2)
            os.system("cls")
            try:
                os.mkdir("src")
                os.mkdir("src/static")
                os.makedirs("src/static/css", exist_ok=True)
                os.makedirs("src/static/js", exist_ok=True)
                os.makedirs("backend", exist_ok=True)
                os.makedirs("database", exist_ok=True)
                os.makedirs("src/api", exist_ok=True)

                with open("src/static/index.html", "w", encoding="utf-8") as fichier:
                    fichier.write("""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QxTools</title>
</head>
<body>
    <!-- Create By QxTools -->
</body>
</html>
                    """)
                with open("src/static/css/styles.css", "w", encoding="utf-8") as fichier:
                    fichier.write("""* {
background-color: black;
} """)
                with open("src/static/js/script.js", "w", encoding="utf-8") as fichier:
                    fichier.write("console.log('Create by QxTools')")
                with open("backend/server.js", "w", encoding="utf-8") as fichier:
                    fichier.write("console.log('Create by QxTools')")
                with open("database/main.sql", "w", encoding="utf-8") as fichier:
                    fichier.write("-- Create by QxTools")
                with open("src/api/api.js", "w", encoding="utf-8") as fichier:
                    fichier.write("console.log('Create by QxTools')")
            except Exception as e:
                print(f"Error {e}")
                
            print("Votre Structure web a bien etais crée")
            time.sleep(2)
            os.system("cls")
        elif sur == "non":
            print("Ok au-revoir")
            time.sleep(2)
        else:
            print(f"choisis une réponse valide sois Oui sois Non ta réponse actuel etais ( {sur} )")

    elif choix == "Base Structure":
        os.system("cls")
        surs = input("Ette vous sur de votre choix ? (Oui ou Non) : ").lower()

        if surs == "oui":
            try:
                os.system("cls")
                print(f"Votre Base Structure est entrains d'ètre crée")
                time.sleep(1)
                os.system("cls")
                os.mkdir("src")
                os.mkdir("database")
                os.mkdir("docs")
                
                with open("src/main.py", "w", encoding="utf-8") as fichier:
                    fichier.write("# Create by QxTools")
                with open("database/db.sql", "w", encoding="utf-8") as fichier:
                    fichier.write("-- Create by QxTools")
                with open("docs/index.html", "w", encoding="utf-8") as fichier:
                    fichier.write("""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QxTools</title>
    <style>
    * {
    background-color: black;
    }
    </style>
</head>
<body>
    <!-- Create By QxTools -->
</body>
</html>
        """)
                os.system("cls")
                print("Votre Base Structure a etais crée avec succées")
                time.sleep(2)
            except Exception as e:
                print(f"Error {e}")
        elif surs == "non":
            print("Au-Revoir")
            time.sleep(2)
        else:
            print(f"choisis une réponse valide sois Oui sois Non ta réponse actuel etais ( {sur} )")
            time.sleep(2)

    elif choix == "Ai Structure":
        os.system("cls")
        sur = input("Ette vous sur de votre choix ? (Oui ou Non) : ").lower()

        if sur == "oui":
            os.system("cls")
            print("Votre Ai Structure est entrains d'ètre crée")
            time.sleep(1)
            os.system("cls")

            try:
                os.makedirs("ai", exist_ok=True)
                os.makedirs("ai/models", exist_ok=True)
                os.makedirs("ai/data", exist_ok=True)
                os.makedirs("ai/utils", exist_ok=True)
                os.makedirs("ai/api", exist_ok=True)

                with open("ai/main.py", "w", encoding="utf-8") as fichier:
                    fichier.write("print('Creat by QxTools')")

                with open("ai/models/model.py", "w", encoding="utf-8") as fichier:
                    fichier.write("print('Creat by QxTools')")

                with open("ai/data/dataset.json", "w", encoding="utf-8") as fichier:
                    fichier.write("{}")

                with open("ai/utils/helpers.py", "w", encoding="utf-8") as fichier:
                    fichier.write("print('Creat by QxTools')")

                with open("ai/api/server.py", "w", encoding="utf-8") as fichier:
                    fichier.write("print('Creat by QxTools')")

            except Exception as e:
                print(f"Error {e}")

            print("Votre Ai Structure a etais crée avec succées")
            time.sleep(2)
            os.system("cls")

        elif sur == "non":
            print("Au-Revoir")
            time.sleep(2)

        else:
            print(f"choisis une réponse valide sois Oui sois Non ta réponse actuel etais ( {sur} )")

    elif choix == "Tkinter Structure":
        os.system("cls")
        sur = input("Êtes-vous sûr de votre choix ? (Oui ou Non) : ").lower()

        if sur == "oui":
            os.system("cls")
            print("Votre structure Tkinter est en train d'être créée...")
            time.sleep(1)
            os.system("cls")

            try:
                os.makedirs("src", exist_ok=True)

                with open("src/main.py", "w", encoding="utf-8") as fichier:
                    fichier.write("""import tkinter as tk

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
""")

                print("Votre structure Tkinter a été créée avec succès.")

            except Exception as e:
                print(f"Erreur : {e}")

        elif sur == "non":
            print("Au revoir")
            time.sleep(2)

        else:
            print(f"Choisissez une réponse valide. Vous avez répondu : {sur}")

    elif choix == "Quit":
        print("Bon bah salut ;)")
        time.sleep(2)
    
    else:
        print("Wesh tu bypass les questionary en mode tki tes eliot andersonne ?")

projet()