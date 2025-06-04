from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import string
import random
from utils import generate_short_code

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize DB
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    long_url TEXT NOT NULL,
                    short_code TEXT NOT NULL UNIQUE
                )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        try:
            c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
            conn.commit()
            short_url = request.host_url + short_code
            return render_template('result.html', short_url=short_url)
        except sqlite3.IntegrityError:
            flash("Short code collision. Please try again.")
        finally:
            conn.close()

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "<h1>404 - URL Not Found</h1>", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
