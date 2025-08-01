Court Case Info Fetcher (Flask App)
This is a Flask web application that simulates fetching and displaying court case information based on user input. The data is stored in an SQLite database, and the app can be extended to integrate real-time web scraping or external APIs in the future.

🚀 Features
Input form for case type, case number, and filing year

Simulated data retrieval (can be replaced with real scraping logic)

Displays:

Case parties

Filing date

Next hearing date

List of document links (PDFs)

Stores queries and raw HTML into a local SQLite database

Error handling for unexpected issues

🛠 Tech Stack
Flask (Python Web Framework)

SQLite (Lightweight SQL Database)

HTML/CSS (with Jinja2 templates for rendering)

Simulated scraping logic (can be extended)

📂 Folder Structure
pgsql
Copy
Edit
project/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── error.html
├── database.db
└── app.py
💡 Getting Started
Clone the repo

Install Flask

bash
Copy
Edit
pip install flask
Run the app

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000

🔄 Future Improvements
Integrate actual web scraping logic (e.g. with requests + BeautifulSoup)

PDF download feature using send_file

Admin panel to view stored queries

Add authentication layer

Export database entries as CSV

🧠 Author
Developed with 💻 SRINJOY BISWAS
