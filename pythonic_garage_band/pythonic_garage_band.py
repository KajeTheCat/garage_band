from unicodedata import name


class Band:
    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        return Band.instances


class Musician(Band):
    @classmethod
    def get_instrument(cls):
        return cls.instrument


class Guitarist(Musician):
    instrument = "guitar"

    def __init__(self, name):
        self.name = name
        Guitarist.instrument

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    instrument = "bass"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    instrument = "drums"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def play_solo():
        return "rattle boom crash"
