
class Car():
    def __init__(self, model, year, make):
        self.model = model;
        self.year = year;
        self.make = make;
        self.odometer = 0;

    def get_descritive_name(self):
        long_name = f"{self.year} {self.make} {self.model}";
        return long_name.title();
    
    def Odometer (self):
        return f"This car has {self.odometer} miles"
    
    def Uptade_Odometer (self, uptade): #Modificando o valor do atributo
        if uptade <= self.odometer:
            print ("You can't uptade!");
        else:
            self.odometer = uptade
            return f"This car has {self.odometer} miles"

    def Incremeat_Odometer (self, miles):
        self.odometer += miles
        return f"This car has {self.odometer} miles"


my_new_car = Car("Audi", 2002, "A4")
print(my_new_car.Incremeat_Odometer(20))

class Eletric_Car(Car):
    def __init__(self, model, year, make):
        self.BatterySize = 70;
        super().__init__(model, year, make) # Herda todos os atributos da classe pai

    def describe_battery(self):
        return f"The battery has {self.BatterySize}"

carro_eletrico = Eletric_Car("Tesla", 2020, "Model S")
print(carro_eletrico.get_descritive_name())