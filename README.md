# FreeriderHD Track Downloader Website

## 🚀 Live Site: [https://freeriderhd-track-downloader.onrender.com](https://freeriderhd-track-downloader.onrender.com)

*(It may take a few minutes to load from a cold spin-up.)*

A streamlined open-source Flask web application designed to help FreeRiderHD players efficiently retrieve, view, and copy raw track codes directly from any FreeRiderHD track URL. Simply paste a track link, and the app extracts the unique track code from FreeRiderHD's CDN, allowing you to easily back up, edit, or share your track data.

---

## 🧩 What this does

This lightweight web app extracts the unique track code from any FreeRiderHD track URL.
By parsing the track ID and fetching JSON data directly from FreeRiderHD’s CDN, it allows players to easily view and copy their raw track code for editing or backup.

---

## ⚙️ How it works

1. **User Input:**
   The web interface accepts a FreeRiderHD track URL via a paste friendly input field.

2. **Track Number Extraction:**
   The backend isolates the track number using a regular expression (`t/(\d+)-`).

3. **Data Retrieval:**
   The app constructs a CDN request URL and fetches the JSON track data.

4. **Code Extraction:**
   The JSON response is parsed to isolate the `code` field, which is displayed to the user.

5. **Statistics Display:**
   Track ID, code length, and element count are calculated and displayed in an elegant stats bar.

6. **Copy & Download Functions:**
   Users can either copy the extracted track code directly to the clipboard or download it as a `.txt` file.

7. **Error Handling:**
   Invalid URLs or failed fetches return clean, user-friendly messages with visual feedback.

---

## 🧠 Key Functions

**`index()`**
Displays the main page (`index.html`) with the step-by-step UI, animated particles, and dark mode toggle.

**`about()`**
Renders the about page (`about.html`) with project information and development roadmap.

**`popular()`**
Displays the popular tracks page (`popular.html`) with custom SVG track previews and quick download options.

**`fetch_data()`**

* Extracts the track number from the user-provided link.
* Fetches the FreeRiderHD JSON data file from the CDN.
* Parses and returns the `code` field along with statistics.

---

## 📂 Folder Layout

```
FRHDTrackPuller/
│
├── static/
│   ├── favicon.png
│   └── styles.css
│
├── templates/
│   ├── index.html          
│   ├── about.html          
│   └── popular.html       
│
├── app.py
└── requirements.txt
```

---

## 🚀 Quick Start

**Local Installation**

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

**Build Command:**

```
pip install -r requirements.txt
```

**Start Command:**

```
python app.py
```

---

## 🧾 Example

**Input URL:**

```
https://www.freeriderhd.com/t/123456-sample-track
```

**Output:**

```
{ "code": "1i 11 1i,-d 1i 3 1j g 1i,10 1i..." }
```

**Actions:**

📋 Copy to Clipboard - 💾 Download as File - 🗑️ Clear All

---

## 🌟 Pages

**Home:** 
Main track downloader with code extraction, stats, and download tools.

**About:**
Project overview, roadmap, and the future features that will be added.

**Popular:**
Browse featured and popular tracks with quick preview, copy, and download.

---

## 🛠️ Technologies

* **Backend:** Flask (Python)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Design:** Glass-morphism, gradient themes, SVG graphics
* **Animations:** CSS keyframes, transform animations
* **Icons:** Unicode emoji and custom SVG

---

## 🌓 Light & Dark Themes

**Light Mode:**
Clean, modern interface with floating purple and pink particle effects.

**Dark Mode:**
Elegant dark theme with enhanced particle visibility and purple accents.

---

## ⚖️ Notes

* This project is intended for **personal use only**.
* Use responsibly; do not redistribute copyrighted FreeRiderHD tracks.
* All credit for FreeRiderHD and its content belongs to the original developers.
* The UI design features modern web technologies including CSS backdrop filters, CSS gradients, and SVG graphics.
  
---

## 📜 License

Open Source, feel free to fork, modify, and use for personal projects.

---

## 👨‍💻 Credits & Contact

Created by **[@Praetorian301](https://github.com/Praetorian301)**.

---
