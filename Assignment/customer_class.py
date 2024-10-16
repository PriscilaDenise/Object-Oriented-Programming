class Customer:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer information: \nName: {self.name}\nAddress: {self.address}"
    
if __name__ == "__main__":
    #creating object
    customer1 = Customer("Denise Priscila", "Jinja")

    #printing the info
    print (customer1)