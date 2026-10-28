# class: Phone
# attributes: brand, model, price, color
# methods: show_info: "men telefonman"


class Phone:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.prce = price
        self.color = color

    def show_info(self):
        print("Men telefonman")


pph1 = Phone("Apple", "Iphone 15", 20_000, "blue")
