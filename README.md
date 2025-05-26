# Face Recognition Attendance System

This project implements an automated attendance system using face recognition with Python. It captures face images, recognizes faces in real-time via a webcam, and logs attendance to an Excel sheet. The system has both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter.

## Features

1.Capture New Face Images via webcam.

2.Real-time Face Recognition with face_recognition library.

3.Excel Attendance Logging (attendance.xlsx).

4.Intuitive GUI for ease of use.

5.Timeout Support for auto-closing attendance after a set time(adjustable , default : 120 seconds).

6. Exit option ("q") during attendance marking.

## 🛠 Requirements
- Python 3.x
- Libraries:
  - `opencv-python`
  - `face_recognition`
  - `numpy`
  - `openpyxl`
Install dependencies using:

pip install opencv-python face_recognition numpy openpyxl




## 📸 Usage
1. **Clone or Download the Repository**
- Clone with Git:
     git clone https://github.com/TrinanjanSen/face_detection_system.git
- Or download the ZIP and extract.

2. **Add Icons (Optional but Recommended)**
   - Place icons (e.g., capture.png, attendance.png, exit.png) inside an "icons" folder in the same directory as the GUI script.

3. **Run the GUI Application**
   - Open a terminal, navigate to the project directory.
   - Run:
     python your_gui_script.py
   - This will launch the GUI window.

4. **Capture Face Images**
   - Enter a name in the "Enter Name" field.
   - Click the "Capture Face" button.
   - The webcam will open; press SPACE to capture images. ESC to cancel.

5. **Start Attendance**
   - Enter the attendance gap (in minutes) in the field (default is 30).
   - Click the "Start Attendance" button.
   - The system will recognize faces and mark attendance in 'attendance.xlsx'.

6. **View Attendance Percentage**
   - Click the "Attendance %" button.
   - A pop-up will display the attendance percentage for each person.

7. **Exit Application**
   - Click the "Exit" button or close the window.

Optional: Command Line Interface (CLI)
-------------------------------------
- Run: python face_attendance_system.py
- Select options from the CLI menu to capture images or start attendance.

License:
--------
This project is open-source and free to use for educational purposes.

Contributions:
--------------
Feel free to fork this repo and contribute!
