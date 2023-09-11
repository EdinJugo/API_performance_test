class StudentDao(object):
    def __init__(self, sid, first_name, last_name):
        self.sid = sid
        self.first_name = first_name
        self.last_name = last_name
    def serialize(self):
        return {"sid": self.sid,
                "first_name": self.first_name,
                "last_name": self.last_name}
students = [StudentDao("11/22", "Chad", "Farley"),
            StudentDao("24/22", "Dominic", "Bonilla"),
            StudentDao("15/21", "Mario", "Donovan")
            ]