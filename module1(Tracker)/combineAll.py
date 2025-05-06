from captureImage import picture
from imageToSunCoords import sunBoundingBox
from rotationLogic import rotateMotorAntiClockwise, rotateMotorClockwise

while True:
    currImage = picture()
    sunLocation = sunBoundingBox(currImage)
    sunCenter = (sunLocation[0] + sunLocation[2]) / 2
    imageCenter = (0 + currImage.shape[1]) / 2
    if sunCenter < imageCenter:
        rotateMotorClockwise()
    else:
        rotateMotorAntiClockwise()