import numpy as np
import cv2 as cv

# read in video recording
A = cv.VideoCapture("C:/Users/mart_/Research Resources/Archive/001/exports/000/world.mp4")

# list to hold all gaze intersection points in camera coordinates
points = []

# read in gaze data
with open("test_data.txt", "r") as test_data:
    lines = test_data.readlines()
    for line in lines:
        line = line[1:-2]
        point = line.split(", ")
        point = list(float(val) for val in point)
        point.append(1.0)
        points.append(point)

#print(points)

# get video dimensions
width = A.get(3)
height = A.get(4)
w = int(width/2)
h = int(height/2)

# viewing transformation not needed as 
# gaze already given in camera coordinates

# defining view box values for perspective projection
n = 10000       # near
f = 1           # far
l = -w          # left
r = w           # right
b = -h          # bottom
t = h           # top

# create perspective transformation matrix to NDC based on above values
# it has been slightly modified and the dot is certainly moving a lot now,
# but still does not seem to be matching the movements from exported video
m1 = np.array([
    [(2*n)/(r-l), 0, (r+l)/(r-l), 0],
    [0, (2*n)/(t-b), (t+b)/(t-b), 0],
    [0, 0, -(f+n)/(f-n), (-2*f*n)/(f-n)],
    [0, 0, 1, 0],
])

# holds coordinates mapped to NDC
ndc_points = []

# homogeneous_ndc_coordinate
for a in range(len(points)):
    result = np.dot(m1, points[a])
    ndc_points.append(result)

# dehomogenize and map to pixel values
for i in range(len(ndc_points)):
    ww = ndc_points[i][3]
    ndc_points[i] = list(val / ww for val in ndc_points[i])
    ndc_points[i][0] = int(ndc_points[i][0] * w) #+ w)
    ndc_points[i][1] = int(ndc_points[i][1] * h) #+ h)
    #print(f"({ndc_points[i][0]}, {ndc_points[i][1]})")

# find frame information to sync video with gaze line
frames = int(A.get(cv.CAP_PROP_FRAME_COUNT))
ppf = len(ndc_points)/frames

i = 0 # frame counter
j = 0 # points counter

# draw onto video
while A.isOpened():
    ret, frame = A.read()
    while j < ppf*i:
        result = cv.circle(frame, (ndc_points[i][0], ndc_points[i][1]), 5, (0, 0, 255), thickness=-1)
        cv.imshow("INDEV", result)
        cv.waitKey(75)
        j += ppf
    i += 1

# exit program
A.release()
cv.destroyAllWindows()