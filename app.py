class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def get_place(self):
        return self.airplane.get_seating_plan()


class AirPlane:
    def get_seats_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)


class AirbusA380(AirPlane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus A380'

    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'


class Boeing737Max(AirPlane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing 737 Max'

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'


airbus = AirbusA380()
boeing = Boeing737Max()

f = Flight('LO127', airbus)

# print(f.get_place())
#
# print(f.get_model())
# print(f.get_airline())
# print(f.get_number())
# print(f.get_model())

print(boeing.get_seats_no())
print(airbus.get_seats_no())
