# 🎭 Facial Recognition Attendance System

## 📌 Overview
This project is a facial recognition-based attendance system for online school portals, classrooms, or school photo verification. It uses facial recognition to identify and mark students as present in a Firebase database.

## 🚀 Features
- Register students and store their images in Firebase
- Encode student images for facial recognition
- Real-time face scanning using OpenCV and dlib
- Automatic attendance marking upon successful face match
- Prevents duplicate marking within a short time window
- Stores student information such as major, enrollment year, and attendance history

## 🛠️ Technologies Used
- **Python** 🐍
- **OpenCV** 📷
- **dlib** 🧠
- **Firebase** 🔥
- **Face Recognition Library**

## 🏗️ Setup and Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/MakanakaMamutse/FacialRecogntionAttendance.git
   ```
2. Navigate into the project folder:
   ```sh
   cd FacialRecogntionAttendance
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your Firebase project and add the necessary credentials (do not commit `serviceAccountKey.json` to GitHub).
5. Run the application:
   ```sh
   python main.py
   ```

## ⚡ How It Works
1. **Student Registration**: When a student is registered, their image is stored in Firebase.
2. **Encoding Process**: The face is encoded into numerical data for comparison.
3. **Face Scanning**: The system scans a live video feed frame by frame.
4. **Comparison**: If a detected face matches a stored face within a set threshold, the student is marked present.
5. **Duplicate Prevention**: If the same face is detected in a short interval, it does not re-mark the student.
6. **Database Logging**: Attendance records, including date and student details, are saved in Firebase.

## 🔧 Possible Improvements
The current implementation has some performance limitations, especially in:
- **Face Detection and Comparison Speed**: The process can be slow when dealing with a large number of faces.
- **Firebase Data Fetching**: Retrieving and comparing data from Firebase can introduce delays.

### 🔹 Suggested Enhancements
1. **Use Asynchronous Functions**: Implement `asyncio` in Python to handle database fetching and face comparisons without blocking execution.
2. **Optimize Face Encoding**: Use more efficient data structures or caching mechanisms to reduce redundant computations.
3. **Parallel Processing**: Utilize multiprocessing or threading to speed up frame analysis.
4. **Model Optimization**: Consider using a lighter model for facial recognition to reduce computation time.
5. **Indexed Database Queries**: Optimize Firebase queries by structuring the database for faster lookups.

## 🤝 Contributing
Feel free to fork this project and contribute improvements!

![facialRecogntion](https://github.com/user-attachments/assets/7c2d5bb6-f910-455e-bf14-4a5a69c556f9)


