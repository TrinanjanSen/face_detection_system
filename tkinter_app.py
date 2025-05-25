import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from face_attendance_system import capture_face_image, recognize_and_mark_attendance

def capture_face():
    name = name_entry.get()
    if not name:
        messagebox.showwarning("Input Error", "Please enter a name before capturing.")
        return
    try:
        capture_face_image(name)
        messagebox.showinfo("Capture Complete", f"Image for {name} captured successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def start_attendance():
    messagebox.showinfo("Attendance System", "Starting attendance system...")
    try:
        recognize_and_mark_attendance(timeout=60)  # Optional: Adjust timeout here
        messagebox.showinfo("Done", "Attendance marking completed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def exit_app():
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("600x400")
root.configure(bg="#2E4053")

header = tk.Label(root, text="Face Recognition Attendance System", font=("Helvetica", 20, "bold"), fg="white", bg="#2E4053")
header.pack(pady=20)

name_frame = tk.Frame(root, bg="#2E4053")
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="Enter Name:", font=("Helvetica", 14), fg="white", bg="#2E4053")
name_label.pack(side="left", padx=5)

name_entry = tk.Entry(name_frame, font=("Helvetica", 14), width=20)
name_entry.pack(side="left", padx=5)

# Button icons
icon_size = (64, 64)
capture_icon = ImageTk.PhotoImage(Image.open("icons/capture.png").resize(icon_size))
attendance_icon = ImageTk.PhotoImage(Image.open("icons/attendance.png").resize(icon_size))
exit_icon = ImageTk.PhotoImage(Image.open("icons/exit.png").resize(icon_size))

button_frame = tk.Frame(root, bg="#2E4053")
button_frame.pack(pady=20)

capture_button = tk.Button(button_frame, image=capture_icon, text="Capture Face", compound="top", font=("Helvetica", 12), fg="white", bg="#1ABC9C", command=capture_face, width=120, height=120)
capture_button.grid(row=0, column=0, padx=20)

attendance_button = tk.Button(button_frame, image=attendance_icon, text="Start Attendance", compound="top", font=("Helvetica", 12), fg="white", bg="#3498DB", command=start_attendance, width=120, height=120)
attendance_button.grid(row=0, column=1, padx=20)

exit_button = tk.Button(button_frame, image=exit_icon, text="Exit", compound="top", font=("Helvetica", 12), fg="white", bg="#E74C3C", command=exit_app, width=120, height=120)
exit_button.grid(row=0, column=2, padx=20)

root.mainloop()
