# 🔗 URL Shortener

A simple and efficient **URL Shortener** built using Flask and SQLite. This application allows users to convert long URLs into short, shareable links that automatically redirect to the original website.

---

## 📌 Features

- 🔍 Shorten long URLs  
- 🔁 Redirect from short URL to original URL  
- 💾 Store URL mappings in SQLite  
- 🎨 Clean and responsive UI  
- 📦 Easy to run locally  

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- Flask  
  ```bash
  pip install flask
  ```

### ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/omkar1143-eng/secure-url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Visit in browser:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📁 Project Structure

```
url_shortener/
├── app.py                 # Main Flask application
├── utils.py               # Helper functions for code generation
├── database.db            # SQLite database (auto-generated)
├── templates/
│   ├── index.html         # Main input page
│   └── result.html        # Result page with shortened link
├── static/
│   └── style.css          # Styling for frontend
└── README.md              # Project documentation
```

---

## ✨ Example

- **Original URL**: `https://www.example.com/some/very/long/link`  
- **Shortened URL**: `http://127.0.0.1:5000/Xyz12`

---

## 💡 Future Improvements

- [ ] Click analytics (number of visits, timestamp)  
- [ ] QR code generation  
- [ ] User authentication and dashboard  
- [ ] Expiration date for short URLs  
- [ ] Custom short codes  

---

## 👨‍💻 Author

**KANDUKURI OMKAR**  
📧 omkark5125@gmail.com  
📍 India
