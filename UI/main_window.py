import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        tab_control = ttk.Notebook()
        ess_tab = ttk.Frame(tab_control)
        kis_tab = ttk.Frame(tab_control)
        pyat_tab = ttk.Frame(tab_control)
        jel_tab = ttk.Frame(tab_control)
        archive_tab = ttk.Frame(tab_control)
        tab_control.add(ess_tab, text="ЕЭУ")
        tab_control.add(kis_tab, text="КЭУ")
        tab_control.add(pyat_tab, text="ПЭУ")
        tab_control.add(jel_tab, text="ЖЭУ")
        tab_control.add(archive_tab, text="Архивы")
        tab_control.pack(expand=1, fill="both")


class SensorFrame(tk.LabelFrame):
    pass


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.title("Мониторинг")
    root.geometry("1400x600")
    root.resizable(False, False)
    root.mainloop()
