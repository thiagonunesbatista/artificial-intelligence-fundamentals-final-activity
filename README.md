### **Color Vision for Deuteranopia**

A project created for the Fundamentals of Artificial Intelligence (FIA) course - Undergraduate, by students Thiago Nunes Batista and Eduardo Gonçalves Souza.

---

## About the Project

This project uses Artificial Intelligence with Computer Vision to identify colors in real-time and display them in two ways:

1. **Detected Color:** How the color is seen by people without color blindness.
2. **Deuteranopia Simulation:** How the color is seen by people with deuteranopia (a type of color blindness that affects the perception of green and red colors).

The idea for this project came from a personal experience: a close family member has Deuteranopia. The solution aims to promote inclusion and accessibility, as well as raise awareness about how people with this condition see the world.

The code detects shades of green in an image in HSV (Hue, Saturation, Value) format and simulates Deuteranopic vision by changing the perception of green to how a person with this condition sees it.

It's important to note that for the code to work correctly, it's necessary to be in an environment with good lighting.

---

## Project Objectives

- Real-time color identification using a webcam or built-in camera.
- Simulation of deuteranopic vision to help people without color blindness understand the perceptual differences.
- Education and Awareness - To show, in a practical and visual way, how deuteranopia impacts color perception.

---

## ️ Technologies Used

- **Python:** Main language, including the use of data types from the standard library (`typing`, `List`, `Tuple`, etc.).
- **OpenCV:** For image capture and color manipulation.
- **NumPy:** For matrix operations and color calculations.

---

## Installation of Dependencies

Install the dependencies listed in the `requirements.txt` file with the following command:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the following command to execute the project:

```bash
python main.py
```
