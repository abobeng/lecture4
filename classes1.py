class Flight:


    def __init__(self, origin,destination,duration):
        self.origin = origin 
        self.destination = destination
        self.duration = duration

def main():
    #creating flight.
    f = Flight(origin="Accra", destination="Kumasi", duration="30")

    #print details about flight
    print(f.origin)
    print(f.destination)
    print(f.duration)


if __name__ == "__main__":
    main()