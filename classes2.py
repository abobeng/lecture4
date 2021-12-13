class Flight:


    def __init__(self, origin,destination,duration):
        self.origin = origin 
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destinaniton: {self.destination}")
        print(f"Flight duration(in mins): {self.duration}")

def main():
         f1 = Flight(origin="Accra", destination="Kumasi", duration="40")
         f1.print_info()

         f2 = Flight(origin="Accra", destination="Cape Coast", duration="30")
         f2.print_info()


if __name__ == "__main__":
    main()