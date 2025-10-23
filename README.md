# FreeriderHD-Track-Downloader

A streamlined open-source Flask web app that helps FreeRiderHD players quickly retrieve and copy raw track codes from any track URL.
Hosted version: https://freeriderhd-track-downloader.onrender.com
 (the website may take a few minutes to load)

---

## 🧩 What this does

This lightweight web app extracts the unique **track code** from any FreeRiderHD track URL.
By parsing the track ID and fetching JSON data directly from FreeRiderHD’s CDN, it allows players to easily view and copy their raw track code for editing or backup.

---

## ⚙️ How it works

1. **User Input:**
   The web interface accepts a FreeRiderHD track URL.

2. **Track Number Extraction:**
   The backend isolates the track number using a regular expression (`t/(\d+)-`).

3. **Data Retrieval:**
   The app constructs a CDN request URL and fetches the JSON track data.

4. **Code Extraction:**
   The JSON response is parsed to isolate the `code` field, which is displayed to the user.

5. **Copy Function:**
   Users can copy the extracted track code directly to the clipboard.

6. **Error Handling:**
   Invalid URLs or failed fetches return clean, user-friendly messages.

---

## 🧠 Key Functions

**`index()`**
Displays the main page (`index.html`) with the input field and UI layout.

**`fetch_data()`**

* Extracts the track number from the user-provided link.
* Fetches the FreeRiderHD JSON data file from the CDN.
* Parses and returns the `code` field for display.

**`find_available_port()`** *(optional utility)*
Ensures the app locates an available port to run when deployed locally.

---

## 📂 Folder Layout

```
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
```

---

## 🚀 Quick Start

### Local Installation

1. Install dependencies:

   ```
   pip install flask requests
   ```
2. Run the app:

   ```
   python app.py
   ```
3. Open your browser and visit:

   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Deployment

This app can be easily deployed using [Render](https://render.com), [Heroku](https://heroku.com), or any Flask-compatible hosting service.
Ensure your environment defines the `PORT` variable when deploying.

---

## 🧾 Example

**Input URL:**

```
https://www.freeriderhd.com/t/123456-sample-track
```

**Output:**

```
{ "code": "AAAAABBBBCCCC..." }
```

---

## ⚖️ Notes

* This project is intended for **personal use only**.
* Use responsibly; do not redistribute copyrighted FreeRiderHD tracks.
* All credit for FreeRiderHD and its content belongs to the original developers.

---

## 👨‍💻 Credits & Contact

Created by **[@Praetorian301](https://github.com/Praetorian301)**.

---
