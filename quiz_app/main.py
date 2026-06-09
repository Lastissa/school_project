import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self):
        self.format = """[["Question", ["Option 1", "Option 2", "Option 3", "Option 4"], "Answer"]]"""
        
    
    def cos(self):
        return [
        #algorithm and heuristic
       
    [
        "Why is a greedy algorithm considered a heuristic rather than a classical algorithm?",
        [
            "Because it always guarantees the globally optimal solution",
            "Because it makes locally optimal choices at each step, which may not produce the overall optimal solution",
            "Because it does not follow any steps",
            "Because it requires human intuition"
        ],
        "b"
    ],
    [
        "Which of the following is an example of a heuristic approach in computing?",
        [
            "Antivirus software scanning for patterns",
            "Sorting numbers with bubble sort",
            "Calculating factorials recursively",
            "Binary search on a sorted list"
        ],
        "a"
    ],
    [
        "The greedy algorithm solves problems by:",
        [
            "Trying all possible solutions simultaneously",
            "Choosing the locally optimal option at each step",
            "Making random guesses",
            "Breaking tasks into pseudocode"
        ],
        "b"
    ],
    [
        "Why might antivirus software be classified as a heuristic method?",
        [
            "Because it uses exact step-by-step rules to remove all malware",
            "Because it uses pattern recognition and educated guesses to detect unknown threats",
            "Because it compiles code",
            "Because it only scans text files"
        ],
        "b"
    ],
    [
        "A limitation of greedy algorithms is that:",
        [
            "They are always slow",
            "They may not find the globally optimal solution despite solving problems quickly",
            "They cannot be implemented in software",
            "They require user input at every step"
        ],
        "b"
    ],
    [
        "What is an algorithm?",
        [
            "A mental shortcut used for problem-solving",
            "A precise set of rules or procedures for solving a problem",
            "A guess-based method",
            "A computer hardware component"
        ],
        "b"
    ],
    [
        "Algorithms guarantee:",
        [
            "That a solution will be reached following the given steps",
            "Fastest solution in all cases",
            "Approximate or intuitive results",
            "Random results"
        ],
        "a"
    ],
    [
        "Which of the following is an everyday example of an algorithm?",
        [
            "Using intuition to guess answers",
            "Following a recipe with step-by-step instructions",
            "Walking randomly in a park",
            "Brainstorming ideas without structure"
        ],
        "b"
    ],
    [
        "A heuristic is best described as:",
        [
            "A precise step-by-step formula",
            "A technique to quickly obtain an acceptable solution, often using intuition or exploration",
            "A programming language",
            "A mathematical proof"
        ],
        "b"
    ],
    [
        "One key difference between an algorithm and a heuristic is:",
        [
            "Algorithms are approximate; heuristics are precise",
            "Algorithms must be followed exactly; heuristics are general problem-solving frameworks",
            "Heuristics require computers; algorithms do not",
            "Heuristics guarantee correct results; algorithms do not"
        ],
        "b"
    ],
    [
        "Heuristics are particularly useful when:",
        [
            "Exact solutions are known and easy to compute",
            "Time is limited or information is incomplete",
            "All problem steps are predefined",
            "Problems have a single correct answer"
        ],
        "b"
    ],
    [
        "The precision-speed trade-off in heuristics refers to:",
        [
            "Faster results may not be the most accurate or optimal",
            "Slower results are always worse",
            "Exact solutions take less time",
            "Heuristics always produce precise results instantly"
        ],
        "a"
    ],
    [
        "Working backwards is an example of a heuristic where:",
        [
            "You start solving the problem from the end goal",
            "You guess the solution",
            "You follow a strict algorithm",
            "You ignore the problem constraints"
        ],
        "a"
    ],
    [
        "Breaking a large task into smaller steps is a heuristic that:",
        [
            "Makes complex tasks manageable",
            "Increases complexity",
            "Guarantees an optimal solution",
            "Removes the need for reasoning"
        ],
        "a"
    ],
    [
        "Heuristics cannot be mathematically proven because:",
        [
            "They rely on intuition, exploration, and may not be replicable",
            "They always produce exact results",
            "They are a type of algorithm",
            "They follow strict logical steps"
        ],
        "a"
    ],
    [
        "One of the applications of heuristics is in:",
        [
            "Traveling Salesperson Problem",
            "Printing documents",
            "Storing files",
            "Installing operating systems"
        ],
        "a"
    ],
    [
        "The goal of heuristics in optimization problems is to:",
        [
            "Find a timely and acceptable solution",
            "Guarantee the exact optimal solution always",
            "Ignore constraints",
            "Produce random results"
        ],
        "a"
    ],
    [
        "Heuristics can be used when:",
        [
            "There is access to very little information",
            "The problem is simple and routine",
            "Exact formulas exist",
            "All steps are predetermined"
        ],
        "a"
    ],
    [
        "Which of the following is true about algorithms?",
        [
            "They may produce different results each time",
            "They are suitable for precise, repeatable computations",
            "They rely on intuition",
            "They avoid step-by-step instructions"
        ],
        "b"
    ],
    [
        "Heuristics are often called mental shortcuts because:",
        [
            "They follow strict rules",
            "They allow quick problem-solving using experience and intuition",
            "They always guarantee optimal results",
            "They do not require reasoning"
        ],
        "b"
    ],
        #tsp 
    [
        "The Traveling Salesperson Problem (TSP) is an example of:",
        [
            "A sorting problem",
            "An optimization problem",
            "A search problem",
            "A networking problem"
    	],
    ],
    	
        #Fermi problem
    [
        "What is a Fermi problem primarily designed to test?",
        [
            "Exact numerical calculation",
            "Estimation and reasoning skills",
            "Memory of formulas",
            "Graph plotting"
        ],
        "b"
    ],
    [
        "A key characteristic of a Fermi problem is that:",
        [
            "All data values are precisely known",
            "Exact answers are often unknown and estimation is required",
            "It requires programming knowledge",
            "It only involves geometry"
        ],
        "b"
    ],
    [
        "Solving a Fermi problem usually involves:",
        [
            "Guessing randomly",
            "Applying step-by-step reasoning and breaking down large problems into smaller parts",
            "Copying solutions from a textbook",
            "Using only addition and subtraction"
        ],
        "b"
    ],
    [
        "Which of the following is an example of a Fermi problem?",
        [
            "Calculating the area of a rectangle",
            "Estimating the number of piano tuners in a city",
            "Finding the derivative of a function",
            "Solving a quadratic equation"
        ],
        "b"
    ],
    [
        "Why is justification of reasoning important in Fermi problems?",
        [
            "Because the final answer is always exact",
            "Because the reasoning demonstrates logical steps and approximations used to reach an estimate",
            "Because calculators are not allowed",
            "Because only arithmetic operations matter"
        ],
        "b"
    ],
    #fermi and non routine
    [
        "Which statement is true about non-routine problems and Fermi problems?",
        [
            "All non-routine problems are Fermi problems",
            "All Fermi problems are non-routine problems, but not all non-routine problems are Fermi problems",
            "Fermi problems always have exact numerical answers",
            "Non-routine problems always use estimation"
        ],
        "b"
    ],
    [
        "A key difference between non-routine and Fermi problems is:",
        [
            "Non-routine problems require estimation; Fermi problems have exact solutions",
            "Non-routine problems test creativity; Fermi problems focus on approximate reasoning",
            "Fermi problems are simpler than non-routine problems",
            "There is no difference"
        ],
        "b"
    ],
    [
        "In terms of data availability:",
        [
            "Non-routine problems always provide exact data; Fermi problems do not",
            "Fermi problems provide all information; non-routine problems do not",
            "Non-routine problems provide some or all data; Fermi problems often require assumptions and estimations",
            "Both always provide complete data"
        ],
        "c"
    ],
    [
        "The main objective of a Fermi problem is to:",
        [
            "Find an exact solution using formulas",
            "Reach a reasonable estimate using approximation and logical decomposition",
            "Follow standard algorithms",
            "Test memorization skills"
        ],
        "b"
    ],
    [
        "Which example correctly illustrates a Fermi problem as opposed to a general non-routine problem?",
        [
            "Design a bridge with unusual constraints",
            "Estimate the number of piano tuners in a city",
            "Solve a unique mathematical puzzle with given formulas",
            "Write an essay on a topic"
        ],
        "b"
    ],
    #os related
    [
        "Operating systems can be classified based on the type of computer they control and the type of applications they support into how many major categories?",
        [
            "2",
            "3",
            "4",
            "5"
        ],
        "c"
    ],
    [
        "Which type of operating system is primarily used to control machinery, scientific instruments and industrial systems?",
        [
            "Batch OS",
            "Multi-user OS",
            "Real-Time OS",
            "Time-Sharing OS"
        ],
        "c"
    ],
    [
        "The most important characteristic of a Real-Time Operating System (RTOS) is:",
        [
            "Large storage capacity",
            "Precise and predictable response time",
            "Multiple graphical interfaces",
            "Network connectivity"
        ],
        "b"
    ],
    [
        "What is the major difference between a hard RTOS and a soft RTOS?",
        [
            "Hard RTOS guarantees deadlines while Soft RTOS gives priority without strict guarantees",
            "Hard RTOS supports networking while Soft RTOS does not",
            "Hard RTOS is multi-user",
            "Soft RTOS is faster"
        ],
        "a"
    ],
    [
        "Which operating system is designed for one user performing one task at a time?",
        [
            "Single-User Single-Tasking OS",
            "Multi-User OS",
            "Distributed OS",
            "Network OS"
        ],
        "a"
    ],
    [
        "Palm OS is an example of:",
        [
            "Single-User Single-Tasking OS",
            "Multi-User OS",
            "Distributed OS",
            "Batch OS"
        ],
        "a"
    ],
    [
        "Windows 98 and Mac OS are examples of:",
        [
            "Single-User Multi-Tasking OS",
            "Batch OS",
            "Distributed OS",
            "Real-Time OS"
        ],
        "a"
    ],
    [
        "A Multi-User Operating System allows:",
        [
            "One user with many tasks",
            "Many users to use computer resources simultaneously",
            "One process at a time",
            "Only network access"
        ],
        "b"
    ],
    [
        "Which of the following is a true Multi-User Operating System?",
        [
            "Unix",
            "Windows 98",
            "Palm OS",
            "Mac OS"
        ],
        "a"
    ],
    [
        "Which operating system environment does not allow interaction with a job during its execution?",
        [
            "Time-Sharing OS",
            "Batch Processing OS",
            "Real-Time OS",
            "Distributed OS"
        ],
        "b"
    ],
    [
        "In a Batch Processing Operating System, the response time is measured as:",
        [
            "Execution time",
            "Turnaround time",
            "Clock cycle",
            "Interrupt time"
        ],
        "b"
    ],
    [
        "Which operating system allows users to interact with their programs during execution?",
        [
            "Batch Processing OS",
            "Time-Sharing OS",
            "Single-Tasking OS",
            "Firmware"
        ],
        "b"
    ],
    [
        "In a Time-Sharing Operating System, users share:",
        [
            "Only memory",
            "Only storage",
            "CPU, memory and other system resources",
            "Only printers"
        ],
        "c"
    ],
    [
        "Which operating system is designed for applications where delayed response could result in disaster?",
        [
            "Batch OS",
            "Time-Sharing OS",
            "Real-Time OS",
            "Single-Tasking OS"
        ],
        "c"
    ],
    [
        "Which of the following is an example of a Real-Time Operating System application?",
        [
            "Word processing",
            "Airline reservation systems",
            "Text editing",
            "Spreadsheet software"
        ],
        "b"
    ],
    [
        "A multiprogramming operating system allows:",
        [
            "Multiple processors",
            "Multiple active programs in memory simultaneously",
            "Multiple users only",
            "Multiple operating systems"
        ],
        "b"
    ],
    [
        "Which statement is correct?",
        [
            "Every multiprogramming system is time-sharing",
            "Every time-sharing system is multiprogramming",
            "Multiprocessing and multiprogramming are identical",
            "None of the above"
        ],
        "b"
    ],
    [
        "Multiprocessing refers to:",
        [
            "Many users",
            "Many programs",
            "More than one independent processing unit",
            "Many networks"
        ],
        "c"
    ],
    [
        "In a Network Operating System, users are aware of:",
        [
            "Only one computer",
            "The existence of multiple computers",
            "No hardware resources",
            "Only processors"
        ],
        "b"
    ],
    [
        "A major feature of a Network Operating System is:",
        [
            "Remote login and file sharing",
            "Hard real-time processing",
            "Single-task execution",
            "No networking support"
        ],
        "a"
    ],
    [
        "What distinguishes a Distributed Operating System from a Network Operating System?",
        [
            "Users see multiple machines directly",
            "Users perceive the system as a single computer",
            "It has no communication capability",
            "It does not support file sharing"
        ],
        "b"
    ],
    [
        "In a true Distributed Operating System, users should:",
        [
            "Know where programs are running",
            "Know where files are stored",
            "Be unaware of processor and file locations",
            "Manage processor allocation manually"
        ],
        "c"
    ],
    [
        "Which function of an operating system is responsible for assigning the CPU to tasks?",
        [
            "Memory Management",
            "Processor Management",
            "File Management",
            "Security Management"
        ],
        "b"
    ],
    [
        "Memory Management is concerned with:",
        [
            "Allocating memory to programs and data",
            "Managing printers",
            "Managing networks",
            "Managing processors"
        ],
        "a"
    ],
    [
        "Input/Output Management involves:",
        [
            "Managing CPU registers",
            "Coordinating input and output devices",
            "Compiling programs",
            "Managing databases"
        ],
        "b"
    ],
    [
        "File Management is responsible for:",
        [
            "Allocating processors",
            "Storing and modifying files",
            "Executing instructions",
            "Managing interrupts"
        ],
        "b"
    ],
    [
        "Which of the following is NOT a major function of an Operating System?",
        [
            "Establishing job priorities",
            "Interpreting commands",
            "Manufacturing hardware",
            "Facilitating communication between user and computer"
        ],
        "c"
    ],
    [
        "Why do operating systems contain flaws?",
        [
            "Because computers are defective",
            "Because operating systems are written by humans who make mistakes",
            "Because processors fail",
            "Because memory is limited"
        ],
        "b"
    ],
    [
        "Which of the following is NOT a common consequence of operating system flaws?",
        [
            "System crashes",
            "Security vulnerabilities",
            "Peripheral device incompatibility",
            "Automatic hardware upgrades"
        ],
        "d"
    ],
    [
        "A security flaw in an operating system may:",
        [
            "Improve performance",
            "Allow unauthorized access",
            "Increase storage",
            "Prevent networking"
        ],
        "b"
    ],
#problem solving
    [
        "A problem is best defined as:",
        [
            "A difficult mathematical question",
            "A gap between the current state and the desired state",
            "An unsolved computer error",
            "Any situation that causes stress"
        ],
        "b"
    ],
    [
        "Problem solving is defined as:",
        [
            "Finding answers quickly",
            "Knowing what to do when you don't know what to do",
            "Using computers to solve problems",
            "Following instructions exactly"
        ],
        "b"
    ],
    [
        "What must be done before attempting to find a solution to a problem?",
        [
            "Select a strategy",
            "Apply trial and error",
            "Clearly identify the problem",
            "Gather resources"
        ],
        "c"
    ],
    [
        "A problem-solving strategy is:",
        [
            "A computer program",
            "A plan used to find a solution or overcome a challenge",
            "A mathematical formula",
            "A type of algorithm only"
        ],
        "b"
    ],
    [
        "Which of the following is mentioned as a well-known problem-solving strategy?",
        [
            "Flowcharting",
            "Simulation",
            "Trial and Error",
            "Programming"
        ],
        "c"
    ],
    [
        "Effective problem solving requires all of the following EXCEPT:",
        [
            "Identifying the problem",
            "Selecting an appropriate process",
            "Following a suitable plan",
            "Ignoring the cause of the problem"
        ],
        "d"
    ],
    [
        "Problems are broadly classified into:",
        [
            "Simple and Complex",
            "Technical and Non-Technical",
            "Ill-Defined and Well-Defined",
            "Logical and Mathematical"
        ],
        "c"
    ],
    [
        "An ill-defined problem is characterized by:",
        [
            "Clear goals and clear solutions",
            "Specific solution paths",
            "Lack of clear goals, solution paths, or expected solutions",
            "Only one correct answer"
        ],
        "c"
    ],
    [
        "A well-defined problem is characterized by:",
        [
            "Unclear goals and outcomes",
            "Specific goals and clearly defined solutions",
            "No expected solution",
            "Unlimited solution paths"
        ],
        "b"
    ],
    [
        "Problem solving often involves:",
        [
            "Logical reasoning",
            "Interpretation of meanings",
            "Creativity and abstract thinking",
            "All of the above"
        ],
        "d"
    ],
    [
        "Why is it important to understand multiple problem-solving strategies?",
        [
            "Every problem requires the same approach",
            "Different problems may require different approaches",
            "Strategies eliminate all mistakes",
            "Strategies are only useful in business"
        ],
        "b"
    ],
    [
        "Mastering several problem-solving strategies helps individuals:",
        [
            "Avoid all future problems",
            "Select appropriate solutions more effectively",
            "Memorize solutions",
            "Reduce creativity"
        ],
        "b"
    ],
    [
        "The first step in the problem-solving process is:",
        [
            "Analyzing the problem",
            "Gathering information",
            "Identifying the problem",
            "Developing solutions"
        ],
        "c"
    ],
    [
        "Problem identification involves:",
        [
            "Recognizing and defining an issue that needs attention",
            "Implementing solutions immediately",
            "Evaluating outcomes",
            "Writing reports"
        ],
        "a"
    ],
    [
        "What occurs during the 'Recognize the Problem' stage?",
        [
            "Finding the solution",
            "Noticing a gap between the current and desired state",
            "Collecting data",
            "Developing alternatives"
        ],
        "b"
    ],
    [
        "The purpose of defining a problem is to:",
        [
            "Understand and clearly articulate the issue",
            "Solve the problem instantly",
            "Create multiple solutions",
            "Avoid gathering information"
        ],
        "a"
    ],
    [
        "Why is information gathered during problem identification?",
        [
            "To increase the size of the problem",
            "To better understand the problem",
            "To avoid analysis",
            "To generate random solutions"
        ],
        "b"
    ],
    [
        "Analyzing a problem involves:",
        [
            "Ignoring minor details",
            "Breaking the problem into smaller parts to identify root causes",
            "Choosing a solution immediately",
            "Creating a problem statement first"
        ],
        "b"
    ],
    [
        "The main purpose of problem analysis is to identify:",
        [
            "Expected profits",
            "Root causes",
            "Employees",
            "Deadlines"
        ],
        "b"
    ],
    [
        "The final step in problem identification is:",
        [
            "Recognizing the problem",
            "Gathering information",
            "Analyzing the problem",
            "Developing a problem statement"
        ],
        "d"
    ],
    [
        "A problem statement should be:",
        [
            "Long and detailed",
            "Clear and concise",
            "Technical and complex",
            "Based on assumptions"
        ],
        "b"
    ],
    [
        "Which sequence correctly represents the steps in problem identification?",
        [
            "Recognize → Define → Gather Information → Analyze → Problem Statement",
            "Define → Analyze → Recognize → Gather Information → Problem Statement",
            "Gather Information → Define → Analyze → Recognize → Problem Statement",
            "Recognize → Analyze → Define → Problem Statement → Gather Information"
        ],
        "a"
    ],
#others
    [
        "What is pseudocode?",
        [
            "A programming language",
            "A simple and concise sequence of English-like instructions used to solve a problem",
            "A compiler",
            "A flowchart symbol"
        ],
        "b"
    ],
    [
        "Why is pseudocode commonly used before programming?",
        [
            "To replace source code",
            "To help understand the problem without worrying about syntax",
            "To compile programs",
            "To execute programs"
        ],
        "b"
    ],
    [
        "Which of the following is an advantage of pseudocode over flowcharts?",
        [
            "It requires special software",
            "It takes more time to create",
            "It is easier to fit on a page",
            "It cannot represent decisions"
        ],
        "c"
    ],
    [
        "Pseudocode is often preferred because:",
        [
            "It is a programming language",
            "It closely resembles actual program code",
            "It replaces algorithms",
            "It executes automatically"
        ],
        "b"
    ],
    [
        "Which control structure involves listing instructions step-by-step in order?",
        [
            "Condition",
            "Repetition",
            "Sequence",
            "Storage"
        ],
        "c"
    ],
    [
        "The statement 'x ← a new bulb' demonstrates which control structure?",
        [
            "Condition",
            "Storage",
            "Repetition",
            "Sequence"
        ],
        "b"
    ],
    [
        "The most important requirement of an algorithm is that:",
        [
            "It must be written in Python",
            "Its steps must be clear and unambiguous",
            "It must contain loops",
            "It must contain variables"
        ],
        "b"
    ],
    [
        "Before implementing an algorithm, it should be:",
        [
            "Compiled",
            "Converted to machine code",
            "Tested manually",
            "Encrypted"
        ],
        "c"
    ],
    [
        "A flaw in an algorithm is often discovered when:",
        [
            "It is manually tested",
            "It is printed",
            "It is deleted",
            "It is stored"
        ],
        "a"
    ],
    [
        "A test case is:",
        [
            "A software bug",
            "A fixed set of input data used to test an algorithm",
            "A compiler error",
            "A flowchart symbol"
        ],
        "b"
    ],
    [
        "Writing a program from an algorithm is also called:",
        [
            "Debugging",
            "Simulation",
            "Coding or Implementation",
            "Evaluation"
        ],
        "c"
    ],
    [
        "Source code refers to:",
        [
            "The algorithm only",
            "The program itself",
            "The operating system",
            "The compiler"
        ],
        "b"
    ],
    [
        "Compiling is the process of:",
        [
            "Testing a program",
            "Converting a program into instructions understood by the computer",
            "Finding bugs",
            "Writing pseudocode"
        ],
        "b"
    ],
    [
        "A missing semicolon in a program may cause:",
        [
            "A runtime error",
            "A compile-time error",
            "A hardware error",
            "A network error"
        ],
        "b"
    ],
    [
        "Running a program means:",
        [
            "Writing source code",
            "Compiling the program",
            "Executing compiled instructions",
            "Deleting errors"
        ],
        "c"
    ],
    [
        "If a program produces incorrect output, the cause may be:",
        [
            "A poor algorithm",
            "Incorrect implementation",
            "Instructions executed out of order",
            "All of the above"
        ],
        "d"
    ],
    [
        "Bugs are:",
        [
            "Hardware devices",
            "Errors that cause incorrect or undesirable results",
            "Programming languages",
            "Flowchart symbols"
        ],
        "b"
    ],
    [
        "Debugging refers to:",
        [
            "Writing pseudocode",
            "Finding and fixing program errors",
            "Creating algorithms",
            "Compiling code"
        ],
        "b"
    ],
    [
        "A collection of test cases is known as:",
        [
            "A test suite",
            "A data set",
            "A compiler",
            "A package"
        ],
        "a"
    ],
    [
        "Why is it useful to have other people test a program?",
        [
            "They may discover situations you overlooked",
            "They can compile faster",
            "They reduce memory usage",
            "They replace debugging"
        ],
        "a"
    ],
    [
        "Evaluating a solution involves determining whether:",
        [
            "The problem has been solved correctly",
            "The computer is turned on",
            "The compiler exists",
            "The algorithm contains loops"
        ],
        "a"
    ],
    [
        "Python is classified as a:",
        [
            "Low-level language",
            "High-level interpreted language",
            "Machine language",
            "Assembly language"
        ],
        "b"
    ],
    [
        "Python is designed to be highly:",
        [
            "Complex",
            "Readable",
            "Encrypted",
            "Hardware dependent"
        ],
        "b"
    ],
    [
        "Python programs are generally executed by:",
        [
            "A linker",
            "An interpreter",
            "A router",
            "A kernel"
        ],
        "b"
    ],
    [
        "Python supports which programming paradigm?",
        [
            "Object-Oriented Programming",
            "Structured Programming",
            "Functional Programming",
            "All of the above"
        ],
        "d"
    ],
    [
        "Python is particularly suitable for beginners because:",
        [
            "It has simple syntax and readability",
            "It requires machine code",
            "It lacks libraries",
            "It only supports one paradigm"
        ],
        "a"
    ],
    [
        "PEP stands for:",
        [
            "Python Execution Program",
            "Python Enhancement Proposal",
            "Programming Enhancement Package",
            "Python Engineering Process"
        ],
        "b"
    ],
    [
        "Which statement reflects Python's design philosophy?",
        [
            "Complex is better than simple",
            "Beautiful is better than ugly",
            "Implicit is better than explicit",
            "Complicated is better than complex"
        ],
        "b"
    ],
    [
        "Python follows a 'batteries included' philosophy because:",
        [
            "It ships with a comprehensive standard library",
            "It uses batteries for execution",
            "It avoids modules",
            "It removes built-in functions"
        ],
        "a"
    ],
    [
        "Which field commonly uses Python libraries such as NumPy and Pandas?",
        [
            "Data Science",
            "Electrical Wiring",
            "Mechanical Repair",
            "Networking Hardware"
        ],
        "a"
    ],
    [
        "Which Python framework is mentioned for web development?",
        [
            "Django",
            "Flutter",
            "Laravel",
            "Spring"
        ],
        "a"
    ],
    [
        "What is the output of the statement print('Hello, World!')?",
        [
            "Hello",
            "World",
            "Hello, World!",
            "print"
        ],
        "c"
    ]
]
        
    def mth(self):
        return [
            [
                "What is the base of the binary number system?",
                ["Base 2", "Base 8", "Base 10", "Base 16"],
                "a"
            ],
            [
                "What are the only two digits used in the binary number system?",
                ["0 and 1", "0, 1, and 2", "0 through 7", "0 through 9"],
                "a"
            ],
            [
                "What is the base of the octal number system?",
                ["Base 2", "Base 8", "Base 10", "Base 16"],
                "b"
            ],
            [
                "What are the digits used in the octal number system?",
                ["0 and 1", "0, 1, and 2", "0 through 7", "0 through 9"],
                "c"
            ],
            [
                "What is the base of the decimal number system?",
                ["Base 2", "Base 8", "Base 10", "Base 16"],
                "c"
            ],
            [
                "What are the digits used in the decimal number system?",
                ["0 and 1", "0, 1, and 2", "0 through 7", "0 through 9"],
                "d"
            ],
            [
                "Which number system utilizes base 16 representations?",
                ["Binary", "Octal", "Decimal", "Hexadecimal"],
                "d"
            ],
            [
                "What is the decimal equivalent of the binary number 101?",
                ["3", "5", "6", "7"],
                "b"
            ],
            [
                "Convert the binary representation 1111 to its decimal equivalent.",
                ["7", "11", "15", "16"],
                "c"
            ],
            [
                "What is the binary representation of the decimal number 8?",
                ["100", "1000", "111", "1010"],
                "b"
            ],
            [
                "Which of the following values represents the octal equivalent of decimal 9?",
                ["10", "11", "12", "15"],
                "b"
            ],
            [
                "What decimal value is represented by the octal number 20?",
                ["16", "20", "24", "32"],
                "a"
            ],
            [
                "How many bits are required to represent any single octal digit in binary?",
                ["2 bits", "3 bits", "4 bits", "8 bits"],
                "b"
            ],
            [
                "What is the binary representation of the octal number 7?",
                ["100", "110", "111", "1000"],
                "c"
            ],
            [
                "Which of the following is not a valid number in the octal system?",
                ["107", "764", "812", "555"],
                "c"
            ],
            [
                "Convert the decimal number 12 into binary format.",
                ["1010", "1100", "1110", "1111"],
                "b"
            ],
            [
                "What is the sum of binary 10 and binary 01?",
                ["10", "11", "100", "01"],
                "b"
            ],
            [
                "Which positional value represents the third digit from the right in a decimal integer?",
                ["Ones", "Tens", "Hundreds", "Thousands"],
                "c"
            ],
            [
                "What is the highest single digit value usable in the octal system?",
                ["6", "7", "8", "9"],
                "b"
            ],
            [
                "What system is natively utilized by computer hardware for low-level storage?",
                ["Decimal", "Octal", "Hexadecimal", "Binary"],
                "d"
            ],

            [
                "Which of the following is the correct solution for the inequality -3x + 5 < 11?",
                ["x < -2", "x > -2", "x < 2", "x > 2"],
                "b"
            ],
            [
                "What is the simplified value of (8^(2/3)) * (4^(-1/2))?",
                ["1", "2", "4", "8"],
                "b"
            ],
            [
                "If log_b(x) = y, which of the following expressions is its equivalent exponential form?",
                ["b^x = y", "x^y = b", "b^y = x", "y^b = x"],
                "c"
            ],
            [
                "Solve the linear inequality for x: 2x - 7 >= 3.",
                ["x <= 5", "x >= 5", "x >= 2", "x <= 2"],
                "b"
            ],
            [
                "When multiplying two identical exponential bases, what must you do with their indices?",
                ["Multiply them", "Divide them", "Subtract them", "Add them"],
                "d"
            ],
            [
                "What is the numeric value of any non-zero base raised to the power of 0?",
                ["0", "1", "The base itself", "Infinity"],
                "0"
            ],
            [
                "Simplify the following index expression: (x^5) / (x^2).",
                ["x^7", "x^10", "x^3", "x^(2.5)"],
                "c"
            ],
            [
                "What is the simplified value of 5^(-2)?",
                ["-10", "-25", "1/10", "1/25"],
                "d"
            ],
            [
                "Evaluate the expression log_10(1000).",
                ["2", "3", "10", "100"],
                "b"
            ],
            [
                "According to logarithmic laws, what is log(A) + log(B) equivalent to?",
                ["log(A + B)", "log(A / B)", "log(A * B)", "log(A^B)"],
                "c"
            ],
            [
                "Simplify the logarithmic term log_2(16).",
                ["2", "4", "8", "16"],
                "b"
            ],
            [
                "What happens to the direction of an inequality sign when both sides are multiplied by -1?",
                ["It flips", "It stays the same", "It changes to an equals sign", "It becomes undefined"],
                "a"
            ],
            [
                "Solve the quadratic inequality x^2 - 4 < 0.",
                ["x > 2", "x < -2", "-2 < x < 2", "x < -2 or x > 2"],
                "c"
            ],
            [
                "What is the single value of log_b(1) for any valid base b?",
                ["0", "1", "b", "Undefined"],
                "a"
            ],
            [
                "Simplify the radical expression using indices: square root of x^6.",
                ["x^2", "x^3", "x^4", "x^12"],
                "b"
            ],
            [
                "Express log(x^4) in an expanded linear coefficient form.",
                ["log(4x)", "4 * log(x)", "log(x) / 4", "log(x) + 4"],
                "b"
            ],
            [
                "Solve the exponential equation 3^x = 81.",
                ["2", "3", "4", "5"],
                "c"
            ],
            [
                "What is the value of log_3(1/9)?",
                ["2", "-2", "3", "-3"],
                "b"
            ],
            [
                "Simplify the power of a power expression: (y^3)^4.",
                ["y^7", "y^12", "y^34", "y^1.33"],
                "b"
            ],
            [
                "Find the solution range for the linear inequality 5 - x >= 2.",
                ["x <= 3", "x >= 3", "x <= -3", "x >= -3"],
                "a"
            ],

            [
                "A binary operation * on a set is associative if which of the following conditions holds true?",
                ["a * b = b * a", "(a * b) * c = a * (b * c)", "a * e = a", "a * b = 0"],
                "b"
            ],
            [
                "If a binary operation is defined as a * b = a + b - 3, what is the identity element 'e'?",
                ["0", "1", "3", "-3"],
                "c"
            ],
            [
                "Under an operation with identity element 0 where a * b = a + b + 5, what is the inverse of the element 2?",
                ["-2", "-5", "-7", "-12"],
                "d"
            ],
            [
                "What algebraic property is demonstrated by the specific condition a * b = b * a?",
                ["Closure", "Associativity", "Commutativity", "Distributivity"],
                "c"
            ],
            [
                "For an identity element 'e' under operation *, which property must be satisfied for all 'a'?",
                ["a * e = 0", "a * e = e", "a * e = a", "a * e = -a"],
                "c"
            ],
            [
                "If an element 'x' has an inverse 'y' under operation *, what must x * y equal?",
                ["0", "1", "The identity element e", "The element x"],
                "c"
            ],
            [
                "Under standard real multiplication, what is the identity element?",
                ["-1", "0", "1", "Infinity"],
                "c"
            ],
            [
                "Under standard real addition, what is the identity element?",
                ["-1", "0", "1", "None"],
                "b"
            ],
            [
                "What is the additive inverse of the real number 7?",
                ["1/7", "0", "-7", "7"],
                "c"
            ],
            [
                "What is the multiplicative inverse of the non-zero real number 5?",
                ["-5", "1/5", "0.5", "1"],
                "b"
            ],
            [
                "If a binary operation is defined as x * y = 2xy, find the value of 3 * 4.",
                ["12", "14", "24", "48"],
                "c"
            ],
            [
                "Which mathematical operation on integers lacks an identity element?",
                ["Addition", "Multiplication", "Subtraction", "None"],
                "c"
            ],
            [
                "If a binary operation is defined as a * b = a^b, evaluate the expression 2 * 3.",
                ["5", "6", "8", "9"],
                "c"
            ],
            [
                "The binary operation a * b = a + b + ab is checked for identity. Find 'e'.",
                ["-1", "0", "1", "2"],
                "b"
            ],
            [
                "Is standard division on real numbers commutative?",
                ["Yes", "No", "Only for 0", "Only for 1"],
                "b"
            ],
            [
                "If a set is closed under an operation, where must the output of any pair belong?",
                ["Outside the set", "Inside the set", "Positive reals", "Integers only"],
                "b"
            ],
            [
                "Evaluate (1 * 2) * 3 if the operation is defined explicitly as x * y = x + y.",
                ["5", "6", "7", "8"],
                "b"
            ],
            [
                "Which operation satisfies associativity over the set of rational numbers?",
                ["Subtraction", "Division", "Addition", "Exponentiation"],
                "c"
            ],
            [
                "Find the identity element for the binary operation a * b = ab/4.",
                ["1", "2", "4", "8"],
                "c"
            ],
            [
                "What is the inverse of 3 under the operation a * b = ab/4, given identity e=4?",
                ["4/3", "3/4", "12/3", "16/3"],
                "d"
            ],

            [
                "What is the exact derivative of f(x) = sin(3x) with respect to x?",
                ["cos(3x)", "3cos(3x)", "-3cos(3x)", "3sin(3x)"],
                "b"
            ],
            [
                "Which of the following represents the fundamental circular identity for any angle theta?",
                ["sin^2(theta) - cos^2(theta) = 1", "tan^2(theta) + 1 = sec^2(theta)", "cos^2(theta) + sin^2(theta) = 0", "1 - cot^2(theta) = csc^2(theta)"],
                "b"
            ],
            [
                "What is the indefinite integral of (4x^3 - 2x) dx?",
                ["x^4 - x^2 + C", "12x^2 - 2 + C", "x^4 - 2x^2 + C", "4x^4 - 2x^2 + C"],
                "a"
            ],
            [
                "What is the derivative of a constant value with respect to x?",
                ["1", "0", "The constant itself", "Undefined"],
                "b"
            ],
            [
                "Find the derivative of f(x) = x^5 using the basic power rule.",
                ["5x", "5x^4", "x^4", "20x^3"],
                "b"
            ],
            [
                "What function is produced by differentiating cos(x)?",
                ["sin(x)", "-sin(x)", "tan(x)", "-cos(x)"],
                "b"
            ],
            [
                "What is the basic integral of cos(x) dx?",
                ["sin(x) + C", "-sin(x) + C", "cos(x) + C", "-cos(x) + C"],
                "a"
            ],
            [
                "Using integration rules, evaluate the indefinite integral of 1/x dx.",
                ["x + C", "-1/x^2 + C", "ln|x| + C", "e^x + C"],
                "c"
            ],
            [
                "What is the derivative of the natural exponential function e^x?",
                ["e^x", "xe^(x-1)", "1/e^x", "ln(x)"],
                "a"
            ],
            [
                "Evaluate the definite integral of 2x dx evaluated from x=0 to x=3.",
                ["3", "6", "9", "12"],
                "c"
            ],
            [
                "What is the derivative of tan(x) with respect to x?",
                ["sec(x)", "sec^2(x)", "csc^2(x)", "-sec^2(x)"],
                "b"
            ],
            [
                "Which calculus rule is explicitly used to differentiate a product of two functions?",
                ["Chain Rule", "Quotient Rule", "Product Rule", "Power Rule"],
                "c"
            ],
            [
                "Which calculus method is used to differentiate composite functions like f(g(x))?",
                ["Product Rule", "Chain Rule", "Quotient Rule", "Integration by parts"],
                "b"
            ],
            [
                "What is the value of the trigonometric function sin(pi/2) in radians?",
                ["0", "0.5", "1", "-1"],
                "c"
            ],
            [
                "What is the value of cos(pi) in radians?",
                ["1", "0", "-1", "Undefined"],
                "c"
            ],
            [
                "Convert a 180-degree angle completely into radian units.",
                ["pi/2 radians", "pi radians", "2pi radians", "3pi/2 radians"],
                "b"
            ],
            [
                "What is the period of the standard circular function y = sin(x)?",
                ["pi", "2pi", "pi/2", "3pi"],
                "b"
            ],
            [
                "What is the period of the standard circular function y = tan(x)?",
                ["pi", "2pi", "pi/2", "Zero"],
                "a"
            ],
            [
                "Find the second derivative of the algebraic function f(x) = x^3.",
                ["3x^2", "6x", "6", "0"],
                "b"
            ],
            [
                "Integration can be geometrically interpreted as finding what property under a curve?",
                ["Slope", "Arc length", "Area", "Volume"],
                "c"
            ],

            [
                "What is the equation of a line passing through the point (2, 3) with a slope of 4?",
                ["y = 4x + 5", "y = 4x - 5", "4y = x + 2", "y = 4x + 3"],
                "b"
            ],
            [
                "What is the slope of a straight line that runs perpendicular to the line y = -3x + 7?",
                ["3", "-3", "1/3", "-1/3"],
                "c"
            ],
            [
                "In the standard slope-intercept form equation y = mx + c, what does 'm' represent?",
                ["X-intercept", "Y-intercept", "Slope", "Coordinates"],
                "c"
            ],
            [
                "In the standard slope-intercept form equation y = mx + c, what does 'c' represent?",
                ["Slope", "Y-intercept", "X-intercept", "Origin"],
                "b"
            ],
            [
                "What is the slope of a completely horizontal line plotted on a Cartesian plane?",
                ["0", "1", "Undefined", "Infinite"],
                "a"
            ],
            [
                "What is the slope of a completely vertical line plotted on a Cartesian plane?",
                ["0", "1", "Undefined", "-1"],
                "c"
            ],
            [
                "Find the slope of a straight line passing through the points (1, 2) and (3, 6).",
                ["1", "2", "3", "4"],
                "b"
            ],
            [
                "What is the relationship between the slopes of two distinct parallel lines?",
                ["They are negative reciprocals", "They multiply to -1", "They are exactly equal", "They add up to zero"],
                "c"
            ],
            [
                "Convert the slope-intercept equation y = 2x + 3 into standard linear form (Ax + By + C = 0).",
                ["2x - y + 3 = 0", "2x + y + 3 = 0", "x - 2y + 3 = 0", "2x - y - 3 = 0"],
                "a"
            ],
            [
                "What is the y-intercept value of the straight line defined by 3x + 2y = 6?",
                ["2", "3", "6", "0"],
                "b"
            ],
            [
                "What is the x-intercept value of the straight line defined by 4x - 2y = 8?",
                ["2", "-4", "4", "8"],
                "a"
            ],
            [
                "Identify the equation of a line parallel to y = 5x - 2 that passes through the origin.",
                ["y = -5x", "y = 5x", "y = x/5", "y = 5"],
                "b"
            ],
            [
                "What is the product of the slopes of two non-vertical lines that intersect perpendicularly?",
                ["0", "1", "-1", "2"],
                "c"
            ],
            [
                "Find the midpoint of a line segment connecting the points (2, 4) and (6, 8).",
                ["(4, 6)", "(3, 5)", "(8, 12)", "(2, 2)"],
                "a"
            ],
            [
                "Which of the following points explicitly lies on the line y = 3x + 1?",
                ["(0, 0)", "(1, 4)", "(2, 6)", "(3, 9)"],
                "b"
            ],
            [
                "What is the equation of the horizontal line passing through the coordinate point (-5, 7)?",
                ["x = -5", "y = 7", "y = -5", "x = 7"],
                "b"
            ],
            [
                "What is the equation of the vertical line passing through the coordinate point (3, -2)?",
                ["x = 3", "y = -2", "x = -2", "y = 3"],
                "a"
            ],
            [
                "Find the slope of the line represented by the general linear equation 5x + y = 10.",
                ["5", "-5", "10", "1"],
                "b"
            ],
            [
                "Calculate the distance between points (0,0) and (3,4) using the Euclidean distance formula.",
                ["5", "7", "12", "25"],
                "a"
            ],
            [
                "What is the equation of a line with a slope of 0 that passes through the origin (0,0)?",
                ["x = 0", "y = 0", "y = x", "y = 1"],
                "b"
            ]
        ]
        
    def sta(self):
        return [
            # [
            #     "What is a function that assigns a real number X(s) to each element s of a sample space S called?",
            #     ["A sample factor", "A random variable", "An experiment constant", "A distribution function"],
            #     "b"
            # ],
            # [
            #     "If a coin is tossed once and a random variable X maps Head to 1 and Tail to 0, what is the range space?",
            #     ["R = {1}", "R = {0}", "R = {0, 1}", "R = {-1, 1}"],
            #     "c"
            # ],
            # [
            #     "What is the total number of ordered pairs in the sample space when a fair die is tossed twice?",
            #     ["6 outcomes", "12 outcomes", "24 outcomes", "36 outcomes"],
            #     "d"
            # ],
            # [
            #     "A random variable is classified as discrete if its range space contains what type of points?",
            #     ["Finite or countably infinite", "Uncountably infinite", "Continuously intervals only", "Negative integers only"],
            #     "a"
            # ],
            # [
            #     "Which of the following describes the fundamental requirement for any probability mass function f(x)?",
            #     ["f(x) <= 0", "f(x) >= 0", "f(x) must equal 1 for all x", "f(x) must be a complex number"],
            #     "b"
            # ],
            # [
            #     "What must the sum of all probabilities over the range space of a discrete random variable equal?",
            #     ["0.0", "0.5", "1.0", "Expected value"],
            #     "c"
            # ],
            # [
            #     "If three electronic components are tested and X is the number of defectives, what is the range space?",
            #     ["R = {0, 1}", "R = {1, 2, 3}", "R = {0, 1, 2, 3}", "R = {1, 2, 3, 4}"],
            #     "c"
            # ],
            # [
            #     "What notation is typically used to represent the probability density (mass) function f(x)?",
            #     ["Pr(X < x)", "Pr(X = x)", "Pr(X > x)", "Pr(X != x)"],
            #     "b"
            # ],
            # [
            #     "If three components are tested with equal likelihood, what is the probability of finding exactly 0 defectives?",
            #     ["1/8", "3/8", "1/2", "7/8"],
            #     "a"
            # ],
            # [
            #     "If three components are tested with equal likelihood, what is the probability of finding exactly 1 defective?",
            #     ["1/8", "3/8", "5/8", "7/8"],
            #     "b"
            # ],
            # [
            #     "If three components are tested with equal likelihood, what is the probability of finding at most 2 defectives?",
            #     ["1/8", "3/8", "7/8", "1.0"],
            #     "c"
            # ],
            # [
            #     "If three components are tested with equal likelihood, what is the probability of finding more than 0 defectives?",
            #     ["1/8", "3/8", "5/8", "7/8"],
            #     "d"
            # ],
            # [
            #     "If a discrete random variable has f(x) = k(2x + 1) for x = 1, 2, ..., 6, what is the value of k?",
            #     ["k = 1/12", "k = 1/24", "k = 1/36", "k = 1/48"],
            #     "d"
            # ],
            # [
            #     "For a discrete pdf f(x) = 1/48(2x + 1) where x = 1,2,...,6, what is the value of Pr(X > 2)?",
            #     ["1/6", "3/6", "4/6", "5/6"],
            #     "d"
            # ],
            # [
            #     "Which term refers to the set of all possible real numbers mapped from a random experiment's sample space?",
            #     ["Sample set", "Domain range", "Range space", "Probability space"],
            #     "c"
            # ],
            # [
            #     "If a fair die is tossed twice and X is the sum of outcomes, what is the minimum value in the range space?",
            #     ["0", "1", "2", "3"],
            #     "c"
            # ],
            # [
            #     "If a fair die is tossed twice and X is the sum of outcomes, what is the maximum value in the range space?",
            #     ["6", "10", "12", "36"],
            #     "d"
            # ],
            # [
            #     "For a discrete random variable, how is the probability Pr(X < 2) computed from its values?",
            #     ["f(2)", "f(0) + f(1)", "f(0) + f(1) + f(2)", "1 - f(2)"],
            #     "b"
            # ],
            # [
            #     "If a random variable Y has points that cannot be counted or listed, it is classified as what?",
            #     ["Discrete", "Continuous", "Countable", "Null"],
            #     "b"
            # ],
            # [
            #     "In a random experiment, what does the letter 'S' universally stand for?",
            #     ["Standard deviation", "Sample space", "Success rate", "Sum of parameters"],
            #     "b"
            # ],

            # [
            #     "What formula is used to calculate the mathematical expectation E(X) of a discrete random variable?",
            #     ["Sum of f(x)", "Sum of x * f(x)", "Sum of x^2 * f(x)", "Sum of (x - mu) * f(x)"],
            #     "b"
            # ],
            # [
            #     "If a is a constant value, what is the mathematical expectation E(a) equal to?",
            #     ["0", "1", "a", "a * E(X)"],
            #     "c"
            # ],
            # [
            #     "If a is a constant and h(X) is a function, what is E[a * h(X)] equivalent to?",
            #     ["E[h(X)]", "a + E[h(X)]", "a * E[h(X)]", "a^2 * E[h(X)]"],
            #     "c"
            # ],
            # [
            #     "Which of the following expressions is the shortcut formula used to compute the Variance of X?",
            #     ["E(X^2) - E(X)", "E(X^2) - [E(X)]^2", "[E(X^2)]^2 - E(X)", "E(X) - E(X^2)"],
            #     "b"
            # ],
            # [
            #     "What is the expected value of X given the values 0, 1, 2 with probabilities 1/4, 1/2, 1/4 respectively?",
            #     ["0.5", "1.0", "1.5", "2.0"],
            #     "b"
            # ],
            # [
            #     "In a game of chance, a die yields N1000 for {1,2,3}, N5000 for {4,5}, and N35000 for {6}. What is the expected payout?",
            #     ["N5,000", "N6,000", "N7,500", "N8,000"],
            #     "d"
            # ],
            # [
            #     "If a discrete random variable X has a mean of 1 and E(X^2) = 6, what is its variance?",
            #     ["4", "5", "6", "7"],
            #     "b"
            # ],
            # [
            #     "What is the standard deviation of a random variable X if its variance is computed to be 1100?",
            #     ["10.00", "33.17", "55.00", "110.0"],
            #     "b"
            # ],
            # [
            #     "If a player wins N90 with probability 1/6, loses N30 with 1/6, and gets N0 with 4/6, what is the expected win?",
            #     ["Loss of N10", "Win of N0", "Win of N10", "Win of N15"],
            #     "c"
            # ],
            # [
            #     "If a random variable has values -2, 1, 3 with probabilities 1/3, 1/6, 1/2, what is the calculated mean?",
            #     ["-1", "0", "1", "2"],
            #     "c"
            # ],
            # [
            #     "Using the expectation property, if E(X) = 1, what is the value of E(2X + 5)?",
            #     ["5", "6", "7", "8"],
            #     "c"
            # ],
            # [
            #     "What is the mathematical expectation of a function h(X) for a discrete random variable?",
            #     ["Sum of h(x)", "Sum of h(x) * f(x)", "Sum of x * f(h(x))", "Integral of h(x) dx"],
            #     "b"
            # ],
            # [
            #     "If the standard deviation of a random variable is 12.2, what is its approximate variance?",
            #     ["12.2", "24.4", "148.84", "227.5"],
            #     "c"
            # ],
            # [
            #     "If f(x) = x/10 for x = 1, 2, 3, 4, what is the calculated mean E(X)?",
            #     ["2.0", "2.5", "3.0", "3.5"],
            #     "c"
            # ],
            # [
            #     "If f(x) = x/10 for x = 1, 2, 3, 4, given E(X) = 3 and E(X^2) = 10, what is the variance?",
            #     ["1", "2", "3", "4"],
            #     "a"
            # ],
            # [
            #     "When a fair die is cast, what is the probability assigned to each individual face turning up?",
            #     ["1/2", "1/4", "1/6", "1/36"],
            #     "c"
            # ],
            # [
            #     "The variance of a random variable can never result in which type of numerical value?",
            #     ["Zero", "A fraction", "An integer", "A negative number"],
            #     "d"
            # ],
            # [
            #     "What is the standard deviation defined as in relation to the variance?",
            #     ["The square of variance", "The positive square root of variance", "The variance divided by 2", "The inverse of variance"],
            #     "b"
            # ],
            # [
            #     "If E(X) = 4 and E(X^2) = 25, what is the variance of X?",
            #     ["3", "9", "16", "21"],
            #     "b"
            # ],
            # [
            #     "Which property is always true for variance when a constant 'c' is added, such as Var(X + c)?",
            #     ["Var(X) + c", "Var(X) + c^2", "Var(X)", "c^2 * Var(X)"],
            #     "c"

            # ],

            # [
            #     "For a continuous random variable X, what is the probability that X takes on any one particular single value?",
            #     ["Exactly 0", "Exactly 0.5", "Exactly 1.0", "Determined by f(x)"],
            #     "a"
            # ],
            # [
            #     "The total area under the probability density function curve of a continuous random variable must equal what?",
            #     ["0", "0.5", "1", "Infinity"],
            #     "c"
            # ],
            # [
            #     "Which operation replaces summation when evaluating a continuous random variable's parameters?",
            #     ["Differentiation", "Multiplication", "Integration", "Permutation"],
            #     "c"
            # ],
            # [
            #     "How is the probability Pr(a <= X <= b) calculated for a continuous random variable?",
            #     ["f(b) - f(a)", "Derivative of f(x) from a to b", "Integral of f(x) dx from a to b", "f(a) + f(b)"],
            #     "c"
            # ],
            # [
            #     "Which statement is true regarding inequalities for a continuous random variable?",
            #     ["Pr(a < X < b) != Pr(a <= X <= b)", "Pr(a < X < b) = Pr(a <= X <= b)", "Pr(X > a) = 1 + Pr(X < a)", "Pr(X = a) = 1"],
            #     "b"
            # ],
            # [
            #     "What is the requirement for a continuous function f(x) to be a valid pdf for all real values?",
            #     ["f(x) must be negative", "f(x) >= 0", "f(x) <= 1 everywhere", "f(x) must be differentiable only"],
            #     "b"
            # ],
            # [
            #     "How is the expected value E(X) defined for a continuous random variable with a pdf f(x)?",
            #     ["Integral of f(x) dx", "Integral of x * f(x) dx", "Integral of x^2 * f(x) dx", "Derivative of x * f(x)"],
            #     "b"
            # ],
            # [
            #     "If the range of a continuous variable is from negative to positive infinity, what is the integral of f(x) dx over that range?",
            #     ["0", "0.5", "1", "Undefined"],
            #     "c"
            # ],
            # [
            #     "To find the variance of a continuous random variable, what function's expectation E(h(X)) is required first?",
            #     ["h(X) = X", "h(X) = X^2", "h(X) = 1/X", "h(X) = e^X"],
            #     "b"
            # ],
            # [
            #     "If a continuous pdf is evaluated and has a mean of 1.6 and E(X^2) = 3, what is its variance?",
            #     ["0.44", "1.40", "2.56", "3.44"],
            #     "a"
            # ],
            # [
            #     "What graphical component represents the probability of an interval for a continuous variable?",
            #     ["The peak of the curve", "The x-intercept", "The area under the density function curve", "The slope of the tangent"],
            #     "c"
            # ],
            # [
            #     "If a continuous random variable is defined only on a positive interval, what is f(x) elsewhere?",
            #     ["1", "0", "-1", "Infinite"],
            #     "b"
            # ],
            # [
            #     "What is the mathematical expectation of a constant 'a' times a continuous function h(X)?",
            #     ["a + E(h(X))", "a * E(h(X))", "a^2 * E(h(X))", "E(h(X)) / a"],
            #     "b"
            # ],
            # [
            #     "The integral of a continuous pdf over a subinterval yields which of the following values?",
            #     ["A value between 0 and 1", "A value greater than 1", "A negative value", "The variance always"],
            #     "a"
            # ],
            # [
            #     "What type of function is defined as non-negative and integrable over an interval or union of intervals?",
            #     ["Discrete mass function", "Continuous probability density function", "Linear regression line", "Correlation scale"],
            #     "b"
            # ],
            # [
            #     "If the variance of a continuous random variable is 0.44, what is its standard deviation?",
            #     ["0.22", "0.44", "0.663", "0.88"],
            #     "c"
            # ],
            # [
            #     "When finding Pr(X > 1) for a continuous variable, what is the lower limit of the definite integral?",
            #     ["Negative infinity", "0", "1", "Infinity"],
            #     "c"
            # ],
            # [
            #     "The expression E(X - mu)^2 represents which characteristic of a continuous distribution?",
            #     ["The Mean", "The Median", "The Variance", "The Expected Coefficient"],
            #     "c"
            # ],
            # [
            #     "Which type of random variable is defined over continuous intervals of positive real values?",
            #     ["Bernoulli variable", "Poisson variable", "Continuous random variable", "Binomial variable"],
            #     "c"
            # ],
            # [
            #     "If a continuous variable's pdf is symmetric around a value, that value represents what?",
            #     ["The variance", "The range space", "The mean", "The sample size"],
            #     "c" ],

            # [
            #     "What is a random experiment with exactly two possible outcomes ('success' and 'failure') called?",
            #     ["A Poisson process", "A Bernoulli trial", "A uniform distribution", "A continuous system"],
            #     "b"
            # ],
            # [
            #     "In a Bernoulli trial, if the probability of success is denoted by p, how is failure denoted?",
            #     ["p", "1 - p", "p^2", "1/p"],
            #     "b"
            # ],
            # [
            #     "What are the parameters that uniquely define a standard Binomial distribution?",
            #     ["Mean and Variance", "Parameters (n, p)", "Lambda only", "Interval limits alpha and beta"],
            #     "b"
            # ],
            # [
            #     "What is the formula for the mathematical mean of a standard Bernoulli distribution?",
            #     ["q", "p", "pq", "np"],
            #     "b"
            # ],
            # [
            #     "What is the formula for the variance of a standard Bernoulli distribution?",
            #     ["p", "q", "p(1 - p)", "npq"],
            #     "c"
            # ],
            # [
            #     "Which of the following represents the correct probability mass function of a Binomial distribution?",
            #     ["nCx * p^x * q^(n-x)", "p^x * q^(1-x)", "e^(-lambda) * lambda^x / x!", "1 / (beta - alpha)"],
            #     "a"
            # ],
            # [
            #     "Which of the following is NOT an explicit assumption of the Binomial distribution?",
            #     ["The trials are independent", "Each trial has only two outcomes", "The probability of success changes each trial", "The number of trials n is fixed"],
            #     "c"
            # ],
            # [
            #     "If 5 insects are sprayed with an insecticide where survival p = 0.75, what is the probability that all die?",
            #     ["(0.75)^5", "(0.25)^5", "1 - (0.75)^5", "5 * (0.25)"],
            #     "b"
            # ],
            # [
            #     "If the parameters of a binomial distribution are n = 5 and p = 0.75, what is the calculated mean?",
            #     ["1.25", "2.50", "3.75", "4.00"],
            #     "c"
            # ],
            # [
            #     "What is the variance of a binomial distribution with parameters n = 5 and p = 0.75?",
            #     ["0.2500", "0.7500", "0.9375", "3.7500"],
            #     "c"
            # ],
            # [
            #     "Flip a coin 10 times and count the number of heads. What distribution does this follow?",
            #     ["Poisson", "Geometric", "Binomial", "Uniform"],
            #     "c"
            # ],
            # [
            #     "A multiple choice test has 10 questions with 4 choices each. If you guess, what is the probability of success p?",
            #     ["0.10", "0.25", "0.40", "0.50"],
            #     "b"
            # ],
            # [
            #     "If an occupant installs 20 fans with p = 0.2 of lasting 3 months, what is the average number that function?",
            #     ["2", "4", "5", "16"],
            #     "b"
            # ],
            # [
            #     "If 4 out of 20 fans function on average, what is the average number of fans to be replaced?",
            #     ["4", "10", "16", "20"],
            #     "b"
            # ],
            # [
            #     "In a binomial formula, what does the combination term nCx represent?",
            #     ["The probability of success", "The probability of failure", "The number of different groups of x objects from n objects", "The mean of trials"],
            #     "c"
            # ],
            # [
            #     "If the probability of a component surviving an electric shock is 3/4, what is the probability of failure?",
            #     ["1/4", "1/2", "3/4", "1.0"],
            #     "a"
            # ],
            # [
            #     "What is the relationship between the labels 'success' and 'failure' in a Bernoulli trial?",
            #     ["They are moral judgments", "They are grammatical definitions", "They are simply arbitrary labels for the two outcomes", "They represent high and low values"],
            #     "c"
            # ],
            # [
            #     "What is the maximum value that the random variable X can take in a binomial distribution with n trials?",
            #     ["n - 1", "n", "Infinity", "1"],
            #     "b"
            # ],
            # [
            #     "If a binomial distribution has n = 10 and p = 0.5, what is its expected mean value?",
            #     ["2.5", "5.0", "7.5", "10.0"],
            #     "b"
            # ],
            # [
            #     "Which method can be used to derive the mean and variance of a binomial distribution?",
            #     ["Direct method", "Method of moments", "Moment generating function", "All of the options"],
            #     "d" ],

            # [
            #     "Which distribution defines an experiment that consists of repeated Bernoulli trials until the FIRST success occurs?",
            #     ["Binomial distribution", "Geometric distribution", "Poisson distribution", "Normal distribution"],
            #     "b"
            # ],
            # [
            #     "What is the mathematical formula for the mean E(X) of a Geometric distribution?",
            #     ["1/p", "p/q", "1/p^2", "np"],
            #     "a"
            # ],
            # [
            #     "What is the mathematical formula for the variance of a Geometric distribution?",
            #     ["q/p", "q/p^2", "1/p", "npq"],
            #     "b"
            # ],
            # [
            #     "If a geometric distribution has a success probability of p = 0.5, what is its calculated mean?",
            #     ["1", "2", "4", "0.5"],
            #     "b"
            # ],
            # [
            #     "If a geometric distribution has a success probability of p = 0.5, what is its calculated variance?",
            #     ["1", "2", "4", "0.5"],
            #     "b"
            # ],
            # [
            #     "Products are inspected on a line until the first defective is found. What distribution does this represent?",
            #     ["Uniform", "Geometric", "Poisson", "Binomial"],
            #     "b"
            # ],
            # [
            #     "What is the probability mass function of a geometric distribution for finding the first success on trial x?",
            #     ["p * q^(x-1)", "p^x * q", "nCx * p^x", "e^(-lambda)"],
            #     "a"
            # ],
            # [
            #     "If the probability that a terminal is ready is p = 0.20, what is the average number of terminals polled to find a ready one?",
            #     ["2 terminals", "4 terminals", "5 terminals", "10 terminals"],
            #     "c"
            # ],
            # [
            #     "Which distribution is appropriate for counting the number of occurrences of an event per unit of time or space?",
            #     ["Geometric", "Uniform", "Poisson", "Normal"],
            #     "c"
            # ],
            # [
            #     "What parameter represents the mean number of occurrences per unit in a Poisson distribution?",
            #     ["p", "q", "lambda", "mu"],
            #     "c"
            # ],
            # [
            #     "What is the mathematical formula for the pdf of a Poisson distribution?",
            #     ["(e^-lambda * lambda^x) / x!", "1 / (beta - alpha)", "p * q^(x-1)", "nCx * p^x"],
            #     "a"
            # ],
            # [
            #     "If the average number of radioactive particles passing a point is 4 per millisecond, what is the value of lambda?",
            #     ["2", "4", "6", "8"],
            #     "b"
            # ],
            # [
            #     "A sales firm receives an average of 3 calls per hour. What distribution models the number of calls per hour?",
            #     ["Uniform", "Geometric", "Poisson", "Binomial"],
            #     "c"
            # ],
            # [
            #     "What unique property do the mean and variance share in a standard Poisson distribution?",
            #     ["They are inverses", "They sum to 1", "They are exactly equal (both equal lambda)", "Variance is the square of the mean"],
            #     "c"
            # ],
            # [
            #     "What is the support/range space for a standard Poisson random variable?",
            #     ["{0, 1}", "{1, 2, ..., n}", "Non-negative integers {0, 1, 2, ...}", "Continuous real numbers"],
            #     "c"
            # ],
            # [
            #     "If the parameter lambda of a Poisson distribution is 3, what is its exact variance?",
            #     ["1.5", "3.0", "9.0", "1.73"],
            #     "b"
            # ],
            # [
            #     "In a geometric distribution, what must be true about the probability of success p across all trials?",
            #     ["It decreases", "It increases", "It remains completely constant", "It alternates between 0 and 1"],
            #     "c"
            # ],
            # [
            #     "If a coin is tossed repeatedly until the first head shows up, which distribution tracks the trial count?",
            #     ["Poisson", "Geometric", "Uniform", "Normal"],
            #     "b"
            # ],
            # [
            #     "What is the value of 0! (zero factorial) used in the denominator of Poisson probabilities?",
            #     ["0", "1", "Infinity", "Undefined"],
            #     "b"
            # ],
            # [
            #     "Which distribution is often called a 'waiting-time' distribution for the occurrence of the first success?",
            #     ["Binomial", "Uniform", "Geometric", "Poisson"],
            #     "b" ],

            # [
            #     "A continuous random variable is uniformly distributed if it is equally likely to be near any value in what?",
            #     ["A discrete set", "A specific interval [alpha, beta]", "A positive integer series", "A single coordinate point"],
            #     "b"
            # ],
            # [
            #     "What is the probability density function f(x) of a continuous Uniform distribution over [alpha, beta]?",
            #     ["1 / (beta - alpha)", "1 / alpha", "beta - alpha", "1 / (alpha + beta)"],
            #     "a"
            # ],
            # [
            #     "What is the mathematical formula for the mean of a continuous uniform distribution over [alpha, beta]?",
            #     ["(alpha - beta) / 2", "(alpha + beta) / 2", "(beta - alpha) / 12", "alpha * beta"],
            #     "b"
            # ],
            # [
            #     "What is the mathematical formula for the variance of a continuous uniform distribution over [alpha, beta]?",
            #     ["(beta - alpha)^2 / 2", "(beta - alpha)^2 / 12", "(alpha + beta) / 12", "beta - alpha"],
            #     "b"
            # ],
            # [
            #     "If an operator fills a form in a time uniformly distributed between 1.5 and 2.2 minutes, what is the mean time?",
            #     ["1.50 minutes", "1.85 minutes", "2.00 minutes", "2.20 minutes"],
            #     "b"
            # ],
            # [
            #     "What is the uniform distribution pdf if the current in a wire is measured uniformly between 0 and 20 mA?",
            #     ["0.01", "0.05", "0.10", "0.20"],
            #     "b"
            # ],
            # [
            #     "What is the expected mean current if the measurements are uniformly distributed between 0 and 20 mA?",
            #     ["5 mA", "10 mA", "15 mA", "20 mA"],
            #     "b"
            # ],
            # [
            #     "Which standard distribution is famously characterized by a bell-shaped, symmetric curve around its mean?",
            #     ["Uniform distribution", "Poisson distribution", "Geometric distribution", "Normal distribution"],
            #     "d"
            # ],
            # [
            #     "What notation is universally used to denote a normal distribution with mean mu and variance sigma^2?",
            #     ["U(mu, sigma^2)", "N(mu, sigma^2)", "P(lambda)", "B(n, p)"],
            #     "b"
            # ],
            # [
            #     "For any normal random variable, what is the approximate probability that X lies within one standard deviation of the mean?",
            #     ["0.5000", "0.6827", "0.9545", "0.9973"],
            #     "b"
            # ],
            # [
            #     "For any normal random variable, what is the approximate probability that X lies within two standard deviations of the mean?",
            #     ["0.6827", "0.8500", "0.9545", "0.9973"],
            #     "c"
            # ],
            # [
            #     "For any normal random variable, what is the approximate probability that X lies within three standard deviations of the mean?",
            #     ["0.6827", "0.9545", "0.9900", "0.9973"],
            #     "d"
            # ],
            # [
            #     "What transformation formula is used to create a standard normal random variable Z from a normal variable X?",
            #     ["Z = (X - mu) / sigma", "Z = (X - sigma) / mu", "Z = X - mu", "Z = (X - mu) / sigma^2"],
            #     "a"
            # ],
            # [
            #     "What are the expected mean and variance values of the transformed standard normal variable Z?",
            #     ["Mean=1, Variance=0", "Mean=0, Variance=1", "Mean=mu, Variance=sigma", "Mean=0, Variance=0"],
            #     "b"
            # ],
            # [
            #     "If the amount of recycling newspaper is normally distributed with mean 28 pounds and standard deviation 2, what is sigma?",
            #     ["1 pound", "2 pounds", "4 pounds", "28 pounds"],
            #     "b"
            # ],
            # [
            #     "The cumulative distribution function of a standard normal random variable is commonly denoted by which symbol?",
            #     ["f(x)", "p(x)", "Phi(z)", "Lambda(x)"],
            #     "c"
            # ],
            # [
            #     "What is the range of real values allowed for the variable x in a standard normal distribution pdf?",
            #     ["From 0 to infinity", "From negative infinity to positive infinity", "From alpha to beta", "From -1 to +1"],
            #     "b"
            # ],
            # [
            #     "If a wire current measurement has a mean of 10 mA and variance of 4, what is the standard deviation?",
            #     ["2 mA", "4 mA", "10 mA", "16 mA"],
            #     "a"
            # ],
            # [
            #     "The continuous uniform distribution is used when an event is described as being what over an interval?",
            #     ["Highly skewed", "Equally likely", "Normally centered", "Exponentially decaying"],
            #     "b"
            # ],
            [
                "The total area under the standard normal curve to the left of its mean of 0 is equal to what value?",
                ["0.0", "0.25", "0.50", "1.00"],
                "c"
            ]
        ]




