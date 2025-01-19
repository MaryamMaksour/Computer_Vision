# AI Personal Trainer

### About the Project

This application leverages advanced computer vision techniques to create an AI-powered personal trainer. 
It analyzes workout movements in real-time, providing feedback on form and counting repetitions of exercises such as dumbbell curls.

  **Key Features:**
        - **Real-time pose detection** using MediaPipe.
        - **Repetition counting** based on the angles between joints.
        - **Visual feedback** on workout performance.
        - Highly customizable for various exercises.

  **Technologies Used:**
        - **OpenCV**: For video capture and frame processing.
        - **NumPy**: For numerical operations and interpolation.
        - **MediaPipe**: For accurate pose detection and landmark tracking.
        - **Streamlit**: To create an interactive web interface.

  **How It Works:**
        1. The application captures video frames from a pre-recorded video or webcam.
        2. Detects body landmarks and calculates angles between joints using MediaPipe.
        3. Tracks the exercise repetitions and provides real-time feedback.

  **Use Cases:**
        - Fitness training with form correction.
        - Home workouts with AI-driven guidance.
        - Rehabilitation exercises requiring precise movements.
