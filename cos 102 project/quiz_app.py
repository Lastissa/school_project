import tkinter, sys
from pathlib import Path
from tkinter import messagebox

#i need to pick the calculator so i have to use sys to perforn pickup
parent_path = Path(__file__).resolve().parent
sys.path.append(str(parent_path))

from calculator import CoverUp  # utilziing the abstraction concept
from utility import Question    # the questions i am going to use(i avoid local db to avoid data loss)

class QuizApp(tkinter.Tk, Question):
    def __init__(self):
        super().__init__()
        self.width = 650
        self.height  =600
        self.bg = "#0B0F19" #background color
        
        self.current_question_index = tkinter.IntVar(value=0) # for tracking the current question index in the quiz_start
        self.current_score_list = tkinter.StringVar(value="")#track current opt picks "a,b,c,d,c,a" and so on
        self.selected_option = tkinter.StringVar(value="") # for tracking the selected option in the quiz_start and addi

        self.courses = [i for i in dir(Question) if "__" not in i] # course for the dropdown menu, i use the __ to remove all automatic func that follows all classes by default
        self.selected_course = tkinter.StringVar(master = self,value=self.courses[0]) #for the dropwown in the welcome page
        self.hours = [f"{x:02d}" for x in range(5)]#4 hour max
        self.selected_hour = tkinter.StringVar(master = self,value="0")
        self.minutes = [f"{i:02d}" for i in range(0, 60, 5)]
        self.minutes.insert(1, "01") # for testing what happens on time run out
        self.minutes.insert(2, "02")
        self.selected_min = tkinter.StringVar(master = self,value="10")
        self.selected_question_lenght = tkinter.StringVar(master = self,value="00") # the lenght of the question the user want to do
        self.question_option = [f"{i:02d}" for i in range(0, 101, 5)]
        
        #the welcome page setup
        self.title("group 1 quiz app project")
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.configure(bg=self.bg)
        
        #the home frame and the quiz frame set up
        self.home_frame = tkinter.Frame(self, bg= self.bg)
        self.quiz_frame = tkinter.Frame(self, bg=self.bg, padx=10, pady=12)
        
        # Display the home screen directly
        self.build_home_page()
    
    def build_home_page(self):
        self.home_frame.pack(fill="both", expand=True)
        #a new wrapper inside the home frame - i used it for better layout
        self.content_wrapper = tkinter.Frame(self.home_frame, bg="#0B0F19", padx=40, pady=40)#for inner frame so i can del all stuff without delay like the calculator
        self.content_wrapper.pack(fill="both", expand=True)
        #intro label
        lbl_welcome = tkinter.Label(self.content_wrapper, text="QUIZ APP", font=("Segoe UI", 26, "bold"), fg="#F8FAFC", bg="#0B0F19")
        lbl_welcome.pack(anchor="w", pady=(0, 4))
        #intro words
        lbl_desc = tkinter.Label(self.content_wrapper, text="A simple quiz app that help access your knowledge on a course", font=("Segoe UI", 11), fg="#64748B", bg=self.bg)
        lbl_desc.pack(anchor="w", pady=(0, 25))
        #the divider for decoration
        divider = tkinter.Frame(self.content_wrapper, height=1, bg="#1F2937")
        divider.pack(fill="x", pady=(0, 30))
        #Frame for selecting course, duration and question
        data_collection_frame = tkinter.Frame(self.content_wrapper, bg="#111827", padx=35, pady=35, highlightbackground="#1F2937", highlightthickness=1)
        data_collection_frame.pack(fill="x", pady=(0, 35))
        # 1. Course Selection Dropdown Section
        lbl_course_title = tkinter.Label(data_collection_frame, text="SELECT COURSE", font=("Segoe UI", 9, "bold"), fg="#94A3B8", bg="#111827")
        lbl_course_title.pack(anchor="w", pady=(0, 8))
        #courses option
        course_menu = tkinter.OptionMenu(data_collection_frame, self.selected_course, *self.courses, command = None)
        self.style_option_menu(course_menu)
        course_menu.pack(fill="x", pady=(0, 25))
        # 2. Time Allocation Dropdown Section
        lbl_duration_title = tkinter.Label(data_collection_frame, text="LIMIT DURATION", font=("Segoe UI", 9, "bold"), fg="#94A3B8", bg="#111827")
        lbl_duration_title.pack(anchor="w", pady=(0, 8))
        #for hour and course
        picker_row = tkinter.Frame(data_collection_frame, bg="#111827")
        picker_row.pack(anchor="w", fill="x")
        #for the hour selector
        hour_menu = tkinter.OptionMenu(picker_row, self.selected_hour, *self.hours)
        self.style_option_menu(hour_menu)
        hour_menu.pack(side="left")
        lbl_colon = tkinter.Label(picker_row, text=":", font=("Segoe UI", 14, "bold"), fg="#4B5563", bg="#111827")
        lbl_colon.pack(side="left", padx=12)
        #for the minute selector
        min_menu = tkinter.OptionMenu(picker_row, self.selected_min, *self.minutes)
        self.style_option_menu(min_menu)
        min_menu.pack(side="left")
        #duration suffix
        lbl_suffix = tkinter.Label(picker_row, text="HH : MM", font=("Segoe UI", 10, "bold"), fg="#4B5563", bg="#111827")
        lbl_suffix.pack(side="left", padx=15)
        #question_count label
        question_count_lbl = tkinter.Label(picker_row, text="question lenght".upper(), font=("Segoe UI", 9, "bold"), fg="#94A3B8", bg="#111827")
        question_count_lbl.pack(anchor="e")
        #question amount selector
        question_count = tkinter.OptionMenu(picker_row, self.selected_question_lenght, *self.question_option)
        self.style_option_menu(question_count)
        question_count.pack(anchor="e")
        #start quiz button
        self.btn_start = tkinter.Button(self.content_wrapper, text="Start", font=("Segoe UI Semibold", 12), bg="#2563EB", fg="#FFFFFF", padx=35, pady=12, command=self.start_quiz)
        self.btn_start.pack(anchor="se")

    #styling the Option menu
    def style_option_menu(self, menu_widget):
        menu_widget.config(bg="#1F2937", fg="#F3F4F6", activebackground="#374151", activeforeground="#FFFFFF", bd=0, highlightthickness=1, highlightbackground="#374151", font=("Segoe UI", 11), indicatoron=0, padx=15, pady=8)
    
    #for starting the quiz
    def start_quiz(self):
        #check if question count is not zero nd real time was inserted
        duration = (int(self.selected_hour.get())*3600) + (int(self.selected_min.get())*60) # total time in seconds
        if duration == 0 or int(self.selected_question_lenght.get()) == 0:
            try: # incase this is the first time THE ERROR IS SHOWN as pack_forget wont work yet so the except should br used
                self.dur_err_warn.pack_forget()
                self.dur_err_warn = tkinter.Label(self.content_wrapper, text="INCOMPLETE PARAMETERS!!!", fg="#ff8888", bg = self.bg, font=("Segoe UI", 13, "bold"),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            except:
                self.dur_err_warn = tkinter.Label(self.content_wrapper, text="INCOMPLETE PARAMETERS!!!", fg="#ff8888", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            return # to stop the following line from working
            
        #to reset the timer incase the user have press quit and come bacl yes the quiz_frame was suppose to destroy and it did  but the attribute hour_in_sec is still alive keeping the duration from restarting
        try:
            self.time_in_sec - 20 # if it works , it mean the user have been in the quiz frame befpre and i need to reset it
            hour_in_sec, min_in_sec,self.time_in_sec  = [int(self.selected_hour.get())*3600, int(self.selected_min.get())*60,hour_in_sec + min_in_sec]
        except:
            pass
        #to reset the current index too
        try:
            self.current_question_index.set(0)
        except:
            pass
        #reset the selected answer incase the user have pressed it before
        self.selected_option.set("")
        #populate a list for list of question len so i can modify it later during submission
        self.answer_pool = ["0" for i in range(0, int(self.selected_question_lenght.get()))]
        #the quiz questions
        self.questionFilter() # question filtered # self.question_pool is now populated with the selected course question
        if self.questionFilter() == False:
            try: # incase this is the first time THE ERROR IS SHOWN as pack_forget wont work yet so the except should br used
                self.dur_err_warn.pack_forget()
                self.dur_err_warn = tkinter.Label(self.content_wrapper, text= f"Errror, Max allowed question is  {len(self.allQuestionBeforeFilter)}", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            except:
                self.dur_err_warn = tkinter.Label(self.content_wrapper, text= f"Error, Max allowed question is  {len(self.allQuestionBeforeFilter)}", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            return
        
        #No missing parameter, Erase home_frame and add the quiz frame
        for i in self.home_frame.winfo_children():
            i.destroy() #destroy all home frame content cos i want to rebuld it
        self.home_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)

        

        self.quiz_first_frame() #course and duration
        self.quiz_second_frame() #question
        self.quiz_third_frame() #options
        self.quiz_fourth_frame() # prev, quit, submit, and next
        self.quiz_fifth_frame() #for the question index button at the footer

    #for quiz_frame refrence
    def time_formater(self, seconds: int):#formatting the time for display in the quiz frame
        #for turning normal seconds to formatted hh:mm, i need this for the time formating inside the quiz time place for duration formatting
        hour = seconds//3600
        min = (seconds - (hour * 3600))//60
        sec =seconds - ((hour * 3600) + (min*60))
        result = f"{hour} : {min:02d} : {sec:02d}"
        return result
        
    def duration_countdown_display(self):#duration widget
        try:
            self.time_in_sec -= 1 # if this fail, it mean we are just getting opening the start_quiz
            if self.time_in_sec < 1: # when user run out of time
                 for i in self.quiz_frame.winfo_children():
                    i.destroy() #destroy all quiz frame content
                 self.quiz_frame.pack_forget() #hide the quiz frame
                 self.loadAnalysis()#load the analysis into display
                 return    
        except:
            hour_in_sec = int(self.selected_hour.get())*3600
            min_in_sec = int(self.selected_min.get())*60
            self.time_in_sec = hour_in_sec + min_in_sec
           
        #the duration counter label 
        self.duration_lbl = tkinter.Label(
            self.quiz_header_frame, 
            text=self.time_formater(self.time_in_sec),
            font=("Segoe UI", 15, "bold"), 
            bg=self.bg, 
            fg="white",
            anchor="w"
            )
        self.duration_lbl.pack(anchor="e", expand=True, padx=3, pady=3)
        self.duration_lbl.after(1000, lambda:  [
                self.duration_lbl.pack_forget(),
                self.duration_countdown_display()])
        # else:#for when the time hit zero, the quiz frame should auto close            

    def configureQuestionWidth(self, event, widget): #for wrapping the text label inside the frame to make it responsive
        widget.config(wraplength = event.width - 40, justify  ="left")
        
    def questionFilter(self):#scrutinizing the pool to select question from  based on selected course
        self.allQuestionBeforeFilter = [] #this is to first bring in all the question from the course without shufffling or caring about lenght
        #get all the method from the Question class automatically
        func_i_need =[i for i in dir(Question) if "__" not in i] #used the __ to remove tee default follow come methods
        for index in func_i_need:
             if self.selected_course.get() == str(index):
                 self.allQuestionBeforeFilter.extend(getattr(Question(), index)())
                 break
        
        #incase nothing came back from the methods or there was an errror
        if len(self.allQuestionBeforeFilter) < int(self.selected_question_lenght.get()):
            return False
        self.question_pool = [] # this will house the question displayed to the user for the duration of the quiz
        import random
        try:
            for i in range(int(self.selected_question_lenght.get())):
                random_index = random.randint(0, len(self.allQuestionBeforeFilter)-1) # for getting a random index
                picked_question = self.allQuestionBeforeFilter[random_index]
                self.question_pool.append(picked_question)
                self.allQuestionBeforeFilter.remove(picked_question) # remove the question so it wont be pick again at random
        except:#incase the question is too long fot the question pool
            return False
    def calculator_func(self):
        try: 
            if self.calculator_is_active :# cal was on before, off it
                self.calculator_is_active = False
                self.calc.config(text="calc", bg="green", fg="white")
                CoverUp().destroy()
                return
        
        except:
            pass
    
        #cal is not on, proceed to on it
        self.calculator_is_active = True
        self.calc.config(text="off", bg="red", fg="white")
        CoverUp(width_pos = self.width, height_pos = 0).mainloop()
        
        CoverUp(width_pos = self.width, height_pos = 0).mainloop()     
    def quiz_first_frame(self):
        self.quiz_header_frame = tkinter.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_header_frame.pack(fill="x", pady=10, padx=10)

        #Left: Course Title
        self.course_lbl = tkinter.Label(self.quiz_header_frame, text=self.selected_course.get(), font=("Segoe UI", 15, "bold"), bg=self.bg, fg="white", anchor="w")
        self.course_lbl.pack(side="left", padx=10)
        #cal btn
        self.cal = tkinter.Button(self.quiz_header_frame, text="Calculator", font=("Segoe UI", 10), bg="#aaaaaa", fg="white", padx=10, pady=5 ,bd=0, command=lambda: CoverUp().mainloop())

        self.calc = tkinter.Button(self.quiz_header_frame, text="calc", font=("Segoe UI", 9), bg="green", fg="white", padx=10, pady=5 ,bd=0, command=lambda : self.calculator_func())
        self.calc.pack(side="left", padx=10)
        #right: Duration Title
        self.duration_countdown_display()
    
    def quiz_second_frame(self):
        self.quiz_questioon_frame = tkinter.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_questioon_frame.pack(fill="both", expand=True, padx=10, pady=20)
        self.quiz_questioon_label = tkinter.Label(self.quiz_questioon_frame, text=self.question_pool[self.current_question_index.get()][0], font=("Segoe UI", 12), bg=self.bg, fg="white", justify="left", wraplength= self.width - 40)
        self.quiz_questioon_label.pack(fill="x")
        
        #for resing the question incase its too long
        self.quiz_questioon_label.bind("<Configure>", lambda event, extra = self.quiz_questioon_label: self.configureQuestionWidth(widget=  extra, event=event))
        
    def quiz_third_frame(self):
        self.quiz_option_frame = tkinter.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_option_frame.pack(fill="x", padx=10, pady=10)
        #the options radio buttons
        #(1)
        self.quiz_opt_btn_1 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="A. " + self.question_pool[self.current_question_index.get()][1][0],
                value = "A",
                variable= self.selected_option,
                font=("Segoe UI", 11), 
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                activebackground=self.bg,
                activeforeground="#00ff00",
                command= self.optButtonSelected)
        self.quiz_opt_btn_1.pack(anchor="w", pady=5, padx=10)
        #(2)
        self.quiz_opt_btn_2 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="B. " + self.question_pool[self.current_question_index.get()][1][1],
                value = "B",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                activebackground=self.bg,
                activeforeground="#00ff00",
                command= self.optButtonSelected)
        self.quiz_opt_btn_2.pack(anchor="w", pady=5, padx=10)
        #(3)
        self.quiz_opt_btn_3 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="C. " + self.question_pool[self.current_question_index.get()][1][2],
                value = "C",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                activebackground=self.bg,
                activeforeground="#00ff00",
                command= self.optButtonSelected)
        self.quiz_opt_btn_3.pack(anchor="w", pady=5, padx=10)
         #(4)
        self.quiz_opt_btn_4 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="D. " + self.question_pool[self.current_question_index.get()][1][3],
                value = "D",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                activebackground=self.bg,
                activeforeground="#00ff00",
                command= self.optButtonSelected)
        self.quiz_opt_btn_4.pack(anchor="w", pady=5, padx=10)
        
    def quiz_fourth_frame(self):
        #for the footer = prev, quiz, submit and next
        self.quiz_footer_frame = tkinter.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_footer_frame.pack(fill="x", expand=True)

        #prev
        self.footer_button_prev = tkinter.Button(self.quiz_footer_frame, text="Previous", font=("Segoe UI", 11), bg="#aaaaaa", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Prev"))
        self.footer_button_prev.grid(row=0, column= 0, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(0, weight= 1)
        
        #quit
        self.footer_button_quit = tkinter.Button(self.quiz_footer_frame, text="Quit", font=("Segoe UI", 11), bg="#DC2626", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Quit"))
        self.footer_button_quit.grid(row=0, column= 1, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(1, weight= 1)
        
        #submit
        self.footer_button_submit = tkinter.Button(self.quiz_footer_frame, text="Submit", font=("Segoe UI", 11), bg="#16A34A", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Submit"))
        self.footer_button_submit.grid(row=0, column= 2, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(2, weight= 1)
        
        #next
        self.footer_button_next = tkinter.Button(self.quiz_footer_frame, text="Next", font=("Segoe UI", 11), bg="#173E94", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Next"))
        self.footer_button_next.grid(row=0, column= 3, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(3, weight= 1)
          
    def quiz_fifth_frame(self):
        self.quiz_footer_second_frame = tkinter.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_footer_second_frame.pack(anchor="s", pady=10, padx=10, fill="x", expand=True)
        self.current_question_footer = tkinter.Label(self.quiz_footer_second_frame, text=f"Question {self.current_question_index.get() + 1} of {int(self.selected_question_lenght.get())}", font=("Segoe UI", 14, "bold"), bg=self.bg, fg="#94A3B8")
        self.current_question_footer.pack(anchor="e")
    
    #for styking and changing the correct ans value
    def deepAnalysisRightAns(self):
        try:
            #check if the user got it right
            chosen_answer = str(self.answer_pool[self.current_question_index.get()]).upper()
            correct_ans = self.question_pool[self.current_question_index.get()][-1].upper()
            print(chosen_answer, self.correct_answer)
            if chosen_answer ==  correct_ans:
                bg  = "#00ff00"
                fg = "#555555"
            else:
                bg = "#ff0000"
                fg = "#ffffff"
            self.correct_answer.config(text= f"Option {self.question_pool[self.current_question_index.get()][-1].upper()} is the correct answer", bg = bg, fg = fg)#updating the summary correct answer
        except Exception as e:#incase the user have not reach there si the app wnt crash
            print(f"{e}")
   
    #for prev, next...
    def prevQuiSubmitNext(self, action):
        if action == "Prev":
            #update the color of the next button to show it is clickable
            self.footer_button_next.config( bg="#173E94", state="normal")
            
            if self.current_question_index.get() > 0:
                self.current_question_index.set(self.current_question_index.get() - 1) # updating the current index in thr question pool
                print(f"current index {self.current_question_index.get()}")
                if self.current_question_index.get() == 0:
                    self.footer_button_prev.config( bg="#aaaaaa", state="disabled")#change the prev colour 
                self.selected_option.set(self.answer_pool[self.current_question_index.get()])#the current should be what was in the answer pool
                self.quiz_questioon_label.config(text= self.question_pool[self.current_question_index.get()][0])#updating the question
                self.current_question_footer.config(text= f"Question {self.current_question_index.get() + 1} of {int(self.selected_question_lenght.get())}") # updating the footer
                self.quiz_opt_btn_1.config(text="A. " + self.question_pool[self.current_question_index.get()][1][0])#updating the 1st option
                self.quiz_opt_btn_2.config(text="B. " + self.question_pool[self.current_question_index.get()][1][1])#updating the 2nd option
                self.quiz_opt_btn_3.config(text="C. " + self.question_pool[self.current_question_index.get()][1][2])#updating the 3rd option
                self.quiz_opt_btn_4.config(text="D. " + self.question_pool[self.current_question_index.get()][1][3])#updating the 4th option
                
                #for styking and changing the correct ans value
                self.deepAnalysisRightAns()
            else:
                pass
              
        elif action == "Next":
            #update the color of the previous button to show it is now clickable
            self.footer_button_prev.config( bg="#173E94", state="normal")
            if self.current_question_index.get() < int(self.selected_question_lenght.get()) - 1:
                #updating the color of the next to ash to when the user get to the last q, it will notify them its inactive
                if self.current_question_index.get() == int(self.selected_question_lenght.get()) - 2:
                    self.footer_button_next.config(bg = "#aaaaaa", state="disabled")
                self.current_question_index.set(self.current_question_index.get() + 1) # updating the current index in thr question pool
                print(f"current index {self.current_question_index.get()}")
                self.selected_option.set(self.answer_pool[self.current_question_index.get()])#the current should be what was in the answer pool
                self.quiz_questioon_label.config(text= self.question_pool[self.current_question_index.get()][0])#updating the question
                self.current_question_footer.config(text= f"Question {self.current_question_index.get() + 1} of {self.selected_question_lenght.get()}") # updating the footer
                self.quiz_opt_btn_1.config(text="A. " + self.question_pool[self.current_question_index.get()][1][0])#updating the 1st option
                self.quiz_opt_btn_2.config(text="B. " + self.question_pool[self.current_question_index.get()][1][1])#updating the 2nd option
                self.quiz_opt_btn_3.config(text="C. " + self.question_pool[self.current_question_index.get()][1][2])#updating the 3rd option
                self.quiz_opt_btn_4.config(text="D. " + self.question_pool[self.current_question_index.get()][1][3])#updating the 4th option
                
                #for styking and changing the correct ans value
                self.deepAnalysisRightAns()
            else:
                pass
                    
        elif action == "Submit":
            total_answered = 0
            for i in self.answer_pool:
                if i != "0":
                    total_answered += 1
            shouldSunbmit = tkinter.messagebox.askyesno("Submit", f"Are you sure you want to submit?\nYou have answered {total_answered} out of {len(self.answer_pool)}")
            if shouldSunbmit:
                self.home(old_frame=self.quiz_frame, new_frame_method=self.loadAnalysis) # changing the current frame
                
            
        elif action == "Quit":
            messagebox = tkinter.messagebox.askyesno("Quit Quiz", "Are you sure you want to quit?\nCurrent Data will be lost!")
            if messagebox:
                for i in self.quiz_frame.winfo_children():
                    i.destroy() #destroy all quiz frame content 
                self.quiz_frame.pack_forget() #hide the quiz frame
                try:
                    for i in self.deepAnalysisFrame.winfo_children(): #or the deepanalysis frame
                        i.destroy()
                    self.deepAnalysisFrame.pack_forget()
                except Exception as e:pass
                self.build_home_page() # Go back to the home page
   
    #for when ans is selected
    def optButtonSelected(self):
        self.answer_pool[self.current_question_index.get()] = self.selected_option.get()
    
    #the analysis frame
    def loadAnalysis(self):
        #toNeed
        total_question_answered = 0 # setting them to zero first so i can update the later or not update them at all if the user did not attempt any q
        total_correct_answer = 0
        
        #for checking the total attempted question
        for i in self.answer_pool:
            if i != "0":
              total_question_answered += 1
        #for increasing the correct score count
        for i in range(len(self.question_pool)):
            print(self.answer_pool[i], self.question_pool[i][-1])
            #incase the user did not attempt the question, the answer pool will have a "0" and this will cause an error when comparing it to the correct answer which is a string, so i used try except to bypass it
            try:
                if (self.answer_pool[i]).upper() == (self.question_pool[i][-1]).upper():
                    total_correct_answer += 1
            except:
                pass
        total_allocated_duration_in_sec = int(self.selected_hour.get())*3600 + int(self.selected_min.get())*60
        duration_used =total_allocated_duration_in_sec - self.time_in_sec
        #speed and speed remaek
        try:
            speed = f"{(duration_used/ total_question_answered):.1f} sec / Question"
            if int(duration_used/ total_question_answered) <=5:
                word_remark_text = "Welcome, flash."
            elif int(duration_used/ total_question_answered) <=10:
                word_remark_text = "That speed is cool, chop knuckles"
            elif int(duration_used/ total_question_answered) <=15:
                word_remark_text = "Good but speed can be better"
            else:
                word_remark_text = "Guy, even tortoise fast pass u"
        except ZeroDivisionError:
            speed = "Not Available"
            word_remark_text = "No question Attempted"
        
        #int to remark e.g A, B,C,etc
        def converter(value:int):
            if value <= 39:
                return "F"
            elif value >=40 and value <= 50:
                return "D"
            elif value >=51 and value<=60:
                return "C"
            elif value >=61 and value <=70:
                return "B"
            else:
                return "A"
        percentage_rel_to_total_que = f"{int((total_correct_answer / len(self.question_pool)) * 100)} %"
        remark_rel_to_total_que = converter(total_correct_answer/len(self.question_pool) * 100)
        try: 
            percentage_rel_to_attemp_que = f"{int((total_correct_answer / total_question_answered) * 100)} %"
            remark_rel_to_attempt_que = converter(total_correct_answer/ total_question_answered * 100)
        except:
            percentage_rel_to_attemp_que = "0 %"
            remark_rel_to_attempt_que = "F"
        information_to_display = {
            "Course" : self.selected_course.get(),
            "Total Question" : int(self.selected_question_lenght.get()),
            "Attempted Question" : total_question_answered,
            "Correct Question" : total_correct_answer ,
            "% rel to Total que" : percentage_rel_to_total_que + " - " + remark_rel_to_total_que,
            "% rel to Attempted que" : percentage_rel_to_attemp_que + " - " + remark_rel_to_attempt_que,
            "Duration Allocated" : f"{self.selected_hour.get()}hr {self.selected_min.get()}min",
            "Duration Used" : f"{self.time_formater(duration_used).split(":")[0]}hr {self.time_formater(duration_used).split(":")[1]}min {self.time_formater(duration_used).split(":")[2]} sec",
            "speed" : speed,     
        }
        
        #widget drawup
        self.analysis_frame = tkinter.Frame(self, bg=self.bg)
        self.analysis_frame.pack(expand=True, fill="both", padx=10, pady=10)

        #the  report label
        report = tkinter.Label(self.analysis_frame, text = "ANALYSIS",font=("Segoe UI", 26, "bold"), fg="#F8FAFC", bg="#0B0F19")
        report.pack(expand=True, fill="x", anchor="n")
        
        #used an inner frame so i can use a grid inside as the current frame is beign run by a pack
        inner_frame = tkinter.Frame(self.analysis_frame, bg= self.bg)
        inner_frame.pack(expand=True, fill="both")
        
        for index, value in enumerate(information_to_display.keys()):
            btn_left = tkinter.Label(inner_frame, text=value, font=("Segoe UI", 11), bg = self.bg, fg="white", pady=1, anchor="w")
            btn_left.grid(row=index, column=0,pady=5, padx=10, sticky="ew")
            inner_frame.grid_rowconfigure(index, weight=1)
            inner_frame.grid_columnconfigure(0, weight=1)
            
            btn_right = tkinter.Label(inner_frame, text=information_to_display[value], justify="right",font=("Segoe UI", 13, "bold"), bg = self.bg, fg="white", pady=1, anchor="center")
            btn_right.grid(row=index, column=1,pady=5, sticky="ew")
            inner_frame.grid_rowconfigure(index, weight=1)
            inner_frame.grid_columnconfigure(1, weight=1)
        
        #the analysis btn
        analysis_btn = tkinter.Button(self.analysis_frame, text="Q SUMMARY", font=("Segoe UI Semibold", 12),bg="#2563EB",  fg="#FFFFFF",padx=35, command= self.eachQuestionAnalysis)
        analysis_btn.pack(fill="x", expand=True, padx=40)
        
        #the speech button - speed remark
        word_remark = tkinter.Label(self.analysis_frame, text=word_remark_text,font=("Segoe UI", 11, "italic"), fg="#AFCFF0", bg="#0B0F19")
        word_remark.pack(fill="x", expand=True)
        
        #the home button
        home = tkinter.Button(self.analysis_frame, text="HOME", font=("Segoe UI Semibold", 12),bg="#2563EB",  fg="#FFFFFF",padx=35,  command= lambda: self.home(old_frame = self.analysis_frame, new_frame_method=self.build_home_page))
        home.pack(fill="x", expand=True,padx=40)
        
        
    def eachQuestionAnalysis(self):
        #reset the current_index and the selected option in prep fr the deepSummary
        self.current_question_index.set(0)
        self.selected_option.set(self.answer_pool[0])
        print(self.answer_pool)
        #clear the analysis frame from view
        for i in self.analysis_frame.winfo_children():
            i.destroy()
        self.analysis_frame.pack_forget()
            
        #create a new frame for deep analysis
        self.deepAnalysisFrame = tkinter.Frame(self, padx=10, pady=10, bg=self.bg)
        self.deepAnalysisFrame.pack(expand=True, fill="both")
        
        #the course label
        self.course_lbl = tkinter.Label(
            self.deepAnalysisFrame, 
            text=self.selected_course.get(), 
            font=("Segoe UI", 15, "bold"), 
            bg=self.bg,
            fg="white",
            anchor="w"
        )
        self.course_lbl.pack(side="top", padx=10, anchor="nw")

        #question label
        self.quiz_questioon_label = tkinter.Label(self.deepAnalysisFrame, text=self.question_pool[self.current_question_index.get()][0], font=("Segoe UI", 12), bg=self.bg, fg="white", justify="left", wraplength= self.width - 40, pady=15)
        self.quiz_questioon_label.pack(fill="x")
        self.quiz_questioon_label.bind("<Configure>", lambda event, extra = self.quiz_questioon_label: self.configureQuestionWidth(widget=  extra, event=event))
        
        #for the options radio buttons
        self.quiz_option_frame = tkinter.Frame(self.deepAnalysisFrame, bg= self.bg)
        self.quiz_option_frame.pack(fill="x", padx=10, pady=30)
        #(1)
        self.quiz_opt_btn_1 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="A. " + self.question_pool[self.current_question_index.get()][1][0],
                value = "A",
                variable= self.selected_option,
                font=("Segoe UI", 11), 
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                disabledforeground= "white",
                activebackground=self.bg,
                activeforeground="#00ff00",
                state="disabled")
        self.quiz_opt_btn_1.pack(anchor="w", pady=5, padx=10)
        #(2)
        self.quiz_opt_btn_2 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="B. " + self.question_pool[self.current_question_index.get()][1][1],
                value = "B",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                disabledforeground= "white",
                activebackground=self.bg,
                activeforeground="#00ff00",
                state="disabled"
                )
        self.quiz_opt_btn_2.pack(anchor="w", pady=5, padx=10)
        #(3)
        self.quiz_opt_btn_3 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="C. " + self.question_pool[self.current_question_index.get()][1][2],
                value = "C",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                disabledforeground= "white",
                activebackground=self.bg,
                activeforeground="#00ff00",
                state="disabled"
                )
        self.quiz_opt_btn_3.pack(anchor="w", pady=5, padx=10)
         #(4)
        self.quiz_opt_btn_4 = tkinter.Radiobutton(
                self.quiz_option_frame,
                text="D. " + self.question_pool[self.current_question_index.get()][1][3],
                value = "D",
                variable= self.selected_option,
                font=("Segoe UI", 11),
                bg=self.bg,
                fg="white",
                indicatoron=0,
                bd=0,
                selectcolor= "#008800",
                disabledforeground= "white",
                activebackground=self.bg,
                activeforeground="#00ff00",
                state="disabled"
                )
        self.quiz_opt_btn_4.pack(anchor="w", pady=5, padx=10)
        
        #correct answer message
        self.correct_answer = tkinter.Label(self.deepAnalysisFrame, text= f"Option {self.question_pool[self.current_question_index.get()][-1].upper()} is the correct answer", fg="white", font=("Segoe UI", 11),)
        self.deepAnalysisRightAns()
        self.correct_answer.pack(fill="x", expand=True, padx=40)
        self.correct_answer.bind("<Configure>", lambda event, extra = self.correct_answer: self.configureQuestionWidth(widget=  extra, event=event))
        
        #prev, back, home, next btns replacing the former ones
        self.quiz_footer_frame = tkinter.Frame(self.deepAnalysisFrame, bg= self.bg)
        self.quiz_footer_frame.pack(fill="x", expand=True)

        #prev
        self.footer_button_prev = tkinter.Button(self.quiz_footer_frame, text="Previous", font=("Segoe UI", 11), bg="#aaaaaa", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Prev"))
        self.footer_button_prev.grid(row=0, column= 0, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(0, weight= 1)
       
        #back - to analysis frame
        self.footer_button_quit = tkinter.Button(self.quiz_footer_frame, text="Back", font=("Segoe UI", 11), bg= "#173E94", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.home(old_frame=self.deepAnalysisFrame, new_frame_method=self.loadAnalysis))
        self.footer_button_quit.grid(row=0, column= 1, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(1, weight= 1)
         
        #home
        self.footer_button_submit = tkinter.Button(self.quiz_footer_frame, text="Home", font=("Segoe UI", 11), bg="#DC2626", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.home(old_frame=self.deepAnalysisFrame, new_frame_method=self.build_home_page))
        self.footer_button_submit.grid(row=0, column= 2, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(2, weight= 1)
        
        #next
        self.footer_button_next = tkinter.Button(self.quiz_footer_frame, text="Next", font=("Segoe UI", 11), bg="#173E94", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Next"))
        self.footer_button_next.grid(row=0, column= 3, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(3, weight= 1)
        
        
        #for showimg current question index
        self.quiz_footer_second_frame = tkinter.Frame(self.deepAnalysisFrame, bg= self.bg)
        self.quiz_footer_second_frame.pack(anchor="s", pady=10, padx=10, fill="x", expand=True)
        self.current_question_footer = tkinter.Label(self.quiz_footer_second_frame, text=f"Question {self.current_question_index.get() + 1} of {int(self.selected_question_lenght.get())}", font=("Segoe UI", 14, "bold"), bg=self.bg, fg="#94A3B8")
        self.current_question_footer.pack(anchor="e")
  
    #for when a transition from a page to another need to happen
    def home(self, old_frame, new_frame_method):
        for i in old_frame.winfo_children():
            i.destroy()
        old_frame.pack_forget()
        #restart app cycle
        new_frame_method()
        

#this is to avoid the file runnning auto when import is done
if __name__ == "__main__":
    QuizApp().mainloop()