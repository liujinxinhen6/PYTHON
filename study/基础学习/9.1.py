class Restaurant():
    restaurant_name = 'liujinxin'
    cuisine_type = 'fandian'
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("the restaurant is opening")
restaurant = Restaurant()
restaurant.describe_restaurant()
restaurant.cuisine_type