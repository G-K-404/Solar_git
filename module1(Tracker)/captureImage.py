def picture():
    import cv2
    import time

    # Initialize the camera
    camera = cv2.VideoCapture(0)

    # Allow the camera to warm up
    time.sleep(2)

    # Capture a single frame
    ret, frame = camera.read()

    # Save the captured image to a file
    cv2.imwrite("captured_image.jpg", frame)

    # Release the camera
    camera.release()
    return ret