from .airplane import AirPlane

class AirbusA380(AirPlane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus A380'

    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'
