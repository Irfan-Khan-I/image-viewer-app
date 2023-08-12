# image-viewer-app
          python image_viewer.py

Installation
    1. Ensure you have Python 3.x installed on your system.
    2. Open a terminal/command prompt.
    3. Navigate to the directory where the image_viewer.py file is located.
    4. Run the app by entering the following command:
          python image_viewer.py
 
      
Introduction
The Image Viewer App is a Python-based graphical user interface (GUI) application that allows users to load, navigate, and zoom images. The app is built using the tkinter library for creating the user interface and the PIL (Pillow) library for image processing and display.

Features
The Image Viewer App provides the following features:
    1. Load Image: Users can load images from their local file system using the "Load Image" button.
    2. Navigation: Users can navigate between loaded images using "Previous" and "Next" buttons.
    3. Zoom In and Out: Users can zoom in and out of images using the "Zoom In" and "Zoom Out" buttons.

      
How to Use
    1. Launch the Image Viewer App.
    2. Click the "Load Image" button to select an image file from your local file system.
    3. Use the "Previous" and "Next" buttons to navigate between loaded images.
    4. Use the "Zoom In" and "Zoom Out" buttons to adjust the zoom level of the displayed image.
    5. Close the app by clicking the close button (X) on the application window.
Code Structure
The image_viewer.py file contains the source code for the Image Viewer App. It is organized as follows:
    • Class Definition: ImageViewerApp class defines the main functionality of the app.
    • Initialization: App initialization and UI setup are performed in the __init__ method.
    • Load Image: load_image method allows users to load an image from the local file system.
    • Display Image: display_image method displays the loaded image on the canvas.
    • Navigation: show_previous_image and show_next_image methods navigate between loaded images.
    • Zoom Functionality: zoom_in, zoom_out, and update_zoom methods handle zooming in and out of images.
    • Main Loop: The if __name__ == "__main__": block initializes the app and starts the main event loop.
Dependencies
    • Python 3.x
    • tkinter library (included with Python standard library)
    • Pillow library (pip install Pillow)
Contributions and Support
This Image Viewer App is open for contributions and improvements. If you encounter any issues or have suggestions, please feel free to contact.
License
This project is licensed under the MIT License.
