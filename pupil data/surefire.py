import numpy as np
import cv2 as cv
import math

# use a normal image as a placeholder background to test line drawing
#back = cv.imread("C:/Users/mart_/MP4 Cache/animee.png")

# get saved video
A = cv.VideoCapture("world.mp4")

points = []

# get test data
with open("test_data.txt", "r") as test_data:
    lines = test_data.readlines()
    for line in lines:
        line = line[1:-2]
        point = line.split(", ")
        point = list(float(val) for val in point)
        point.append(1.0)
        points.append(point)

"""
a = [-50, 50, -10, 1]
b = [-50, 50, -25, 1]
c = [-70, 50, -25, 1]

points = [a, b, c]
"""

#height = int(back.shape[0] / 2)
#width = int(back.shape[1] / 2)
height = int(A.get(4) / 2)
width = int(A.get(3) / 2)

"""
# draw points onto image
cv.line(back, (int(points[0][0]), int(points[0][1])), (int(points[1][0]), int(points[1][1])), (0, 0, 255), thickness=5)
cv.line(back, (int(points[1][0]), int(points[1][1])), (int(points[2][0]), int(points[2][1])), (0, 0, 155), thickness=5)
cv.imshow("TEST", back)
cv.waitKey()
cv.destroyAllWindows()
"""

    # world to camera transformation
rt = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
])

# focal length, figure out using trial and error for right now
fx = 1000
fy = 1000

# projection transformation using focal length and principle point
ci = np.array([
    [fx, 0, width],
    [0, fy, height],
    [0, 0, 1],
])

# project points and dehomogenize
for i in range(len(points)):
    points[i] = np.dot(rt, points[i])
    points[i] = np.dot(ci, points[i])
    w = points[i][2]
    points[i][0] /= w
    points[i][1] /= w

# find frame information to sync video with gaze line
frames = int(A.get(cv.CAP_PROP_FRAME_COUNT))
ppf = len(points)/frames

i = 0 # frame counter

# draw onto video
while A.isOpened():
    # get current frame
    ret, frame = A.read()

    # get which point is closest matched to current frame
    x = int(i*ppf)

    # create point on frame and display
    cv.circle(frame, (int(points[x][0]), int(points[x][1])), 5, (0, 0, 255), thickness=-1) # gaze point
    cv.circle(frame, (0, 0), 10, (255, 0, 0), thickness=-1) # screen origin
    cv.circle(frame, (width, height), 10, (0, 255, 0), thickness=-1) # view origin
    cv.imshow("INDEV", frame)
    cv.waitKey(40)
    i += 1

# exit program
A.release()
cv.destroyAllWindows()