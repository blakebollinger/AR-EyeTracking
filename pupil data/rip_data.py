from data_point import DataPoint

data_points = []

f = open("decoded_gaze_data.txt", "r")

lineCounter = 1

counter = 0

total_point_counter = 0

for i in f.readlines():

    if counter == 0:
        topic = i
    elif counter == 1:
        norm_pos = i
    elif counter == 2:
        dispersion = i
    elif counter == 3:
        method = i
    elif counter == 4:
        base_data = i
    elif counter == 5:
        timestamp = i
    elif counter == 6:
        duration = i
    elif counter == 7:
        confidence = i
    elif counter == 8:
        gaze_point_3d = i
    elif counter == 9:
        identifier = i

    counter += 1

    if counter > 10:
        data_points.append(DataPoint(topic, norm_pos, dispersion, method, base_data, timestamp, duration, confidence, gaze_point_3d, identifier, total_point_counter))
        counter = 0
        total_point_counter += 1

for i in data_points:
    i.printInfo()

f.close()