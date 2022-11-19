class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__purchase_history = []
        self.entry_hall(Hall)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        lst = []
        lstr = []
        c = 'A'
        for i in range(self.__rows):
            for j in range(self.__cols):
                lstr.append(c+str(j))
            lst.append(lstr)
            lstr = []
            c = chr(ord(c)+1)

        self.__seats[id] = lst

    def book_seats(self, name, phone, id, seat_lst):
        print("                                       |BOOK TICKET|")
        print("--------------------------------------------------------------------------------------------\n")
        valid_id = False
        for shows in self.__show_list:
            if shows[0] == id:
                valid_id = True
                break

        if valid_id:
            valid_seats = []
            for k in range(len(seat_lst)):
                flag = 1
                for row in self.__seats[id]:
                    for i, seat in enumerate(row):
                        if seat_lst[k] == seat:
                            row[i] += " -X"
                            flag = 0
                            valid_seats.append(seat_lst[k])
                            break

                        elif 'X' in seat and seat_lst[k] in seat:
                            print("THESE SEATS WERE BOOKED - ", seat_lst[k])
                            print(
                                "\n--------------------------------------------------------------------------------------------\n")
                            flag = 0
                            break

                    if flag == 0:
                        break
                if flag == 1:
                    print("INVALID SEAT NO - ", seat_lst[k], "TRY AGAIN!")
                    print(
                        "\n--------------------------------------------------------------------------------------------\n")

            if valid_seats:
                print(
                    "                             ##### TICKET BOOKED SUCCESSFULLY #####\n")
                print(
                    "--------------------------------------------------------------------------------------------\n")
                print("NAME: ", name)
                print("PHONE NUMBER: ", phone, end="\n\n")

                for show in self.__show_list:
                    if show[0] == id:
                        print(f"MOVIE NAME: {show[1]}", end="")
                        self.__print_space(show[1])
                        print(f"TIME: {show[2]}", end="\n")

                print("TICKETS: ", end="")
                for seatno in valid_seats:
                    print(seatno, end=" ")

                print("\nHALL: ", self.__hall_no)
                print(
                    "\n--------------------------------------------------------------------------------------------\n")
                self.__purchase_history.append((name, phone, id, valid_seats))

        else:
            print("Id didn't match with any show!")
            print(
                "\n--------------------------------------------------------------------------------------------\n")

    @classmethod
    def __print_space(cls, name):
        for i in range(22-len(name)):
            print(end=" ")

    def view_show_list(self):
        print("                                    |VIEW ALL SHOWS TODAY|")
        print("--------------------------------------------------------------------------------------------\n")
        for show in self.__show_list:
            print(f"MOVIE NAME: {show[1]}", end="")
            self.__print_space(show[1])

            print(f"SHOW ID: {show[0]}", end="")
            self.__print_space(show[0])

            print(f"TIME: {show[2]}", end="")
            self.__print_space(show[2])

            print()
        print("\n--------------------------------------------------------------------------------------------\n")

    def view_available_seats(self, id):
        valid_id = False
        print("                                    |VIEW AVAILABLE SEATS|")
        print("--------------------------------------------------------------------------------------------")
        for shows in self.__show_list:
            if shows[0] == id:
                valid_id = True
                print(f"MOVIE NAME: {shows[1]}", end="")
                self.__print_space(shows[1])
                print(f"TIME: {shows[2]}\nX for already booked seats")
                print(
                    "--------------------------------------------------------------------------------------------\n")
                for seat in self.__seats[id]:
                    for s in seat:
                        print(s, end="")
                        self.__print_space(f"{s}       ")
                    print()
                print(
                    "\n--------------------------------------------------------------------------------------------\n")
                break

        if valid_id == False:
            print("\nId didn't match with any show!")
            print(
                "\n--------------------------------------------------------------------------------------------\n")


Mitali_hall = Hall(5, 7, "mitali004")

Mitali_hall.entry_show("kgfc2", "KGF-chapter 2", "Nov 18 2022 10:00 PM")
Mitali_hall.entry_show("rrrk", "RRR", "Nov 18 2022 07:00 PM")

while True:
    inp = int(input(
        "1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. '0' for EXIT\nENTER OPTION: "))

    if inp == 1:
        Mitali_hall.view_show_list()

    elif inp == 2:
        id = input("ENTER SHOW ID: ")
        Mitali_hall.view_available_seats(id)

    elif inp == 3:
        name = input("ENTER CUSTOMER NAME: ")
        phone = input("ENTER CUSTOMER PHONE NUMBER: ")
        id = input("ENTER SHOW ID: ")
        quantity = int(input("QUANTITY OF TICKETS (Max: 35): "))

        if quantity > 35:
            print(
                "--------------------------------------------------------------------------------------------\n")
            print("MAX QUANTITY REACHED! try again")
            print(
                "\n--------------------------------------------------------------------------------------------\n")
            continue

        lst = []
        for i in range(quantity):
            lst.append(input(f"{i+1}. ENTER SEAT NO: "))

        Mitali_hall.book_seats(name, phone, id, lst)

    elif inp == 0:
        break

    else:
        print(
            "--------------------------------------------------------------------------------------------\n")
        print("Invalid Option try again!")
        print(
            "\n--------------------------------------------------------------------------------------------\n")