class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.width = 580
        self.height  =700
        self.bg = "#0B0F19" #background color
        
        self.current_question_index = tk.IntVar(value=0) # for tracking the current question index in the quiz_start
        self.current_score_list = tk.StringVar(value="")#track current opt picks "a,b,c,d,c,a" and so on
        self.selected_option = tk.StringVar(value="") # for tracking the selected option in the quiz_start and addi


        self.courses = ["COS 102","MTH 114", "STA 112" ] # course for the dropdown menu
        self.selected_course = tk.StringVar(value=self.courses[0]) #for the dropwown in the welcome page
        self.hours = [f"{x:02d}" for x in range(5)]#4 hour max
        self.selected_hour = tk.StringVar(value="0")
        self.minutes = [f"{i:02d}" for i in range(0, 60, 5)]
        self.minutes.insert(1, "01") # for testing what happens on time run out
        self.selected_min = tk.StringVar(value="10")
        self.selected_question_lenght = tk.StringVar(value="00") # the lenght of the question the user want to do
        self.question_option = [f"{i:02d}" for i in range(0, 101, 5)]
        
        
        #the welcome page setup
        self.title("group 1 quiz app project")
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.configure(bg=self.bg)
        
        #the home frame and the quiz frame set up
        self.home_frame = tk.Frame(self, bg= self.bg)
        self.quiz_frame = tk.Frame(self, bg=self.bg, padx=10, pady=12)
        
        # Display the home screen directly
        self.build_home_page()
    
    def build_home_page(self):
        self.home_frame.pack(fill="both", expand=True)
        #a new wrapper inside the home frame - i used it for better layout
        self.content_wrapper = tk.Frame(self.home_frame, bg="#0B0F19", padx=40, pady=40)#for inner frame so i can del all stuff without delay like the calculator
        self.content_wrapper.pack(fill="both", expand=True)
        #intro label
        lbl_welcome = tk.Label(
            self.content_wrapper,
            text="QUIZ APP",
            font=("Segoe UI", 26, "bold"),
            fg="#F8FAFC",
            bg="#0B0F19"
        )
        lbl_welcome.pack(anchor="w", pady=(0, 4))
        #intro words
        lbl_desc = tk.Label(
            self.content_wrapper,
            text="A simple quiz app that help access your knowledge on a course",
            font=("Segoe UI", 11),
            fg="#64748B",
            bg=self.bg
        )
        lbl_desc.pack(anchor="w", pady=(0, 25))
        #the divider
        # Decorative divider line
        divider = tk.Frame(self.content_wrapper, height=1, bg="#1F2937")
        divider.pack(fill="x", pady=(0, 30))
        
        #Frame for selecting course, duration and question
        data_collection_frame = tk.Frame(
            self.content_wrapper, 
            bg="#111827", 
            padx=35, 
            pady=35, 
            highlightbackground="#1F2937", 
            highlightthickness=1
        )
        data_collection_frame.pack(fill="x", pady=(0, 35))
        
        # 1. Course Selection Dropdown Section
        lbl_course_title = tk.Label(
            data_collection_frame,
            text="SELECT COURSE",
            font=("Segoe UI", 9, "bold"),
            fg="#94A3B8",
            bg="#111827"
        )
        lbl_course_title.pack(anchor="w", pady=(0, 8))
        
        #courses option
        course_menu = tk.OptionMenu(data_collection_frame, self.selected_course, *self.courses, command = None)
        self.style_option_menu(course_menu)
        course_menu.pack(fill="x", pady=(0, 25))
            
        # 2. Time Allocation Dropdown Section
        lbl_duration_title = tk.Label(
            data_collection_frame,
            text="LIMIT DURATION",
            font=("Segoe UI", 9, "bold"),
            fg="#94A3B8",
            bg="#111827"
        )
        lbl_duration_title.pack(anchor="w", pady=(0, 8))
        #for hour and course
        picker_row = tk.Frame(data_collection_frame, bg="#111827")
        picker_row.pack(anchor="w", fill="x")
        
        #for the hour selector
        hour_menu = tk.OptionMenu(picker_row, self.selected_hour, *self.hours)
        self.style_option_menu(hour_menu)
        hour_menu.pack(side="left")
        
        lbl_colon = tk.Label(picker_row, text=":", font=("Segoe UI", 14, "bold"), fg="#4B5563", bg="#111827")
        lbl_colon.pack(side="left", padx=12)
        
        #for the minute selector
        min_menu = tk.OptionMenu(picker_row, self.selected_min, *self.minutes)
        self.style_option_menu(min_menu)
        min_menu.pack(side="left")
        
        #duration suffix
        lbl_suffix = tk.Label(picker_row, text="HH : MM", font=("Segoe UI", 10, "bold"), fg="#4B5563", bg="#111827")
        lbl_suffix.pack(side="left", padx=15)
         
        #question_count label
        question_count_lbl = tk.Label(picker_row, text="question lenght".upper(), font=("Segoe UI", 9, "bold"),
            fg="#94A3B8",
            bg="#111827")
        question_count_lbl.pack(anchor="e")
        
        #question amount selector
        question_count = tk.OptionMenu(picker_row, self.selected_question_lenght, *self.question_option)
        self.style_option_menu(question_count)
        question_count.pack(anchor="e")
        
        #start quiz button
        self.btn_start = tk.Button(
            self.content_wrapper,
            text="Start",
            font=("Segoe UI Semibold", 12),
            bg="#2563EB",  
            fg="#FFFFFF",
            padx=35,
            pady=12,
            command=self.start_quiz)
        self.btn_start.pack(anchor="se")
                
    #styling the Option menu
    def style_option_menu(self, menu_widget):
        menu_widget.config(
            bg="#1F2937",          
            fg="#F3F4F6",          
            activebackground="#374151",
            activeforeground="#FFFFFF",
            bd=0,
            highlightthickness=1,
            highlightbackground="#374151", 
            font=("Segoe UI", 11),
            indicatoron=0,         # Hide standard Windows native drop down arrow
            padx=15,
            pady=8
        )
    

    #for starting the quiz
    def start_quiz(self):
        #check if question count is not zero nd real time was inserted
        duration = (int(self.selected_hour.get())*3600) + (int(self.selected_min.get())*60) # total time in seconds
        if duration == 0 or int(self.selected_question_lenght.get()) == 0:
            try: # incase this is the first time THE ERROR IS SHOWN as pack_forget wont work yet so the except should br used
                self.dur_err_warn.pack_forget()
                self.dur_err_warn = tk.Label(self.content_wrapper, text="INCOMPLETE PARAMETERS!!!", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            except:
                self.dur_err_warn = tk.Label(self.content_wrapper, text="INCOMPLETE PARAMETERS!!!", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            return
            
            
        #to reset the timer incase the user have press quit and come bacl yes the quiz_frame was suppose to destroy and it did  but the attribute hour_in_sec is still alive keeping the duration from restarting
        try:
            self.time_in_sec - 20 # if it works , it mean the user have been in the quiz frame befpre and i need to reset it
            hour_in_sec = int(self.selected_hour.get())*3600
            min_in_sec = int(self.selected_min.get())*60
            self.time_in_sec = hour_in_sec + min_in_sec
        except:
            pass
        #to reset the current index too
        try:
            self.current_question_index.set(0)
        except:
            pass
        #reset the selected answer incase the user have pressed it before
        self.selected_option.set("")
        #populate a list for list of question so i can modify it later during submission
        self.answer_pool = ["0" for i in range(0, int(self.selected_question_lenght.get()))]
        #the quiz questions
        self.questionFilter() # question filtered # self.question_pool is now populated with the selected course question
        if self.questionFilter() == False:
            try: # incase this is the first time THE ERROR IS SHOWN as pack_forget wont work yet so the except should br used
                self.dur_err_warn.pack_forget()
                self.dur_err_warn = tk.Label(self.content_wrapper, text= f"Errror, Max allowed question is  {len(self.allQuestionBeforeFilter)}", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            except:
                self.dur_err_warn = tk.Label(self.content_wrapper, text= f"Error, Max allowed question is  {len(self.allQuestionBeforeFilter)}", fg="red", bg = self.bg, font=("Segoe UI", 11),)
                self.dur_err_warn.pack()
                self.dur_err_warn.after(2500,lambda: [self.dur_err_warn.destroy()])
            return
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
        # print(seconds)
        hour = seconds//3600
        min = (seconds - (hour * 3600))//60
        sec =seconds - ((hour * 3600) + (min*60))
        result = f"{hour} : {min:02d} : {sec:02d}"
        # print(result)
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
            
        self.duration_lbl = tk.Label(
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
        self.allQuestionBeforeFilter = [] #this is to first bring in all the question from the course without shufffling or giving a fuck about lenght
        if self.selected_course.get() == "COS 102":self.allQuestionBeforeFilter.extend(Question().cos())
        elif self.selected_course.get() == "MTH 114":self.allQuestionBeforeFilter.extend(Question().mth())
        elif self.selected_course.get() == "STA 112":self.allQuestionBeforeFilter.extend(Question().sta())
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
            
        
        	
        
    def quiz_first_frame(self):
        self.quiz_header_frame = tk.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_header_frame.pack(fill="x", pady=10, padx=10)
        
        #Left: Course Title
        self.course_lbl = tk.Label(
            self.quiz_header_frame, 
            text=self.selected_course.get(), 
            font=("Segoe UI", 15, "bold"), 
            bg=self.bg, 
            fg="white",
            anchor="w"
        )
        self.course_lbl.pack(side="left", padx=10)
        
        #right: Duration Title
        self.duration_countdown_display()
    
    def quiz_second_frame(self):
        self.quiz_questioon_frame = tk.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_questioon_frame.pack(fill="both", expand=True, padx=10, pady=20)
        self.quiz_questioon_label = tk.Label(self.quiz_questioon_frame, text=self.question_pool[self.current_question_index.get()][0], font=("Segoe UI", 12), bg=self.bg, fg="white", justify="left", wraplength= self.width - 40)
        self.quiz_questioon_label.pack(fill="x")
        
        self.quiz_questioon_label.bind("<Configure>", lambda event, extra = self.quiz_questioon_label: self.configureQuestionWidth(widget=  extra, event=event))
        
    def quiz_third_frame(self):
        self.quiz_option_frame = tk.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_option_frame.pack(fill="x", padx=10, pady=10)
        
        #the options radio buttons
        #(1)
        self.quiz_opt_btn_1 = tk.Radiobutton(
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
        self.quiz_opt_btn_2 = tk.Radiobutton(
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
        self.quiz_opt_btn_3 = tk.Radiobutton(
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
        self.quiz_opt_btn_4 = tk.Radiobutton(
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
        self.quiz_footer_frame = tk.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_footer_frame.pack(fill="x", expand=True)

        #prev
        self.footer_button_prev = tk.Button(self.quiz_footer_frame, text="Previous", font=("Segoe UI", 11), bg="#aaaaaa", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Prev"))
        self.footer_button_prev.grid(row=0, column= 0, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(0, weight= 1)
        
        #quit
        self.footer_button_quit = tk.Button(self.quiz_footer_frame, text="Quit", font=("Segoe UI", 11), bg="#DC2626", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Quit"))
        self.footer_button_quit.grid(row=0, column= 1, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(1, weight= 1)
        
        #submit
        self.footer_button_submit = tk.Button(self.quiz_footer_frame, text="Submit", font=("Segoe UI", 11), bg="#16A34A", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Submit"))
        self.footer_button_submit.grid(row=0, column= 2, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(2, weight= 1)
        
        #next
        self.footer_button_next = tk.Button(self.quiz_footer_frame, text="Next", font=("Segoe UI", 11), bg="#173E94", fg="white", padx=10, pady=5 ,bd=0, command=lambda: self.prevQuiSubmitNext("Next"))
        self.footer_button_next.grid(row=0, column= 3, padx=10, pady=10, sticky="ew")
        self.quiz_footer_frame.grid_rowconfigure(0, weight = 1)
        self.quiz_footer_frame.grid_columnconfigure(3, weight= 1)
        
        
    def quiz_fifth_frame(self):
        self.quiz_footer_second_frame = tk.Frame(self.quiz_frame, bg= self.bg)
        self.quiz_footer_second_frame.pack(anchor="s", pady=10, padx=10, fill="x", expand=True)
        self.current_question_footer = tk.Label(self.quiz_footer_second_frame, text=f"Question {self.current_question_index.get() + 1} of {int(self.selected_question_lenght.get())}", font=("Segoe UI", 14, "bold"), bg=self.bg, fg="#94A3B8")
        self.current_question_footer.pack(anchor="e")
    
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
                
            else:
                # submit  = tk.messagebox.askyesno("Submit Quiz", "This is the last question, submit ?\nNG: Once submited, otilor!")
                # if submit:
                #     for i in self.quiz_frame.winfo_children():
                #         i.destroy() #destroy all quiz frame content
                #     self.quiz_frame.pack_forget() #hide the quiz frame
                #     #bring on the analysis Frame
                #     self.loadAnalysis()
                pass
                    
        elif action == "Submit":
            total_answered = 0
            for i in self.answer_pool:
                if i != "0":
                    total_answered += 1
            shouldSunbmit = tk.messagebox.askyesno("Submit", f"Are you sure you want to submit?\nYou have answered {total_answered} out of {len(self.answer_pool)}")
            if shouldSunbmit:
                for i in self.quiz_frame.winfo_children():
                    i.destroy() #destroy all quiz frame content
                    self.quiz_frame.pack_forget() #hide the quiz frame
                
                #bring on the analysis Frame
                self.loadAnalysis()
                
            
        elif action == "Quit":
            messagebox = tk.messagebox.askyesno("Quit Quiz", "Are you sure you want to quit?\nCurrent Data will be lost!")
            if messagebox:
                for i in self.quiz_frame.winfo_children():
                    i.destroy() #destroy all quiz frame content
                self.quiz_frame.pack_forget() #hide the quiz frame
                self.build_home_page() # Go back to the home page
                
                
    #for when ans is selected
    def optButtonSelected(self):
        self.answer_pool[self.current_question_index.get()] = self.selected_option.get()
    
    #the analysis frame
    def loadAnalysis(self):
        #toNeed
        total_question_answered = 0
        total_correct_answer = 0
        
        #for checking the total attempted question
        for i in self.answer_pool:
            if i != "0":
              total_question_answered += 1
        #for increasing the correct score count
        for i in range(len(self.question_pool)-1):
            print(self.answer_pool[i], self.question_pool[i][-1])
            if (self.answer_pool[i]).upper() == (self.question_pool[i][-1]).upper():
                total_correct_answer += 1
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
        self.analysis_frame = tk.Frame(self, bg=self.bg)
        self.analysis_frame.pack(expand=True, fill="both", padx=10, pady=10)

        #the  report label
        report = tk.Label(self.analysis_frame, text = "ANALYSIS",font=("Segoe UI", 26, "bold"), fg="#F8FAFC", bg="#0B0F19")
        report.pack(expand=True, fill="x", anchor="n")
        
        #used an inner frame so i can use a grid inside as the current frame is beign run by a pack
        inner_frame = tk.Frame(self.analysis_frame, bg= self.bg)
        inner_frame.pack(expand=True, fill="both")
        
        for index, value in enumerate(information_to_display.keys()):
            btn_left = tk.Label(inner_frame, text=value, font=("Segoe UI", 11), bg = self.bg, fg="white", pady=5, anchor="w")
            btn_left.grid(row=index, column=0,pady=10, padx=10, sticky="ew")
            inner_frame.grid_rowconfigure(index, weight=1)
            inner_frame.grid_columnconfigure(0, weight=1)
            
            btn_right = tk.Label(inner_frame, text=information_to_display[value], justify="right",font=("Segoe UI", 13, "bold"), bg = self.bg, fg="white", pady=5, anchor="center")
            btn_right.grid(row=index, column=1,pady=10, sticky="ew")
            inner_frame.grid_rowconfigure(index, weight=1)
            inner_frame.grid_columnconfigure(1, weight=1)
        
        #the analysis btn
        analysis_btn = tk.Button(self.analysis_frame, text="Q SUMMARY", font=("Segoe UI Semibold", 12),bg="#2563EB",  fg="#FFFFFF",padx=35, command= self.eachQuestionAnalysis)
        analysis_btn.pack(fill="x", expand=True, padx=40)
        #the speech button
        word_remark = tk.Label(self.analysis_frame, text=word_remark_text,font=("Segoe UI", 13, "italic"), fg="#AFCFF0", bg="#0B0F19")
        word_remark.pack(fill="x", expand=True)
        #the home button
        home = tk.Button(self.analysis_frame, text="HOME", font=("Segoe UI Semibold", 12),bg="#2563EB",  fg="#FFFFFF", command= self.home)
        home.pack(fill="x", expand=True, anchor="s",padx=40)
        
    def eachQuestionAnalysis(self):
        #remove the analysis Frame from view
        #Bring up the new each question anaylysis frame
        #question load up
        #options load up (choosen one highlight green),correct ans is highlighted with a mark
        #prev, back, home, next btns replacing the former ones
        pass

        
        
    #for when home btn is pressed in analyss
    def home(self):
        for i in self.analysis_frame.winfo_children():
            i.destroy()
        self.analysis_frame.pack_forget()
        
        #restart app cycle
        self.build_home_page()
if __name__ == "__main__":
    QuizApp().mainloop()