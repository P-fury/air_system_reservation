from flight import Flight
from planes import AirbusA380,Boeing737Max
from helpers import card_printer

def main():
    airbus = AirbusA380()
    boeing = Boeing737Max()


    f = Flight('LO127', airbus)

    f_2 = Flight('LO128', boeing)
    print(f_2.get_empty_seat())
    f_2.allocate_passenger(passenger='Jak Mak', seat='24A')
    f_2.allocate_passenger(passenger='Jak Bak', seat='15A')
    print(f_2.get_empty_seat())
    f_2.allocate_passenger(passenger='Zak Bak', seat='15B')
    f_2.allocate_passenger(passenger='Fak Bak', seat='12A')
    print(f_2.get_empty_seat())
    print([passenger for passenger in f_2.get_passenger_list()])

    print(f_2.print_tickets(card_printer))

print(__name__)
if __name__ == '__main__':
    main()