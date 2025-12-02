class Car:
    def __init__(self, make, model, year=2020, price=0.0, owner=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.owner = owner
        self.features = []
        self.running = False

    def start(self):
        """Start the car."""
        self.running = True

    def stop(self):
        """Stop the car."""
        self.running = False

    def add_feature(self, feature):
        """Add a new feature if not already present."""
        if feature not in self.features:
            self.features.append(feature)

    def set_owner(self, owner_name):
        """Assign an owner to the car."""
        self.owner = owner_name

    def clear_owner(self):
        """Remove owner information."""
        self.owner = None

    def increase_price(self, amount):
        """Increase price by a given amount."""
        self.price += amount

    def get_price_with_tax(self, tax_rate):
        """Return total price including tax."""
        return self.price * (1 + tax_rate)
