from log.gui.main_window import LogApp


def main():
    app = LogApp()
    app.run()


if __name__ == "__main__":
    main()

# print("SentinelLog is starting...")

# import tkinter as tk

# root = tk.Tk()
# root.title("SentinelLog Test")
# root.geometry("500x300")

# label = tk.Label(
#     root,
#     text="SentinelLog is running!",
#     font=("Arial", 18)
# )
# label.pack(pady=50)

# print("Window initialized. Starting mainloop...")

# root.mainloop()