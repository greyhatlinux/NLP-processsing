import bs4
import urllib3
import tkinter as tk

def initialise():
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenmmheight()
    root.geometry('%dx%d+%d+%d' % (w/2, h/2, w/4, h/4))
    return root

class ui(tk.Frame):
    # class for the UI
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("NLP UI")

    def gui_exit(self):
        exit()
    
    def client_get_url(self):
        url = self.entry_url.get()
        http = urllib3.PoolManager()
        page = http.request('GET', url)
        soup = bs4.BeautifulSoup(page.data, "html.parser")
        # print(soup)

root = initialise()

app = ui(root)
root.mainloop()