class Journey(object):

    def __init__(self, steps, sequence):
        self.steps = steps
        self.sequence = sequence
        self.valleys = 0

    def num_valleys(self, valleys):
        self.valleys = valleys
