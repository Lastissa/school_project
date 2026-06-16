from tkinter import *
from tkinter import ttk,messagebox
import math

app_documentation = """
the app is splitted into two frame on the main window(i said main window cos we have other window for solving cal involving extensive equation)
the two frame contains - display and bottom

"""
mapping = {
    "*": "mul",
    "+" : "add",
     "-" : "sub",
    "/" : "div"
}
history = []
#for extra hand i migth both in cal and quiz app need and i dont want to torepeat the code like checking if something is into or float
class Utility:
    def __init__(self):
        pass
    
    def tryFloatToInt(self, value):
        try:#incase anything go wrong
            #if its int, to remove the unnnesary float
            if int(float(value)) == float(value):
                return  int(float(value))# its a int that just have a trailing .0
            return value #inditcating the number is indeed a float
        except Exception as e:
            print(f"{e} - Error main utility num to float converter in uitlity class")
            return value
    
    def clipLenght(self, value : float, lenght : int):
        try:#incase what was pass was not a number
            str_value = str(value)
            if len(str_value) <= lenght: #meaning the value is within the required lenght
                return str(value)
            
            #find the index of . so we can know wether the leght stopped on the . as just add extra one digit to it so as to avoid error
            try:
                #to check if the number is a decimal
                dot_index = str_value.index(".")
                
                if lenght == dot_index: # if there will be a trailing decimal right at the end after the first lenght have been selected
                    print("req lenght is on the decimal")
                    integer = int(str_value[:lenght])
                    if int(str_value[dot_index+1]) >= 5: #knowing wht come after the decimal so i can add one to the approx integer
                        if integer < 0: #-ve numbers
                            return f"{integer - 1}"
                        else:#=ve num
                            return f"{integer + 1}" 
                    else: 
                        return str(integer)
            except Exception as e:
                dot_index = len(str_value)  #i need it frthe exp
                print(f"{e} - clip warning - warning catch 100, ignore just a way for me to say its whole num we are dealing with")
                
            #lenght did not stop on dot, lenght is smaller compared to the value, so now clipping / approximation
            if dot_index > len(str_value): #for whole numbers, i added the dot_index on purpose at the end so this will be true for whole num
                exp = len(str_value) - lenght - 1 #i rem one again cos i am adding a one dp
                first_part = str_value[:lenght] # the : auto reduce by one
                last_value = int(str_value[lenght]) #the last value in what we need to deliver
                if last_value >= 5:
                    last_value += 1
                return first_part + f".{last_value}E{exp}"
            else:#decimals
                print({"lenght req" : lenght, "number lenght": len(str_value), "dot pos": dot_index})
                if dot_index > lenght: 
                    first_part = str_value[:lenght]
                    proper_first_part_vibe = f"{first_part[:-1]}.{first_part[-1]}" #to format the index to have a decimal form so the comversion when using the sci can be more accurate
                    exp = dot_index - lenght + 1
                    output = f"{proper_first_part_vibe}E{exp}"
                    return output
                elif dot_index < lenght:
                    needed_part = str_value[:lenght+2] #i add 2 cos the : will auto reduce it and i need to get one last value for the incrementation
                    first_part = needed_part[:-1] #rem the last part cos i nned it for approx
                    toAdd = 0
                    #check the decimal place of the last value so we can either increment it or leave it
                    place_value_of_last_index = len(first_part)
                    place_value_of_last_index = place_value_of_last_index - dot_index - 1 # this shows how far the last index from need is from the dot
                    if int(needed_part[-1]) >= 5:
                        toAdd += 1
                    #i noticed an error, if the ending num is 9, there is an error with the adding od +1 so i need to fix it here 
                    if float(needed_part[-1]) == 9:
                        print("issue almost caued as the ending value is 9")
                        return first_part # this way the error will not even pop up to begin with cos the necxt few line will nt be reached
                    denominator = int(f"{toAdd}{"0"*place_value_of_last_index}") # had to place it like this to catch div by zero error
                    if denominator == 0:
                        output = first_part
                    else:
                        output = float(first_part) + 1/denominator
                        output = str(output)[:6] #had to put the [] cos python itself fall my hand sometime for exampke  pi * 8
                    output = output
                    
                    return output
        except Exception as e:
            print(f"{e} - Error main clip function")
            return value
    def isErrorPresent(self, stringVar : StringVar):#for checking wether error is in the display
        if "syntax error" in stringVar.get() or "Limit Error" in stringVar.get() or "infinity" in stringVar.get() or "inf" in stringVar.get():
            stringVar.set("0")
            return True
        else:
            return False
    def isAddSubMulDivPresent(self, stringVar : StringVar):
        if "add" in stringVar.get() == "sub" == stringVar.get() or "mul" == stringVar.get() or "div" == stringVar.get():
            stringVar.set("0")
            return True
        else:
            return False
    def tryEval(self, StringVar : StringVar):
        try:
            
            StringVar.set(str(eval(StringVar.get())))
            return True
        except Exception as e:
            print(f"unable to eval --- {e}")
            return False
        
    def quadratic_solving(self, method_var: StringVar,x2:str, x: str, c: str, stringVar : StringVar):
        for_faster_clipping = lambda number : Utility().clipLenght(Utility().tryFloatToInt(number), 3)
        x2_clip = for_faster_clipping(x2) #String
        x_clip =  for_faster_clipping(x)#String
        c_clip =  for_faster_clipping(c)#String
        if method_var.get().upper() == "FORMULA METHOD":
            try:
                
                #breakdown of working
                first0 = -1 * float(x) #-b
                first1 = float(x)**2 #b ^ 2
                second0 = float(x2) * 4*float(c) # 4ac
                second1 = 2*float(x2) # 2a - denominator
                sqrt = math.sqrt(first1 - second0)
                final_num_negative = (first0 - sqrt ) / second1
                final_num_positive = (first0 + sqrt ) / second1
                print([final_num_negative, final_num_positive])
                #use the formual method
                result =  f"""
USING FORMULA METHOD
=> -b +/- √(b² - 4ac)   / 2a
where a = {x2_clip}, b = {x_clip} and c = {c_clip}
replacing the value => 
numerator = {for_faster_clipping(first0)} ± √({x_clip}² - 4*{x2_clip}*{c_clip})
denominator = 2*{x2_clip}

simplify => {for_faster_clipping(first0)} ± √{for_faster_clipping(first1 - second0)} / {for_faster_clipping(second1)}
simplify => {for_faster_clipping(first0)} ± {for_faster_clipping(sqrt)} / {for_faster_clipping(second1)}
X =  {for_faster_clipping(first0)} + {for_faster_clipping(sqrt)} / {for_faster_clipping(second1)}
or 
X = {for_faster_clipping(first0)} - {for_faster_clipping(sqrt)} / {for_faster_clipping(second1)}

result => x = {for_faster_clipping(final_num_negative)} OR {for_faster_clipping(final_num_positive)}

x = {for_faster_clipping(final_num_negative)},{for_faster_clipping(final_num_positive)}
"""
                return stringVar.set(result)
            except Exception as e:
                print(f"{e} -- quad form method no work" )
                if ZeroDivisionError:
                    result = "Zero Spotted in the wrong place!!!"
                    return stringVar.set(result)
                result = "Invalid inputs spotted!!!"
                return stringVar.set(result)
                
                
        elif method_var.get().strip().upper() == "FACTORIZATION METHOD":
            result =  "Stil in progress, explore other method."
            return stringVar.set(result)
            # try:
                # product_of_two_num = for_faster_clipping((float(c)*float(x2)))
        else:
            result = "Error: Method not selected"
            return stringVar.set(result)
    def simultaneous_solving(self, method_var: StringVar, x1 : str, y1 : str, z1 : str, x2: str, y2 : str, z2: str,stringVar : StringVar):
        for_faster_clipping = lambda number : Utility().clipLenght(Utility().tryFloatToInt(number), 3)
        x1_clip = for_faster_clipping(x1)
        y1_clip = for_faster_clipping(y1)
        z1_clip = for_faster_clipping(z1)
        x2_clip = for_faster_clipping(x2)
        y2_clip = for_faster_clipping(y2)
        z2_clip = for_faster_clipping(z2)
        
        if method_var.get().upper() == "SUBSTITUTION METHOD":
            try:
                sub_of_the_form = ["unknown", "unknown"] #[the actual value, the index wether first equ or second equ]
                if float(x1) != 0:
                    sub_of_the_form = [float(x1), 0]
                elif float(y1) != 0:
                    sub_of_the_form = [float(y1), 0]
                elif float(x2) != 0:
                    sub_of_the_form = [float(x2), 1]
                elif float(y2) != 0:
                    sub_of_the_form = [float(y2), 1]
                    
                if sub_of_the_form[1] == 0 :#the order still stay cos i got the subject from the first equ
                    first_equation = [float(x1), float(y1), float(z1)]
                    second_equation = [float(x2), float(y2), float(z2)]
                elif  sub_of_the_form[1] == 1 :#the order flip cos i got the subject from the second equ
                    first_equation = [float(x2), float(y2), float(z2)]
                    second_equation = [float(x1), float(y1), float(z1)]
                else:
                    result = "You dey whine, how can all value be zero"
                    return stringVar.set(result)

                
                #i have gotten the order right, now solving
                #for flipping symbol
                flip = {"+": "-", "-": "+"}
                #get the symbol infront of each value
                first_equation_symbol = []
                second_equation_symbol = []   
                for i in first_equation:
                    if str(i)[0] == "-": first_equation_symbol.append("-")
                    else:first_equation_symbol.append("+")  
                          
                for i in second_equation:
                    if str(i)[0] == "-": second_equation_symbol.append("-")
                    else:second_equation_symbol.append("+")        
                
                #first, try to get the 3rd equ
                if first_equation[0] == 1: # since its one , dont do div
                    third_equ = f"""{flip[first_equation_symbol[1]]}{for_faster_clipping(abs(first_equation[1]))}y {first_equation_symbol[2]} {for_faster_clipping(abs(first_equation[2]))}""" #+y + z vibes
                    continutation = f"""x = {third_equ} --equation 3
Sub equation(3) for x in equation {(sub_of_the_form[1] + 1)%2+1}
=> {for_faster_clipping(second_equation[0])}({third_equ.strip()}) {second_equation_symbol[1]} {for_faster_clipping(abs(second_equation[1]))}y = {for_faster_clipping(second_equation[2])}"""

                    remove_bracket = [second_equation[0] * first_equation[1]*-1, second_equation[0]*first_equation[2]] # [x2(y1), x2(z1)]
                    continutation = f"""
{continutation}
=> {for_faster_clipping((remove_bracket[0]))} + {for_faster_clipping(remove_bracket[1])}  {second_equation_symbol[1]} {for_faster_clipping(abs(second_equation[1]))}y = {for_faster_clipping(second_equation[2])}
"""
                    simplify = eval(f"{for_faster_clipping((remove_bracket[0]))} + {for_faster_clipping(remove_bracket[1])}")
                    continutation = f"""{continutation}
=> {for_faster_clipping(simplify)} {second_equation_symbol[1]} {for_faster_clipping(abs(second_equation[1]))}y = {for_faster_clipping(second_equation[2])}
"""                 
                    continutation = f"""
{continutation}
=> {for_faster_clipping(second_equation[1])}y =  {for_faster_clipping(second_equation[2])} + {simplify * -1}
"""
                    y_result = eval(f"{second_equation[2]} + {self.tryFloatToInt(simplify * -1)}")
                    continutation = f"""
{continutation}
=> y = {for_faster_clipping(y_result)}                  
"""
                    continutation =f"""
{continutation}
=> sub {for_faster_clipping(y_result)} for y in equation 3
x = {for_faster_clipping(y_result * eval(f"{flip[first_equation_symbol[1]]}{abs(first_equation[1])}"))}
"""
                
                elif first_equation[0] == 0:#this mean, the 3rd equ will just use y and the other
                    third_equ = f""""""
                else: # a proper sub method with div and all
                    pass
                    pass
                
                result = f"""
USING SUBSTITUTION METHOD
from equation {sub_of_the_form[1] + 1} =>
make x the subject of the formula
{continutation}
"""

                return stringVar.set(result)
            except Exception as e:
                print(e)
                result = "Errror, please check other method"
                return stringVar.set(result)
        elif method_var.get().upper() == "ELIMINATION METHOD":
            try:
                result = """
    USING ELIMINATION METHOD
    """
                
                return stringVar.set(result)
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "please check other method")
        
        else:
            print("no method choosen")
            result = "Please select a method"
            return stringVar.set(result)    
    def ap_solving(self, method_var: StringVar, nth_term : str, first_term : str, diff : str):
        if method_var.get().upper() == "FIND N-TH TERM":
            pass
        
   
   
