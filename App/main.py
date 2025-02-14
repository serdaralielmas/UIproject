import tkinter as tk
from UIproject.Controllers.user_controller import UserController

def main():
    root = tk.Tk()
    controller = UserController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
