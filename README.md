# 📱 Phone Number Information Tool (OSINT Project)

A simple yet powerful **Phone Number Information Tool** built using **Python** and the **NumVerify API**. This tool fetches detailed information about a phone number such as **country, carrier, location, and line type**.

---

## 🔥 Project Overview

This project demonstrates how to use **APIs in Python** to perform basic **OSINT (Open Source Intelligence)** operations. It allows users to input a phone number and retrieve useful metadata about it.

---

## ✨ Features

✔️ Validate phone numbers
✔️ Get international format
✔️ Detect country and country code
✔️ Identify carrier (network provider)
✔️ Get location (region/city)
✔️ Detect line type (mobile, landline, etc.)
✔️ Simple CLI-based interface

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Library:** requests
* **API:** NumVerify API

---

## ⚙️ How It Works

* User enters phone number and country code
* Script sends request to NumVerify API
* API returns JSON response
* Script extracts and displays useful information

---

## 📂 Project Structure

```id="pyproj11"
📁 Phone-Info-Tool
│── phone_info.py     # Main script
│── README.md         # Documentation
```

---

## 🖥️ Installation & Setup

### 1️⃣ Install Python

Make sure Python is installed on your system

### 2️⃣ Install Required Library

```bash id="pip11"
pip install requests
```

### 3️⃣ Add Your API Key

Replace this line in code:

```python id="api12"
API_KEY = 'YOUR_API_KEY'
```

Get your API key from: https://numverify.com

---

## ▶️ How to Run

```bash id="run12"
python phone_info.py
```

Then enter:

* Phone number
* Country code (e.g., IN, US)

---

## 🧠 Learning Outcomes

* Working with APIs in Python
* JSON data handling
* HTTP requests using requests library
* Basics of OSINT tools
* CLI-based application development

---

## ⚠️ Disclaimer

This tool is created for **educational purposes only**.
Do not use it for illegal activities or to invade someone's privacy.

---

## 🔐 Future Enhancements

🚀 Add GUI interface (Tkinter / PyQt)
🚀 Add bulk number lookup
🚀 Save results to file (CSV/JSON)
🚀 Integrate with other OSINT APIs
🚀 Add number spam detection

---

## 👨‍💻 Author

**Aayush Parekh**
💻 Full Stack Developer | Ethical Hacker | OSINT Enthusiast

🛡️ *"Hack the bad, protect the good."*

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
