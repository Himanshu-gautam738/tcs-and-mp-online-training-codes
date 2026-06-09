# Movie class stores movie details
class Movie:
    def __init__(self, movie_id, title, genre, duration):
        self.movie_id = int(movie_id)
        self.title = title
        self.genre = genre
        self.duration = int(duration)

    def display(self):
        print(self.movie_id, self.title, self.genre, self.duration, "min")


# Customer class stores customer info
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = int(customer_id)
        self.name = name
        self.bookings = []

    def display(self):
        print(self.customer_id, self.name)


# Booking class links customer and movie
class Booking:
    def __init__(self, booking_id, customer, movie, seats, amount):
        self.booking_id = int(booking_id)
        self.customer = customer
        self.movie = movie
        self.seats = int(seats)
        self.amount = float(amount)

    def display(self):
        print(self.booking_id, self.customer.name, self.movie.title, self.seats, self.amount)


# Theater class controls whole system
class Theater:
    def __init__(self):
        self.movies = []
        self.customers = []
        self.bookings = []

    # add new movie
    def add_movie(self):
        mid = int(input("Movie ID: "))
        title = input("Title: ")
        genre = input("Genre: ")
        duration = int(input("Duration: "))
        m = Movie(mid, title, genre, duration)
        self.movies.append(m)
        print("Movie added\n")

    # show all movies
    def show_movies(self):
        for m in self.movies:
            m.display()
        print()

    # add customer
    def add_customer(self):
        cid = int(input("Customer ID: "))
        name = input("Name: ")
        c = Customer(cid, name)
        self.customers.append(c)
        print("Customer added\n")

    # show customers
    def show_customers(self):
        for c in self.customers:
            c.display()
        print()

    # book ticket
    def book_ticket(self):
        bid = int(input("Booking ID: "))
        cid = int(input("Customer ID: "))
        mid = int(input("Movie ID: "))
        seats = int(input("Seats: "))
        price = float(input("Price per seat: "))

        customer = None
        movie = None

        for c in self.customers:
            if c.customer_id == cid:
                customer = c

        for m in self.movies:
            if m.movie_id == mid:
                movie = m

        if customer is None or movie is None:
            print("Invalid customer or movie\n")
            return

        total = seats * price
        b = Booking(bid, customer, movie, seats, total)
        self.bookings.append(b)
        customer.bookings.append(b)
        print("Booking done\n")

    # show bookings
    def show_bookings(self):
        for b in self.bookings:
            b.display()
        print()


theater = Theater()

while True:
    print("1 Add Movie")
    print("2 Show Movies")
    print("3 Add Customer")
    print("4 Show Customers")
    print("5 Book Ticket")
    print("6 Show Bookings")
    print("7 Exit")

    ch = input("Choice: ")

    if ch == "1":
        theater.add_movie()
    elif ch == "2":
        theater.show_movies()
    elif ch == "3":
        theater.add_customer()
    elif ch == "4":
        theater.show_customers()
    elif ch == "5":
        theater.book_ticket()
    elif ch == "6":
        theater.show_bookings()
    elif ch == "7":
        break
    else:
        print("Wrong choice\n")