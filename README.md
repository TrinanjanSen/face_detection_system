# Face Recognition Attendance System

This project implements an automated attendance system using face recognition with Python. It captures face images, recognizes faces in real-time via a webcam, and logs attendance to an Excel sheet. The system has both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter.

## Features

1.Capture New Face Images via webcam.

2.Real-time Face Recognition with face_recognition library.

3.Excel Attendance Logging (attendance.xlsx).

4.Intuitive GUI for ease of use.

5.Timeout Support for auto-closing attendance after a set time(adjustable , default : 120 seconds).

6. Exit option ("q") during attendance marking.

## 📁 Project Structure

📂 face-recognition-attendance

├── 📜 face_attendance_system.py

├── 📜 gui.py

├── 📜 README.md

├── 📁 images/ # Stored face images

├── 📁 icons/ # App button icons

│ ├── capture.png

│ ├── attendance.png

│ └── exit.png

└── 📜 attendance.xlsx # Attendance log


# Working steps: -

1.Capture Face
enter user_name -> click on capture face -> enter SPACE to stop

2.Start Attendance
attendace start window -> click ok -> once attendance is marked a message will be displayed "Attendance marked for user_name" ->press "q" to exit
here the date and time is updated in attendace excel sheet (genreated automatically)

3.exit
click on exit to close the face attendance system

# USE
Graphical User Interface (GUI)

python gui.py

Features:

Enter a name and click "Capture Face" to store the face image.

Start Attendance System with one click.

Exit the app.

Attendance

All attendance records are stored in attendance.xlsx.

Images are saved in the images/ folder.


Run the CLI application

python face_attendance_system.py
 
Command Line Interface (CLI)

python face_attendance_system.py

Follow the menu:

Capture new face images.

Start attendance system.

Exit.

Press q to stop attendance check during face recognition.




