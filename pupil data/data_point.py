class DataPoint:

    def __init__(self, topic, norm_pos, dispersion, method, base_data, timestamp, duration, confidence, gaze_point_3d, id, number):

        self.topic = topic
        self.norm_pos = norm_pos
        self.dispersion = dispersion
        self.method = method
        self.base_data = base_data
        self.timestamp = timestamp
        self.duration = duration
        self.confidence = confidence
        self.gaze_point_3d = gaze_point_3d
        self.id = id
        self.number = number

    def printInfo(self):
        print("Datapoint #" + str(self.number))

        print(self.timestamp)