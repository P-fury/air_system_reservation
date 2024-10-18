from .airplane import AirPlane

class Boeing737Max(AirPlane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing 737 Max'

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'