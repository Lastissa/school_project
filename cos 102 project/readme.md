# COS 102 Group Project — Desktop Suite

Welcome to our project repository. This suite brings together two primary tools built to make mathematics and learning highly visual and completely dynamic: an **Advanced Step-by-Step Mathematical Engine** and a **Simulated Computer-Based Testing (CBT) Quiz Hub**. 

Both components are designed from the ground up to be bulletproof, meaning they actively monitor user input to handle edge cases gracefully, preventing crashes and keeping you moving forward without generic, unhelpful error prompts.

---

## 🧭 Repository Navigation

* [📋 Project Architecture](#-project-architecture)
* [🧮 Calculator Module (`calculator.py`)](#-calculator-module-calculatorpy)
* [🧠 Simulated CBT Engine (`quiz_app.py`)](#-simulated-cbt-engine-quiz_apppy)
* [🛠️ Core Logic Core (`utility.py`)](#-core-logic-core-utilitypy)
* [👥 Project Contributors (`group_members.xlsx`)](#-project-contributors-group_membersxlsx)

---

## 📋 Project Architecture

To run or inspect our project files, please refer to the structure mapped out inside the project root workspace directory.

```text
ROOT/
├── .venv/                     # Python isolation layer (dependencies)
├── .git/                      # Version history tracking
└── cos 102 project/           # Main Project Directory
    ├── calculator.py          # Primary Math Solver Application
    ├── group_members.xlsx     # Registry of Project Contributors
    ├── quiz_app.py            # Computer Based Test (CBT) Application
    ├── readme.md              # Current Documentation Portal
    └── utility.py             # Shared Operational Component Engine
```

---

## 🧮 Calculator Module (`calculator.py`)

The [calculator.py](./calculator.py) module houses a high-precision graphical utility built using Python's interface libraries. Beyond standard arithmetic functions, it is equipped to process advanced academic workflows:

* **Scientific Mathematical Toolkit:** Built-in computation wrappers for trigonometric functions such as `sin`, `cos`, and `tan`.
* **Step-by-Step Solution Engine:** An intelligent system that resolves complex quadratic equations through both the Quadratic Formula and the Factorization method. Instead of providing just a raw numerical output, it generates complete, explicit step-by-step mathematical working lines showing exactly how mid-coefficients are split and handled.
* **Proactive Defensiveness:** Built-in intelligent interception routines that trap real-world computational edge cases—such as syntax anomalies or calculation boundary threshold violations (value overflow limit errors)—and cleanly translates them to clear diagnostic feedback rather than crashing out.

---

## 🧠 Simulated CBT Engine (`quiz_app.py`)

The [quiz_app.py](./quiz_app.py) component is a realistic testing client crafted to mirror the environments of modern professional computer-based tests.

* **Dynamic Question Sourcing:** The testing system relies directly on algorithms embedded inside [utility.py](./utility.py) to map out available topics, pooling dynamically generated problems for a comprehensive evaluation.
* **Realistic Testing Environment:** Features integrated timing mechanisms that continuously track progress, enforcing constraints to closely simulate the pacing of real exams.
* **Post-Evaluation Analytics:** Upon submission, the app parses responses to provide an granular breakdown of scores, accuracy, and operational performance trends.
* **Zero-Lock Interception:** Every text submission path is deeply managed to handle incomplete entries or typing errors smoothly, avoiding the frustrating, unhelpful "ERROR" messages found in simpler codebases.

---

## 🛠️ Core Logic Core (`utility.py`)

The [utility.py](./utility.py) asset acts as the core foundational backing of this workspace. It houses shared algorithms, mathematical conversions, and interface metrics utilized continuously by both the calculator engine and the interactive testing workspace. 

Because it controls vital operations like numbers clipping, type transformations, and course category tracking, **this file must remain pristine and local** within the execution path for either application component to build successfully.

---

## 👥 Project Contributors (`group_members.xlsx`)

The [group_members.xlsx](./group_members.xlsx) binary asset maintains the official ledger of all students assigned to this group effort. It holds full identification indexes, including names and corresponding university matric numbers tracking individual participation records across this collaborative university task.

---
*Developed cleanly for the COS 102 Practical Suite.*