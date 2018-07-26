from textwrap import wrap

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.bound = None
    
    def info(self):
        info_message = self.name + ':\t' + self.description
        return '\n'.join(wrap(info_message, width=50))+ '\n' + '-'*50