class Door(object):
    def __init__(self, description="a wooden door", key=None, status=True):
        self.description = description
        self.key = key
        self.status = status

    def unlock(self, key):
        if key == self.key and not self.status:
            self.status = True
            print("you unlock the door.")

    @property
    def is_locked(self):
        return not self.status

