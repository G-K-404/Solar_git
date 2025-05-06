from captureImage import picture
from imgToSunBoundingBox import sunBoundingBox
from rotateMotor import rotateMotorAntiClockwise, rotateMotorClockwise
def trackSun():
    """
    Continuously track the sun by capturing images and adjusting the motor position.
    """
    while True:
        # Capture an image
        currImage = picture()
        
        # Get the bounding box of the sun in the image
        sunLocation = sunBoundingBox(currImage)
        
        # Calculate the center of the sun and the center of the image
        sunCenter = (sunLocation[0] + sunLocation[2]) / 2
        imageCenter = (0 + currImage.shape[1]) / 2
        
        # Adjust motor position based on sun's position relative to image center
        if sunCenter < imageCenter:
            rotateMotorClockwise()
        else:
            rotateMotorAntiClockwise()