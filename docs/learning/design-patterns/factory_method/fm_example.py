# Creator Method
# The Creator class declares the factory method that returns new product objects. 
# It’s important that the return type of this method matches the product interface.


# Product Interface
from abc import ABC, abstractmethod


class TransportMode(ABC):
    """
    The Product interface declares the operations that all concrete products must implement.
    """
    @abstractmethod
    def OperationMode(self, message: str) -> str:
        pass

# Various implementation of the TransportMode interface
class TransportModeAir(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Flying in the air"

class TransportModeLand(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Driving on the land"

class TransportModeWater(TransportMode):
    def OperationMode(self, message: str) -> str:
        return f"{message}, Sailing on the water"


# Create Transportation 
class TransportationCreator(ABC):
    @abstractmethod
    def create_transportation(self) -> TransportMode:
        pass

    def output_mode_status(self, message: str) -> None:
        mode = self.create_transportation()
        print(mode.OperationMode(message))

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

land_transport_handler = LandTransportationCreator()
land_transport_handler.output_mode_status("Hello from land")

water_transport_handler = WaterTransportationCreator()
water_transport_handler.output_mode_status("Hello from water")
