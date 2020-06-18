'''
MouseBoundingBoxes from : http://tsaith.github.io/define-a-detection-window-on-image-with-mouse-through-python-3-and-opencv-3.html
IOUCalculation from : https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
'''
import cv2
from skimage import data
import tkinter
from tkinter import filedialog

def define_rect(image):
    """
    Define a rectangular window by click and drag your mouse.

    Parameters
    ----------
    image: Input image.
    """

    clone = image.copy()
    rect_pts = [] # Starting and ending points
    win_name = "image" # Window name

    def select_points(event, x, y, flags, param):
        i = 0
        nonlocal rect_pts
        if event == cv2.EVENT_LBUTTONDOWN:
            rect_pts = [(x, y)]

        if event == cv2.EVENT_LBUTTONUP:
            rect_pts.append((x, y))

            # draw a rectangle around the region of interest
            cv2.rectangle(clone, rect_pts[0], rect_pts[1], (255, 0, 0), 2)
            cv2.imshow(win_name, clone)

    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, select_points)
    
    while True:
        # display the image and wait for a keypress
        cv2.imshow(win_name, clone)
        key = cv2.waitKey(0) & 0xFF

        if key == ord("r"): # Hit 'r' to replot the image
            clone = image.copy()

        elif key == ord("c"): # Hit 'c' to confirm the selection
            break
    
    # close the open windows
    cv2.destroyWindow(win_name)

    return rect_pts

# Prepare Tkinter
root = tkinter.Tk()
root.withdraw()

# Prepare an image for testing
image_path = filedialog.askopenfilename() 
image = cv2.imread(image_path) # A image array with RGB color channels
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert RGB to BGR

# Points of the target window
print("define bounding box for = ground truth (press C if done)")
gt = define_rect(image)
print("define bounding box for = prediction (press C if done)")
pred = define_rect(image)

print("--- target window ---")
xA = max(gt[0][0], pred[0][0])
yA = max(gt[0][1], pred[0][1])
xB = min(gt[1][0], pred[1][0])
yB = min(gt[1][1], pred[1][1])

interArea = max(0, xB-xA+1) * max(0, yB-yA+1)
gtArea = (gt[1][0] - gt[0][0] + 1) * (gt[1][1] - gt[0][1])
predArea = (pred[1][0] - pred[0][0] + 1) * (pred[1][1] - pred[0][1])

iou = interArea/float(gtArea + predArea - interArea)
print("IOU = " + str(iou))