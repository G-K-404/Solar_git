def sunBoundingBox(image):
    """
    Calculate the bounding box of the image.
    
    Parameters:
    image (numpy.ndarray): The input image.
    
    Returns:
    tuple: A tuple containing the coordinates of the bounding box (x_min, y_min, x_max, y_max).
    """
    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Define the bounding box coordinates
    x_min = 0
    y_min = 0
    x_max = width - 1
    y_max = height - 1
    
    return (x_min, y_min, x_max, y_max)
