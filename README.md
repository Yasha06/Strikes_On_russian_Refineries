# Burning Barrels: The Russian Oil Refinery Strike Tracker

## Live Demo

**The project is hosted on Render and is available at the following link:**

### ==> [https://burningbarrels.onrender.com](https://burningbarrels.onrender.com) <==

---

**Burning Barrels** is a web-based project developed for a Web Programming course. It provides an interactive visualization of Ukrainian drone strikes on Russian oil refineries since the beginning of the full-scale invasion. The project aims to track and display the economic and strategic impact of these attacks in an accessible and engaging way.

The core feature of the site is an interactive map that visualizes the geography and intensity of the strikes, turning raw data into a compelling story.

## Features

- **Interactive Map:** A dynamic map built with Leaflet.js that displays each targeted refinery.
- **Clustered Data:** Multiple strikes on a single refinery are grouped under one marker, which displays the total number of attacks.
- **Detailed Information:** Clicking on a marker reveals a popup with detailed information about each strike, including the date, a description of the damage, and a photo.
- **Dynamic Data Loading:** All strike data is loaded asynchronously from an external `refineries.json` file, making it easy to update and manage.
- **Responsive Design:** The website is built with Bootstrap 3, ensuring it is accessible on various devices.

## Tech Stack

This project is built with a combination of front-end and back-end technologies:

- **Back-end:**
  - **Python:** The core programming language for the server.
  - **Flask:** A lightweight web framework used to serve the HTML pages and static files.
- **Front-end:**
  - **HTML5:** For the structure of the web pages.
  - **CSS3:** For styling, including custom styles and the Bootstrap framework.
  - **JavaScript (ES6):** For client-side logic and interactivity.
- **Libraries:**
  - **Leaflet.js:** An open-source JavaScript library for creating interactive maps.
  - **Bootstrap 3:** A popular CSS framework for building responsive layouts.
  - **jQuery:** Required for Bootstrap 3 components to function properly.
  ## Asset Setup & Project Videos

**IMPORTANT:** To ensure the website displays correctly, you need to download the media files (images, logos, etc.) which are hosted separately to keep the repository lightweight.

**1. Download the assets:**
   - All necessary media files are available for download from the following Google Drive link:
   
     [**Download All Project Assets from Google Drive**](https://drive.google.com/drive/folders/1bjTYue6w3rUz7_Zd1ZaNtPtvJwVV9ryp?usp=sharing)

**2. What's included:**
   - **Website Media:** A folder with all the images and icons needed for the website to function correctly.
   - **Project Presentation Video:** A short video demonstrating the website's features and functionality.
   - **Project Trailer:** A humorous, entertaining trailer created to set the tone and mood of the project.

**3. Place the files in the correct directory:**
   - After downloading, find the folder containing the website's images (`logo.png`, `pic1.jpg`, etc.).
   - Place all these files inside the `static/assets/` directory in your project folder.
