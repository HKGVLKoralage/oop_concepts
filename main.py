# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)
    

# r1 = Rectangle(10, 5)

# print("Area:", r1.area())
# print("Perimeter:", r1.perimeter())

class Vehicle:
    company_name = 'national transport service'

    def __init__(self, vehicle_id, plate_number,capacity):
        self.vehicle_id = vehicle_id
        self.plate_number = plate_number
        self.capacity = capacity
        self._status = 'Available'

    def start(self):
        self._status = 'On Trip'
        print(f'Vehicale {self.plate_number} started trip')

    def stop(self):
        self._status = 'Available'
        print(f'Vehicale {self.plate_number} trip completed')

    def get_status(self):
        return self._status
    

class bus(Vehicle):
    def __init__(self, vehicle_id, plate_number, capacity,route_number):
        super().__init__(vehicle_id, plate_number, capacity)
        self.route_number = route_number

    def calcutale_fare(self, distance):
        return distance * 2.5
    #this is 

class Driver:
    def __init__(self, driver_id,name,licence_number):
        self.driver_id = driver_id
        self.name =name
        self.licence =licence_number
        self.assigned_vehicle = None
        
    def assign_vehicle(self,vehicle):
        self.assigned_vehicle =vehicle
        print(f'{self.nmae} assigned to {vehicle.plate_number}')

class Route:
    def __init__(self, route_number, start_point,end_point,distance):
        self.route_number = route_number
        self.start_point = start_point
        self.end_point = end_point
        self,distance = distance
    def route_info(self):
        return f'Route{ self.route_number}: {self.start_point} --> {self.end_point}'
    
class Maintenace:
    @staticmethod
    def perform_service(Vehicale):
        vehicle,_status = 'under Maintance'
        print(f'{vehicle.plate_number} is under maintance')

class MiniBus(bus):

    def calcutale_fare(self, distance):
        return distance * 3.0
    

route1 = Route(101,'colombo','kandy',135)

id(self)
type(self)