# 🔐 Cryptographic Lab — Basic Encryption & Decryption

## 📌 Project Overview

**Cryptographic Lab** is a beginner-friendly cybersecurity project developed for **DecodeLabs Cyber Security — Project 2**.

The application demonstrates the basic concepts of **encryption and decryption** using the **Caesar Cipher**. Users can enter a message, select a shift key, encrypt the message, and decrypt the encrypted text back to its original form.

---

## 🎯 Objective

The main objectives of this project are:

* Understand the basic concept of encryption and decryption.
* Implement a simple cryptographic algorithm.
* Encrypt user-provided text using a custom shift key.
* Decrypt encrypted text back to its original message.
* Understand how basic data protection techniques work.

---

## ✨ Features

* 🔐 Caesar Cipher encryption
* 🔓 Caesar Cipher decryption
* 🔢 Custom shift key from 1–25
* 📝 User-friendly text input
* 🔄 Reset functionality
* 📊 Clear encryption and decryption outputs
* 💻 Professional Streamlit interface
* 🛡️ Educational security note

---

## 🔑 How the Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions.

### Example

**Original Text:**

```text
Hello World
```

**Shift Key:**

```text
3
```

**Encrypted Text:**

```text
Khoor Zruog
```

The decryption process shifts the characters back by the same number to recover the original message.

---

## 🖥️ Screenshots

### Main Interface

![Main Interface](screenshots/main-interface.png)

### Encryption Output

![Encryption Output](screenshots/encryption-output.png)

### Decryption Output

![Decryption Output](screenshots/decryption-output.png)

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Caesar Cipher**
* **Python Standard Library**

---

## 📂 Project Structure

```text
DecodeLabs_Project_2/
│
├── app.py
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── main-interface.png
    ├── encryption-output.png
    └── decryption-output.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Open the project folder:

```bash
cd DecodeLabs_Project_2
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser.

---

## 🧪 Example Workflow

1. Enter a message.
2. Select a shift key.
3. Click **Encrypt**.
4. View the encrypted message.
5. Enter/use the encrypted text.
6. Click **Decrypt**.
7. View the original message.

---

## 🛡️ Security Note

The Caesar Cipher is a simple educational cryptographic technique and is **not suitable for protecting real confidential information**.

This project is intended to demonstrate fundamental encryption and decryption concepts.

---

## 🎓 Internship Project

**DecodeLabs Cyber Security — Project 2**

**Project:** Basic Encryption & Decryption
**Technique:** Caesar Cipher
**Platform:** Streamlit
**Language:** Python

---

## 👨‍💻 Author

**Mubashir Rehman**

Cybersecurity Student | Python & Web Development Enthusiast

---

## 📄 License

This project is created for educational and learning purposes.
