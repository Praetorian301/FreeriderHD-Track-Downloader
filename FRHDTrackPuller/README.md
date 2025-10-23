[# FreeriderHD-Track-Downloader

https://freeriderhd-track-downloader.onrender.com

Seamless FRHD track code downloader.
](https://freeriderhd-track-downloader.onrender.com
FreeriderHD Track Downloader is a streamlined open source Flask web application designed to help FreeRiderHD players retrieve track data quickly and efficiently. With this tool, users can input a track URL from FreeRiderHD, and the app will automatically extract and display the unique track code.

How It Works

User Input: The app interface accepts a FreeRiderHD track URL from the user.

Track Number Extraction: The app uses a regular expression to isolate the track number from the URL, an essential part of constructing a data link to FreeRiderHD’s servers.

Data Retrieval: Using the extracted track number, the app generates a URL and sends an HTTP request to FreeRiderHD to fetch the track data in JSON format.

Error Handling: If the URL is invalid or data cannot be retrieved, the app provides user-friendly error messages.

Display and Copy: The app extracts the track code from the fetched data and displays it to the user, who can then easily copy it to their clipboard.

Key Functions

index(): Displays the main page with an input field for the track URL.

fetch_data(): Handles the URL processing and data retrieval. This function: Extracts the track number from the URL. Constructs and fetches data from the FreeRiderHD server.Parses the response, isolating the code field, and returns it for display.

find_available_port(start_port, max_port): Ensures the app finds an available port to run, incrementing until it finds an open one.)
