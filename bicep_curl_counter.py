import numpy as np
import mediapipe as mp
import cv2
from tkinter import Tk, Button, Label,PhotoImage
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

from PIL import Image
mp_drawing =mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

import tkinter
splash =Tk()


backgroundImage = PhotoImage(file="Background.png")
bg_image = Label(splash,image=backgroundImage)
bg_image.pack()

splash.overrideredirect(True)


label = Label(
    splash,
    text="YOUR PERSONAL AI TRAINER IS LOADING PLEASE WAIT....",
    font=("yu gothic ui bold", 15 * -1),
    bg="#1F41A9",
    fg="#FFFFFF"
)
label.place(x=60,y=180)


root=Tk()
def main_window():
    splash.withdraw()


    root.configure(bg="#525561")
    root.geometry("1240x650")
    height = 650
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.quit()


    def ExitWindow():
        root.quit()
    root.protocol("WM_DELETE_WINDOW" , ExitWindow)


gifImage = "load.gif"
openImage =Image.open(gifImage)
frames = openImage.n_frames
imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
count = 0
showAnimation = None


def animation(count):
    global showAnimation
    newImage = imageObject[count]


    gif_Label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation =splash.after(50, lambda :animation(count))
gif_Label = Label(splash, image="")
gif_Label.place(x=200, y=220, width=100, height=100)

splash.after(3000, main_window)

animation(count)

splash.mainloop()










def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle


def count_bicep_curls(landmarks, prev_angle, counter, stage, hand):
    shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
             landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
             landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

    if hand == "left":
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

    angle = calculate_angle(shoulder, elbow, wrist)

    if angle > 160:
        stage = "down"

    if angle < 50 and stage == 'down':
        stage = "up"
        counter += 1
        print(f'{hand.capitalize()} Bicep Curl Reps: {counter}')

    return angle, counter, stage


def update_interface(selection):
    global selected_hand
    selected_hand = selection
    root.quit()



root.title("Bicep Curl Interface Selection")
root.geometry("400x300")
root.configure(bg="#3498db")

label = Label(root, text="Select Hand", font=("Helvetica", 20), bg="#3498db", fg="#ffffff")
label.pack(pady=20)

left_button = Button(root, text="Left Hand", command=lambda: update_interface("left"), font=("Helvetica", 14),
                     bg="#2ecc71", fg="#ffffff", width=15, height=2)
left_button.pack(pady=10)

right_button = Button(root, text="Right Hand", command=lambda: update_interface("right"), font=("Helvetica", 14),
                      bg="#e74c3c", fg="#ffffff", width=15, height=2)
right_button.pack(pady=10)

root.mainloop()

if selected_hand is None:
    print("No hand selected. Exiting.")
else:

    cap = cv2.VideoCapture(0)


    counter_bicep_curl = 0
    stage_bicep_curl = "up"
    prev_angle_bicep_curl = 0


    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                # Count bicep curls based on the selected hand
                angle_bicep_curl, counter_bicep_curl, stage_bicep_curl = \
                    count_bicep_curls(landmarks, prev_angle_bicep_curl, counter_bicep_curl, stage_bicep_curl, selected_hand)

                # Display angle near the selected elbow
                selected_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value] if selected_hand == "right" else landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
                cv2.putText(image, f'{selected_hand.capitalize()} Elbow Angle: {angle_bicep_curl:.2f}',
                            (int(selected_elbow.x * image.shape[1]), int(selected_elbow.y * image.shape[0])),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))


            cv2.rectangle(image, (5, 5), (180, 80), (0, 0, 0), -1)
            cv2.putText(image, f'{selected_hand.capitalize()} Bicep Curls: {counter_bicep_curl}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f'Stage: {stage_bicep_curl}', (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('Bicep Curl Cam', image)

            if cv2.waitKey(10) & 0xFF == ord('`'):
                break


    cap.release()
    cv2.destroyAllWindows()
