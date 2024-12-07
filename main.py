import cv2
from util import get_limits

COLORS = {
    'Red': [0, 0, 255],
    'Yellow': [0, 255, 255],
    'Blue': [255, 0, 0]
}

MIN_CONTOUR_AREA = 500
WINDOW_NAME = 'Color Detection'

def draw_contours(frame, contours, color_name):
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > MIN_CONTOUR_AREA:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, color_name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

def process_frame(frame, lower_limits, upper_limits, color_names):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for lower, upper, name in zip(lower_limits, upper_limits, color_names):
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        draw_contours(frame, contours, name)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    lower_limits, upper_limits = get_limits(list(COLORS.values()))
    color_names = list(COLORS.keys())

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        processed_frame = process_frame(frame, lower_limits, upper_limits, color_names)
        cv2.imshow(WINDOW_NAME, processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
