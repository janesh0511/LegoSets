
class LegoSet:
    _total_created = 0
    _active_count = 0
    _total_active_pieces = 0
    _next_id = 1

    def __init__(self, name=None, pieces=None, price=None):
        if name is None and pieces is None and price is None:
            name = "Classic LEGO Set"
            pieces = 1000
            price = 49.99
        elif name is None or pieces is None or price is None:
            raise ValueError("All properties must be provided.")

        self._validate_name(name)
        self._validate_pieces(pieces)
        self._validate_price(price)

        self._set_id = f"LEGO-{LegoSet._next_id:03d}"
        self._name = name
        self._pieces = pieces
        self._price = price
        self._active = True

        LegoSet._next_id += 1
        LegoSet._total_created += 1
        LegoSet._active_count += 1
        LegoSet._total_active_pieces += pieces

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty.")

    @staticmethod
    def _validate_pieces(pieces):
        if type(pieces) != int or pieces <= 0:
            raise ValueError("Pieces must be a positive integer.")

    @staticmethod
    def _validate_price(price):
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

    def get_name(self):
        return self._name

    def get_pieces(self):
        return self._pieces

    def get_price(self):
        return self._price

    def get_active(self):
        return self._active

    def set_name(self, name):
        self._validate_name(name)
        self._name = name

    def set_pieces(self, pieces):
        self._validate_pieces(pieces)

        if self._active:
            LegoSet._total_active_pieces += pieces - self._pieces

        self._pieces = pieces

    def set_price(self, price):
        self._validate_price(price)
        self._price = price

    def upgrade(self, additional_pieces):
        self._validate_pieces(additional_pieces)

        if not self._active:
            raise ValueError("Cannot upgrade an inactive set.")

        self.set_pieces(self._pieces + additional_pieces)
        print(f"{self._name} upgraded to {self._pieces} pieces.")

    def deactivate(self):
        if not self._active:
            print(f"{self._name} is already inactive.")
            return

        self._active = False
        LegoSet._active_count -= 1
        LegoSet._total_active_pieces -= self._pieces

        print(f"{self._name} has been deactivated.")

    def display_info(self):
        print(
            f"ID: {self._set_id} | Name: {self._name} | "
            f"Pieces: {self._pieces} | Price: ${self._price:.2f} | "
            f"Active: {self._active}"
        )

    @classmethod
    def display_stats(cls):
        print(
            f"Total Created: {cls._total_created} | "
            f"Active Sets: {cls._active_count} | "
            f"Active Pieces: {cls._total_active_pieces}"
        )


def main():
    print("LEGO SET MANAGEMENT SYSTEM")

    print("\nPhase 1: Creating LEGO sets")

    set1 = LegoSet()
    set2 = LegoSet("Millennium Falcon", 1353, 169.99)
    set3 = LegoSet("Hogwarts Castle", 2660, 199.99)

    set1.display_info()
    set2.display_info()
    set3.display_info()
    LegoSet.display_stats()

    print("\nPhase 2: Testing invalid values")

    try:
        set2.set_pieces(-500)
    except ValueError as error:
        print("Error:", error)

    try:
        set2.set_name("")
    except ValueError as error:
        print("Error:", error)

    set2.display_info()
    LegoSet.display_stats()

    print("\nPhase 3: Upgrading a LEGO set")

    set2.upgrade(200)
    set2.display_info()
    LegoSet.display_stats()

    print("\nPhase 4: Deactivating a LEGO set")

    set3.deactivate()
    LegoSet.display_stats()

    print("\nPhase 5: Testing repeated deactivation")

    set3.deactivate()
    LegoSet.display_stats()

    print("\nTEST SUITE COMPLETE")


if __name__ == "__main__":
    main()
