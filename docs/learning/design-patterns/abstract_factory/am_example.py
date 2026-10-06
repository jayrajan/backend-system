# abstract method example
# family of related products

# Interface for each of the distinct products
from abc import ABC, abstractmethod


class Ship(ABC):
    @abstractmethod
    def sail(self) -> str:
        pass

class Plane(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

class Car(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

class Truck(Car):
    def drive(self) -> str:
        pass

class Ferry(Ship):
    def sail(self) -> str:
        pass

class Helicopter(Plane):
    def fly(self) -> str:
        pass

# Air Transport products
class AirTransportPlane(ABC):
    def create_plane(self) -> Plane:
        return Plane()
    def fly(self) -> str:
        return "I am a plane Flying in the air"
    
class AirTransportHelicopter(ABC):
    def create_helicopter(self) -> Plane:
        return Helicopter()
    def fly(self) -> str:
        return "I am a helicopter Flying in the air"

# Land Transport products
class LandTransportCar(ABC):
    def create_car(self) -> Car:
        return Car()
    def drive(self) -> str:
        return "I am a car Driving on the land"
    
class LandTransportTruck(ABC):
    def create_truck(self) -> Truck:
        return Truck()
    def drive(self) -> str:
        return "I am a truck Driving on the land"

# Water Transport products
class waterTransportShip(ABC):
    def create_ship(self) -> Ship:
        return Ship()
    def sail(self) -> str:
        return "I am a ship Sailing on the water"

class WaterTransportFerry(ABC):
    def create_ferry(self) -> Ship:
        return Ferry()
    def sail(self) -> str:
        return "I am a ferry Sailing on the water"

# Abstract Factory:
class TransportFactory(ABC):
    @abstractmethod
    def create_air_transport(self) -> Plane:
        pass

    @abstractmethod
    def create_land_transport(self) -> Car:
        pass

    @abstractmethod
    def create_water_transport(self) -> Ship:
        pass

# Concrete Factory - 1:
class TransportFactory1(TransportFactory):
    def create_air_transport(self) -> Plane:
        return AirTransportPlane()
    
    def create_land_transport(self) -> Car:
        return LandTransportCar()
    
    def create_water_transport(self) -> Ship:
        return waterTransportShip()

# Concrete Factory - 2:
class TransportFactory2(TransportFactory):
    def create_air_transport(self) -> Plane:
        return AirTransportHelicopter()
    
    def create_land_transport(self) -> Car:
        return LandTransportTruck()
    
    def create_water_transport(self) -> Ship:
        return WaterTransportFerry()

class Application:
    def __init__(self, factory: TransportFactory) -> None:
        self.factory = factory

    def run(self) -> None:
        air_transport = self.factory.create_air_transport()
        land_transport = self.factory.create_land_transport()
        water_transport = self.factory.create_water_transport()

        print(air_transport.fly())
        print(land_transport.drive())
        print(water_transport.sail())


factory = TransportFactory1()
app = Application(factory)
app.run()

factory2 = TransportFactory2()
app2 = Application(factory2)
app2.run()