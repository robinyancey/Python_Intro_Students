class Employee:
    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary
        
    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent) 
        
    def work(self):
        print(self.name, "does stuff") 
        
    def __str__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
class Customer:
    def __init__(self, name):
        self.name = name
        
    def order(self, server):
        print(self.name, "orders from", server) 
        
    def pay(self, server):
        print(self.name, "pays for item to", server)
    
class Oven:
    def bake(self):
        print("oven bakes")
        
class PizzaShop:
    
    def __init__(self):
        self.server = Server('Pat')  # Changed to a Server object
        self.chef = Chef('Bob')      # Changed to a Chef object
        self.oven = Oven()
    
    def order(self, name):
        customer = Customer(name) 
        customer.order(self.server) 
        self.chef.work() 
        self.oven.bake() 
        customer.pay(self.server)
        
class Server(Employee):
    """ Another employee with a set salary and work method"""
    def __init__(self, name):
        Employee.__init__(self, name, 40000) 
        
    def work(self):
        Employee.work(self)
        super().work()
        print(self.name, "interfaces with customer")

class Chef(Employee):
    """Employee with a set salary and work method"""
    def __init__(self, name):
        Employee.__init__(self, name, 50000) 
        
    def work(self):
        print(self.name, "makes food")

    def recommend(self):
        print(self.name, "recommends the margherita!")
        
if __name__ == "__main__":
    scene = PizzaShop() 
    scene.order('Homer') 
    print('...') 
    scene.order('Shaggy')