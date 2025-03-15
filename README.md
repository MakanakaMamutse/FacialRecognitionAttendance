🎭 Facial Recognition Attendance System 📚

📌 Overview

This project is a Facial Recognition Attendance System designed for an online school portal. It leverages facial recognition technology to automate attendance tracking in virtual classrooms. The system registers students, stores their images in a Firebase database, and uses facial recognition libraries to verify attendance in real-time.

✨ Features

📝 Student Registration: Saves student photos into a Firebase database upon registration.

🔍 Face Encoding: After saving the photo, an encoding process takes place to generate unique facial embeddings.

📷 Real-Time Face Scanning: The system continuously scans faces frame by frame.

✅ Automated Attendance Marking:

If the detected face matches a registered student within a set threshold, they are marked "Present". ✅

If the same face is detected too close together in time, it prevents duplicate marking. 🔄

If an unregistered face is detected, no action is taken. ❌

📅 Attendance Logging:

Saves the date and time of attendance. ⏳

Stores student major, study start year (e.g., 2022-2024), and degree information.

🛠 Technologies Used

🐍 Python

📸 OpenCV (for image processing)

🧑‍💻 dlib (for facial recognition)

🔥 Firebase (for storing student images and attendance data)

👁 Face Recognition Library (for encoding and verification)

🚀 Installation & Setup

Clone the Repository

git clone https://github.com/MakanakaMamutse/FacialRecogntionAttendance.git
cd FacialRecogntionAttendance

Install Dependencies 📦

pip install -r requirements.txt

Setup Firebase 🔐

Add your serviceAccountKey.json file (DO NOT COMMIT IT TO GITHUB! ⚠️).

Configure Firebase database settings.

Run the Application ▶️

python main.py

🎯 Usage

Register a new student: Add their image and details to Firebase. 🖼️

Run the recognition system: The system will scan faces and mark attendance. 📊

View attendance logs: Data is stored in Firebase for reference. 📂

🔒 Security Considerations

Ensure serviceAccountKey.json is kept private 🔑.

Do not share personal student data publicly ❌.

Use authentication mechanisms for database access 🔏.

🚧 Future Improvements

🌐 Implement a web interface for easier management.

🔐 Add multi-factor authentication for security.

⚡ Optimize face encoding & detection algorithms for faster processing.