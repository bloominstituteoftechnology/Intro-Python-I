# Create Item class, arguments are name and description

class Item():
    def _init__(self, name, description)
        self.name = name
        self.description = description
        self.owner = None

    def info(self):
        info_message = self.name + ':\t' + self.description
        return '\n'.join(wrap(info_message, width=50))+ '\n' + '-'*50
