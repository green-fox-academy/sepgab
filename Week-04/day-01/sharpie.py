# Create Sharpie class
# We should know about each sharpie their color (which should be a string), width (which will be a floating point number), ink_amount (another floating point number)
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects
# which decreases inkAmount

class Sharpie:
    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = float(100)

    def use(self, num):
        self.ink_amount -= num
        return self.ink_amount

pen1 = Sharpie('blue', 0.5)
pen1.use(10)
print(pen1.color, pen1.width, pen1.ink_amount)
