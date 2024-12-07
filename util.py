import numpy as np
import cv2
from typing import List, Tuple

def get_green_limits() -> List[Tuple[np.ndarray, np.ndarray]]:
    green_variants = [
        ((35, 50, 50), (85, 255, 255)),   # Verde padrão (ampla faixa)
        ((30, 40, 40), (50, 255, 255)),   # Verde amarelado
        ((70, 40, 40), (90, 255, 255)),   # Verde azulado
        ((35, 50, 20), (85, 255, 100)),   # Verde escuro
        ((35, 20, 20), (85, 255, 80)),    # Verde muito escuro
        ((35, 100, 100), (85, 255, 255)), # Verde brilhante
        ((35, 50, 150), (85, 150, 255)),  # Verde claro
        ((45, 50, 50), (75, 255, 255)),   # Verde médio
        ((20, 50, 50), (40, 255, 255)),   # Verde oliva
        ((50, 100, 100), (70, 255, 255)), # Verde limo
    ]
    return [(np.array(lower, dtype=np.uint8), np.array(upper, dtype=np.uint8)) for lower, upper in green_variants]

def create_color_mask(hsv_image: np.ndarray, lower_limits: List[np.ndarray], upper_limits: List[np.ndarray]) -> np.ndarray:
    mask = np.zeros(hsv_image.shape[:2], dtype=np.uint8)
    for lower, upper in zip(lower_limits, upper_limits):
        mask |= cv2.inRange(hsv_image, lower, upper)
    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask

def apply_deuteranopia_filter(frame: np.ndarray) -> np.ndarray:
    lms_convert = np.array([
        [17.8824, 43.5161, 4.11935],
        [3.45565, 27.1554, 3.86714],
        [0.0299566, 0.184309, 1.46709]
    ]) / 100.0
    
    deuteranopia_sim = np.array([
        [1, 0, 0],
        [0.494207, 0, 1.24827],
        [0, 0, 1]
    ])
    
    rgb_convert = np.array([
        [0.0809444479, -0.130504409, 0.116721066],
        [-0.0102485335, 0.0540193266, -0.113614708],
        [-0.000365296938, -0.00412161469, 0.693511405]
    ]) * 100.0
    
    deuteranopia_matrix = rgb_convert @ deuteranopia_sim @ lms_convert
    return cv2.transform(frame, deuteranopia_matrix)

