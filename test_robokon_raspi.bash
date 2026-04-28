#!/bin/bash -xv
# SPDX-FileCopyrightText: 2026 Ruiyyyyy
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "Error at line ${1}: Test failed!"
    res=1
}

res=0

### 1. LIBRARY CHECK ###
# Check if required Python libraries are installed
python3 -c "import cv2; import numpy; import picamera2" || ng "$LINENO"

### 2. FILE EXISTENCE TEST ###
# Verify that all necessary script files are present
[ -f "display_camera.py" ] || ng "$LINENO"
[ -f "color_calibrator.py" ] || ng "$LINENO"

### 3. HARDWARE RECOGNITION TEST ###
# Check if the Raspberry Pi detects the camera module
libcamera-hello --list-cameras || ng "$LINENO"

### 4. EXECUTION TEST (Smoke Test) ###
# Try running the script for 3 seconds to ensure it doesn't crash immediately
# (Note: This requires a desktop environment/display)
timeout 3s python3 display_camera.py
status=$?

# Status 124 means it was stopped by 'timeout' (which is SUCCESS for us)
# Status 0 means it was closed manually within 3 seconds
[ $status -eq 124 ] || [ $status -eq 0 ] || ng "$LINENO"

[ "$res" = 0 ] && echo "OK - All tests passed!"

exit $res
