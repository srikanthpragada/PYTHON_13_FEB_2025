class Course:
    # static attributes or class attributes
    taxrate = 18

    @staticmethod
    def gettaxrate():
        return Course.taxrate

    # Constructor
    def __init__(self, title, fee = 10000):
        # Object Attributes
        self.title = title
        self.fee = fee

    # Methods
    def show(self):
        print(f"Title : {self.title}")
        print(f"Fee   : {self.fee}")

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate / 100


# Create an object
c1 = Course("Python")
c1.show()
print(c1.getnetfee())
c2 = Course("Generative AI", 15000)
c2.show()

# Static method
print(Course.gettaxrate())
