# Creator Method
# The Creator class declares the factory method that returns new product objects. 
# It’s important that the return type of this method matches the product interface.


# Product Interface
from abc import ABC, abstractmethod
from turtle import mode


class TransportMode(ABC):
    """
    The Product interface declares the operations that all concrete products must implement.
    """
    @abstractmethod
    def OperationMode(self, message: str) -> str:
        pass
    @abstractmethod
    def SpeedLimit(self, speed: int ) -> str:
        pass

# Various implementation of the TransportMode interface
class TransportModeAir(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Flying in the air"
    def SpeedLimit(self, speed):
        return f"Speed limit is {speed} km/h for air transport"

class TransportModeLand(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Driving on the land"
    def SpeedLimit(self, speed):
        return f"Speed limit is {speed} km/h for land transport"

class TransportModeWater(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Sailing on the water"
    def SpeedLimit(self, speed):
        return f"Speed limit is {speed} km/h for water transport"


# Create Transportation 
class TransportationCreator(ABC):
    # THis the factory method that determines which 
    # product objects gets created. The factory method is 
    # abstract and must be implemented by the subclasses.
    @abstractmethod
    def create_transportation(self) -> TransportMode:
        pass

    def create_transportation_ctx(self) -> TransportMode:
        return self.create_transportation()

    
    def output_mode_status(self, message: str) -> None:
        print(self.create_transportation_ctx().OperationMode(message))

    def output_speed_limit(self, speed: int) -> None:
        print(self.create_transportation_ctx().SpeedLimit(speed))

class AirTransportationCreator(TransportationCreator):
    def create_transportation(self) -> TransportMode:
        return TransportModeAir()

class LandTransportationCreator(TransportationCreator):
    def create_transportation(self) -> TransportMode:
        return TransportModeLand()

class WaterTransportationCreator(TransportationCreator):
    def create_transportation(self) -> TransportMode:
        return TransportModeWater()

air_transportation_creator = AirTransportationCreator()
air_transportation_creator.output_mode_status("Hello from air")
air_transportation_creator.output_speed_limit(800)

land_transport_handler = LandTransportationCreator()
land_transport_handler.output_mode_status("Hello from land")
land_transport_handler.output_speed_limit(120)

water_transport_handler = WaterTransportationCreator()
water_transport_handler.output_mode_status("Hello from water")
water_transport_handler.output_speed_limit(60)
