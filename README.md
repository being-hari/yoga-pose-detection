
STATEMENT:
* The fundamental goal of Yoga pose detection and correction is to provide standard yoga poses and help the user to correct their poses with the help of real-time feedback. This proposed tool can assist the user in practicing nine different yoga poses using computer vision, it analyzes the human poses, detects and corrects the user, ensuring  a healthier lifestyle, and promotes well-being for people belonging to all age groups. This application provides a user-friendly environment that benefits users in the process of yoga learning and practice. Live webcams are used to detect the pose of the user and display the name of the Asana with accuracy. Corrections in angles would be mentioned and highlighted. This provides the user a choice to choose from i.e. Demo and Practice where a learning pathway consisting of several Asanas in the right order  is accessible to the user and the detection of yoga poses is also available. The history of learned and practiced Asanas are maintained and displayed to the user.

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
