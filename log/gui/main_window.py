import tkinter as tk
from tkinter import ttk


class LogApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Security Log Analyzer")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title_label = ttk.Label(
            main_frame,
            text="Log",
            font=("Segoe UI", 26, "bold")
        )
        title_label.pack(anchor="w")

        desc_label = ttk.Label(
            main_frame,
            text="Security Log Analyzer and Incident Investigation Tool.",
            font=("Segoe UI", 12)
        )
        desc_label.pack(anchor="w", pady=(5, 20))

        welcome_label = ttk.Label(
            main_frame,
            text="Welcome to the log analyzer. Import a log file to begin analysis.",
            font=("Segoe UI", 12)
        )
        welcome_label.pack(anchor="w", pady=10)

        import_button = ttk.Button(
            main_frame,
            text="Import Log File",
            command=self.import_log
        )
        import_button.pack(anchor="w", pady=10)

        self.status_label = ttk.Label(
            self.root,
            text="Ready | No Log File Loaded",
            relief="sunken",
            anchor="w",
            padding=5
        )
        self.status_label.pack(side="bottom", fill="x")

    def import_log(self):
        print("Log import functionality coming soon!")

    def run(self):
        self.root.mainloop()

