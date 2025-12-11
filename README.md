🧠 Real-Time Face Recognition System

A complete Python-based Face Recognition System that allows you to:

Capture 100 grayscale images of a user using a webcam

Automatically store them in a user-specific dataset folder

Train a LBPH face recognition model

Perform real-time face recognition with bounding boxes and user labels

Detect unknown faces and label them as “Unknown”

This project uses OpenCV, LBPH, and Haar Cascades to implement a simple yet highly practical face recognition workflow.

🚀 Features
📸 Dataset Preparation

Captures 100 images per user

Converts them to grayscale

Saves them to dataset/<username>/

Perfect for training classical and deep-learning models

🧑‍🏫 Model Training

Uses LBPH Face Recognizer

Learns from the dataset and builds a robust face recognition model

Saves:

face_model.yml

labels.txt

🎥 Real-Time Recognition

Detects faces via webcam using Haar Cascades

Predicts user identity using the trained model

Draws bounding boxes around faces

Displays username above the box

Shows “Unknown” for unrecognized faces

📂 Project Structure
.
├── capture_dataset.py
├── train_model.py
├── realtime_predict.py
├── requirements.txt
├── .gitignore
├── README.md
└── dataset/
    └── <username>/
        ├── image_0.jpg
        ├── ...
        └── image_99.jpg

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2️⃣ Install dependencies
pip install -r requirements.txt

📸 Step 1: Capture Images (Dataset Creation)

Run:

python capture_dataset.py


Enter your name when prompted

Webcam will open

100 grayscale images will be captured

All images stored in:

dataset/<your-name>/

🧑‍🏫 Step 2: Train the Face Recognition Model

Run:

python train_model.py


This script:

Loads all user folders in dataset/

Trains the LBPH model

Saves:

face_model.yml

labels.txt

🎥 Step 3: Real-Time Face Recognition

Run:

python realtime_predict.py


The system will:

Detect faces in webcam feed

Predict the user’s identity

Draw a bounding box

Display the username

Label unknown faces as Unknown

Exit using Q

📌 Requirements
opencv-contrib-python
opencv-python
numpy

🧾 .gitignore (included)

Excludes dataset/

Excludes trained model files

Excludes Python cache, logs, venv

This protects user privacy and keeps the repo clean.

🛠️ Technologies Used

Python

OpenCV / Haar Cascades

LBPH Face Recognizer

NumPy

🔒 Privacy & Security Notes

Your dataset is automatically excluded from GitHub using .gitignore

User images remain fully local

No data leaves your machine

📌 Future Improvements (Optional Enhancements)

You can expand this project with:

Deep learning (FaceNet, OpenFace, Dlib)

Attendance tracking system

GUI using Tkinter or PyQt

FastAPI backend + React frontend

Cloud-based model training

Multi-user recognition

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to modify.

📜 License

This project is licensed under the MIT License.