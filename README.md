### iou-calculator
A simple python program to define and calculate Intersection Over Union (IOU).
Based on:
- http://tsaith.github.io/define-a-detection-window-on-image-with-mouse-through-python-3-and-opencv-3.html
- https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/

### Requirements:
- opencv-python
- scikit-image

### How to use:
1. Run the program through cmd/powershell using "py iou-calculator.py".
2. Load image through the file dialog.
3. Drag cursor from top-left to bottom-right to make a rectangle that marks the ground truth. Press 'c' when done.
4. Drag cursor from top-left to bottom-right to make a rectangle that marks the prediction result. Press 'c' when done.
5. The IOU result should be printed on cmd/powershell.
