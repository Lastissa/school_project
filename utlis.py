class Utils:
    def __init__(self):
        self.cos_question = cos = [
    # --- MODULE 1: OPERATING SYSTEM ---
    [
        "What is the primary role of an operating system concerning computer resources?",
        ["To compile code into byte code", "To design graphical layouts", "To manage hardware and software resources", "To provide internet routing protocols"],
        "c"
    ],
    [
        "How does an operating system maintain system equilibrium?",
        ["By running multiple antivirus scans", "By maintaining a proper balance between software and hardware", "By written completely in assembly language", "By using a single uniprocessor simulation"],
        "b"
    ],
    [
        "The operating system acts as a ________ for applications that are run on the machine.",
        ["compiler", "host", "text editor", "network driver"],
        "b"
    ],
    [
        "By handling hardware details, what does the operating system relieve application programs from doing?",
        ["Managing hardware details directly", "Using variable names", "Executing logic paradigms", "Interacting with the user interface"],
        "a"
    ],
    [
        "From which point of view does an OS manage the different parts of the system efficiently?",
        ["Extended machines point of view", "Resource manager point of view", "Multi-paradigm point of view", "Heuristic point of view"],
        "b"
    ],
    [
        "Which point of view states that an OS provides a virtual machine that is more convenient to use?",
        ["Resource manager point of view", "Decidable framework point of view", "Extended machines point of view", "Imperative programming point of view"],
        "c"
    ],
    [
        "Which of the following is NOT listed as a basic task at the foundation of all system software?",
        ["Controlling and allocating memory", "Prioritizing system requests", "Compiling Python source code to byte code", "Managing file systems"],
        "c"
    ],
    [
        "The operating system forms a platform for which two types of software?",
        ["Firmware and BIOS software", "Other system software and application software", "Text editors and TOML files", "Heuristics and optimization codes"],
        "b"
    ],
    [
        "What occurs when software hides lower-level details and provides a set of higher-level functions?",
        ["An abstraction", "An algorithm", "A loop hierarchy", "A system crash"],
        "a"
    ],
    [
        "The OS transforms the physical world of devices, instructions, and memory into a ________ world.",
        ["logical simulated", "uniprocessor", "virtual", "multi-user network"],
        "c"
    ],
    [
        "What is the first reason provided for the necessity of hardware abstraction?",
        ["The code needed to control peripheral devices is not standardized", "The user interface needs to be flashy", "Memory allocation is always infinite", "Security cannot be enforced manually"],
        "a"
    ],
    [
        "What abstraction does the OS introduce so that programs do not have to deal directly with disks?",
        ["The process abstraction", "The file abstraction", "The thread abstraction", "The socket abstraction"],
        "b"
    ],
    [
        "Through what lens does each active process view the system hardware?",
        ["The lens of abstraction", "The lens of a compiler", "The lens of an algorithm", "The lens of a bootstrap loader"],
        "a"
    ],
    [
        "In resource management, processes are considered active agents while resources are considered:",
        ["dynamic components", "passive entities", "abstract structures", "system variables"],
        "b"
    ],
    [
        "What are users usually interested in when interacting with the user interface of an OS?",
        ["The raw hardware drivers", "The look and feel of the operating system", "The underlying byte code structures", "The total number of built-in keywords"],
        "b"
    ],
    [
        "Which of the following is NOT listed as one of the most important components of a user interface?",
        ["The command interpreter", "The file system", "The hardware registers", "On-line help"],
        "c"
    ],
    [
        "When a computer is powered on, where is the first program that runs usually kept?",
        ["On the hard disk drive", "In the computer's read-only memory (ROM)", "In the main random access memory (RAM)", "Within the network interface controller"],
        "b"
    ],
    [
        "What does the acronym POST stand for in the boot process sequence?",
        ["Primary Operating System Tracker", "Power-on self test", "Processor Optimization System Template", "Peripheral Output Serial Terminal"],
        "b"
    ],
    [
        "Which hardware components are checked for errors during the POST?",
        ["The monitor, mouse, and external printer", "The CPU, memory, and basic input-output system (BIOS)", "The text editors and local directory files", "The local network routers and proxy elements"],
        "b"
    ],
    [
        "Where are the results of the POST stored upon execution?",
        ["In a special memory location", "Directly into a text file on disk", "On a remote distributed server", "Inside the command interpreter queue"],
        "a"
    ],
    [
        "Software loaded in ROM is sometimes referred to as BIOS or:",
        ["middleware", "firmware", "hardware templates", "algorithmic code"],
        "b"
    ],
    [
        "What specific program has the single function of loading the operating system into memory?",
        ["The device driver subroutine", "The bootstrap loader", "The standard compiler module", "The system administrator account"],
        "b"
    ],
    [
        "What is established by the bootstrap loader to hold signals, flags, and semaphores?",
        ["The physical disk sectors", "Data structures used to communicate within and between subsystems", "The graphical user interface template", "The network file transfer protocols"],
        "b"
    ],
    [
        "Operating systems are categorized into four types based on what two factors?",
        ["The price of hardware and the programming language used", "The types of computer they control and the sort of applications they support", "The size of main memory and network cable type", "The date of software release and testing benchmarks"],
        "b"
    ],
    [
        "Which type of operating system is used to control machinery, scientific instruments, and industrial systems?",
        ["Time Sharing Operating System", "Single-User, Single-Tasking Operating System", "Real-Time Operating System (RTOS)", "Network Operating System"],
        "c"
    ],
    [
        "Why must an RTOS manage resources so that operations execute in precisely the same amount of time every single time?",
        ["To make the look and feel appealing", "Because variation in execution time in a complex machine could be catastrophic", "To allow multiple remote users to log in easily", "To minimize the use of read-only memory instructions"],
        "b"
    ],
    [
        "What is the operational guarantee provided by a 'hard' RTOS?",
        ["It guarantees that critical tasks are performed on time", "It guarantees that a graphical user interface is present", "It guarantees that it runs only on mainframe configurations", "It guarantees an infinite number of system processes"],
        "a"
    ],
    [
        "How does a 'soft' RTOS handle critical tasks compared to a hard RTOS?",
        ["It ignores critical tasks if resources are busy", "A critical task gets priority over others and retains it until completion", "It rejects any task that takes more than a microsecond", "It relies strictly on batch input queues"],
        "b"
    ],
    [
        "The Palm OS for Palm handheld computers is a classic example of what OS category?",
        ["Multi-User Operating System", "Single-User, Single-Tasking Operating System", "Distributed Operating System", "Real-Time Multi-programming System"],
        "b"
    ],
    [
        "Windows 98 and the Mac O.S. are categorized as what type of operating system?",
        ["Single-User, Multi-Tasking Operating System", "Single-User, Single-Tasking Operating System", "Distributed Uniprocessor Framework", "Batch Processing Environment"],
        "a"
    ],
    [
        "What must a multi-user operating system ensure regarding its users' programs?",
        ["That they all share the exact same variable spaces", "That each has sufficient and separate resources so a problem with one doesn't affect all", "That they are written in the same multi-paradigm language", "That they interact only via the background batch process queue"],
        "b"
    ],
    [
        "Which of the following is explicitly listed as a true multi-user operating system?",
        ["Windows 98", "Unix", "Palm OS", "Novell Netware"],
        "b"
    ],
    [
        "Why is the system administrator considered the only true user for Windows 2000 or Novell Netware in their fundamental design plan?",
        ["Because these systems cannot connect to a network interface", "Because remote logins are treated as a program being run by the administrative user", "Because they do not have a bootstrap loader subroutine", "Because they are classified strictly as hard real-time systems"],
        "b"
    ],
    [
        "Operating systems are classified into batch, time-shared, and real-time based on what specific nature?",
        ["The size of the physical storage components", "The nature of interaction between the computer user and his/her program during processing", "The number of independent processing units present in the hardware", "The specific PEP guide followed by the developer"],
        "b"
    ],
    [
        "In a batch processing environment, where are submitted jobs collected before being run?",
        ["Inside an interactive window", "Into a batch, and subsequently placed on an input queue", "Directly into the main memory random sectors", "On a network interface controller buffer"],
        "b"
    ],
    [
        "What constitutes the 'response time' in a Batch Processing OS?",
        ["A few seconds of screen interactive delay", "The turnaround time", "The time required to activate the ROM self-test", "The speed of the network data transfer"],
        "b"
    ],
    [
        "How do multiple users share resources concurrently in a Time Sharing OS environment?",
        ["In a manner facilitated, controlled, and monitored by the operating system", "By running tasks sequentially one day at a time", "By submitting physical punch cards to a central operator", "Through an automated sealed-box optimization algorithm"],
        "a"
    ],
    [
        "What is the expected response time of a computer program in a typical Time Sharing OS?",
        ["No more than a few seconds", "Exactly equal to the overall turnaround time", "Completely instantaneous with zero microseconds delay", "Varying from several hours to a business day"],
        "a"
    ],
    [
        "Airlines reservations and nuclear power station monitoring systems are examples of what OS application?",
        ["Batch Processing OS", "Real Time OS", "Single-User Single-Tasking OS", "Standard Network Interface Framework"],
        "b"
    ],
    [
        "What are real-time operating systems designed to be interrupted by?",
        ["An internal text editing routine", "An external signal that requires immediate attention", "An administrative user logging in via mixedCase variables", "A secondary compilation failure event"],
        "b"
    ],
    [
        "An operating system that provides more than one type of computing service simultaneously is called a:",
        ["uniprocessor", "hybrid", "sealed box", "decidable system"],
        "b"
    ],
    [
        "What type of system environment is commonly found running as a background task in hybrid operating systems?",
        ["A background batch system", "An active graphical user interface simulator", "A hard real-time mechanical controller", "An independent CPython virtual machine"],
        "a"
    ],
    [
        "What is a multiprogramming operating system?",
        ["A system with multiple physical computer towers connected by cords", "A system that allows more than one active user program to be stored in main memory simultaneously", "A system that runs exactly 35 distinct keywords at once", "A hardware configuration containing multiple CPUs"],
        "b"
    ],
    [
        "Complete the statement from the text: A time-sharing system is a multiprogramming system, but:",
        ["it cannot handle input/output operations", "a multiprogramming system is not necessarily a time-sharing system", "it is limited only to children's routine problem tasks", "it cannot function without a network controller interface"],
        "b"
    ],
    [
        "What defines a 'multiprocessing' system in terms of computer hardware configuration?",
        ["It consists of a single processor simulating a network environment", "It includes more than one independent processing unit", "It relies entirely on a background batch queue interface", "It stores files across distinct geographical text files"],
        "b"
    ],
    [
        "Where are large multiprocessing system hardware complexes generally found?",
        ["In small handheld electronic devices like Palm pilots", "In major scientific or commercial applications", "Inside the read-only memory architecture of local PCs", "Within the standard TKinter graphical library toolkit"],
        "b"
    ],
    [
        "What characterizes a Network Operating System in terms of user awareness?",
        ["Users are completely oblivious to the existence of separate computers", "Users are aware of the existence of multiple computers and can log in to remote machines", "Users interact with the system via a sealed-box interface only", "Users must manually input arithmetic symbols to shift file states"],
        "b"
    ],
    [
        "What extra feature must each computer's OS contain in a networked computing system besides stand-alone functionality?",
        ["Provisions for handling communication and transfer of programs and data", "A built-in CPython source code compiler", "A hard real-time execution constraint tracker", "An automated Fermi estimation template"],
        "a"
    ],
    [
        "Why are network operating systems not considered fundamentally different from single processor operating systems?",
        ["Because they do not allow remote file access", "Because their additions do not change the essential structure of the operating system", "Because they can only run batch processing operations", "Because they lack a command interpreter completely"],
        "b"
    ],
    [
        "How does a Distributed Operating System contrast sharply with a Network Operating System?",
        ["It forces users to look up files using physical index directories", "It appears to its users as a traditional uniprocessor system", "It can only handle simple single-tasking mobile devices", "It requires the system administrator to run all functions manually"],
        "b"
    ],
    [
        "In a true distributed system, what should users NOT be aware of?",
        ["The name of the operating system brand they are using", "Where their programs are being run or where their files are located", "The look and feel of their command interpreter integration", "The number of variables declared with underscores"],
        "b"
    ],
    [
        "Which core function of an operating system deals with the assignment of the processor to different tasks?",
        ["Memory management", "Processor management", "Input/output management", "File management"],
        "b"
    ],
    [
        "Which core function deals with the allocation of main memory and other storage areas to system and user programs?",
        ["Processor management", "Memory management", "File management", "Input/output management"],
        "b"
    ],
    [
        "What operating system function deals with the co-ordination and assignment of input and output devices?",
        ["File management", "Memory management", "Input/output management", "Priority system management"],
        "c"
    ],
    [
        "How does the file management function allow files to be easily changed and modified?",
        ["By running automatic self-tests on the hard drive", "Through the use of text editors or other file manipulation routines", "By re-compiling intermediate independent platform byte code", "Through the utilization of strict greedy heuristics"],
        "b"
    ],
    [
        "What does the OS use to determine and maintain the order in which jobs are executed?",
        ["An execution timeline matrix", "A priority system", "An NP-hard approximation guide", "An interactive inspection window"],
        "b"
    ],
    [
        "The OS facilitates easy communication between the computer system and which specific entity?",
        ["The physical network interface cable", "The computer operator (human)", "The internal TOML parser module", "The uniprocessor simulation model"],
        "b"
    ],
    [
        "Why can errors exist in operating system code despite pre-release testing?",
        ["Because they are written by human programmers who make mistakes", "Because hardware architectures change their physical shape", "Because the PEP 8 standards are constantly shifting", "Because algorithms never guarantee a definitive endpoint"],
        "a"
    ],
    [
        "What is a system crash defined as in the section on operating system flaws?",
        ["The physical damage caused by dropping a desktop system", "The act of a system freezing and becoming unresponsive, requiring a reboot", "The leakage of data to unauthorized network intruders", "The failure of a program to show quotation marks in an output window"],
        "b"
    ],
    [
        "What do unauthorized intruders attempt to exploit when they try to gain illegal access to a system?",
        ["Main storage memory divisions", "Security flaws", "The bootstrap loader semaphores", "The standard graphics library toolkit"],
        "b"
    ],
    [
        "What action is explicitly mentioned as helping keep your computer system secure from discovered flaws?",
        ["Re-formatting variable underscores", "Patching these flaws", "Utilizing introspection methods", "Shifting to single-tasking modes"],
        "b"
    ],

    # --- MODULE 2: PROBLEMS AND PROBLEM-SOLVING ---
    [
        "According to the text, what is the definition of a problem?",
        ["A failure in the bootstrap loader configuration", "A gap between where you are and where you would like to be", "An explicit set of instructions that yields errors", "A decision that lacks clear empirical variables"],
        "b"
    ],
    [
        "How is the phrase 'problem solving' defined in the text?",
        ["Knowing what to do when you don't know what to do", "Following an exact recipe to achieve a sub-optimal solution", "Representing data using mathematical templates exclusively", "Running a search on the Internet via an algorithmic tool"],
        "a"
    ],
    [
        "What is the prerequisite step before any problem-solving strategy can be applied to find a solution?",
        ["The code must be run in interactive mode", "The problem must first be clearly identified", "A group brainstorming session must be evaluated", "A Fermi estimate must be performed"],
        "b"
    ],
    [
        "What is a problem-solving strategy defined as?",
        ["A mental loophole used to bypass security controls", "A plan used to find a solution or overcome a challenge", "A mathematical formula verified by CPython execution", "An automatic symbol-based template response"],
        "b"
    ],
    [
        "Which well-known problem-solving strategy is explicitly mentioned as having an associated action plan?",
        ["Heuristic searching", "Trial and error", "Simulated annealing", "Hill-climbing"],
        "b"
    ],
    [
        "What type of problems represent issues that do NOT have clear goals, solution paths, or expected solutions?",
        ["Well-defined problems", "Ill-defined problems", "Routine business problems", "Decidable hardware computations"],
        "b"
    ],
    [
        "What type of problems have specific goals, clearly defined solutions, and clear expected solutions?",
        ["Ill-defined problems", "Well-defined problems", "NP-hard optimization problems", "Heuristic exploration models"],
        "b"
    ],
    [
        "Which of the following is NOT listed as a method of studying problem solving?",
        ["Introspection and simulation", "Computer modelling and experimentation", "Variable inspection in IDLE", "Abstract thinking and creativity"],
        "c"
    ],
    [
        "What is the first step in the problem-solving process?",
        ["Developing a flowchart", "Identifying a problem", "Prioritizing solutions", "Brainstorming rules"],
        "b"
    ],
    [
        "What is the 5th step outlined in the key steps of 'Problem Identification'?",
        ["Gather Information", "Develop a Problem Statement", "Analyze the Root Causes", "Recognize the Gap"],
        "b"
    ],
    [
        "According to 'Problem Solving Steps', what should you do the moment you experience a problem?",
        ["Write down a list of 100 questions", "Stop and think", "Reboot the entire operating system", "Apply trial and error immediately"],
        "b"
    ],
    [
        "Complete the quote highlighted in the text: 'A problem well-stated is a...'",
        ["solution guaranteed", "problem half-solved", "clear algorithm achieved", "goal fully transformed"],
        "b"
    ],
    [
        "What is Step 3 of the problem-solving steps?",
        ["Generate and evaluate potential solutions", "Transform the problem into a goal", "Prioritize the different solutions", "Implement the step-by-step plan"],
        "b"
    ],
    [
        "Which of the following is NOT listed under the specific Brainstorming Rules in Step 4?",
        ["Think of lots of ideas", "Criticize weak ideas immediately to save time", "Use your imagination", "Write down all ideas"],
        "b"
    ],
    [
        "According to the text, when may indistinct ideas be clarified during brainstorming?",
        ["As soon as the idea is uttered by a participant", "After all ideas have been exhausted", "Before any imagination is used", "Only when a supervisor criticizes the statement"],
        "b"
    ],
    [
        "What factors are explicitly listed as things that may affect a solution in Step 5 (Prioritizing)?",
        ["Variable spaces, compilers, and byte codes", "Timeframe, money, people, procedures, policies, and rules and regulations", "Software quality control and human programmer errors", "The number of active computer nodes in a network"],
        "b"
    ],
    [
        "What is the purpose of Step 7 in the problem-solving checklist?",
        ["To select the right mathematical template", "To assess and evaluate whether the problem has been solved", "To turn a procedure formally into a true algorithm", "To inspect the value within the interactive window"],
        "b"
    ],
    [
        "Problem solving is categorized into which two basic types?",
        ["Decidable and Undecidable", "Routine and non-routine", "Algorithmic and Heuristic", "Interactive and Editor-based"],
        "b"
    ],
    [
        "What defines routine problems?",
        ["Issues that are completely unique and have never been seen before", "Issues that occur regularly and have known solutions", "Problems that cannot be resolved using standard arithmetic", "Challenges that evoke a sudden 'eureka' discovery reaction"],
        "b"
    ],
    [
        "What can be used to solve repetitive, regular routine problems?",
        ["Heuristics seeking to discover", "Established procedures or standard operating procedures (SOPs)", "Abstract creative designs", "Trial and error strategies exclusively"],
        "b"
    ],
    [
        "At what age do children typically begin performing routine problem solving like separating toys?",
        ["Age 1 or 2", "Age 5 or 6", "Age 10 or 12", "Only when they enter preschool"],
        "b"
    ],
    [
        "Which of the following is an example of an adult routine problem regarding administrative tasks?",
        ["Fixing a printer that frequently jams", "Processing payroll or managing inventory", "Addressing common customer complaints", "Calculating the area of a non-standard triangle"],
        "b"
    ],
    [
        "Solving routine problems invariably involves using what?",
        ["Complex machine-learning models", "At least one of the four arithmetic operations (and/or ratio)", "Intuitive exploration scripts", "Turing machine decidability domains"],
        "b"
    ],
    [
        "According to the text, does being good at doing arithmetic guarantee success at solving routine problems?",
        ["Yes, because doing calculation is the main key", "No, the critical matter is knowing what arithmetic to do", "Yes, because pencil and paper methods prevent all flaws", "No, because routine problems never use numbers"],
        "b"
    ],
    [
        "The research evidence suggests that good routine problem solvers rely on representing what is going on by selecting from what?",
        ["A set of random guesses and checks", "A limited set of mathematical templates or models", "A collection of complex network protocols", "A document outlining PEP guidelines"],
        "b"
    ],
    [
        "How can complexity be achieved when dealing with routine problem solving?",
        ["Through multi-step problems or through Fermi problems", "By changing from lowercase to mixedCase variables", "By removing the bootstrap loader from memory storage", "Through the deployment of antivirus scanning code signatures"],
        "a"
    ],
    [
        "What characterizes Fermi problems?",
        ["The total lack of any goals or expected paths", "The need to estimate something and the need to obtain relevant data", "The usage of 35 standard language keywords exclusively", "The immediate application of Turing machine states"],
        "b"
    ],
    [
        "What specific example of a Fermi problem is provided in the text?",
        ["Fixing a jammed printer on a deadline", "How many cars are there in Manitoba?", "Placing numbers 1 to 9 along a triangle side", "Processing a store jacket sales promotion drop"],
        "b"
    ],
    [
        "Non-routine problem solving is mostly concerned with developing students':",
        ["mechanical calculation speed", "mathematical reasoning power and understanding math as a creative endeavour", "ability to memorize standard operating procedures (SOPs)", "skills in debugging syntax errors in local environments"],
        "b"
    ],
    [
        "Which instructional stage can teachers use non-routine problem solving for to introduce ideas?",
        ["MAINTAIN stage of teaching", "SET SCENE stage of teaching", "POST self-test stage of teaching", "DECIDABILITY domain stage"],
        "b"
    ],
    [
        "What type of reaction does non-routine problem solving evoke?",
        ["An 'Aha, I know what is going on here' reaction", "An 'I tried this and I tried that, and eureka, I finally figured it out' reaction", "A completely unresponsive system freeze reaction", "A predictable sub-optimal automated output loop"],
        "b"
    ],
    [
        "Which of the following strategies is NOT considered the core essence of non-routine problem solving, but rather just a preliminary step?",
        ["Looking for a pattern", "Reading the question carefully, drawing a diagram, or making a table", "Guessing and checking", "Working backwards from the goal state"],
        "b"
    ],
    [
        "Which non-routine problem strategy involves breaking up the main challenge?",
        ["Act it out or make a physical model", "Break up the problem into smaller ones and try to solve these first", "Make and solve a much tougher problem", "Look for a standard operating procedure matrix"],
        "b"
    ],

    # --- MODULE 3: METHODS OF SOLVING COMPUTING PROBLEMS ---
    [
        "What is an algorithm defined as?",
        ["An intuitive exploration path based on guesses", "A precise set of rules or procedures for solving a problem or completing a task", "A general mental shortcut that skips steps", "A graphical user interface toolkit layout plan"],
        "b"
    ],
    [
        "An algorithm consists of a sequence of steps with a starting point and what?",
        ["An unpredictable loop path", "A known endpoint", "An infinite runtime timeline", "A sub-optimal choice template"],
        "b"
    ],
    [
        "Why can you think of an algorithm as a highly detailed recipe?",
        ["Because it relies on individual intuition", "Because it produces the same result every time it is performed", "Because it cannot be mathematically proven by code", "Because it represents an NP-hard optimization problem"],
        "b"
    ],
    [
        "What is the core trade-off when using a heuristic problem-solving approach?",
        ["The trade-off between user interface and security", "The trade-off between precision and speed", "The trade-off between memory and storage files", "The trade-off between underscores and mixedCase names"],
        "b"
    ],
    [
        "Besides the precision-speed trade-off, what are two other points to consider with heuristics?",
        ["Syntax and logic completeness", "Completeness and optimality", "Abstraction and encapsulation", "Serialization and data compression"],
        "b"
    ],
    [
        "Why can't heuristics be mathematically proven?",
        ["Because they always use more than 35 keywords", "Because the methodology used is often based on intuition and explorations", "Because they are written solely in intermediate platform byte code", "Because they are limited to uniprocessor execution matrices"],
        "b"
    ],
    [
        "While an algorithm must be followed exactly, a heuristic is a general:",
        ["unsolvable computation status", "problem-solving framework", "finite sequence pattern", "rigid standard operating procedure"],
        "b"
    ],
    [
        "Heuristics can be thought of as ________ used to solve problems.",
        ["exact formulas", "mental shortcuts", "hardware drivers", "system abstractions"],
        "b"
    ],
    [
        "How many explicit conditions trigger the impulse to use a heuristic according to the text?",
        ["Three conditions", "Five conditions", "Eight conditions", "Thirty-five conditions"],
        "b"
    ],
    [
        "Which condition would prompt someone to use a heuristic framework?",
        ["When faced with absolutely no information at all", "When the time to make a decision is limited", "When the decision to be made is highly critical and dangerous", "When there is an exact formula template available"],
        "b"
    ],
    [
        "Why are heuristics highly attractive in computing applications?",
        ["Because they guarantee an optimal answer mathematically", "Because they find solutions in a timely manner", "Because they completely eliminate human programmer mistakes", "Because they prevent the need to reboot during freezes"],
        "b"
    ],
    [
        "What is the primary objective of the Traveling Salesperson Problem (TSP)?",
        ["To sort a list of numbers using MergeSort", "To find an optimal route between a set of nodes", "To scan source files for virus code signatures", "To transition control from ROM over to the main OS"],
        "b"
    ],
    [
        "How is the Traveling Salesperson Problem classified in terms of computation difficulty?",
        ["Decidable and basic", "NP-hard", "Unsolvable status forever", "Routine arithmetic template"],
        "b"
    ],
    [
        "What type of algorithms attempt to find locally optimal solutions at each stage?",
        ["Distributed algorithms", "Greedy algorithms", "Binary Search algorithms", "Sorting algorithms"],
        "b"
    ],
    [
        "What is the underlying assumption when applying greedy algorithms?",
        ["That an optimal solution is never possible", "That a set of locally optimal solutions may eventually lead to a globally optimal solution", "That the runtime will match the turnaround time of batch work", "That the system will freeze unless given a heuristic shortcut"],
        "b"
    ],
    [
        "How does antivirus software apply heuristics when scanning for threats?",
        ["By executing every single file to see if it crashes", "By searching for samples of code that resemble viruses in files", "By forcing the CPU to run a power-on self test sequence", "By checking if file names use lowercase with underscores"],
        "b"
    ],
    [
        "Which of the following is listed as an additional application of heuristics?",
        ["QuickSort or MergeSort processing", "Searching, simulated annealing, and hill-climbing", "Binary Search over sorted data inputs", "Greatest common divisor computation routines"],
        "b"
    ],
    [
        "In comparing algorithms and heuristics, how do they differ regarding a guarantee?",
        ["Heuristics guarantee optimal paths; algorithms do not", "Algorithms guarantee a solution; heuristics do not", "Both guarantee an optimal result in a finite period", "Neither can provide any assurance of reaching an endpoint"],
        "b"
    ],
    [
        "What type of result will a heuristic usually yield?",
        ["A mathematically perfect result", "A sub-optimal result", "An error compilation exception", "An undecidable logic infinity state"],
        "b"
    ],
    [
        "In computer science, problems are classified as solvable or unsolvable based on whether there exists what?",
        ["A proper graphical user interface look", "An algorithm that can provide a solution", "A network interface controller chip", "A group of people brainstorming ideas"],
        "b"
    ],
    [
        "A problem is considered solvable if there exists a potential solution that can find its answer in:",
        ["exactly a few seconds", "a finite amount of time", "an infinite timeline loop", "the turnaround timeframe baseline"],
        "b"
    ],
    [
        "Which of the following is listed as an explicit example of a solvable problem?",
        ["The Entscheidungsproblem paradox", "Sorting algorithms like QuickSort or MergeSort", "The permanent unsolvable instance loop", "Predicting an undecidable runtime timeline"],
        "b"
    ],
    [
        "What searching algorithm is listed as an example of a solvable computation?",
        ["Heuristic hill-climbing", "Binary Search", "Greedy city tracking", "Simulated sorting models"],
        "b"
    ],
    [
        "What mathematical problem is explicitly provided as a solvable computation example?",
        ["Estimating cars in Manitoba", "Finding the greatest common divisor (GCD) of two numbers", "Proving first-order logic universally valid", "Solving ill-defined workplace deadlines"],
        "b"
    ],
    [
        "What is the nature of an unsolvable status in computer science according to the text description?",
        ["It means the problem is missing text editors", "It can be a temporary status of the problem for a given input at an instant of time", "It means the problem was written by a human programmer who made typos", "It implies the problem requires simple arithmetic operations only"],
        "b"
    ],
    [
        "What famous problem is mentioned as an example under unsolvable problems?",
        ["The Traveling Salesperson Problem (TSP)", "The Entscheidungsproblem", "The Fermi car estimation query", "The jacket price drop promotion task"],
        "b"
    ],
    [
        "Solvable problems themselves are broadly divided into what two categories?",
        ["Routine and non-routine frameworks", "Decidable and Undecidable", "Algorithmic and Heuristic plans", "Interactive and script-based windows"],
        "b"
    ],
    [
        "To understand the depth of the decidability domain, a good knowledge of which theoretical machine model is required?",
        ["The Palm OS terminal model", "The Turing Machine", "The CPython virtual reference engine", "The network interface configuration server"],
        "b"
    ],
    [
        "What two important terms are used specifically when talking about decidable problems?",
        ["Underscores and mixedCase names", "Algorithms and procedures", "Intuition and exploration models", "Completeness and optimality guidelines"],
        "b"
    ],
    [
        "According to the decidability domain definition, when does a procedure formally become an algorithm?",
        ["When it is tested by a software quality control company", "When we say what is the approximate time to solve a problem", "When it incorporates intuitive guesses and checks", "When it is written inside a standard library package"],
        "b"
    ],
    [
        "What characterizes an 'Undecidable Problem' regarding its execution timeline?",
        ["It executes in precisely the same amount of time every single instance", "We cannot predict the time of the problem in which it can be solved", "It has a known turnaround baseline exactly under a few seconds", "It matches the POST self-test configuration framework duration"],
        "b"
    ],

    # --- PYTHON PROGRAMMING SECTIONS ---
    [
        "What is the newly added module in Python's standard library mentioned in the future text?",
        ["tkinter", "tomllib", "pandas", "numpy"],
        "b"
    ],
    [
        "What language format can be parsed using the functions inside the new tomllib module?",
        ["JSON script templates", "TOML (Tom's Obvious Minimal Language)", "XML markup tags", "HTML application files"],
        "b"
    ],
    [
        "What is the core focus of Python's developer community regarding upcoming updates?",
        ["Adding more than 100 keywords to the syntax list", "Performance improvements making it more efficient while retaining ease of use", "Phasing out object-oriented structures completely", "Restricting the software to only Windows architectures"],
        "b"
    ],
    [
        "Python is heavily utilized in which of the following rapidly growing fields?",
        ["Sealed-box real-time machinery manufacturing", "Machine learning, AI, and data science", "Traditional uniprocessor batch file queue formatting", "Industrial mechanical instrument timing loops"],
        "b"
    ],
    [
        "What factor is solidifying Python's long-term place in the global technology landscape?",
        ["It is increasingly becoming the first programming language taught in schools and universities", "It completely forbids the use of variable underscores", "It avoids the use of modules or external packages entirely", "It guarantees an absolute optimal solution for NP-hard challenges"],
        "b"
    ],
    [
        "Which of the following descriptions matches the core programming features of Python?",
        ["Low-level compiled assembly blueprint configuration language", "Feature-rich, high-level, interpreted, interactive, and object-oriented", "Strictly single-paradigm non-interactive text-based framework", "Sealed-box real-time automated macro system code"],
        "b"
    ],
    [
        "Why is Python's interactive mode considered especially useful for developers?",
        ["It compiles code directly into unchangeable ROM firmware", "To get familiar with a library and test out its functionality", "It bypasses the need for any computer operating system platform", "It automatically checks the system hardware architecture for errors"],
        "b"
    ],
    [
        "What can you test out in the interactive mode before committing to writing a full program?",
        ["Complete mainframe configurations", "Small code snippets", "NP-hard optimization limits", "Decidable procedure models"],
        "b"
    ],
    [
        "What completely object-oriented rule applies to everything within a Python program?",
        ["Everything is a string literal", "Everything in a Python program is an object", "Everything must be written using mixedCase tags", "Everything must contain at least one comment tag"],
        "b"
    ],
    [
        "Python conveniently encapsulates its object orientation to allow it to be used as what kind of language?",
        ["An imperative or procedural language – such as C", "A pure hardware machine instruction language", "A hard real-time mechanical scripting syntax", "An undecidable logic equation simulation format"],
        "a"
    ],
    [
        "How many keywords does the Python software standard distribution have?",
        ["Only Twelve keywords", "Only Thirty-Five keywords", "Exactly Eighty-five keywords", "Over One hundred keywords"],
        "b"
    ],
    [
        "What philosophy describes Python's rich distributed environment of modules and packages?",
        ["Sealed box delivery", "Batteries included approach", "Greedy local search model", "Trial and error framework"],
        "b"
    ],
    [
        "Which of the following is NOT listed as one of Python's popular standard modules?",
        ["NumPy or Pandas", "Matplotlib or Math", "Tkinter", "Novell Netware Tracker"],
        "d"
    ],
    [
        "From where can Python's standard distribution be downloaded without any restrictions?",
        ["https://www.python.org/downloads/", "A remote distributed network server drive path", "The CUsersGraceDesktop folder structure", "The read-only memory bootstrap loader storage"],
        "a"
    ],
    [
        "What license governs the distribution of Python software and its official documentation?",
        ["MVS Mainframe Proprietary License", "Python Software Foundation License", "Standard Sealed Box Commercial Agreement", "Novell Netware Security Template Document"],
        "b"
    ],
    [
        "The Python Software Foundation License is a BSD-style permissive software license compatible with which of the following?",
        ["Novell Network OS Protocol", "GNU GPL (General Public License)", "Palm OS Firmware Architecture", "Entscheidungsproblem Universally Valid First-Order Rules"],
        "b"
    ],
    [
        "What is the official reference implementation of Python called?",
        ["Jython", "CPython", "IPython", "PySimpleGUI"],
        "b"
    ],
    [
        "In what programming language is the reference implementation CPython written?",
        ["Written entirely in Java", "Written in C", "Written in C#", "Written in Assembly"],
        "b"
    ],
    [
        "A Python program is first compiled into what intermediate format before execution?",
        ["A raw hardware register instruction set", "Platform independent byte code", "An optimal heuristic route array", "A text file variable statement config"],
        "b"
    ],
    [
        "What entity inside the interpreter executes the compiled intermediate byte code?",
        ["The physical network interface controller", "The virtual machine", "The bootstrap loader subroutine", "The command interpreter user profile"],
        "b"
    ],
    [
        "What excellent graphics library is included in Python's standard distribution for GUI needs?",
        ["PyQt", "Tkinter", "WxWidgets", "PySimpleGUI"],
        "b"
    ],
    [
        "Tkinter is a Python port for which vastly popular GUI toolkit?",
        ["TCL/Tk", "C/C++ Graphics Core", "Jython UI Elements", "IDLE Script Framework"],
        "a"
    ],
    [
        "What specific set of specifications allows Python to communicate with relational databases?",
        ["PEP 8 Guide Documents", "DB-API", "TOML Parser Functions", "C-API Extensibility Models"],
        "b"
    ],
    [
        "With many third-party libraries, Python can work with which NoSQL database explicitly named?",
        ["SQL Server", "MongoDB", "Oracle DB", "PostgreSQL"],
        "b"
    ],
    [
        "What does the term 'extensibility' imply regarding software features?",
        ["The restriction of execution to a single user uniprocessor", "The ability to add new features or modify existing features", "The trade-off between execution speed and disk file sizing", "The strict verification of NP-hard mathematical problems"],
        "b"
    ],
    [
        "What alternative implementation of Python is written specifically in Java?",
        ["CPython", "Jython", "IPython", "IronPython"],
        "b"
    ],
    [
        "Describe the 'mixedCase' variable naming system used in many other programming languages.",
        ["You leave every letter in lowercase and separate each word with an underscore", "You capitalize the first letter of every word except the first and leave all other letters in lowercase", "You capitalize every single letter across all declared words", "You append a pound symbol hashtag at the front of the variable"],
        "b"
    ],
    [
        "In Python variable naming conventions, what system is more commonly used?",
        ["mixedCaseSystem", "lower_case_with_underscores", "UPPERCASE_WITH_HASH", "CamelCaseFormat"],
        "b"
    ],
    [
        "What document codifies the lowercase with underscores convention as the official style guide for writing Python?",
        ["PEP 24", "PEP 8", "GPL License V3", "PSF Documentation Index"],
        "b"
    ],
    [
        "What does the abbreviation PEP stand for in the Python development community?",
        ["Program Execution Procedure", "Python Enhancement Proposal", "Processor Efficiency Protocol", "Peripheral Extension Package"],
        "b"
    ],
    [
        "What is the ultimate purpose of following the layout standards outlined in PEP 8?",
        ["It ensures that your Python code is readable by most Python programmers", "It forces the virtual machine to run twice as fast", "It allows the code to access NoSQL databases without a driver", "It automatically adds inline block comments to your strings"],
        "a"
    ],
    [
        "What happens when you type a variable name like 'greeting' and press Enter in IDLE's interactive window?",
        ["A system crash exception is triggered", "Variable inspection displays the value as it appears in the code", "The interpreter clears out the main memory storage", "A print subroutine is permanently added to the editor file"],
        "b"
    ],
    [
        "Why does inspecting 'x' show '2' while inspecting 'y' shows ''2'' with single quotes in the interactive window?",
        ["Because x is a string and y is a standard math template", "Because 2 is a number and '2' is a string literal text", "Because the print function alters the internal values dynamically", "Because the PEP 8 guide mandates single quotation marks for all digits"],
        "b"
    ],
    [
        "What is the key takeaway difference between using print() and performing variable inspection?",
        ["print() can only be executed inside a bootstrap loader routine", "print() displays a readable representation, while inspection displays the value as it appears in the code", "Inspection works across both editor and interactive windows seamlessly", "print() requires a NoSQL DB specifications connection to display strings"],
        "b"
    ],
    [
        "Where does variable inspection work exclusively?",
        ["Inside the background batch processing system queue", "Only in the interactive window", "Within the main text editor script window before execution", "Inside a sealed-box RTOS terminal interface"],
        "b"
    ],
    [
        "What happens if you type a variable name alone on a line inside the editor window and run the program?",
        ["The program crashes with a fatal bug", "The program executes without any errors, but it doesn’t display any output", "The system displays the value wrapped in single quotes", "It opens an on-line help user interface component automatically"],
        "b"
    ]
]