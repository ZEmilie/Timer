import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Minuteur")
        self.master.geometry("250x100")
        
        self.time_left = 0
        
        self.label = tk.Label(self.master, text="")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.start_button = tk.Button(self.master, text="Démarrer", command=self.start_timer)
        self.start_button.pack()
        
    def start_timer(self):
        try:
            self.time_left = int(self.entry.get())
            self.update_timer()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        
    def update_timer(self):
        if self.time_left > 0:
            self.label.config(text=str(self.time_left))
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.label.config(text="Temps écoulé!")
        
def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
