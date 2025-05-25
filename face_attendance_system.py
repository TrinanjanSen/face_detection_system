import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
from openpyxl import Workbook, load_workbook
import time

def capture_face_image(person_name):
    folder = 'images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = f"{folder}/{person_name}.jpg"

    cap = cv2.VideoCapture(0)
    print("Press SPACE to capture image, ESC to cancel")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Capture Face", frame)
        key = cv2.waitKey(1)

        if key % 256 == 27:  # ESC
            print("Capture cancelled.")
            break
        elif key % 256 == 32:  # SPACE
            if face_locations:
                cv2.imwrite(file_path, frame)
                print(f"Image saved as {file_path}")
            else:
                print("No face detected! Try again.")
            break

    cap.release()
    cv2.destroyAllWindows()


def load_known_faces(known_faces_dir='images'):
    known_encodings = []
    known_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"Warning: No face found in {filename}")
    return known_encodings, known_names


def mark_attendance_excel(name):
    file_name = 'attendance.xlsx'
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(file_name):
        wb = Workbook()
        ws = wb.active
        ws.append(['Name', 'Timestamp'])
        wb.save(file_name)

    wb = load_workbook(file_name)
    ws = wb.active

    today = now.strftime('%Y-%m-%d')
    already_marked = False
    for row in ws.iter_rows(values_only=True):
        if row[0] == name and row[1].startswith(today):
            already_marked = True
            break

    if not already_marked:
        ws.append([name, dt_string])
        wb.save(file_name)
        print(f"Attendance marked for {name}")


def recognize_and_mark_attendance(timeout=120):
    known_encodings, known_names = load_known_faces()
    if not known_encodings:
        print("No known faces found. Please add images first.")
        return

    cap = cv2.VideoCapture(0)
    print("Starting Face Recognition Attendance System...")

    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
                mark_attendance_excel(name)

            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Attendance System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("User pressed 'q'. Exiting...")
            break

        if time.time() - start_time > timeout:
            print(f"Timeout reached ({timeout}s), closing...")
            break

    cap.release()
    cv2.destroyAllWindows()


def cli_main():
    while True:
        print("\n=== Face Recognition Attendance System ===")
        print("1. Capture New Face Image")
        print("2. Start Attendance System")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            person_name = input("Enter the name of the person to capture: ")
            capture_face_image(person_name)
        elif choice == '2':
            recognize_and_mark_attendance()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


