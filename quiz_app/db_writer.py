import sqlite3 as sql





action = input("View data(v)/ create data(c): ")






#view Data in the db
if action.upper() == "V":
	try:
		open = sql.connect("db")
		selector = open.cursor().execute("SELECT *, oid FROM question")
		response = selector.fetchall()
		if len(response) == 0:
			print("empty")
		else:
			for i in response:
				print(f"""
				
TITLE : {i[0]},
QUESTION : {i[1]},
OPT A : {i[2]},
OPT B : {i[3]},
OPT C : {i[4]},
OPT D : {i[5]},
CORRECT ANSWER : {i[6]}
INDEX : {i[7]}

					
					""")
	except Exception as e:
		print(f"ERROR : {e}")
		
		
		
		
#update data 
#   - coming soon
#delete data
#   - coming soo 






#create data
elif action.upper() ==  "C":
	batch_update = input("BATCH (Y/N: ")#y when u want to upload multiple data at once
	if batch_update.upper() == "Y":
		pass
	else:
		#collect single data for backup
		title = input ("COURSE title: ").strip()
		question = input("question: ").strip()
		optA = input("OPTION A: ").strip()
		optB = input("OPTION B: ").strip()
		optC = input("OPTION C: " ).strip()
		optD = input("OPTION D: ").strip()
		correct_opt = input("CORRECT OPTION (A,B,C,D) : ").strip()
		
		open = sql.connect("db")
		cursor = open.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS question(title text, question text, optA text, optB text, optC text, optD text, correct_opt text)")
		
		cursor.execute("INSERT INTO question VALUES ( :title, :question, :optA, :optB, :optC, :optD, :correct_opt)", {
		"title" : title.upper().strip(),
		"question" : question.upper().strip(),
		"optA" : optA.upper().strip(),
		"optB" : optB.upper().strip(),
		"optC" : optC.upper().strip(),
		"optD" : optD.upper().strip(),
		"correct_opt" : correct_opt.upper().strip()
		})
		open.commit()
		open.close()