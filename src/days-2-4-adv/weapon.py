class Weapon (object):
    def __init__(self,weapon_name, power, fast_move, kill_shot, smart_move):
        self.weapon_name = weapon_name 
        self.power = power
        self.fast_move = fast_move
        self.kill_shot = kill_shot
        self.smart_move = smart_move
    def __repr__(self):
        return f"Weapon name: {self.weapon_name}, Weapon power: {self.power}, Fast move: {self.fast_move}, Kill shot: {self.kill_shot}, Smart Move: {self.smart_move}"
