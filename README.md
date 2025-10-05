# YouTube Gesture Controller

Small Python project that uses MediaPipe and OpenCV to detect hand gestures from your webcam and control YouTube playback using keyboard shortcuts (via PyAutoGUI).

## Features

- Detects simple finger gestures to control YouTube:
  - Play (Palm)
  - Pause (Fist)
  - Next video (Pointer finger)
- Visualizes hand landmarks in a window using OpenCV.
- Uses a cooldown (default 3s) to avoid repeated actions.

## Files

- `YoutubeGestureController.py` - Main runner that captures webcam frames, reads gestures and sends keyboard events.
- `HandTrackingModule.py` - Hand detection helper built on MediaPipe. Exposes `handDetector` class with `findHands`, `findPosition`, and `getFingers`.
- `requirements.txt` - Python dependencies used by the project.

## Prerequisites

- Python 3.8+ (3.10/3.11 recommended)
- A working webcam

Note: Use a virtual environment.

## Quick setup

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Run

In the activated virtual environment run:

```powershell
python YoutubeGestureController.py
```

- The script opens a window showing the webcam feed with hand landmarks.
- Gesture labels are drawn on the image.
- By default, press `q` in the video window to quit the `YoutubeGestureController.py` loop. (The `HandTrackingModule.py` sample `main()` uses the `Esc` key to exit.)

## Troubleshooting & Tips

- If actions don't trigger, make sure the browser window with YouTube has focus. PyAutoGUI sends system-wide keyboard events but the player must be focused.
- If the thumb logic is inverted for your hand, try changing `handType` from `"Right"` to `"Left"` when calling `getFingers`.
- If camera index 0 does not work, try `cv2.VideoCapture(1)` or another index.

## Development

- To run the hand tracker visualization only, run `HandTrackingModule.py` (it contains a `main()` helper).
- The code is simple and intended as a starting point; will add more gestures and map them to additional YouTube shortcuts.

## Acknowledgements

Built using MediaPipe, OpenCV and PyAutoGUI.
