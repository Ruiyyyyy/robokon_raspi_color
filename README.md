## Color Calibrator for OpenCV

* This tool allows you to find the optimal HSV (Hue, Saturation, Value) ranges for object detection in real-time. It is particularly useful for robotics projects, such as tracking colored balls or following lines.

# How it works

* The script captures live video from your camera and applies a color filter. By adjusting the trackbars (sliders), you can filter out background noise and isolate a specific object by its color.

# Preparation

* Raspberry Pi (or PC with a webcam)
* Python 3.x
* OpenCV and NumPy libraries

```
$ pip install opencv-python numpy
```

# Setup

* Clone this repository and ensure the script has execution permissions:

```
$ git clone https://github.com/Ruiyyyyy/robokon_raspi_color.git
$ cd robokon_raspi_color
```

## Usage

* Run the script using Python:

```
$ python3 color.py
```

# Instructions:

* Adjust the Sliders: Move the H, S, and V sliders in the "Calibrador" window.

* Isolate the Object: Watch the "Mask" or "Resultado" window. Your goal is to make the target object appear pure white (in the Mask) or in its original color (in Resultado), while the background becomes completely black.

* Get the Values: Once isolated, look at the values on the sliders. You can use these min and max values in your actual robot vision code.

* Exit: Press the q key on your keyboard to stop the program.

# License

* This software package is licensed under the 3-Clause BSD License.
* © 2026 Ruiyyyyy

