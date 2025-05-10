#Spell Checker Web App

A simple and creative web-based Spell Checker built using **Python (Flask)** and **HTML/CSS**. Enter any sentence or word and get an instant spelling correction using the `TextBlob` library.

---

## Features

- Checks and corrects spelling of input text
- Clean, responsive HTML interface
- Runs smoothly on macOS and other platforms
- Built with beginner-friendly Python and Flask

---


## Tech Stack

- **Backend:** Python, Flask, TextBlob
- **Frontend:** HTML, CSS

---

STEP 1: INSTALLATION AND SETUP
1. Install Python 3 (if not already)
Open Terminal and run:

<img width="630" alt="Screenshot 2025-05-10 at 5 52 26 PM" src="https://github.com/user-attachments/assets/0cd666ae-a0ab-4264-981c-16baa59c649e" />


If it's not installed, install it using Homebrew:

<img width="634" alt="Screenshot 2025-05-10 at 5 52 45 PM" src="https://github.com/user-attachments/assets/609d61b7-5382-45ea-8331-32e73acea5ad" />


2. Install Flask and TextBlob

In Terminal:
<img width="643" alt="Screenshot 2025-05-10 at 5 53 12 PM" src="https://github.com/user-attachments/assets/a15bdff4-dc74-45d0-b2f0-a8717d43a0eb" />



flask: Web framework to build backend
textblob: Python library for NLP, used here for spell checking
download_corpora: Downloads grammar rules and dictionary for TextBlob

3. Create Project Folder
In Terminal:

<img width="627" alt="Screenshot 2025-05-10 at 5 53 29 PM" src="https://github.com/user-attachments/assets/cf0796f3-b45d-4394-87d8-ce1929ebd941" />


4. Create Backend File
Create a file named app.py:

<img width="629" alt="Screenshot 2025-05-10 at 5 56 28 PM" src="https://github.com/user-attachments/assets/3441294e-e173-4aa3-a4c3-22d12c8573d7" />


<img width="1156" alt="Screenshot 2025-05-10 at 5 57 29 PM" src="https://github.com/user-attachments/assets/f74e48a4-b088-4054-87e0-9c338c79d878" />

5. Create templates Folder
Flask looks for HTML files in a folder called templates.
<img width="633" alt="Screenshot 2025-05-10 at 6 02 18 PM" src="https://github.com/user-attachments/assets/96cf0ac7-6da9-4c56-a0c1-30a0d5bdfce6" />

<img width="957" alt="Screenshot 2025-05-10 at 6 03 18 PM" src="https://github.com/user-attachments/assets/45b2a911-fff0-43af-a2b3-ce2da1ba24df" />
<img width="896" alt="Screenshot 2025-05-10 at 6 13 46 PM" src="https://github.com/user-attachments/assets/35e48b5c-7d8d-4efe-88f2-bf38087f6481" />


STEP 2: RUNNING THE PROJECT
In Terminal, run:
<img width="625" alt="Screenshot 2025-05-10 at 6 15 07 PM" src="https://github.com/user-attachments/assets/9f798e95-e0aa-460b-95d5-00e0f2fb684f" />

STEP 3: USING THE SPELL CHECKER
1. Open your browser
2. Go to: http://127.0.0.1:5000
3. Type a sentence with incorrect spelling (e.g., Ths is a splel chcker)
4. Click Check Spelling
5. You'll see the corrected version below: This is a spell checker












