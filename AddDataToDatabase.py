import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecognition-1909e-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Makanaka Mamutse",
            "major": "Software Eng.",
            "starting_year": 2023,
            "total_attendance": 8,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-11-11 09:58:21"
        },
    "2":
        {
            "name": "Donald Trump",
            "major": "Politics",
            "starting_year": 2024,
            "total_attendance": 1,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-02-11 15:52:14"
        },
    "3":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2024-09-26 13:59:55"
        },
    "4":
        {
            "name": "Kamala Harris",
            "major": "Politics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2024-09-26 13:59:55"
        }
}

for key, value in data.items():
    ref.child(key).set(value)