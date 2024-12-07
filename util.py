import numpy as np
import cv2
from typing import List, Tuple

def get_limits(colors: List[Tuple[int, int, int]]) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    hsv_colors = cv2.cvtColor(np.array(colors, dtype=np.uint8).reshape(-1, 1, 3), cv2.COLOR_BGR2HSV).reshape(-1, 3)
    lower_limits = []
    upper_limits = []
    
    for hsv in hsv_colors:
        hue = hsv[0]
        if hue >= 165:
            lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upper = np.array([180, 255, 255], dtype=np.uint8)
        elif hue <= 15:
            lower = np.array([0, 100, 100], dtype=np.uint8)
            upper = np.array([hue + 10, 255, 255], dtype=np.uint8)
        else:
            lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upper = np.array([hue + 10, 255, 255], dtype=np.uint8)
        
        lower_limits.append(lower)
        upper_limits.append(upper)
    
    return lower_limits, upper_limits
