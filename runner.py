import sys, tkinter
from tkinter import ttk
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))


from calculator.main import CoverUp 
from quiz_app.main import QuizApp, Question


class ScrollableFrame(tkinter.Frame):
    """A reusable modern scrollable frame container."""
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.canvas = tkinter.Canvas(self, bg=kwargs.get("bg", "#121214"), highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        #for holding main content
        self.scrollable_frame = tkinter.Frame(self.canvas, bg=kwargs.get("bg", "#121214"))
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Create window inside canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Make the inner frame expand to match canvas width
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack layouts
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_canvas_configure(self, event):
        # Dynamically match inner frame width to the canvas width
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        # Smooth scrolling across platforms
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

class AlllProjects(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Hub")
        self.geometry("450x600+0+0")
        
        self.bg_main = "#121214"     
        self.bg_card = "#1a1a1e"      
        self.text_primary = "#ffffff"  
        self.text_muted = "#a1a1aa"    
        self.accent_color = "#6366f1"  
        self.project_location = [str(i).split("\\")[-1] for i in current_dir.glob("*/") if "." not in str(i)]

        self.config(bg=self.bg_main)
        
        # Customizing ttk scrollbar style to blend with dark theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure(
            "Vertical.TScrollbar", 
            gripcount=0,
            background="#27272a", 
            troughcolor=self.bg_main, 
            bordercolor=self.bg_main, 
            lightcolor=self.bg_main, 
            darkcolor=self.bg_main
        )
        
        self.welcome = tkinter.Label(
            self, text="Dev Ope greet you", fg=self.text_primary, bg=self.bg_main,
            font=("Segoe UI", 28, "bold")
        )
        self.info = tkinter.Label(
            self, text=f"This are the projects i have made with tkinter python Library\nCurrent Total : {len(self.project_location)}", fg=self.text_muted, bg=self.bg_main,
            font=("Segoe UI", 11),
            justify="left"
        )
        self.welcome.pack(side="top", anchor="w", padx=40, pady=(30, 2))
        self.info.pack(side="top", anchor="w", pady=(0, 20), fill="x", expand=True)
        self.info.bind("<Configure>", lambda event: self.info.config(wraplength= event.width - 40, justify="left"))

        
       #my projects scrollbar frame
        self.home_container = ScrollableFrame(self, bg=self.bg_main)
        self.home_frame = self.home_container.scrollable_frame
        
        self.home()

    def home(self):
        # Pack the main scrollable container container
        self.home_container.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        for index, i in enumerate(self.project_location):
            print(index)
            #name card
            card = tkinter.Frame(self.home_frame, bg=self.bg_card, bd=0, padx=20, pady=20)
            card.pack(fill="x", pady=10)
            
            lbl_title = tkinter.Label(card, text=i.upper(), fg=self.text_primary, bg=self.bg_card, font=("Segoe UI", 14, "bold"))
            lbl_title.pack(anchor="w")
            #launch
            btn= tkinter.Button(
                card, text=f"Launch {i}", bg=self.accent_color, fg="#ffffff", 
                activebackground="#4f46e5", activeforeground="#ffffff", bd=0, 
                font=("Segoe UI", 10, "bold"), padx=15, pady=6, cursor="hand2",
                command= lambda indx = index:  self.action(indx)
            )
            btn.pack(anchor="w", pady=10)
            
    def action(self, index):
        for i in self.winfo_children():
            i.destroy()
        self.back_btn = tkinter.Button(
        self, # or self.home_frame, depending on where you want it placed
        text="← Back to Dashboard",
        bg="#27272a",          # Zinc dark gray background
        fg="#ffffff",          # Crisp white text
        activebackground="#3f3f46", 
        activeforeground="#ffffff",
        bd=0,                  
        font=("Segoe UI", 12, "bold"),
        padx=20,               
        pady=10,               
        cursor="hand2",  
        command =lambda: self.killAm(self)    
    )
    
        self.back_btn.place(relx=0.5, rely=0.5, anchor="center")
        if index == 0:
            CoverUp().mainloop()
        if index == 1:
            QuizApp().mainloop()
       
    def killAm(self, widget):
        for i in  widget.winfo_children():
            i.destroy()
        widget.destroy()
        AlllProjects().mainloop()
        
if __name__ == "__main__":
    AlllProjects().mainloop()