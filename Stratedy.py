class Strategy:

    def getThreshold(self, x):

        default_threshold = 25
        dynamic_threshold = 100 - x

        if dynamic_threshold < default_threshold:
            return dynamic_threshold
        else:
            return default_threshold

    def shouldHold(self, score):

        if score > self.getThreshold(score):
            return True
        else:
            return False
