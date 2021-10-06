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

        scan_btn = tk.Button(root, text="Scan", command = ui.scan_link)
        scan_btn.pack()

        exit_btn = tk.Button(root, text="Exit", command=self.quit)
        exit_btn.pack()

    def scan_link():
        sub_ui = tk.Tk()
        w = root.winfo_screenwidth()
        h = root.winfo_screenmmheight()
        sub_ui.geometry('%dx%d+%d+%d' % (w/3, h/2, w/3, h/4))

        # sub_ui.geometry('300x100')


        txt_input = tk.Text(sub_ui, height= 1.5)
        txt_input.pack()

        submit_btn = tk.Button(sub_ui, text="Submit Link")
        submit_btn.pack()

        subExit_btn = tk.Button(sub_ui, text="Exit", command=sub_ui.destroy)
        subExit_btn.pack()

        link = txt_input.get("1.0", 'end-1c')
        print(link)

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