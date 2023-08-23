import mediapipe as mp
import matplotlib.pyplot as plt
import cv2
# from calculateAngle import calculateAngle

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

# Setting up the Pose function.
pose = mp_pose.Pose(static_image_mode=True,
                    min_detection_confidence=0.5, model_complexity=2)

# Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils

import math

def calculateAngle(landmark1, landmark2, landmark3):
    

    # Get the required landmarks coordinates.
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3

    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    # Check if the angle is less than zero.
    if angle < 0:

        # Add 360 to the found angle.
        angle += 360
    
    # Return the calculated angle.
    return angle

def classifyPose(landmarks, output_image, display=False):

    # Initialize the label of the pose. It is not known at this stage.
    label = 'Unknown Pose'

    # Specify the color (Red) with which the label will be written on the image.
    color = (0, 0, 255)

    # Calculate the required angles.
    # ----------------------------------------------------------------------------------------------------------------

    # Get the angle between the left shoulder, elbow and wrist points.
    left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

    # Get the angle between the right shoulder, elbow and wrist points.
    right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    # Get the angle between the left elbow, shoulder and hip points.
    left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

    # Get the angle between the right hip, shoulder and elbow points.
    right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                          landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

    # Get the angle between the left hip, knee and ankle points.
    left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    # Get the angle between the right hip, knee and ankle points
    right_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])

    left_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])

    right_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])

    left_bend_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])
    right_bend_hip_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                          landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                          landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])

    left_wrist_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                      landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value])

    right_wrist_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                                       landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value],)

    # ----------------------------------------------------------------------------------------------------------------

    # Check if it is the warrior II pose or the T pose.
    # As for both of them, both arms should be straight and shoulders should be at the specific angle.
    # ----------------------------------------------------------------------------------------------------------------

    # Check if the both arms are straight.
    if left_elbow_angle > 165 and left_elbow_angle < 195 and right_elbow_angle > 165 and right_elbow_angle < 195:

        # Check if shoulders are at the required angle.
        if left_shoulder_angle > 80 and left_shoulder_angle < 110 and right_shoulder_angle > 80 and right_shoulder_angle < 110:

            # Check if it is the warrior II pose.
            # ----------------------------------------------------------------------------------------------------------------

            # Check if one leg is straight.
            if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:

                # Check if the other leg is bended at the required angle.
                if left_knee_angle > 90 and left_knee_angle < 120 or right_knee_angle > 90 and right_knee_angle < 120:

                    # Specify the label of the pose that is Warrior II pose.
                    label = 'Warrior II Pose'

    # ----------------------------------------------------------------------------------------------------------------

    # Check if it is the T pose.
    # ----------------------------------------------------------------------------------------------------------------

            # Check if both legs are straight
            if left_knee_angle > 160 and left_knee_angle < 195 and right_knee_angle > 160 and right_knee_angle < 195:

                # Specify the label of the pose that is tree pose.
                label = 'T Pose'

    # ----------------------------------------------------------------------------------------------------------------

    # Check if it is the tree pose.
    # ----------------------------------------------------------------------------------------------------------------

    # Check if one leg is straight
    if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:

        # Check if the other leg is bended at the required angle.
        if left_knee_angle > 315 and left_knee_angle < 335 or right_knee_angle > 25 and right_knee_angle < 45:

            # Specify the label of the pose that is tree pose.
            label = 'Tree Pose'

    # ----------------------------------------------------------------------------------------------------------------

    # check if it is bhujangasana
    if right_hip_angle >= 110 and right_hip_angle <= 140 or left_hip_angle >= 100 and left_hip_angle <= 140:

        if left_shoulder_angle >= 15 and left_shoulder_angle <= 30 or right_shoulder_angle >= 15 and right_shoulder_angle <= 30:

            if right_knee_angle > 165 and right_knee_angle < 200 or left_knee_angle > 165 and left_knee_angle < 200:

                if right_elbow_angle > 165 and right_elbow_angle < 210 or left_elbow_angle > 165 and left_elbow_angle < 210:
                    label = 'Bhujangasana'

    # ----------------------------------------------------------------------------------------------------------------

    # #check if it is Artha Uttanasana
    if left_hip_angle > 75 and left_hip_angle < 100 or right_hip_angle > 75 and right_hip_angle < 100:
        if left_knee_angle > 175 and left_knee_angle < 190 or right_knee_angle > 175 and right_knee_angle <= 180:
            if left_shoulder_angle > 30 and left_shoulder_angle < 70 or right_shoulder_angle > 30 and right_shoulder_angle < 70:
                label = "Artha Uttanasana"

    # #check if it is uttanpadasana
            if left_shoulder_angle > 165 and left_shoulder_angle < 210 or right_shoulder_angle > 165 and right_shoulder_angle < 210:

                label = "ViraBadhrasana"
    # -----------------------------------------------------------------------------------------------------------------

    # check if trikonasana
    if left_shoulder_angle >= 80 and left_shoulder_angle <= 110 and right_shoulder_angle >= 80 and right_shoulder_angle < 110:
        # if right_bend_hip_angle> 50 and right_bend_hip_angle < 80 or left_bend_hip_angle >50 and left_bend_hip_angle<80:
        if left_hip_angle > 230 and left_hip_angle < 260 or right_hip_angle > 230 and right_hip_angle < 260:
            if left_elbow_angle > 150 and left_elbow_angle < 175 or right_elbow_angle > 150 and right_elbow_angle < 175:
                if left_knee_angle >= 170 and left_knee_angle <= 195 or right_knee_angle >= 170 and right_knee_angle <= 195:
                    label = "Trikonasana"

    # -----------------------------------------------------------------------------------------------------------------

    # check if it is cow pose

    if left_knee_angle > 75 and left_knee_angle <= 110 or right_knee_angle > 75 and right_knee_angle <= 110:
        if left_shoulder_angle > 75 and left_shoulder_angle <= 110 or right_shoulder_angle > 75 and right_shoulder_angle <= 110:
            if left_hip_angle > 75 and left_hip_angle < 100 or right_hip_angle > 75 and right_hip_angle < 100:
                label = "cat-cow pose"

    # -------------------------------------------------------------------------------------------------------------------
    # check for savasana

    # if left_shoulder_angle > 0 and left_shoulder_angle<20 or right_shoulder_angle>0 and right_shoulder_angle<20:
    if left_hip_angle > 165 and left_hip_angle < 210 or right_hip_angle > 165 and right_hip_angle < 210:
        if left_knee_angle > 165 and left_knee_angle < 210 or right_knee_angle > 165 and right_knee_angle <= 210:
            if left_shoulder_angle > 0 and left_shoulder_angle < 20 or right_shoulder_angle > 0 and right_shoulder_angle < 20:
                # if left_wrist_angle>100 and left_wrist_angle< 170 or right_wrist_angle>100 and right_wrist_angle<170:
                label = "savsana"

    # -------------------------------------------------------------------------------------------------------------------
    # check if halasana

    if right_knee_angle >= 70 and right_hip_angle <= 110 or left_knee_angle >= 70 and left_knee_angle <= 110:
        if right_hip_angle >= 30 and right_hip_angle <= 55 or left_hip_angle >= 30 and left_hip_angle <= 55:
            if right_shoulder_angle >= 60 and right_shoulder_angle <= 90 or left_shoulder_angle >= 60 and left_shoulder_angle <= 90:
                label = "Halasana"
    # ---------------------------------------------------------------------------------------------------------------------
     # check if camel pose

    if right_knee_angle >= 80 and right_knee_angle <= 100 or left_knee_angle >= 80 and left_knee_angle <= 100:
        if right_shoulder_angle >= 60 and right_shoulder_angle <= 80 or left_shoulder_angle >= 60 and left_shoulder_angle <= 80:
            if right_hip_angle >= 105 and right_hip_angle <= 145 or left_hip_angle >= 105 and left_hip_angle <= 145:
                label = "camel pose"

    # ---------------------------------------------------------------------------------------------------------------------
    # check if peacock pose

    if left_elbow_angle >= 80 and left_elbow_angle <= 110 or right_elbow_angle >= 80 and right_elbow_angle <= 110:
        if left_hip_angle > 165 and left_hip_angle < 210 or right_hip_angle > 165 and right_hip_angle < 210:
            if left_knee_angle > 165 and left_knee_angle < 210 or right_knee_angle > 165 and right_knee_angle <= 210:
                label = "peacock pose"

    # Check if the pose is classified successfullyu
    if label != 'Unknown Pose':

        # Update the color (to green) with which the label will be written on the image.
        color = (0, 255, 0)

    # Write the label on the output image.
    cv2.putText(output_image, label, (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    # Check if the resultant image is specified to be displayed.
    if display:

        # Display the resultant image.
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')

    else:

        # Return the output image and the classified label.
        return output_image, label
