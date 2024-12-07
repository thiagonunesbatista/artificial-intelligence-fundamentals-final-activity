import cv2
import numpy as np
from util import get_green_limits, create_color_mask, apply_deuteranopia_filter

MIN_CONTOUR_AREA = 500 
WINDOW_NAME = 'Green Variants Detection for Deuteranopia'

def draw_contours(frame: np.ndarray, contours: list[np.ndarray]) -> None:
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Green Area: {area:.0f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

def process_frame(frame: np.ndarray, green_limits: list[tuple[np.ndarray, np.ndarray]]) -> np.ndarray:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limits, upper_limits = zip(*green_limits)
    mask = create_color_mask(hsv, lower_limits, upper_limits)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    draw_contours(frame, contours)
    
    return frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera.")
        return

    green_limits = get_green_limits()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Falha ao capturar o frame.")
                break

            processed_frame = process_frame(frame.copy(), green_limits)
            cv2.putText(processed_frame, 'Visao Normal', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            deuteranopia_frame = apply_deuteranopia_filter(frame)
            cv2.putText(deuteranopia_frame, 'Simulação Com Deuteranopia', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            combined_frame = np.hstack((processed_frame, deuteranopia_frame))
            cv2.imshow(WINDOW_NAME, combined_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
