## Color Calibrator for OpenCV

* This tool allows you to find the optimal HSV (Hue, Saturation, Value) ranges for object detection in real-time. It is particularly useful for robotics projects, such as tracking colored balls or following lines.

## How it works

* The script captures live video from your camera and applies a color filter. By adjusting the trackbars (sliders), you can filter out background noise and isolate a specific object by its color.

## Preparation

# Requirements

* Raspberry Pi (or PC with a webcam)
* Python 3.x
* OpenCV and NumPy libraries

```
$ pip install opencv-python numpy
```

# setup
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
## License

* This software package is licensed under the 3-Clause BSD License.
* © 2026 Ruiyyyyy
