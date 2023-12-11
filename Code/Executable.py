import os


def main():
    # Convertir fichier.py en fichier.exe

    # Utilise PyInstaller pour convertir le fichier main.py
    os.system(f"pyinstaller --onefile main.py")

if __name__ == "__main__":
    main()
