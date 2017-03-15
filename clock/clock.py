class Clock(object):
    def __init__(self, hour, min):
        self.hour = (hour + (min / 60)) % 24
        self.min = min % 60

    def __eq__(self, other):
        return (self.hour == other.hour and
                self.min == other.min)

    def __str__(self):
        return '{0:02d}:{1:02d}'.format(self.hour, self.min)

    def add(self, mins):
        return Clock(((self.hour + (mins / 60)) % 24), (self.min + (mins % 60)))