class CalByOpe(Tk):
    def __init__(self, width_pos, height_pos):
        super().__init__()
        self.is_shift_on = False #for knowing when shift is active
        self.max_calulator_view_lenght = 5 #for the max amoutn of operation the cal is allowed to show
        self.current_display_content =  StringVar(master = self, value="0") #For holding the current text in display
        self.current_meta_data_to_display = StringVar(master = self, value="0") #For the current mode e.g SCI, DEC, FRA, ABS
        self.current_right_mini_info = StringVar(master = self, value="")
        self.ans_key_value = StringVar(master = self, value="0") #for updating the value the ANS key will get
        self.phi = 22/7
        self.e = math.e
        self.geometry(f"400x700+{width_pos}+{height_pos}")
        self.title("Group 1 calculator")
        self.config(bg = self.colors()["bg"])
        self.display()
        self.btns()
        
        

    
    def display(self):
        #for display content
       
        # Top Display Area Frame
        self.display_frame = Frame(self, bg= self.colors()["btn-bg-number"])
        self.display_frame.pack(fill="x", padx=15, pady=15)
        #to display content
        display_content = Label(self.display_frame, textvariable= self.current_display_content, font=("Segoe UI", 32, "bold"),anchor="e", foreground= self.colors()["btn-fg"],bg= self.colors()["btn-bg-number"])
        display_content.pack(expand=True, fill="both", padx=10, pady=10)
        #to display meta data
        metadata = Label(self.display_frame, textvariable= self.current_meta_data_to_display, font=("Consolas", 8), foreground= self.colors()["btn-fg"], bg= self.colors()["btn-bg-number"])
        metadata.pack(anchor="sw")
        rightMiniInfo = Label(self.display_frame, textvariable= self.current_right_mini_info, font=("Consolas", 10), foreground= self.colors()["btn-fg"], bg= self.colors()["btn-bg-number"])
        rightMiniInfo.pack(anchor="e", pady=3)
        
    
    def display_wipeout(self):
        for i in self.display_frame.winfo_children():
            i.destroy()
            
    def btns(self):
        if self.is_shift_on:
            btn =  [
                    ["SHIFT", "Sciⁿ","Fra", "bin", "10ⁿ"],    #1st
                    # ["∫X", "∫∫X", "nPr",   "//"],   #2nd
                    ["sin⁻¹", "cos⁻¹","tan⁻¹" ,"Ln", "Antilog"],#3rd
                    ["√", "∛", "ʸ√", "x!", "|x|"],         #4th
                    ["π", "ClrA",  "M+", "M-", "MC"],            #5th
                    ['7', '8', '9', 'Del', "AC"],   #6th
                    ['4', '5', '6',  '*',   "/"],   #7th
                    ['1', '2', '3',  '+',   "-"],   #8th
                    ['0', '.', 'Ans', "="],  #9th
                    ["History", "Advance"]          #10th
                    ]
        else:
            btn = [
                ["SHIFT", "Sciⁿ","Fra",  "bin", "10ⁿ"],     #1st
                # ["y'", "y''", "nCr", "//"],       #2nd
                ["Sin", "Cos", "Tan", "ln", "Log"],   #3rd
                ["x²", "x³", "xⁿ", "x!", "+/-"],       #4th
                ["π", "ClrA", "M+", "M-", "MC"],          #5th
                ['7', '8', '9', 'Del', "AC"],   #6th
                ['4', '5', '6',  '*',   "/"],   #7th
                ['1', '2', '3',  '+',   "-"],   #8th
                ['0', '.', "Ans", "="],    #9th
                ["History", "Advance"]          #10th
                ]
        self.btn_list = btn
        #btn frame
        self.btn_frame = Frame(self, bg = self.colors()["bg"])
        self.btn_frame.pack(fill="both", padx=15, pady=15, expand=True)
        #buttons
        for index, row in enumerate(btn):
            for inner_index, column in enumerate(row):
                #for targeting numbers
                try:
                    int(column.strip()) + 2 #if this works, it show its a number
                    
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI semibold", 14), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-number"], command= lambda t=column:self.operationNumber(digit=t))
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                    continue
                except:
                    pass
                #for targeting history and advance btn
                if column.upper() == "HISTORY":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-special"])
                    buttons.grid(row= index, column=0, padx=3, pady=3, sticky= "nsew", columnspan=2)
                    continue
                elif column.upper() == "ADVANCE":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-special"], command= self.operationSpecial)
                    buttons.grid(row= index, column=2, padx=3, pady=3, sticky= "nsew", columnspan=3)
                    continue
                elif column == "=":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI ", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-special"],  command = self.operationEQUALTO)
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew", columnspan=2)
                    continue
                elif column.strip() == "Del" or column.strip() ==  "AC" or column == "ClrA":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI semibold", 14), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-danger"], command= lambda t=column : self.operationAC(t))
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                    continue
                elif column.strip() =="M+" or column.strip() =="M-" or column.strip() =="MC":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI ", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-m"] )
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                    continue
                elif  "Sci"  in column.strip() or "Fra"  in column.strip() or "bin"  in column.strip(): 
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI ", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-mode"], command=lambda t=column: self.operationMode(t))
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                    continue
                elif column.strip() == "SHIFT":
                    buttons = Button(self.btn_frame, text= column, font=("Segoe UI ", 14, "bold"), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-m"], command = self.operationShift)
                    buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                    continue
                
                #normal symbol btns 
                command = None #rm soon
                if column == ".":
                    command =self.operationDot
                elif column == "π":
                    command = self.operationPhi
                elif column == "e":
                    command = self.operationEuler
                elif column == "+" or column == "-" or column =="*" or column == "/":
                    command = lambda t=column : self.operationAdd_Sub_Mul_Div(t)
                elif column == "+/-":
                    command = self.operationPlusMinus
                elif column == "|x|" or column == "x!" or column == "xⁿ" or column == "x³" or column == "x²" or column == "√" or column == "∛" or column == "ʸ√":
                    command = lambda t=column : self.xRelated(t)
                elif column == "10ⁿ":
                    command = self.operationExp
                elif column == "Sin" or column == "Cos" or column == "Tan" or column == "sin⁻¹" or column == "cos⁻¹" or column == "tan⁻¹":
                    command = lambda t=column : self.operationTRRIG(t)
                elif column == "Ans":
                    command = self.operationANS
                    
                buttons = Button(self.btn_frame, text= column, font=("Segoe UI semibold", 14), bd=0, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-symbol"], command= command)
                buttons.grid(row= index, column=inner_index, padx=3, pady=3, sticky= "nsew")
                
                # Give the grid cell responsive 'weight' properties
                self.btn_frame.grid_rowconfigure(index, weight=1)
                self.btn_frame.grid_columnconfigure(inner_index, weight=1)
  
    def btns_wipeout(self):
        self.btn_frame.pack_forget()
    
    
    #for the advance ui
    def advance(self):
        self.advance_frame = Frame(self, bg = self.colors()["bg"])
        self.advance_frame.pack(fill="both", expand=True, padx=10, pady=15)
        
        advance_frame_btns_name = [
            # "Solving Equation With Solution",
            "Quad\nEqu",
            "Sim\nEqu",
            "AP",#lcm, hcf , factors
                ]
        def advance_back():
            self.advance_frame.pack_forget()
            advance_frame_back_btn.pack_forget()
            self.display()
            self.btns()
            
        #The back  for going to the cal page
        advance_frame_back_btn = Button(self, text = "Back", font=("Segoe UI", 14, "bold") , foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-danger"], anchor="n", bd= 0,command = advance_back) 
        advance_frame_back_btn.pack(anchor = "s", fill = "x",  padx = 3, pady = 3,expand = True)
       
        #its children 2 (button and displlay)
        advance_frame_header = Frame(self.advance_frame,bg = self.colors()["bg"])
        advance_frame_header.pack(fill = "x", expand = True, anchor = "n")
        advance_frame_body = Frame(self.advance_frame, bg = self.colors()["bg"])
        advance_frame_body.pack(fill = "both", expand = True)

        # the children content- for header
        for  index, name in enumerate(advance_frame_btns_name):
            advance_frame_header_child = Button(advance_frame_header,text = name, font=("Segoe UI", 17, "bold"), bg= self.colors()["btn-bg-number"], fg = "white",bd = 0, command= lambda  t=name : set_mode_life(t) )
            advance_frame_header_child.grid(row = 1, column = index, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_header.grid_columnconfigure(index, weight = 1)
            advance_frame_header.grid_rowconfigure(1, weight= 1)
        
        # the children function content- for body
        def quad_equ_active():
            x2_var = StringVar(master = self, value="1")
            x_var = StringVar(master = self, value="1")
            c_var = StringVar(master = self, value="-1")
            solution_var = StringVar(master = self, value="Awaiting Order")
            method_selector_var = StringVar(master = self, value="What method do you prefer?")
            
            info_text = Label(advance_frame_body, text="Quadratic Equation", fg= "white", bg = self.colors()["bg"], font=("Segoe UI", 13, "bold"),)
            x2_coefficient_input = Entry(advance_frame_body, width=5, textvariable=x2_var, font=("Consolas", 12, "bold"))
            x2_coefficient_label = Label(advance_frame_body, text = "x²", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white", anchor="w")
            x_coefficient_input = Entry(advance_frame_body, width=5, textvariable=x_var, font=("Consolas", 12, "bold"))
            x_coefficient_label = Label(advance_frame_body, text = "X", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white", anchor="w")
            c_coefficient_input = Entry(advance_frame_body, width=5, textvariable= c_var, font=("Consolas", 12, "bold"))
            c_coefficient_label = Label(advance_frame_body, text = "C", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white", anchor="w")
            method_selector = ttk.Combobox(advance_frame_body, values= ["formula method", "factorization method"], state="readonly", textvariable= method_selector_var)
            solve_button = Button(advance_frame_body, bd = 0, bg= self.colors()["btn-bg-m"], fg= "white", text="SOLVE", command=lambda: Utility().quadratic_solving(method_selector_var ,x2_var.get(), x_var.get(), c_var.get(),solution_var))
            solution_label = Label(advance_frame_body, textvariable=solution_var, font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white", anchor="w")
            
            
            
            #locking up the information into place
            info_text.grid(column=0, row=0, columnspan=8, sticky="nsew", pady=6)
            advance_frame_body.grid_rowconfigure(3, weight = 1,)
            advance_frame_body.grid_columnconfigure(0, weight = 0)
            
            x2_coefficient_input.grid(row = 1, column= 0,sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            x2_coefficient_label.grid(row=1, column=1, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(1, weight = 1)
            
            x_coefficient_input.grid(row = 1, column= 2, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(2, weight = 1)
            
            x_coefficient_label.grid(row = 1, column = 3, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(3, weight = 1)
            
            c_coefficient_input.grid(row = 1, column= 4,sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(4, weight = 1)
            
            c_coefficient_label.grid(row = 1, column =5, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(5, weight = 1)

            method_selector.grid(row=2,column =0, sticky = "nsew", padx  = 3 , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            solve_button.grid(row=3,column =0, sticky = "nsew", padx  = 6 , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(3, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            solution_label.grid(row=4,column =0, sticky = "nsew" , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(4, weight = 5)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            

        def sim_equ_active():
            x1_var = StringVar(master = self, value="0")
            y1_var = StringVar(master = self, value="0")
            z1_var = StringVar(master = self, value="0")
            x2_var = StringVar(master = self, value="0")
            y2_var = StringVar(master = self, value="0")
            z2_var = StringVar(master = self, value="0")
            solution_var = StringVar(master = self, value="Awaiting Order")
            method_selector_var = StringVar(master = self, value="What method do you prefer?")
            
            
            info_text = Label(advance_frame_body, text="Simultanous Equation", fg= "white", bg = self.colors()["bg"], font=("Segoe UI", 13, "bold"),)
            x1_coefficient_label = Label(advance_frame_body, text = "x =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            x1_coefficient_input = Entry(advance_frame_body, width=5, textvariable=x1_var, font=("Consolas", 12, "bold"))
            y1_coefficient_label = Label(advance_frame_body, text = "y =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            y1_coefficient_input = Entry(advance_frame_body, width=5, textvariable=y1_var, font=("Consolas", 12, "bold"))
            z1_coefficient_label = Label(advance_frame_body, text = "z =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            z1_coefficient_input = Entry(advance_frame_body, width=5, textvariable= z1_var, font=("Consolas", 12, "bold"))
            x2_coefficient_label = Label(advance_frame_body, text = "x =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            x2_coefficient_input = Entry(advance_frame_body, width=5, textvariable=x2_var, font=("Consolas", 12, "bold"))
            y2_coefficient_label = Label(advance_frame_body, text = "y =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            y2_coefficient_input = Entry(advance_frame_body, width=5, textvariable=y2_var, font=("Consolas", 12, "bold"))
            z2_coefficient_label = Label(advance_frame_body, text = "z =", font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white")
            z2_coefficient_input = Entry(advance_frame_body, width=5, textvariable= z2_var, font=("Consolas", 12, "bold"))
            method_selector = ttk.Combobox(advance_frame_body, values= ["substitution method", "elimination method"], state="readonly", textvariable= method_selector_var)
            solve_button = Button(advance_frame_body, bd = 0, bg= self.colors()["btn-bg-m"], fg= "white", text="SOLVE", command=lambda: Utility().simultaneous_solving(method_selector_var ,x1_var.get(), y1_var.get(),z1_var.get(), x2_var.get(), y2_var.get(), z2_var.get(),solution_var))
            solution_label = Label(advance_frame_body, textvariable=solution_var, font=("Consolas", 12, "bold"), bg=self.colors()["bg"], fg= "white", anchor="w")
            
            
            
            #locking up the information into place
            info_text.grid(column=0, row=0, columnspan=8, sticky="nsew", pady=6)
            advance_frame_body.grid_rowconfigure(5, weight = 1,)
            advance_frame_body.grid_columnconfigure(0, weight = 0)
            
            x1_coefficient_label.grid(row = 1, column = 0, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            x1_coefficient_input.grid(row = 1, column= 1, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(1, weight = 1)
            
            y1_coefficient_label.grid(row = 1, column = 2, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(2, weight = 1)
            
            y1_coefficient_input.grid(row = 1, column= 3, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(3, weight = 1)
            
            z1_coefficient_label.grid(row = 1, column = 4, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(4, weight = 1)
            
            z1_coefficient_input.grid(row = 1, column= 5, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(5, weight = 1)
            
            #begin of second equ
            x2_coefficient_label.grid(row = 2, column = 0, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            x2_coefficient_input.grid(row = 2, column= 1, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(1, weight = 1)
            
            y2_coefficient_label.grid(row = 2, column = 2, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(2, weight = 1)
            
            y2_coefficient_input.grid(row = 2, column= 3, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(3, weight = 1)
            
            z2_coefficient_label.grid(row = 2, column = 4, sticky = "nsew", padx  = 3 , pady = 3)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(4, weight = 1)
            
            z2_coefficient_input.grid(row = 2, column= 5, sticky = "nsew", padx  = 3 , pady = 3),
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(5, weight = 1)
            
            method_selector.grid(row=3,column =0, sticky = "nsew", padx  = 3 , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            solve_button.grid(row=4,column =0, sticky = "nsew", padx  = 6 , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(5, weight = 1)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
            solution_label.grid(row=5,column =0, sticky = "nsew", padx  = 3 , pady = 3, columnspan=6)
            advance_frame_body.grid_rowconfigure(5, weight = 5)
            advance_frame_body.grid_columnconfigure(0, weight = 1)
            
        
        def ap_active():
            pass
        
        #for setting a  mode live
        def set_mode_life(t):
            for i in advance_frame_body.winfo_children():
                i.destroy()
            if t == advance_frame_btns_name[0]: #quadratic mode:
                quad_equ_active()
            elif t == advance_frame_btns_name[1] : #simulataneous
                sim_equ_active()
            elif t == advance_frame_btns_name[2] : #ap
                ap_active()
            else:
                print("nthing here")
                pass
                
            
        
        # for index, name in enumerate(advance_frame_btns_name):
        #     if name == "back":
        #         advance_frame_btns =  Button(self.advance_frame,text= name,  foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-danger"], anchor="n", bd= 0)
        #         advance_frame_btns.grid(row=index, sticky="nsew", padx= 3, pady=3)
        #         self.advance_frame.grid_rowconfigure(index, weight=1)
        #         self.advance_frame.grid_columnconfigure(0, weight=1)
        #         continue
            
        #     advance_frame_btns = Button(self.advance_frame,text= name, foreground= self.colors()["btn-fg"], background= self.colors()["btn-bg-symbol"])
        #     advance_frame_btns.grid(row=index, padx=3, pady=3, sticky="nsew")
        #     self.advance_frame.grid_rowconfigure(index, weight=1)
        #     self.advance_frame.grid_columnconfigure(0, weight=1)


            

    def colors(self):
        return{
    'bg': "#111135",
    "btn-bg-number"   : "#1F1F6E" ,            
    'btn-bg-symbol': "#232381",
    'btn-bg-danger': "#b94d4d",  
    'btn-bg-mode': "#3B3B9E",    
    "btn-bg-special" : "#0000FF",
    "btn-fg": "#e0e0e0",
    "btn-bg-m": "#3A6D18",
}
        #Operations
    def operationShift(self):
        current_state = self.current_meta_data_to_display.get().lower().split("shift")
        #this mean shift exist in the text before so removing it now
        if len(current_state)> 1:
            self.current_meta_data_to_display.set((" ".join(current_state)).strip())
            self.is_shift_on = False
            self.btns_wipeout()
            self.btns()
        else:
            self.current_meta_data_to_display.set(self.current_meta_data_to_display.get() + " shift")
            self.is_shift_on = True
            self.btns_wipeout()
            self.btns()

    def operationDot(self):
        Utility().isErrorPresent(self.current_display_content)
        current_value = self.current_display_content.get()
        if "." in current_value:
            pass
        else:
            self.current_display_content.set(current_value + ".")
            
    #for appening to what is already in the current_value_display_content
    def operationNumber(self, digit):
        Utility().isErrorPresent(self.current_display_content)
        old_digit = self.current_display_content.get()
        try:
            if int(old_digit) == 0:
                old_digit = ""
        except:
            pass    
        
        self.current_display_content.set(old_digit + digit)


    #for clearing all the value in current_display_content or removing one from it
    def operationAC(self, digit):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        
        if digit == "ClrA":
            self.ans_key_value.set("0")
            self.current_display_content.set("0")
        elif digit.strip() == "Del":
            old_value = self.current_display_content.get()
            if len(old_value) == 1:
                self.current_display_content.set("0")
            elif Utility().isErrorPresent(self.current_display_content) :
                pass         
            else:
                self.current_display_content.set(old_value[0:-1])
            #check if fraction is active
            if "fraction" in self.current_meta_data_to_display.get():
                self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("fraction"))) #for removing sci from the meta data
            #check if the last text is "...b",
            if old_value[-1] == "b":
                self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("bin"))) #for removing bin from the meta data
            #check if the last text is "...E",
            if old_value[-1] == "E": 
                self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("sci"))) #for removing sci from the meta data

                

            
        elif digit.strip() == "AC":
            self.current_display_content.set("0")
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("bin"))) #for removing bin from the meta data
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("sci"))) #for removing sci from the meta data
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("div"))) #for removing div from the meta data
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("add"))) #for removing add from the meta data
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("mul"))) #for removing mul from the meta data
            self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split("sub"))) #for removing sub from the meta data

        #if its not Del or AC or ClrA
        else:
            self.current_display_content.set("Error - 001")
        
        

    def operationMode(self, digit):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        #check if what we are getting is a number(or some special chars), if not - ignore the keypress
        try:
            current_value = self.current_display_content.get()
            #for standard form presentation
            if "Sci"  in digit:
                #check if sci exist in the mode
                if "sci" in self.current_meta_data_to_display.get() or "E" in current_value:
                    #try to return it back to normal decimal
                    try:
                        #remove the sci and return back to normal decimal
                        current_value = self.current_display_content.get()
                        new_value = float(current_value)                        
                        new_value = Utility().clipLenght(float(new_value), self.max_calulator_view_lenght)
                        self.current_display_content.set(new_value)
                        self.current_meta_data_to_display.set(" ".join(self.current_meta_data_to_display.get().split("sci")))
                    except Exception as e:
                        print(f"Error -3 -- {e}")
                        
                        
                else:
                    exp = 0 #exponent
                    mantissa = float(current_value)
                    while abs(mantissa) >= 10:
                        mantissa /= 10 #slashing the mantissa by 10
                        exp += 1 # increasing the exponent
                    mantissa = str(mantissa) #converting the result back to string
                    self.current_display_content.set(f"{mantissa[:5]}E{exp}")
                    #add sci to the mode cos its not there before
                    self.current_meta_data_to_display.set(self.current_meta_data_to_display.get() + " sci")
            
            #For fraction form presentation
            elif "Fra"  in digit:
                try:
                    #check if "." exist in current 
                    if "." not in current_value:
                        print("invalid decimal value")             
                    number_after_decimal_count = len(current_value.split(".")[1])
                    fraction_numerator = list(current_value)
                    fraction_numerator.remove(".")
                    fraction_numerator = int("".join(fraction_numerator))
                    fraction_denominator = int("1"+ "0"*number_after_decimal_count)
                    gcd = math.gcd(fraction_numerator, fraction_denominator)
                    output = f"{int(fraction_numerator/gcd)}/{int(fraction_denominator/gcd)}"
                    self.current_display_content.set(output)
                    #setting the mode
                    self.current_meta_data_to_display.set(self.current_meta_data_to_display.get() + " fraction")
                    
                except Exception as e:
                    print(f"{e} = opeyemi")
            
            #For binary form presentation
            elif "bin"  in digit:
                #check if bin exist
                
                if len(self.current_meta_data_to_display.get().split("bin")) > 1:
                    pass
                else:
                    #converting values to bin               
                    int_bin = bin(int(current_value.split(".")[0])) #convert the int side first since the bin method only support integers
                    decimal_bin = "" #holder for holding the bin of the decimal as i cal it using the *2 remainder style
                    try:
                        decimal_part_of_current_value = float("0."+ current_value.split(".")[1])
                    except:
                        decimal_part_of_current_value = 0.0#incase what the user input in is an integer
                    check_infinite = []
                    output = ""
                    while True:
                        if check_infinite.count(str(decimal_part_of_current_value)) > 1: # for checking if the float repeat since sometimes, som decinal cannot be converted to binary
                            output = "infinity"
                            break
                        decimal_part_of_current_value = decimal_part_of_current_value * 2 #doubling the decinal part so as to split the int and mantissa
                        
                        decimal_bin += str(decimal_part_of_current_value).split(".")[0] #taking off the int to add to the mantissa bin of our final ressult bin
                        if decimal_part_of_current_value == int(decimal_part_of_current_value):
                            output = f"{int_bin}.{decimal_bin}"
                            break
                        check_infinite.append(str(decimal_part_of_current_value))
                        decimal_part_of_current_value = float("0." + str(decimal_part_of_current_value).split(".")[1]) #eremove the int so as we can keep dealing with the mantissa
                    self.current_display_content.set(output)

                    #setting the mode
                    self.current_meta_data_to_display.set(self.current_meta_data_to_display.get() + " bin")
                    
        except Exception as e:
            print(f"exception : {e}")
            pass #This mean we did not get a float value
    
    def operationAdd_Sub_Mul_Div(self, digit):
        #to clear off the content in the right mini
        if "shift" in self.current_meta_data_to_display.get():
            self.current_meta_data_to_display.set("shift")
        else:
            self.current_meta_data_to_display.set("")
        
        #check if binary is active, if so, raise a messagebox saying not allowed
        if "bin" in self.current_meta_data_to_display.get():
            #return it back to decimal
            self.current_display_content.set(str(int(self.current_display_content.get().split(".")[0], 2)))
            self.current_right_mini_info.set(digit)
            self.current_meta_data_to_display.set(("".join(self.current_meta_data_to_display.get().split("bin"))).strip()) #for removing bin from the meta data
            return
        elif "sci" in self.current_meta_data_to_display.get():
             self.current_right_mini_info.set(digit)
             self.current_display_content.set(str(float(self.current_display_content.get())))
             self.current_meta_data_to_display.set(("".join(self.current_meta_data_to_display.get().split("sci"))).strip()) #for removing sci from the meta data
             return
        elif "fraction" in self.current_meta_data_to_display.get():
            self.current_right_mini_info.set(digit)
            self.current_display_content.set(str(eval(self.current_display_content.get())))
            self.current_meta_data_to_display.set(("".join(self.current_meta_data_to_display.get().split("fraction"))).strip()) #for removing sci from the meta data
            return
        
        # #This wont affect the workflow of what will happen nxt
        # #if the button is nt hot and active (not in right mini infot) but was pressed before adn its a member is here, still perform its operation but silently
        # if "add" in self.current_meta_data_to_display.get() or "sub" in self.current_meta_data_to_display.get() or "mul" in self.current_meta_data_to_display.get() or "div" in self.current_meta_data_to_display.get():
        #     if "sub" in self.current_display_content.get():
        #         self.ans_key_value.set(f"self.ans_key_value.get()-{self.current_display_content.get()}")
        #     elif "mul" in self.current_display_content.get():
        #         self.ans_key_value.set(f"self.ans_key_value.get()*{self.current_display_content.get()}")
        #     elif "div" in self.current_display_content.get():
        #         self.ans_key_value.set(f"self.ans_key_value.get()/{self.current_display_content.get()}")
        #     elif "add" in self.current_display_content.get():
        #         self.ans_key_value.set(f"self.ans_key_value.get()+{self.current_display_content.get()}")

        
        
        #this mean the button have been pressed before so do the needful
        if digit in self.current_right_mini_info.get():
            old_ans = self.ans_key_value.get()
            current_val = self.current_display_content.get()
            expression = old_ans + digit + current_val
            result = eval(expression)
            print("button pressed before")
            print(expression)
            result = Utility().tryFloatToInt(float(result))
            self.ans_key_value.set(str(result)) #update the answer stringvar
            self.current_display_content.set(result) #update the display too
            self.current_meta_data_to_display.set(mapping[digit])
            return
        
        
        # elif mapping[digit] in self.current_meta_data_to_display.get():
        #     print("the button is active in meta")
        #     #when  expression is going to happen 
        #     #tht digit dey there, so perform operation with collecting result from the ans 
        #     new_value = eval(f"{float(self.ans_key_value)}{digit}{float(self.current_display_content.get())}") #operating the ans + new value
        #     new_value = Utility().tryFloatToInt(new_value) #cleaning it
        #     new_value = Utility().clipLenght(new_value, self.max_calulator_view_lenght)
        #     self.ans_key_value = str(new_value) # setting the new ans key
        #     self.current_right_mini_info.set("")#since we are done, clear
        #     self.current_meta_data_to_display.set("".join(self.current_meta_data_to_display.get().split(mapping[digit])).strip())
        #     self.current_display_content.set(new_value)
        
        #first key press
        else:
          
            #make sure its a number that can be solved and set the ans key to the value collected
            try:
                tester = float(self.current_display_content.get()) + 2.6 # to check if its a num that can be solved
                self.ans_key_value.set(self.current_display_content.get())#Overide the ans value with this new one
                # expression = self.ans_key_value.get()+digit+self.current_display_content.get()
                
                self.current_right_mini_info.set(digit) #set the digit in the right
                self.current_meta_data_to_display.set(mapping[digit]) #set it in meta data
                # self.ans_key_value.set(str(eval(expression))) #update the ans
                print("first key press")
                print(self.ans_key_value.get())
                self.current_display_content.set("0") # clear the currrent content
            except Exception as e:
                print(f"Error {e}- Not a number that can be solved come check, rare to show -opeyemi")
    
    def operationPhi(self):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        if self.current_display_content.get().strip() == "0":
            self.current_display_content.set("π")
        elif self.current_display_content.get()[-1] == "π":
            pass
        else:
            self.current_display_content.set(self.current_display_content.get() + "π")
    
    def operationEuler(self):
        pass
    
    def operationPlusMinus(self):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        #check if any key that is not a number is present
        proceed = True
        for i in self.btn_list:
            for j in i:
                
                if j == "-":#create special treatment for -
                    continue
                try:
                    int(j.strip())
                except:
                    print(j)
                    #if any non number is in the current_display, dont allow the button to do anything
                    if j in self.current_display_content.get():
                            proceed = False
                
        
        if proceed:
            current_value = self.current_display_content.get()
            if current_value[0] == "-":
                self.current_display_content.set(current_value[1:])
                self.ans_key_value.set(current_value[:1])
            else:
                self.current_display_content.set("-" + current_value)
                self.ans_key_value.set("-" + current_value)
         
    def xRelated(self, digit):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        #try to eval the current values
        Utility().tryEval(self.current_display_content)
        
        #check if any key that is not a number is present
        proceed = True
        for i in self.btn_list:
            for j in i:
                try:
                    int(j.strip())
                except:
                    #special weaver for "-" and "." and power and nth self
                    if j =="-" or j == ".":
                        continue
                    #if any non number is in the current_display, dont allow the button to do anything
                    if j in self.current_display_content.get():
                
                            proceed = False
        if proceed:
            current_value = self.current_display_content.get().strip()

            if digit == "x!":
                try:
                    if float(current_value) < 0:#fac acnnot be -ve
                        self.current_display_content.set("syntax error")
                        pass
                    #as per factorial input cannot exceed 2147483647 , i have to set limit
                    elif float(current_value) > 2147483647:
                        self.current_display_content.set("Limit Error")   
                    else:
                        output = Utility().tryFloatToInt(float(current_value))
                        output = math.factorial(output)
                        output = Utility().tryFloatToInt(output)
                        print(output)
                        output = Utility().clipLenght(output, self.max_calulator_view_lenght)
                        print(output)
                        self.current_display_content.set(str(output))
                        self.ans_key_value.set(str(output))
                except Exception as e:
                    if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                    else:self.current_display_content.set("Limit Error")
                    print(f"{e} - Error - Error aab")
            elif digit == "|x|":
                try:
                    output = abs(Utility().tryFloatToInt(float(current_value)))
                    self.current_display_content.set(output)
                    self.ans_key_value.set(str(output))
                except Exception as e:
                    if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                    print(f"{e} - error 099")
                    
            elif digit == "xⁿ":
                #check if P exist in the current display
                if "P" in current_value:
                    return
                else:
                    #add P for power
                    self.current_display_content.set(current_value + "P")
                    
            elif digit == "x²":
                try:
                    new_current_value = math.pow(float(current_value), 2)
                    new_current_value = Utility().tryFloatToInt(new_current_value)
                    new_current_value = Utility().clipLenght(new_current_value, self.max_calulator_view_lenght)
                    self.current_display_content.set(new_current_value)
                    self.ans_key_value.set(str(new_current_value))
                except OverflowError:
                    self.current_display_content.set("Limit Error")
                except Exception as e:
                    if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                    print(f"{e} - error dsfcdfc")
                    
            elif digit == "x³":
                    try:
                        new_current_value = math.pow(float(current_value), 3)
                        new_current_value = Utility().tryFloatToInt(new_current_value)
                        new_current_value = Utility().clipLenght(new_current_value, self.max_calulator_view_lenght)
                        self.current_display_content.set(new_current_value)
                        self.ans_key_value.set(str(new_current_value))
                    except OverflowError:
                        self.current_display_content.set("Limit Error")
                    except Exception as e:
                        if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                        print(f"{e} - error dsfcdfc")
                        
            elif digit == "√":
                try:
                    new_current_value = math.sqrt(float(current_value))
                    if int(str(new_current_value).split(".")[1]) == 0:
                        new_current_value = str(new_current_value).split(".")[0]
                        print("value is a int")
                    else:
                        new_current_value = str(new_current_value)[:4]
                        print("value is a float")
                    self.current_display_content.set(new_current_value)
                    self.ans_key_value.set(str(new_current_value))
                
                except Exception as e:
                    if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                    print(f"{e} - error dsfcdfc")
                    
            elif digit == "∛":
                try:
                    new_current_value = math.cbrt(float(current_value))
                    if int(str(new_current_value).split(".")[1]) == 0:
                        new_current_value = str(new_current_value).split(".")[0]
                        print("value is a int")
                    else:
                        new_current_value = str(new_current_value)[:4]
                        print("value is a float")
                    self.current_display_content.set(new_current_value)
                    self.ans_key_value.set(str(new_current_value))
                except Exception as e:
                    if "p" in self.current_display_content.get() or "P" in self.current_display_content.get():self.current_display_content.set("syntax error")
                    print(f"{e} - error dsfcdfc")
                    
            elif digit == "ʸ√":
                #check if p exist in the current display
                if "P" in current_value:
                    return
                else:
                    #add p for self
                    self.current_display_content.set(current_value + "p")
            
    def operationSpecial(self):
        self.btn_frame.pack_forget()
        self.display_frame.pack_forget()
        self.advance()

    def operationExp(self):
        Utility().isErrorPresent(self.current_display_content)
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        #checking if E exist before so i wont add a new E
        if "E" in self.current_display_content.get():
            pass
        #checking if =-*/ is in the value before a second E can be used
        # elif self.current_display_content.get().split("E"):
        #     print(self.current_display_content.get().split("E"))
            
        else:
            self.current_display_content.set(self.current_display_content.get() + "E")

    def operationTRRIG(self, digit):
        #to clear off the content in the right mini
        self.current_right_mini_info.set("")
        #Check if the incoming text is a number
        try:
            current_value = float(self.current_display_content.get())
        except:
            print("Current Value is text")
            return
        #the text is a number
        if digit == "Sin":
            result = str(math.sin(math.radians(current_value)))
                
            
        elif digit == "Cos":
            result = str(math.cos(math.radians(current_value)))
             
            
        elif digit == "Tan":
            result = str(math.tan(math.radians(current_value)))
            
        
        
        if digit == "sin⁻¹":
            result = str(math.degrees(math.asin(current_value)))
           
            
        elif digit == "cos⁻¹":
            result = str(math.degrees(math.acos(current_value)))
            
            
        elif digit == "tan⁻¹":
            result = str(math.degrees(math.acos(current_value)))
        
      #if its int, to remove the unnnesary float
        result = Utility().clipLenght(result,self.max_calulator_view_lenght) # clip lenght
        result = Utility().tryFloatToInt(float(result)) #checking for whole number
        self.current_display_content.set(result)
        self.ans_key_value.set(result)
  
        
        #update the current right mini info
        if digit == "Sin" or digit == "Cos" or digit == "Tan":
            self.current_right_mini_info.set(f"{digit} {result}°")
        else:
            self.current_right_mini_info.set(f"{digit} {result}")
        
         
 
    def operationANS(self):
        int_or_float = Utility().tryFloatToInt(self.ans_key_value.get())
        self.current_display_content.set(Utility().clipLenght(int_or_float, self.max_calulator_view_lenght))
        if "float" in self.current_meta_data_to_display.get():
            self.current_meta_data_to_display.set("float")
        else:
            self.current_meta_data_to_display.set("")
        
     
    def operationEQUALTO(self):
        if Utility().isErrorPresent(self.current_display_content):
            return
        
        #check if p is present, this mean we have to perform power
        if len(self.current_display_content.get().split("P")) > 1:
            b4_P = self.current_display_content.get().split("P")[0].strip()
            after_P = self.current_display_content.get().split("P")[1].strip()
            print([b4_P, "p", after_P])
            if len(b4_P) == 0:#nothing was before p which is almost impossible cos zero suppose dey front
                self.current_display_content.set("syntax error")
                self.current_right_mini_info.set("")#clear all the stuff there
                return
            #no syntax error
            if len(after_P.strip()) == 0:
                after_P = "1"
            try:
               power =  float(after_P.strip())
            except:
                self.current_display_content.set("syntax error")
                self.current_right_mini_info.set("")#clear all the stuff there
                return
            result = math.pow(float(b4_P), power)
            result = Utility().tryFloatToInt(result)
            result = Utility().clipLenght(result, self.max_calulator_view_lenght)
            self.current_display_content.set(result)
            self.ans_key_value.set(result)
            print("taking care of nth power")
            return
               
        #check if p is present, this mean we have to perform power
        if len(self.current_display_content.get().split("p")) > 1:
            b4_P = self.current_display_content.get().split("p")[0].strip()
            after_p = self.current_display_content.get().split("p")[1].strip()
            print([b4_P, "p", after_p])
            if len(b4_P) == 0:#nothing was before p which is almost impossible cos zero suppose dey front
                self.current_display_content.set("syntax error")
                self.current_right_mini_info.set("")#clear all the stuff there
                return
            #no syntax error
            if len(after_p.strip()) == 0:
                after_p = "1"
            try:
               self =  float(after_p.strip())
            except:
                self.current_display_content.set("syntax error")
                self.current_right_mini_info.set("")#clear all the stuff there
                return
            result = math.pow(float(b4_P), 1/self)
            result = Utility().tryFloatToInt(result)
            result = Utility().clipLenght(result, self.max_calulator_view_lenght)
            self.current_display_content.set(result)
            self.ans_key_value.set(result)
            print("taking care of nth ")
            return
            
        
        #p is not present, P too is not present
        if self.current_right_mini_info.get() == "+" or self.current_right_mini_info.get() == "-" or self.current_right_mini_info.get() == "*" or self.current_right_mini_info.get() == "/":
            #just finish up by performing that operatiton and returning the ans as new ans value
            try:
                current_value = float(self.current_display_content.get())
                expression = f"{current_value}{self.current_right_mini_info.get()}{self.ans_key_value.get()}"
                print("equl to pressed when =-/* is active")
                print(expression)
                output =eval(expression)
                output = Utility().tryFloatToInt(output)
                output = Utility().clipLenght(output, self.max_calulator_view_lenght)
                self.ans_key_value.set(output) #ioveride the former ans value
                self.current_display_content.set(output)
                self.current_right_mini_info.set("")#empty it out
                
                #to clear off the content in the right mini
                if "shift" in self.current_meta_data_to_display.get():
                    self.current_meta_data_to_display.set("shift")
                else:
                    self.current_meta_data_to_display.set("")
                return
                
            except Exception as e:
                print(f"{e} - errorcode Equal to")
                return

        #if its just normal number or the expression can be eval quick
        try:
            output = eval(self.current_display_content.get())
            output = float(output)
            output = Utility().tryFloatToInt(output)
            output = Utility().clipLenght(output, self.max_calulator_view_lenght)

            self.ans_key_value.set(output) #ioveride the former ans value
            self.current_display_content.set(output)
            print("jsut a float or eval fit run am sharp sharp")
            #to clear off the content in the right mini
            if "shift" in self.current_meta_data_to_display.get():
                self.current_meta_data_to_display.set("shift")
            else:
                self.current_meta_data_to_display.set("")
        except Exception as e:
            #its not a float, it have something unusual inside
            print(f"Not a float,jst a warning - {e}")
            analysis = list(self.current_display_content.get()) # split every single one
            toSolve = ""
            for index, i in enumerate(analysis, start=1):
                try:#check if its a number
                    tester = float(i) + 2 
                    toSolve += i
                except:
                    # not a number
                    #for pi 
                    if i == "π":
                        if  index == 1 and len(analysis) == 1:#its at the first and its the only one
                            toSolve += f"{math.pi}"
                        elif index == 1 and len(analysis) > 1: #it was the first and there are other values too
                            toSolve += f"{math.pi}*"
                            continue
                        elif index == len(analysis): # at the end
                            toSolve += f"*{math.pi}"
                            continue
                        else:#it is in the middle
                            toSolve +=  f"*{math.pi}*"
                    #for dot
                    if i == ".":
                        toSolve += "."
                
            print(toSolve)
            # messagebox.showinfo("operation", toSolve)
            try:
                output = eval(toSolve.lstrip("0"))#had to strip the front zero cos eval no allow am   
                print(output)
                output = Utility().clipLenght(float(output), self.max_calulator_view_lenght)
                self.current_display_content.set(output) #update the current val
                self.ans_key_value.set(output) # update the ans value
                print("success is 1")
                
                #to clear off the content in the right mini
                if "shift" in self.current_meta_data_to_display.get():
                    self.current_meta_data_to_display.set("shift")
                else:
                    self.current_meta_data_to_display.set("")
                    
            except Exception as e:
                print(f"Er i am cooked--- {e}")                     
                    
        
class CoverUp(CalByOpe):
    def __init__(self, width_pos = 0, height_pos = 0):
        super().__init__(width_pos = width_pos, height_pos = height_pos)
        
   
if __name__ == "__main__": 
    #Start of calculator app
    CoverUp().mainloop()
