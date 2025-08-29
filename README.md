# Real-Time Face & Feature Detection Web App

This project is a simple yet powerful web application for real-time detection of faces, eyes, and smiles in user-uploaded images. The app is built with Python using OpenCV for the core computer vision logic and Streamlit for the interactive web user interface.


---

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)


---

## 🚀 About The Project

The goal of this project was to create an interactive web application that leverages classic machine learning models for computer vision tasks. The application uses pre-trained Haar Cascade Classifiers, which are efficient and effective for detecting objects like faces and facial features in real-time.

The user can upload an image through a simple web interface and select which feature they want to detect (faces, eyes, or smiles). The application then processes the image and displays the output with the detected features highlighted by bounding boxes.

---

## ✨ Key Features

* **Multi-Feature Detection:** Capable of detecting faces, eyes, and smiles.
* **Interactive Web UI:** Built with Streamlit for a clean, user-friendly, and responsive interface.
* **Image Upload:** Allows users to easily upload images in various formats (`jpg`, `png`, `jpeg`).
* **Real-Time Processing:** Performs detection and displays results instantly after the user clicks "process".
* **Efficient Backend:** Uses OpenCV's highly optimized Haar Cascade models for fast and reliable detection.

---

## 🛠️ Technologies Used

* **Backend & Vision:** Python, OpenCV
* **Web Framework:** Streamlit
* **Image Handling:** Pillow (PIL), NumPy
* **Models:** Pre-trained Haar Cascade Classifiers (`haarcascade_frontalface_default.xml`, `haarcascade_eye.xml`, `haarcascade_smile.xml`)



