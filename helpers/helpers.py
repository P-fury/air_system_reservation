def card_printer(passenger, seat, airplane, flight_number):
    red = '\033[91m'
    reset = '\033[0m'
    message = f"| passenger : {red}{passenger.title()}{reset}, seat: {seat}, airplane: {airplane}, flight number: {flight_number}|"
    frame = f"+{'-' * (len(message) - 2)}+"
    empty_frame = f"|{' ' * (len(message) - 2)}|"

    banner = [frame, empty_frame, message, empty_frame, frame]
    print('\n'.join(banner))
