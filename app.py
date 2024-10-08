class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number

    # def __str__(self):
    #     return str(self.flight_number)

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]


class AirPlane:
    pass


class AirbusA380(AirPlane):
    # def __init__(self):
    #     super().__init__()

    @staticmethod
    def get_airplane_model():
        return 'Aribus A380'


class Boeing737Max(AirPlane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing 737 Max'


a = Boeing737Max()
f = Flight('LO127')
print(f.get_airline())
print(f.get_number())
print(a.get_airplane_model())
