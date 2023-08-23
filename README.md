
TOOL NAME:Mediapipe

TEAM MEMBERS: 
* Ashok A
* Ramalingam A
* Hariram s

PROBLEM STATEMENT : Developing an application for yoga pose detection.The primary goal of Yoga pose detection application is to provide standard and correct yoga postures using computer vision,Analyze human poses to detect and practise yoga poses to benefit humans to achieve a healthier life in their homely environment.

INSTALLATION:
  * Python
  * Mediapipe
  * Open cv
  * Flask

USAGE INSTRUCTIONS:

* Run camera_flask_app.py python file
   		; py camera_flask_app.py 

LIBRARY USAGE :

* Setting up the pose function of mediapipe :

    pose = mp_pose.Pose(static_image_mode=True,min_detection_confidence=0.5, model_complexity=2)

* Calculate landmarks and draw landmarks on image

    mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

* Using landmarks of mediapipe , angle is calculated and yoga pose is classified based on the angles 

    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
