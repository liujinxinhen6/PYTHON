class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The restaurant's type is " + self.restaurant_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening")

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,number):
        self.number_served += number
# my_restaurant=Restaurant("love of home","chuancai")
# # my_restaurant.describe_restaurant()
# # my_restaurant.restaurant_type
# # my_restaurant.set_number_served(25)
# # my_restaurant.increment_number_served(10)
# # print("The restaurant had served " + str(my_restaurant.number_served) + '.')


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,restaurant_type):
        super().__init__(restaurant_name,restaurant_type)
        self.flavors = ["caomei","juzi","lanmei"]

    def show_ice(self):
        print("the ice's flavor is " + str(self.flavors) + '.')


my_ice = IceCreamStand("love","ice")
my_ice.show_ice()