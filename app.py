from pprint import pprint as pp


class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [self.flight_number] + [{letter: None for letter in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def allocate_passenger(self, passenger, seat):
        row, letter = self._parse_seat(seat)

        if self.seating_plan[row][letter] is not None:
            return ValueError("Already allocated passenger")
        self.seating_plan[row][letter] = passenger

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

        return row, letter

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f"Seat is unoccupied")

        row_to, letter_to = self._parse_seat(seat_to)
        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f"New seat is occupied")

        self.allocate_passenger(self.seating_plan[row_from][letter_from], seat_to)
        self.seating_plan[row_from][letter_from] = None


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

f.allocate_passenger(passenger='Jak Srak', seat='24A')
pp(f.seating_plan)
f.relocate_passenger("24A", "12A")
pp(f.seating_plan)
