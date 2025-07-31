from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            raw_html TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_case_details(case_type, case_number, filing_year):
    # Dummy data to simulate scraping
    details = {
        'case_type': case_type,
        'case_number': case_number,
        'filing_year': filing_year,
        'parties': 'John Doe vs Jane Smith',
        'filing_date': '2023-08-10',
        'next_hearing_date': '2025-09-01',
        'pdf_links': [
            {'name': 'Order_2025-06-01.pdf', 'url': '#'},
            {'name': 'Judgment_2025-07-15.pdf', 'url': '#'}
        ]
    }
    raw_html = '<html><body>Simulated HTML response for debugging</body></html>'
    return details, raw_html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    try:
        details, raw_html = fetch_case_details(case_type, case_number, filing_year)

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''
            INSERT INTO queries (case_type, case_number, filing_year, raw_html)
            VALUES (?, ?, ?, ?)
        ''', (case_type, case_number, filing_year, raw_html))
        conn.commit()
        conn.close()

        return render_template('result.html', details=details)
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)