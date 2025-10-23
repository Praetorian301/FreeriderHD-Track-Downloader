FreeriderHD-Track-Downloader

A streamlined open-source Flask web application designed to help FreeRiderHD players retrieve track data quickly and efficiently.
Hosted version: https://freeriderhd-track-downloader.onrender.com

🧩 What this does

This lightweight web app extracts the unique track code from any FreeRiderHD track URL.
By parsing the track ID and fetching JSON data directly from FreeRiderHD’s CDN, it allows players to easily view and copy their raw track code for editing or backup.

⚙️ How it works

User Input:
The web interface accepts a FreeRiderHD track URL.

Track Number Extraction:
The backend isolates the track number using a regular expression (t/(\d+)-).

Data Retrieval:
The app constructs a CDN request URL and fetches the JSON track data.

Code Extraction:
The JSON response is parsed to isolate the code field, which is displayed to the user.

Copy Function:
Users can copy the extracted track code directly to the clipboard.

Error Handling:
Invalid URLs or failed fetches return clean, user-friendly messages.

🧠 Key Functions

index()
Displays the main page (index.html) with the input field and UI layout.

fetch_data()

Extracts the track number from the user-provided link.

Fetches the FreeRiderHD JSON data file from the CDN.

Parses and returns the code field for display.

find_available_port() (optional utility)
Ensures the app locates an available port to run when deployed locally.

🧰 Folder Structure
FRHDTrackPuller/
│
├── static/
│   ├── favicon.png
│   ├── newLogo.png
│   └── styles.css
│
├── templates/
│   └── index.html
│
└── app.py

🚀 Quick Start
Local Installation

Install dependencies:

pip install flask requests


Run the app:

python app.py


Open your browser and visit:

http://127.0.0.1:5000

🌐 Deployment

This app can be easily deployed using Render
, Heroku
, or any Flask-compatible hosting service.
Ensure your environment defines the PORT variable when deploying.

🧾 Example

Input URL:

https://www.freeriderhd.com/t/123456-sample-track


Output:

{ "code": "AAAAABBBBCCCC..." }

⚖️ Notes

This project is intended for personal use only.

Use responsibly; do not redistribute copyrighted FreeRiderHD tracks.

All credit for FreeRiderHD and its content belongs to the original developers.

Created by @Praetorian301
