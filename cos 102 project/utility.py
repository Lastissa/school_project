
#the questions for quiz app - i used AI to generate question to save time and more pool to randomize from
class Question:
    def __init__(self):
        self.format = """[["Question", ["Option 1", "Option 2", "Option 3", "Option 4"], "Answer"]]"""
        self.cos102_lenght = len(self.cos102())
        self.mth114_lenght = len(self.mth114())
        self.sta112_lenght = len(self.sta112())
        
    def cos102(self):
      return [
        #defination and objective of operating system
        [
            "Why is an Operating System often referred to as infrastructure software?",
            [
                "It provides a platform upon which other software can operate",
                "It serves as the physical foundation of the computer system",
                "It is responsible for designing hardware infrastructure",
                "It enables direct communication between processors and users"
            ],
            "a"
        ],
        [
            "Which statement best describes the role of an Operating System as a host?",
            [
                "It executes application programs while shielding them from hardware complexities",
                "It translates high-level languages into machine code during execution",
                "It provides permanent storage for application programs",
                "It controls only the input devices used by applications"
            ],
            "a"
        ],
        [
            "The Operating System relieves application programs from managing hardware details primarily to:",
            [
                "Increase processor speed",
                "Reduce the complexity of application development",
                "Eliminate the need for device drivers",
                "Allow applications to directly access hardware resources"
            ],
            "b"
        ],
        [
            "When viewed as a Resource Manager, an Operating System is mainly concerned with:",
            [
                "Providing a user-friendly abstraction of hardware",
                "Efficient allocation and coordination of available resources",
                "Translating source code into executable programs",
                "Providing internet connectivity to users"
            ],
            "b"
        ],
        [
            "The Extended Machine view of an Operating System emphasizes its ability to:",
            [
                "Manage competing requests for hardware resources",
                "Present users with a more convenient virtual environment",
                "Optimize processor scheduling algorithms",
                "Control the physical architecture of the machine"
            ],
            "b"
        ],
        [
            "Which of the following best illustrates the Operating System's role in resource sharing?",
            [
                "Providing a mechanism through which limited resources can be coordinated among programs",
                "Increasing the physical amount of memory available in the computer",
                "Allowing each application unrestricted access to all hardware resources",
                "Replacing hardware limitations with software solutions"
            ],
            "a"
        ],
        [
            "The relationship between hardware and application software is typically mediated by:",
            [
                "The Operating System",
                "The Compiler",
                "The BIOS only",
                "The File System"
            ],
            "a"
        ],
        [
            "Which task is most directly associated with memory management in an Operating System?",
            [
                "Allocating memory resources to processes as needed",
                "Converting data into binary representation",
                "Expanding physical RAM capacity",
                "Managing network transmission protocols"
            ],
            "a"
        ],
        [
            "An Operating System's responsibility for prioritizing system requests is primarily intended to:",
            [
                "Ensure orderly and efficient system operation",
                "Increase storage capacity",
                "Reduce the need for application software",
                "Improve monitor display quality"
            ],
            "a"
        ],
        [
            "Which statement most accurately distinguishes the Resource Manager and Extended Machine views of an Operating System?",
            [
                "One focuses on efficient resource utilization, while the other focuses on user convenience",
                "One focuses on hardware design, while the other focuses on software design",
                "One is concerned with networking, while the other is concerned with storage",
                "One applies to single-user systems, while the other applies to multi-user systems"
            ],
            "a"
        ],
        [
            "The Operating System forms a platform for both system software and application software because it:",
            [
                "Provides fundamental services required for software execution",
                "Contains all application software within its kernel",
                "Eliminates the need for hardware resources",
                "Compiles every software program before execution"
            ],
            "a"
        ],
        [
            "Which of the following activities would NOT normally be regarded as a core function of an Operating System?",
            [
                "Managing file systems",
                "Allocating memory resources",
                "Facilitating network communication",
                "Developing application software"
            ],
            "d"
        ],
        [
            "In the context of operating systems, an abstraction is best described as:",
            [
                "The replacement of hardware with software components",
                "The hiding of lower-level details while providing higher-level functionality",
                "The direct exposure of hardware resources to users",
                "The conversion of physical memory into virtual memory"
            ],
            "b"
        ],
        [
            "Which statement best explains why operating systems use abstraction?",
            [
                "To eliminate the need for hardware devices",
                "To ensure all peripheral devices are manufactured identically",
                "To shield programs from unnecessary hardware-specific details",
                "To allow applications to communicate directly with hardware"
            ],
            "c"
        ],
        [
            "Device drivers are introduced by the operating system primarily because:",
            [
                "Peripheral device control is not standardized",
                "Processes require independent memory spaces",
                "File systems need protection from users",
                "Graphical interfaces require additional hardware"
            ],
            "a"
        ],
        [
            "The file abstraction provided by an operating system mainly prevents programs from having to deal directly with:",
            [
                "Processes",
                "Memory allocation",
                "Disks and storage details",
                "User interfaces"
            ],
            "c"
        ],
        [
            "When an operating system transforms one physical computer into multiple virtual computers, each virtual computer is associated with a:",
            [
                "File",
                "Driver",
                "Process",
                "Resource"
            ],
            "c"
        ],
        [
            "A process views hardware through the lens of abstraction because the operating system:",
            [
                "Replaces the hardware completely",
                "Provides an abstracted representation of underlying resources",
                "Restricts all access to hardware",
                "Stores all hardware instructions in memory"
            ],
            "b"
        ],
        [
            "Which of the following is NOT presented in the text as a reason for abstraction?",
            [
                "Providing device drivers for non-standardized peripherals",
                "Introducing file abstractions",
                "Enforcing security mechanisms",
                "Increasing processor clock speed"
            ],
            "d"
        ],
        [
            "The ability of an operating system to enforce security is linked in the text to its use of:",
            [
                "Resource allocation",
                "Abstraction",
                "Application integration",
                "Command interpretation"
            ],
            "b"
        ],
        [
            "In resource management, processes are described as:",
            [
                "Passive entities",
                "Hardware abstractions",
                "Active agents",
                "System resources"
            ],
            "c"
        ],
        [
            "According to the text, resources are best described as:",
            [
                "Active entities that request services",
                "Virtual computers created by the operating system",
                "Passive entities accessed by processes",
                "Programs executing in memory"
            ],
            "c"
        ],
        [
            "The primary purpose of resource management is to control:",
            [
                "How users interact with applications",
                "How processes access resources",
                "How files are displayed to users",
                "How drivers communicate with hardware"
            ],
            "b"
        ],
        [
            "A user is primarily concerned with the operating system's 'look and feel' through the:",
            [
                "Resource manager",
                "User interface",
                "Device drivers",
                "Process scheduler"
            ],
            "b"
        ],
        [
            "Which of the following is identified as an important component of the user interface?",
            [
                "Device driver",
                "Memory manager",
                "Command interpreter",
                "Process control block"
            ],
            "c"
        ],
        [
            "Which component would most directly help a user understand available operating system commands?",
            [
                "Application integration",
                "On-line help",
                "Resource allocation",
                "Process abstraction"
            ],
            "b"
        ],
        [
            "A trend toward increasingly integrated graphical user interfaces suggests that modern interfaces:",
            [
                "Focus exclusively on local applications",
                "Reduce interaction among processes",
                "Support activities involving multiple processes and networks",
                "Eliminate command interpreters completely"
            ],
            "c"
        ],
        [
            "Which option correctly matches an operating system goal with its purpose?",
            [
                "Abstraction — controlling how processes access resources",
                "Resource management — controlling access to passive entities",
                "User interface — creating virtual computers for processes",
                "Abstraction — improving the appearance of graphical interfaces"
            ],
            "b"
        ],
        [
            "A student claims that files, processes, and security are unrelated concepts. Based on the text, this claim is incorrect because all three are connected through:",
            [
                "Abstraction provided by the operating system",
                "Resource allocation policies",
                "Graphical user interfaces",
                "Command interpretation"
            ],
            "a"
        ],
        [
            "Which situation best demonstrates the operating system hiding hardware details?",
            [
                "A user opening a file without knowing its disk location",
                "A process competing for CPU time",
                "A scheduler allocating resources",
                "A network connecting two computers"
            ],
            "a"
        ],
        [
            "If a process could access hardware only through abstractions provided by the operating system, the process would primarily interact with:",
            [
                "Virtualized representations of resources",
                "Raw hardware instructions",
                "Physical device circuitry",
                "Machine-level control signals"
            ],
            "a"
        ],
        #type of operating system based on the type of application they support
        [
            "Which characteristic most accurately defines a Real-Time Operating System (RTOS)?",
            [
                "Tasks execute in the shortest possible time",
                "Tasks execute within predictable timing constraints",
                "Multiple users can access the system simultaneously",
                "The system supports only one running application"
            ],
            "b"
        ],
        [
            "Why is predictability more important than speed in many real-time systems?",
            [
                "System resources are always limited",
                "An operation occurring too early can be as harmful as occurring too late",
                "Real-time systems do not use processors",
                "Predictability reduces memory consumption"
            ],
            "b"
        ],
        [
            "What distinguishes a hard RTOS from a soft RTOS?",
            [
                "Hard RTOS guarantees timing requirements for critical tasks",
                "Hard RTOS supports more users than soft RTOS",
                "Hard RTOS contains a graphical interface while soft RTOS does not",
                "Hard RTOS executes all tasks faster than soft RTOS"
            ],
            "a"
        ],
        [
            "A critical task in a soft RTOS typically:",
            [
                "Runs only when the system is idle",
                "Receives priority over non-critical tasks until completion",
                "Shares equal priority with every task",
                "Can be interrupted by any lower-priority task"
            ],
            "b"
        ],
        [
            "Which operating system category is designed for one user performing one task at a time?",
            [
                "Multi-user",
                "Single-user multitasking",
                "Single-user single-tasking",
                "Real-time"
            ],
            "c"
        ],
        [
            "A user editing a document, listening to music, and browsing the web simultaneously is using a system that supports:",
            [
                "Single-tasking",
                "Single-user multitasking",
                "Hard real-time processing",
                "Multi-user processing"
            ],
            "b"
        ],
        [
            "What is the primary responsibility of a multi-user operating system?",
            [
                "Executing only one program at a time",
                "Balancing resource allocation among multiple users",
                "Providing real-time guarantees",
                "Limiting access to a single administrator"
            ],
            "b"
        ],
        [
            "Why are resources allocated separately to users in a multi-user operating system?",
            [
                "To increase processor speed",
                "To prevent one user's activities from affecting others",
                "To eliminate the need for memory management",
                "To simplify network configuration"
            ],
            "b"
        ],
        [
            "Which statement correctly distinguishes a multi-user operating system from a single-user operating system with network support?",
            [
                "Only a multi-user operating system is designed to manage multiple users as operating system users",
                "Only a single-user operating system can support remote logins",
                "Multi-user operating systems cannot support networking",
                "Single-user operating systems cannot support multiple connections"
            ],
            "a"
        ],
        [
            "Which pair of operating systems belong to different task-management categories despite both supporting a single user?",
            [
                "Palm OS and Windows 98",
                "Unix and VMS",
                "MVS and Unix",
                "Windows 2000 and NetWare"
            ],
            "a"
        ],
        [
            "Which operating system environment typically requires users to submit jobs that are later collected into a queue for execution?",
            [
                "Real-Time OS",
                "Time-Sharing OS",
                "Batch Processing OS",
                "Distributed OS"
            ],
            "c"
        ],
        [
            "What best characterizes user involvement during job execution in a Batch Processing Operating System?",
            [
                "Continuous interaction throughout execution",
                "Limited interaction during execution",
                "No interaction during execution",
                "Interaction only when errors occur"
            ],
            "c"
        ],
        [
            "In a Batch Processing Operating System, the most appropriate measure of response is:",
            [
                "Waiting time",
                "Execution time",
                "Turnaround time",
                "Interrupt time"
            ],
            "c"
        ],
        [
            "Turnaround time in a batch environment refers to the time between:",
            [
                "System startup and shutdown",
                "Job submission and availability of results",
                "Program loading and execution",
                "Interrupt generation and handling"
            ],
            "b"
        ],
        [
            "A key distinction between Batch Processing and Time-Sharing Operating Systems is that:",
            [
                "Only batch systems use memory",
                "Only time-sharing systems support processors",
                "Time-sharing systems permit interaction during execution",
                "Batch systems cannot process jobs"
            ],
            "c"
        ],
        [
            "In a Time-Sharing Operating System, users primarily share:",
            [
                "Only storage devices",
                "Only input devices",
                "Processor, memory, and other system resources",
                "Application software exclusively"
            ],
            "c"
        ],
        [
            "The operating system's role in a time-sharing environment is to:",
            [
                "Compile user programs",
                "Facilitate, control, and monitor resource sharing",
                "Eliminate resource competition",
                "Assign a dedicated processor to each user"
            ],
            "b"
        ],
        [
            "A user editing a file while simultaneously interacting with a running program is most characteristic of:",
            [
                "Batch Processing",
                "Time-Sharing",
                "Firmware Control",
                "Single-Tasking"
            ],
            "b"
        ],
        [
            "The expected response time in a Time-Sharing Operating System is generally:",
            [
                "Several hours",
                "Measured by turnaround time only",
                "No more than a few seconds",
                "Independent of user interaction"
            ],
            "c"
        ],
        [
            "Which operating system type is specifically designed for applications where delayed responses may lead to errors or disasters?",
            [
                "Batch Processing OS",
                "Single-Tasking OS",
                "Real-Time OS",
                "Time-Sharing OS"
            ],
            "c"
        ],
        [
            "The defining feature of a Real-Time Operating System is its emphasis on:",
            [
                "Large storage capacity",
                "Fast graphics rendering",
                "Immediate and predictable response",
                "Multi-user support"
            ],
            "c"
        ],
        [
            "An airline reservation system is most appropriately associated with:",
            [
                "Batch Processing",
                "Real-Time Processing",
                "Single-User Processing",
                "Offline Processing"
            ],
            "b"
        ],
        [
            "Monitoring a nuclear power station requires a Real-Time Operating System primarily because:",
            [
                "Many users access the system simultaneously",
                "Jobs must be executed in batches",
                "Critical events require immediate attention",
                "Large files must be processed"
            ],
            "c"
        ],
        [
            "Real-Time Operating Systems are commonly designed to respond to:",
            [
                "Background jobs",
                "External signals requiring immediate attention",
                "Periodic file backups",
                "User logins only"
            ],
            "b"
        ],
        [
            "Which characteristic is shared by both Time-Sharing and Real-Time Operating Systems?",
            [
                "Users have no interaction during execution",
                "Responsiveness is an important consideration",
                "Jobs are always executed in batches",
                "Turnaround time is the primary performance measure"
            ],
            "b"
        ],
        [
            "Which pair of operating system types differs most significantly in the level of user interaction during program execution?",
            [
                "Batch Processing and Time-Sharing",
                "Time-Sharing and Real-Time",
                "Real-Time and Hybrid",
                "Batch Processing and Hybrid"
            ],
            "a"
        ],
        [
            "A system designed to process payroll at the end of each month with no user interaction during execution is most likely a:",
            [
                "Time-Sharing System",
                "Real-Time System",
                "Batch Processing System",
                "Interactive System"
            ],
            "c"
        ],
        [
            "Many modern operating systems are described as hybrids because they:",
            [
                "Support only one processing model at a time",
                "Combine features of multiple operating system types",
                "Alternate between hardware and software control",
                "Operate without user intervention"
            ],
            "b"
        ],
        [
            "Which combination is explicitly identified as being commonly found in hybrid systems?",
            [
                "Real-Time processing with no background tasks",
                "A background batch system operating alongside another processing mode",
                "Single-tasking and firmware execution",
                "Hard RTOS and Soft RTOS running simultaneously"
            ],
            "b"
        ],
        #Other Types of OS based on the Definition of the System/Environment
        [
            "Which statement best defines a multiprogramming operating system?",
            [
                "A system that allows multiple processors to execute tasks simultaneously",
                "A system that keeps more than one active user program in main memory at the same time",
                "A system that allows multiple users to log in remotely",
                "A system that distributes jobs across several computers"
            ],
            "b"
        ],

        [
            "A time-sharing operating system is always:",
            [
                "A multiprocessing system",
                "A distributed system",
                "A multiprogramming system",
                "A network operating system"
            ],
            "c"
        ],

        [
            "Which statement about multiprogramming and time-sharing is correct?",
            [
                "Every multiprogramming system is a time-sharing system",
                "Multiprogramming and time-sharing mean exactly the same thing",
                "A time-sharing system is a multiprogramming system, but not all multiprogramming systems are time-sharing systems",
                "Neither concept is related to the other"
            ],
            "c"
        ],

        [
            "Which operating system type can contain multiple active user programs in memory without necessarily being time-sharing?",
            [
                "Only batch operating systems",
                "Only real-time operating systems",
                "Batch and real-time operating systems",
                "Only network operating systems"
            ],
            "c"
        ],

        [
            "The primary distinction between multiprogramming and multiprocessing is that multiprogramming refers to:",
            [
                "An operating system concept, while multiprocessing refers to a hardware configuration",
                "A hardware configuration, while multiprocessing refers to an operating system concept",
                "Multiple users sharing resources",
                "Multiple computers sharing files"
            ],
            "a"
        ],

        [
            "A multiprocessing system is characterized by the presence of:",
            [
                "Several active programs in memory",
                "Multiple independent processing units",
                "Several networked computers",
                "Multiple logged-in users"
            ],
            "b"
        ],

        [
            "Multiprocessing is most commonly associated with:",
            [
                "Handheld devices",
                "Single-user desktop systems",
                "Large scientific and commercial computer systems",
                "Real-time embedded controllers"
            ],
            "c"
        ],

        [
            "A networked computing system consists primarily of:",
            [
                "Several processors inside one computer",
                "Several physically interconnected computers",
                "Several active programs in memory",
                "Several users sharing a terminal"
            ],
            "b"
        ],

        [
            "In a network operating system, users are generally:",
            [
                "Unaware that multiple computers exist",
                "Aware of multiple computers and can access remote machines",
                "Restricted to local resources only",
                "Unable to transfer files between computers"
            ],
            "b"
        ],

        [
            "The ability to log in to another machine and copy files between systems is a characteristic of:",
            [
                "A network operating system",
                "A batch operating system",
                "A single-tasking operating system",
                "A hard real-time operating system"
            ],
            "a"
        ],

        [
            "In a network operating system, each machine typically:",
            [
                "Runs a single shared operating system",
                "Has no local users",
                "Runs its own local operating system",
                "Depends entirely on a central processor"
            ],
            "c"
        ],

        [
            "Which additional capability must a network operating system provide beyond stand-alone functionality?",
            [
                "Automatic processor replication",
                "Communication and transfer of programs and data between connected computers",
                "Conversion into a distributed system",
                "Replacement of local storage devices"
            ],
            "b"
        ],

        [
            "Which component is specifically required to support networking functionality?",
            [
                "Virtual memory manager",
                "Network interface controller",
                "Command interpreter",
                "Bootstrap loader"
            ],
            "b"
        ],

        [
            "Which capability is commonly provided by a network operating system?",
            [
                "Remote login",
                "Automatic processor allocation",
                "Hardware virtualization",
                "Interrupt scheduling"
            ],
            "a"
        ],

        [
            "A distributed computing system primarily differs from a networked computing system because it:",
            [
                "Contains only one computer",
                "Automatically shares and coordinates processing loads among connected computers",
                "Eliminates communication between computers",
                "Requires only one processor"
            ],
            "b"
        ],

        [
            "A distributed operating system must provide:",
            [
                "Only stand-alone functionality",
                "Coordination of operations and information flow among component computers",
                "Only remote file access",
                "Only processor scheduling"
            ],
            "b"
        ],

        [
            "From the user's perspective, a true distributed operating system appears as:",
            [
                "Several independent computers",
                "A traditional single-processor system",
                "A network operating system",
                "A multiprocessor hardware complex"
            ],
            "b"
        ],

        [
            "Which characteristic most clearly distinguishes a distributed operating system from a network operating system?",
            [
                "Distributed systems contain more computers",
                "Distributed systems use remote login",
                "Users are unaware of where programs execute and files are stored",
                "Distributed systems do not support communication"
            ],
            "c"
        ],

        [
            "In a true distributed system, determining where a user's program executes should be:",
            [
                "The responsibility of the user",
                "Visible through network commands",
                "Handled automatically by the operating system",
                "Determined by the application developer"
            ],
            "c"
        ],

        [
            "Which comparison is correct?",
            [
                "Network OS hides the existence of multiple computers, while Distributed OS exposes them",
                "Both Network OS and Distributed OS completely hide the existence of multiple computers",
                "Network OS exposes the existence of multiple computers, while Distributed OS attempts to hide them",
                "Neither Network OS nor Distributed OS supports resource sharing"
            ],
            "c"
        ],
        [
            "Which operating system function is concerned with the allocation of both main memory and other storage areas to system programs, user programs, and data?",
            [
                "Input/Output management",
                "Memory management",
                "Processor management",
                "File management"
            ],
            "b"
        ],

        [
            "The operating system's responsibility for determining and maintaining the order in which jobs are executed is known as:",
            [
                "Processor management",
                "Command interpretation",
                "Priority establishment and enforcement",
                "Automatic job transition"
            ],
            "c"
        ],

        [
            "Which operating system function is directly concerned with coordinating and assigning input and output devices while one or more programs are executing?",
            [
                "File management",
                "Memory management",
                "Input/Output management",
                "Priority enforcement"
            ],
            "c"
        ],

        [
            "A user modifies a document using a text editor. Which operating system function most directly enables this capability?",
            [
                "Processor management",
                "File management",
                "Memory management",
                "Input/Output management"
            ],
            "b"
        ],

        [
            "Which pair of responsibilities belongs to File Management according to the note?",
            [
                "Storage of files and modification through file manipulation routines",
                "Storage allocation and processor scheduling",
                "Command interpretation and software assignment",
                "Memory allocation and security enforcement"
            ],
            "a"
        ],

        [
            "The assignment of processors to different tasks is related to processor management, whereas determining the order in which jobs are executed is related to:",
            [
                "Memory management",
                "Priority establishment and enforcement",
                "Input/Output management",
                "File management"
            ],
            "b"
        ],

        [
            "A system automatically begins executing Job B immediately after Job A finishes because of:",
            [
                "Processor management",
                "Automatic transition from job to job",
                "Priority establishment",
                "Command interpretation"
            ],
            "b"
        ],

        [
            "Which operating system responsibility would most likely be involved when a user enters a command that must be translated into an action?",
            [
                "Interpretation of commands and instructions",
                "File management",
                "Priority enforcement",
                "Processor management"
            ],
            "a"
        ],

        [
            "Compilers, assemblers, utility programs, and other software are assigned to users through which operating system responsibility?",
            [
                "Software coordination and assignment",
                "Memory management",
                "Input/Output management",
                "Automatic job transition"
            ],
            "a"
        ],

        [
            "Which operating system function is most directly associated with human-computer interaction rather than resource allocation?",
            [
                "Processor management",
                "Facilitating communication between the computer and the operator",
                "Memory management",
                "Priority establishment"
            ],
            "b"
        ],

        [
            "A student claims that establishing job priorities and assigning processors are identical operating system functions. Which statement is most accurate?",
            [
                "Both functions determine execution order only",
                "One determines execution order while the other assigns processing resources",
                "Both functions belong to memory management",
                "Both functions belong to file management"
            ],
            "b"
        ],

        [
            "Which operating system function would remain relevant even if no files were being stored or modified?",
            [
                "File management",
                "Processor management",
                "Text editing support",
                "File manipulation routines"
            ],
            "b"
        ],

        [
            "The phrase 'while one or more programs are being executed' is specifically associated with:",
            [
                "Input/Output management",
                "Memory management",
                "File management",
                "Command interpretation"
            ],
            "a"
        ],

        [
            "Which responsibility extends beyond simple file storage by explicitly supporting file modification?",
            [
                "Processor management",
                "Memory management",
                "File management",
                "Priority establishment"
            ],
            "c"
        ],

        [
            "Data security and integrity are mentioned in the note as part of the operating system's role in:",
            [
                "Facilitating communication between the system and the operator",
                "File management only",
                "Processor management",
                "Memory allocation"
            ],
            "a"
        ],
    #operating system flaws
        [
            "Why can operating systems contain errors even after they are released?",
            [
                "Operating systems are written by humans who can make mistakes despite testing",
                "Operating systems are too large to be tested before release",
                "Only hardware manufacturers can detect software errors",
                "Errors occur only after users install applications"
            ],
            "a"
        ],

        [
            "Differences in operating system quality are attributed primarily to variations in:",
            [
                "Processor architecture",
                "Software quality control and testing practices",
                "Number of installed applications",
                "Amount of available memory"
            ],
            "b"
        ],

        [
            "Which of the following is NOT identified as a major consequence of operating system errors?",
            [
                "System crashes and instabilities",
                "Security flaws",
                "Peripheral device incompatibilities",
                "Automatic processor upgrades"
            ],
            "d"
        ],

        [
            "A system crash is most accurately described as:",
            [
                "A temporary slowdown caused by insufficient memory",
                "A system becoming frozen and unresponsive",
                "A failure to connect to a network",
                "A printer refusing to print a document"
            ],
            "b"
        ],

        [
            "According to the note, recovery from many system crashes typically requires the user to:",
            [
                "Reinstall the operating system",
                "Replace the processor",
                "Reboot the computer",
                "Format the hard disk"
            ],
            "c"
        ],

        [
            "System instability may result from:",
            [
                "Only bugs in the operating system",
                "Only application programs",
                "Both operating system bugs and programs running on the system",
                "Only hardware failures"
            ],
            "c"
        ],

        [
            "Which statement best reflects the relationship between application programs and operating system stability?",
            [
                "Application programs cannot affect operating system stability",
                "Application programs may contribute to instability or even cause crashes",
                "Application programs improve stability by default",
                "Application programs only affect file management"
            ],
            "b"
        ],

        [
            "A security flaw exists when a software error:",
            [
                "Causes excessive memory consumption",
                "Prevents files from being edited",
                "Creates an opportunity for unauthorized access",
                "Reduces processor efficiency"
            ],
            "c"
        ],

        [
            "Unauthorized intruders are most likely to exploit:",
            [
                "System documentation",
                "Security flaws",
                "Memory allocation policies",
                "File naming conventions"
            ],
            "b"
        ],

        [
            "The primary purpose of patching discovered security flaws is to:",
            [
                "Increase processor speed",
                "Improve graphical performance",
                "Maintain system security",
                "Expand storage capacity"
            ],
            "c"
        ],

        [
            "Which pair is most directly related according to the note?",
            [
                "Security flaw and unauthorized access",
                "System crash and file compression",
                "Peripheral device and processor scheduling",
                "Testing and memory allocation"
            ],
            "a"
        ],

        [
            "A flaw that prevents a printer from functioning correctly would fall under which category of operating system problems?",
            [
                "Security flaws",
                "System crashes",
                "Peripheral device compatibility issues",
                "Priority scheduling errors"
            ],
            "c"
        ],

        [
            "A user discovers that the operating system frequently freezes, requiring restarts, but no unauthorized access occurs. This situation is most closely associated with:",
            [
                "Security flaws",
                "System crashes and instabilities",
                "Peripheral incompatibility",
                "Software patching"
            ],
            "b"
        ],

        [
            "Which statement distinguishes a security flaw from a system crash?",
            [
                "A security flaw concerns unauthorized access, whereas a system crash concerns loss of responsiveness",
                "A security flaw affects hardware, whereas a system crash affects software",
                "A security flaw always causes a reboot, whereas a system crash never does",
                "A security flaw affects printers only, whereas a system crash affects processors only"
            ],
            "a"
        ],
        [
            "An operating system works correctly except that it cannot communicate properly with certain printers. This problem is best classified as:",
            [
                "A system instability",
                "A security vulnerability",
                "A peripheral device compatibility problem",
                "A memory management failure"
            ],
            "c"
        ]
        #problem solving
]
        
    def mth114(self):
        return [
        #trigonometry
    [
        "If sinθ = 3/5 and θ is acute, what is cosθ?",
        [
            "4/5",
            "3/4",
            "5/4",
            "2/5"
        ],
        "a"
    ],
    [
        "If cosθ = 12/13 and θ is acute, what is sinθ?",
        [
            "5/13",
            "12/5",
            "13/5",
            "11/13"
        ],
        "a"
    ],
    [
        "A right triangle has opposite = 8 and hypotenuse = 17. What is tanθ?",
        [
            "8/15",
            "15/8",
            "8/17",
            "15/17"
        ],
        "a"
    ],
    [
        "If tanθ = 5/12 and θ is acute, what is sinθ?",
        [
            "5/13",
            "12/13",
            "13/5",
            "5/12"
        ],
        "a"
    ],
    [
        "If tanθ = 5/12 and θ is acute, what is cosθ?",
        [
            "12/13",
            "5/13",
            "13/12",
            "12/5"
        ],
        "a"
    ],
    [
        "Which identity follows directly from the Pythagorean theorem?",
        [
            "sin²θ + cos²θ = 1",
            "tan²θ + cot²θ = 1",
            "sinθ + cosθ = 1",
            "sec²θ + csc²θ = 1"
        ],
        "a"
    ],
    [
        "Which identity is obtained by dividing sin²θ + cos²θ = 1 by cos²θ?",
        [
            "1 + tan²θ = sec²θ",
            "1 + cot²θ = csc²θ",
            "sec²θ - tan²θ = 1",
            "csc²θ - cot²θ = 1"
        ],
        "a"
    ],
    [
        "Which identity is obtained by dividing sin²θ + cos²θ = 1 by sin²θ?",
        [
            "1 + cot²θ = csc²θ",
            "1 + tan²θ = sec²θ",
            "sec²θ - tan²θ = 1",
            "sin²θ = 1 - cos²θ"
        ],
        "a"
    ],
    [
        "If sinθ = 5/13, evaluate 1 - sin²θ.",
        [
            "144/169",
            "25/169",
            "12/13",
            "5/12"
        ],
        "a"
    ],
    [
        "If cosθ = 8/17, evaluate tanθ.",
        [
            "15/8",
            "8/15",
            "17/15",
            "15/17"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to sec²θ - 1?",
        [
            "tan²θ",
            "cot²θ",
            "sin²θ",
            "cos²θ"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to csc²θ - 1?",
        [
            "cot²θ",
            "tan²θ",
            "sec²θ",
            "sin²θ"
        ],
        "a"
    ],
    [
        "If sinθ = 7/25, what is secθ?",
        [
            "25/24",
            "24/25",
            "25/7",
            "24/7"
        ],
        "a"
    ],
    [
        "If cosθ = 4/5, what is cscθ?",
        [
            "5/3",
            "3/5",
            "5/4",
            "4/3"
        ],
        "a"
    ],
    [
        "If tanθ = 3/4, what is secθ?",
        [
            "5/4",
            "4/5",
            "5/3",
            "3/5"
        ],
        "a"
    ],
    [
        "sin²θ + cos²θ equals:",
        [
            "1",
            "0",
            "tan²θ",
            "sec²θ"
        ],
        "a"
    ],
    [
        "1 - cos²θ equals:",
        [
            "sin²θ",
            "tan²θ",
            "sec²θ",
            "cot²θ"
        ],
        "a"
    ],
    [
        "1 - sin²θ equals:",
        [
            "cos²θ",
            "sec²θ",
            "tan²θ",
            "cot²θ"
        ],
        "a"
    ],
    [
        "If secθ = 13/12, what is tanθ?",
        [
            "5/12",
            "12/5",
            "13/5",
            "5/13"
        ],
        "a"
    ],
    [
        "If cscθ = 17/8, what is cotθ?",
        [
            "15/8",
            "8/15",
            "17/15",
            "15/17"
        ],
        "a"
    ],
    [
        "sin(A+B) equals:",
        [
            "sinA cosB + cosA sinB",
            "sinA cosB - cosA sinB",
            "cosA cosB + sinA sinB",
            "cosA cosB - sinA sinB"
        ],
        "a"
    ],
    [
        "sin(A-B) equals:",
        [
            "sinA cosB - cosA sinB",
            "sinA cosB + cosA sinB",
            "cosA cosB - sinA sinB",
            "cosA cosB + sinA sinB"
        ],
        "a"
    ],
    [
        "cos(A+B) equals:",
        [
            "cosA cosB - sinA sinB",
            "cosA cosB + sinA sinB",
            "sinA cosB + cosA sinB",
            "sinA cosB - cosA sinB"
        ],
        "a"
    ],
    [
        "cos(A-B) equals:",
        [
            "cosA cosB + sinA sinB",
            "cosA cosB - sinA sinB",
            "sinA cosB + cosA sinB",
            "sinA cosB - cosA sinB"
        ],
        "a"
    ],
    [
        "tan(A+B) equals:",
        [
            "(tanA + tanB)/(1 - tanA tanB)",
            "(tanA - tanB)/(1 + tanA tanB)",
            "(tanA + tanB)/(1 + tanA tanB)",
            "(tanA - tanB)/(1 - tanA tanB)"
        ],
        "a"
    ],
    [
        "tan(A-B) equals:",
        [
            "(tanA - tanB)/(1 + tanA tanB)",
            "(tanA + tanB)/(1 - tanA tanB)",
            "(tanA - tanB)/(1 - tanA tanB)",
            "(tanA + tanB)/(1 + tanA tanB)"
        ],
        "a"
    ],
    [
        "sin 2θ equals:",
        [
            "2sinθcosθ",
            "sin²θ-cos²θ",
            "2tanθ/(1+tan²θ)",
            "cos²θ-sin²θ"
        ],
        "a"
    ],
    [
        "cos 2θ equals:",
        [
            "cos²θ - sin²θ",
            "2sinθcosθ",
            "1 - sin²θ",
            "1 - cos²θ"
        ],
        "a"
    ],
    [
        "Which is also equal to cos2θ?",
        [
            "1 - 2sin²θ",
            "2sinθcosθ",
            "1 + 2sin²θ",
            "2cos²θ - 1 + 2sin²θ"
        ],
        "a"
    ],
    [
        "Which is also equal to cos2θ?",
        [
            "2cos²θ - 1",
            "2sinθcosθ",
            "1 - 2cos²θ",
            "sin²θ - cos²θ"
        ],
        "a"
    ],
    [
        "tan2θ equals:",
        [
            "2tanθ/(1-tan²θ)",
            "2tanθ/(1+tan²θ)",
            "(1-tan²θ)/(2tanθ)",
            "(1+tan²θ)/(2tanθ)"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to (1-cos2θ)/2?",
        [
            "sin²θ",
            "cos²θ",
            "tan²θ",
            "sec²θ"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to (1+cos2θ)/2?",
        [
            "cos²θ",
            "sin²θ",
            "tan²θ",
            "csc²θ"
        ],
        "a"
    ],
    [
        "Which identity would be most useful to simplify sin²θ/(1-cos²θ)?",
        [
            "1-cos²θ=sin²θ",
            "1+tan²θ=sec²θ",
            "1+cot²θ=csc²θ",
            "cos2θ=cos²θ-sin²θ"
        ],
        "a"
    ],
    [
        "sinθ/cosθ simplifies to:",
        [
            "tanθ",
            "cotθ",
            "secθ",
            "cscθ"
        ],
        "a"
    ],
    [
        "cosθ/sinθ simplifies to:",
        [
            "cotθ",
            "tanθ",
            "secθ",
            "cscθ"
        ],
        "a"
    ],
    [
        "A proof starts with sec²θ - tan²θ. It simplifies to:",
        [
            "1",
            "0",
            "sin²θ",
            "cos²θ"
        ],
        "a"
    ],
    [
        "Which identity is most useful in proving 1 + tan²θ = sec²θ?",
        [
            "sin²θ + cos²θ = 1",
            "sin2θ = 2sinθcosθ",
            "cos(A+B)",
            "tan(A-B)"
        ],
        "a"
    ],
    [
        "sin75° can be evaluated exactly using:",
        [
            "sin(45°+30°)",
            "sin(45°-30°)",
            "cos(45°+30°)",
            "tan(45°+30°)"
        ],
        "a"
    ],
    [
        "cos15° can be evaluated exactly using:",
        [
            "cos(45°-30°)",
            "cos(45°+30°)",
            "sin(45°+30°)",
            "tan(45°-30°)"
        ],
        "a"
    ],
    [
        "Which expression is equal to sin(A+B) - sin(A-B)?",
        [
            "2cosA sinB",
            "2sinA cosB",
            "2sinA sinB",
            "2cosA cosB"
        ],
        "a"
    ],
    [
        "Which expression is equal to sin(A+B) + sin(A-B)?",
        [
            "2sinA cosB",
            "2cosA sinB",
            "2sinA sinB",
            "2cosA cosB"
        ],
        "a"
    ],
    [
        "Which expression is equal to cos(A-B) + cos(A+B)?",
        [
            "2cosA cosB",
            "2sinA sinB",
            "2sinA cosB",
            "2cosA sinB"
        ],
        "a"
    ],
    [
        "Which expression is equal to cos(A-B) - cos(A+B)?",
        [
            "2sinA sinB",
            "2cosA cosB",
            "2sinA cosB",
            "2cosA sinB"
        ],
        "a"
    ],
    [
        "If sin(A+B) = sinA cosB + cosA sinB, the second term represents:",
        [
            "The contribution of A's cosine and B's sine",
            "The contribution of both sines",
            "The contribution of both cosines",
            "The contribution of A's sine and B's cosine"
        ],
        "a"
    ],
    [
        "A student writes cos(A+B)=cosAcosB+sinAsinB. What mistake has been made?",
        [
            "The sign before sinAsinB should be negative",
            "The sign before cosAcosB should be negative",
            "The terms should be divided",
            "The formula is correct"
        ],
        "a"
    ],
    [
        "Which pair of formulas differ only by a sign change?",
        [
            "sin(A+B) and sin(A-B)",
            "sin(A+B) and cos(A+B)",
            "cos(A+B) and tan(A+B)",
            "sin(A-B) and tan(A-B)"
        ],
        "a"
    ],
    [
        "Which pair of formulas contain identical terms but differ only by the sign between them?",
        [
            "cos(A+B) and cos(A-B)",
            "sin(A+B) and cos(A+B)",
            "tan(A+B) and sin(A+B)",
            "tan(A-B) and cos(A-B)"
        ],
        "a"
    ],
    [
        "If A=45° and B=30°, which formula would directly produce an exact value for sin75°?",
        [
            "sin(A+B)",
            "cos(A+B)",
            "tan(A+B)",
            "cos(A-B)"
        ],
        "a"
    ],
    [
        "If A=45° and B=30°, which formula would directly produce an exact value for cos15°?",
        [
            "cos(A-B)",
            "sin(A+B)",
            "tan(A+B)",
            "sin(A-B)"
        ],
        "a"
    ],
    [
        "The denominator of tan(A+B) contains:",
        [
            "1 - tanA tanB",
            "1 + tanA tanB",
            "tanA + tanB",
            "tanA - tanB"
        ],
        "a"
    ],
    [
        "The denominator of tan(A-B) contains:",
        [
            "1 + tanA tanB",
            "1 - tanA tanB",
            "tanA + tanB",
            "tanA - tanB"
        ],
        "a"
    ],
    [
        "Which identity would be most efficient for finding tan75° exactly?",
        [
            "tan(45°+30°)",
            "sin(45°+30°)",
            "cos(45°+30°)",
            "sin2θ"
        ],
        "a"
    ],
    [
        "A student wants to evaluate sin105°. Which decomposition is most useful?",
        [
            "sin(60°+45°)",
            "sin(60°-45°)",
            "sin(90°+15°)",
            "sin(120°-15°)"
        ],
        "a"
    ],
    [
        "Which expression simplifies to sinAcosB?",
        [
            "(sin(A+B)+sin(A-B))/2",
            "(sin(A+B)-sin(A-B))/2",
            "(cos(A-B)+cos(A+B))/2",
            "(cos(A-B)-cos(A+B))/2"
        ],
        "a"
    ],
    [
        "Which expression simplifies to cosAsinB?",
        [
            "(sin(A+B)-sin(A-B))/2",
            "(sin(A+B)+sin(A-B))/2",
            "(cos(A-B)+cos(A+B))/2",
            "(cos(A-B)-cos(A+B))/2"
        ],
        "a"
    ],
    [
        "Which expression simplifies to cosAcosB?",
        [
            "(cos(A-B)+cos(A+B))/2",
            "(cos(A-B)-cos(A+B))/2",
            "(sin(A+B)+sin(A-B))/2",
            "(sin(A+B)-sin(A-B))/2"
        ],
        "a"
    ],
    [
        "Which expression simplifies to sinAsinB?",
        [
            "(cos(A-B)-cos(A+B))/2",
            "(cos(A-B)+cos(A+B))/2",
            "(sin(A+B)-sin(A-B))/2",
            "(sin(A+B)+sin(A-B))/2"
        ],
        "a"
    ],
    [
        "Which product can be converted directly using the identity sin(A+B)+sin(A-B)?",
        [
            "sinA cosB",
            "cosA sinB",
            "sinA sinB",
            "cosA cosB"
        ],
        "a"
    ],
    [
        "Which product can be converted directly using the identity cos(A-B)+cos(A+B)?",
        [
            "cosA cosB",
            "sinA sinB",
            "sinA cosB",
            "cosA sinB"
        ],
        "a"
    ],
    [
        "When expanding cos(A+B), which product is subtracted?",
        [
            "sinA sinB",
            "sinA cosB",
            "cosA sinB",
            "cosA cosB"
        ],
        "a"
    ],
    [
        "When expanding cos(A-B), which product is added?",
        [
            "sinA sinB",
            "sinA cosB",
            "cosA sinB",
            "cosA cosB"
        ],
        "a"
    ],
    [
        "A student remembers 'sine keeps its first sign'. Which pair demonstrates this?",
        [
            "sin(A+B) and sin(A-B)",
            "cos(A+B) and cos(A-B)",
            "tan(A+B) and tan(A-B)",
            "cos(A+B) and sin(A+B)"
        ],
        "a"
    ],
    [
        "If sin(A+B)=1 and sin(A-B)=0, then sin(A+B)+sin(A-B) equals:",
        [
            "1",
            "0",
            "2",
            "-1"
        ],
        "a"
    ],
    [
        "Which formula is most useful when a product of two trigonometric functions needs to be rewritten as a sum?",
        [
            "Product-to-sum identities",
            "Double-angle identities",
            "Reciprocal identities",
            "Pythagorean identities"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to 2sinAcosB?",
        [
            "sin(A+B)+sin(A-B)",
            "sin(A+B)-sin(A-B)",
            "cos(A-B)+cos(A+B)",
            "cos(A-B)-cos(A+B)"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to 2cosAsinB?",
        [
            "sin(A+B)-sin(A-B)",
            "sin(A+B)+sin(A-B)",
            "cos(A-B)+cos(A+B)",
            "cos(A-B)-cos(A+B)"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to 2cosAcosB?",
        [
            "cos(A-B)+cos(A+B)",
            "cos(A-B)-cos(A+B)",
            "sin(A+B)+sin(A-B)",
            "sin(A+B)-sin(A-B)"
        ],
        "a"
    ],
    [
        "Which expression is equivalent to 2sinAsinB?",
        [
            "cos(A-B)-cos(A+B)",
            "cos(A-B)+cos(A+B)",
            "sin(A+B)+sin(A-B)",
            "sin(A+B)-sin(A-B)"
        ],
        "a"
    ]
        ]
           
    def sta112(self):
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
            [
                "What is the expected mean current if the measurements are uniformly distributed between 0 and 20 mA?",
                ["5 mA", "10 mA", "15 mA", "20 mA"],
                "b"
            ],
            [
                "Which standard distribution is famously characterized by a bell-shaped, symmetric curve around its mean?",
                ["Uniform distribution", "Poisson distribution", "Geometric distribution", "Normal distribution"],
                "d"
            ],
            [
                "What notation is universally used to denote a normal distribution with mean mu and variance sigma^2?",
                ["U(mu, sigma^2)", "N(mu, sigma^2)", "P(lambda)", "B(n, p)"],
                "b"
            ],
            [
                "For any normal random variable, what is the approximate probability that X lies within one standard deviation of the mean?",
                ["0.5000", "0.6827", "0.9545", "0.9973"],
                "b"
            ],
            [
                "For any normal random variable, what is the approximate probability that X lies within two standard deviations of the mean?",
                ["0.6827", "0.8500", "0.9545", "0.9973"],
                "c"
            ],
            [
                "For any normal random variable, what is the approximate probability that X lies within three standard deviations of the mean?",
                ["0.6827", "0.9545", "0.9900", "0.9973"],
                "d"
            ],
            [
                "What transformation formula is used to create a standard normal random variable Z from a normal variable X?",
                ["Z = (X - mu) / sigma", "Z = (X - sigma) / mu", "Z = X - mu", "Z = (X - mu) / sigma^2"],
                "a"
            ],
            [
                "What are the expected mean and variance values of the transformed standard normal variable Z?",
                ["Mean=1, Variance=0", "Mean=0, Variance=1", "Mean=mu, Variance=sigma", "Mean=0, Variance=0"],
                "b"
            ],
            [
                "If the amount of recycling newspaper is normally distributed with mean 28 pounds and standard deviation 2, what is sigma?",
                ["1 pound", "2 pounds", "4 pounds", "28 pounds"],
                "b"
            ],
            [
                "The cumulative distribution function of a standard normal random variable is commonly denoted by which symbol?",
                ["f(x)", "p(x)", "Phi(z)", "Lambda(x)"],
                "c"
            ],
            [
                "What is the range of real values allowed for the variable x in a standard normal distribution pdf?",
                ["From 0 to infinity", "From negative infinity to positive infinity", "From alpha to beta", "From -1 to +1"],
                "b"
            ],
            [
                "If a wire current measurement has a mean of 10 mA and variance of 4, what is the standard deviation?",
                ["2 mA", "4 mA", "10 mA", "16 mA"],
                "a"
            ],
            [
                "The continuous uniform distribution is used when an event is described as being what over an interval?",
                ["Highly skewed", "Equally likely", "Normally centered", "Exponentially decaying"],
                "b"
            ],
            [
                "The total area under the standard normal curve to the left of its mean of 0 is equal to what value?",
                ["0.0", "0.25", "0.50", "1.00"],
                "c"
            ]
        ]

 