import tkinter as tk 
from frames import MainFrame, MainMenu    
from constants import constants

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ExpensesTracker")
        self.geometry(f"{constants.WIDTH}x{constants.HEIGHT}+{(self.winfo_screenwidth() - constants.WIDTH) // 2}+{(self.winfo_screenheight() - constants.HEIGHT) // 2}")
        self.iconbitmap(constants.ICON)
        self.minsize(constants.WIDTH,constants.HEIGHT)
        self.maxsize(constants.WIDTH,constants.HEIGHT)
        self.main_frame = MainFrame(self)
        self.main_menu = MainMenu(self)
        self.show_frame(self.main_frame)
        
    def show_frame(self, frame,fetch=False):
        for widget in self.winfo_children():
            widget.pack_forget()
        if fetch:
            frame.fetch_values()
        frame.pack(fill='both', expand=True)
        


if __name__ == '__main__':
    app = App()
    app.mainloop()
        
