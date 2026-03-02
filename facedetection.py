import cv2

import mediapipe as mp


mp_drawing=mp.solutions.drawing_utils # used to draw pts and lines 

mp_face_mesh = mp.solutions.face_mesh # landmark face detection 

drawing_spec=mp_drawing.DrawingSpec(thickness=1 , circle_radius=1, color=(0,255,0)) #drawing on landmarks -> thickness , radius , color
x=int(input("enter the number of faces to detect : "))
cap=cv2.VideoCapture(0) #capture video for indefinite time 

with mp_face_mesh.FaceMesh(
    max_num_faces=x,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh :                                      #initialize the model 
    
    while True:
        _, frame=cap.read()

        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # opencv -> BGR format ,  mediapipe -> RGB format
        frame.flags.writeable=False # improve performance 
        results = face_mesh.process(frame)
        frame= cv2.cvtColor(frame ,cv2.COLOR_RGB2BGR) #convert back to display
        
        if results.multi_face_landmarks:
            cv2.putText(frame, f"FACE: {len(results.multi_face_landmarks)}", (10,40), cv2.FONT_HERSHEY_COMPLEX,1, color=(255,0,0))

            for face_landmarks in results.multi_face_landmarks:  #loop to detect each face
                mp_drawing.draw_landmarks(
                    
                    image=frame,
                    landmark_list=face_landmarks , # facelandmarks return list
                    connections=mp_face_mesh.FACEMESH_TESSELATION, #creates a triangular mesh acroos face 
                    landmark_drawing_spec=drawing_spec,  #thickness , color for landmarks / circles 
                    connection_drawing_spec=drawing_spec # thickness , color for connections ->lines








                )
        cv2.imshow("faces detection", frame)
        if cv2.waitKey(1)==27: #press ESC to exit 
            
            break

cap.release()
cv2.destroyAllWindows()


                 
                


