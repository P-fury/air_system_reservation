from pprint import pprint as pp


class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [{letter: None for letter in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def allocate_passenger(self, passenger="Lech K", seat="12C"):
        row, letter = self._parse_seat(seat)

    def _parse_seat(self, seat):
        rows, seats = self.airplane.get_seating_plan()

        letter = seat[-1]

        if letter not in seats:
            raise ValueError(f"Invalid seat letter: {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")
        if row not in rows:
            raise ValueError(f"Row number is out of range: {row}")

        return row,letter

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
# print(f.get_model())
# print(f.get_airline())
# print(f.get_number())
# print(f.get_model())

print(boeing.get_seats_no())
print(airbus.get_seats_no())

pp(f.seating_plan)

f.allocate_passenger(passenger='Jak Srak', seat='12A')
