class  Bike:
    def  __init__(self, model_name, acceleration):
        self.model_name = model_name
        self.acceleration = acceleration
        self.current_speed =  0
        self.color =  "black"

    def accelerate(self):
        self.current_speed += self.acceleration


def create_bike_object(model_name, acceleration):
	create=Bike(model_name, acceleration)
	return create

def get_bike_object_color(bike_object):
    return bike_object.color

def get_bike_object_current_speed(bike_object):
	return bike_object.current_speed

def change_bike_color(bike_object, new_color):
    bike_object.color=new_color
    return bike_object.color

def increase_bike_speed(bike_object):
    bike_object.current_speed += bike_object.acceleration
    return bike_object.current_speed

if  __name__  ==  '__main__':
    bike_object =  create_bike_object("Yamaha R15",10)
    print(bike_object)
    print(get_bike_object_color(bike_object))
    print(get_bike_object_current_speed(bike_object))
    print(change_bike_color(bike_object, "red"))
    print(increase_bike_speed(bike_object))
    #print(get_bike_object_current_speed(bike_object))