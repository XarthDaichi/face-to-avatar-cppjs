import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
  with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = holistic.process(image)
      resultsHand = hands.process(image)

      # Draw landmark annotation on the image.
      bkg = cv2.imread('c:/Users/Xarthy/Desktop/AIFaceBodyandHandPoseDetection/Background.png')
      bkg.flags.writeable = True
      bkg = cv2.cvtColor(bkg, cv2.COLOR_RGB2BGR)

      mp_drawing.draw_landmarks(
          bkg,
          results.face_landmarks,
          mp_holistic.FACEMESH_CONTOURS,
          landmark_drawing_spec=None,
          connection_drawing_spec=mp_drawing_styles
          .get_default_face_mesh_contours_style())
      # mp_drawing.draw_landmarks(
      #     bkg,
      #     results.pose_landmarks,
      #     mp_holistic.POSE_CONNECTIONS,
      #     landmark_drawing_spec=mp_drawing_styles
      #     .get_default_pose_landmarks_style())
      
      if resultsHand.multi_hand_landmarks:
        for hand_landmarks in resultsHand.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
            bkg,
            hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
      # Flip the image horizontally for a selfie-view display.
      cv2.imshow('MediaPipe Holistic', cv2.flip(bkg, 1))
      if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
