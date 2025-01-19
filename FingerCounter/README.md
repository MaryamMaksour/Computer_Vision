# count finger with cv2


### About the Project

  The AI Finger Counting application uses computer vision techniques to count 
  the number of fingers shown in front of a camera in real-time. It analyzes hand landmarks, checks which fingers are open, and displays a corresponding image.

  **Key Features:**

  - Real-time hand tracking using MediaPipe.
  - Accurate finger counting by analyzing joint positions.
  - Dynamic image overlay based on the number of fingers detected.
  - High performance with smooth rendering and FPS tracking.

  
        
    **Technologies Used:**
    
      - **OpenCV**: For video capture and real-time image manipulation.
      - **MediaPipe**: For hand tracking and landmark detection.
      - **Streamlit**: For creating a user-friendly interface.

    **How It Works:**

    
      1. The application captures video from the webcam.
      2. Detects hands using MediaPipe and identifies the landmarks.
      3. Determines whether each finger is open or closed.
      4. Counts the total number of open fingers and displays an image corresponding to the count.

    **Use Cases:**
    
      - Gesture-based control for interactive applications.
      - Educational tools for teaching numbers to children.
      - Human-computer interaction and AR-based systems.
