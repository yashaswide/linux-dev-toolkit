<div align="center">

# 🚀 Linux Dev Toolkit (LDT)

<p>
  <strong>A smart command-line toolkit for Linux & macOS with Natural Language Understanding.</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/NLP-spaCy-orange" alt="NLP">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</p>

</div>

---

## 📖 Overview

Linux Dev Toolkit (LDT) is a developer-friendly command-line toolkit that simplifies navigation, file management, and common terminal workflows through intuitive commands and Natural Language Processing (NLP).

Instead of memorizing complex commands, users can interact with the terminal using simple English.

---

## ✨ Features

### 📂 Navigation

- goto — Navigate to common locations
- back — Move to parent directory
- where — Show current location

### 📄 File Operations

- make — Create folders
- delete — Delete files or folders
- rename — Rename files
- rename-folder — Rename directories

### 📖 File Inspection

- head — Display first N lines
- tail — Display last N lines

### ⚙️ Utilities

- show — List files and directories
- clear — Clear terminal
- help — Built-in documentation
- shutdown — Shutdown system safely

### 🧠 Natural Language Mode

Examples:

text show me the files 
show me the directories 
show the first 5 lines of main.py 
show the last 10 lines of app.py 
create a folder called ai_project 
go to desktop delete test.py 

### ⌨️ Interactive Shell

bash ldt 

text LDT v0.1.0 | ~/projects 
---------------------------------------- 
ldt > show me the files 
ldt > create a folder called ai_project 
ldt > show the last 10 lines of app.py 

---

## 📦 Installation

### Clone Repository

bash git clone https://github.com/yashaswide/linux-dev-toolkit.git cd linux-dev-toolkit 

### Install

bash pip install . 

### Development Installation

bash pip install -e . 

---

## 🚀 Usage

### Navigation

bash 
ldt goto Desktop 
ldt back 
ldt where 

### File Operations

bash 
ldt make test_folder 
ldt delete test_folder  
ldt rename old.py new.py 
ldt rename-folder old_folder new_folder 

### File Inspection

bash 
ldt head main.py 5 
ldt tail main.py 10 

### Utilities

bash 
ldt show 
ldt help 
ldt clear 

---

## 🏗️ Project Structure

text linux-dev-toolkit/ 
│ 
├── ldt/ 
│   ├── main.py 
│   └── commands/ 
│       ├── nav.py │       
        ├── nlm.py │       
        ├── parser.py │       
        └── help_cmd.py │ 
├── setup.py 
├── pyproject.toml 
├── README.md 
└── LICENSE 

---

## 🛣️ Roadmap

- [ ] Advanced NLP understanding
- [ ] File search functionality
- [ ] Copy & move operations
- [ ] Context-aware commands
- [ ] AI-assisted suggestions
- [ ] Raspberry Pi optimizations

---

## 💡 Motivation

I often found myself forgetting Linux commands and repeating common terminal workflows.

LDT was created to provide a simpler, more intuitive interface while exploring command-line development, software architecture, and Natural Language Processing.

---

## 📜 License

Distributed under the MIT License.
See LICENSE for more informati