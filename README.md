#📝 just simple notpad with Gemini ai and calculator
its a notepad made with Python and PyQt5. You can create paseges type notes evrithing is saved in datbase. It autosaves, so when you close it and open it will save the page you were on and the notes that you where taiking
## ✨ Features

* **AI Chat Integration**: Chat with Gemini 2.5 Flash directly inside the app. 
* **Notepad**: Automatically saves notes to a SQLite database. Includes font scaling (+/-) and autosave
* **Calculator**:basic Calculator with  a secondary window that pulls your Windows Accent Color dynamically for a native OS feel.
* **Modern UI**: Dark mode interface with a custom "Gemini Glow" animated gradient button.

## 🚀 Installation
1. Clone the repository

2.Set up a virtual environment:
 ```bash
   python -m venv .venv
   .venv\Scripts\activate 
```
3.Install dependencies:
```bash
    pip install PyQt5 google-genai python-dotenv
```

4. Create a .env file in the root directory and add your Google API Key:

```bash
    GOOGLE_API_KEY=your_actual_key_here
```

5. And run this app from: 
```bash
    python main/notepad.py
```

## 🖼️UI screenshots

## Notepad
![Notepad](<images/Screenshot 2026-01-30 224244.png>)

## Calculator
![Calculator](images/image.png)

## Ai chat
![Ai chat](images/image-1.png)
