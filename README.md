# Real-Time-Face-Mesh-Detection-using-OpenCV-MediaPipe
This project uses your webcam to detect multiple faces in real-time and draw a detailed face mesh (468 landmarks per face) using MediaPipe.  The user can dynamically choose how many faces to detect.




---

## 🚀 Features

* 🎥 Real-time webcam face detection
* 👥 Detect multiple faces (user-defined input)
* 🧠 468 facial landmarks per face
* 🕸️ Full face mesh visualization
* ⚡ Optimized for real-time performance

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe

---

## 📦 Installation

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```
pip install opencv-python mediapipe
```

---

## ▶️ Usage

Run the script:

```
python facemesh.py
```

Then:

* Enter the number of faces you want to detect
* Press **ESC** to exit

---

## 🧠 How It Works

* Captures video using OpenCV
* Converts frame from BGR → RGB
* Uses MediaPipe FaceMesh to detect facial landmarks
* Draws mesh using predefined connections
* Displays results in real-time

---

## 📸 Output

* Shows webcam feed with:

  * Face mesh overlay
  * Number of faces detected

---

## ⚠️ Requirements

* Webcam
* Python 3.x

---

## 💡 Future Improvements

* Eye blink detection 👁️
* Face recognition system 🔐
* AR filters (like Instagram) 😎
* Drowsiness detection 🚗

---

## 👨‍💻 Author

Shahid Rasool

---

## ⭐ Contribute

Feel free to fork this repo and improve it!
