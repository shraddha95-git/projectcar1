
import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class CarPrice():
    def __init__(self, symboling, normalized_losses,fuel_type, aspiration, num_of_doors, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, num_of_cylinders, engine_size, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, engine_type, body_style , fuel_system, make):
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.engine_type = "engine-type_" + engine_type
        self.body_style = "body-style_" + body_style
        self.fuel_system = "fuel-system_" + fuel_system
        self.make = "make_" + make

    def load_models(self):
        with open (config.MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)
        
        with open (config.JSON_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_car_price(self):

        self.load_models()

        engine_type_index = list(self.json_data['columns']).index(self.engine_type)
        body_style_index = list(self.json_data['columns']).index(self.body_style)
        fuel_system_index = list(self.json_data['columns']).index(self.fuel_system)
        make_index = list(self.json_data['columns']).index(self.make)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.symboling 
        test_array[1] = self.normalized_losses
        test_array[2] = self.json_data['fuel_type'][self.fuel_type]
        test_array[3] = self.json_data['aspiration'][self.aspiration]
        test_array[4] = self.json_data['num_of_doors'][self.num_of_doors]
        test_array[5] = self.json_data['drive_wheels'][self.drive_wheels]
        test_array[6] = self.json_data['engine_location'][self.engine_location]
        test_array[7] = self.wheel_base
        test_array[8] = self.length
        test_array[9] = self.width
        test_array[10] = self.height
        test_array[11] = self.curb_weight
        test_array[12] = self.json_data['num_of_cylinders'][self.num_of_cylinders]
        test_array[13] = self.engine_size
        test_array[14] = self.bore
        test_array[15] = self.stroke
        test_array[16] = self.compression_ratio
        test_array[17] = self.horsepower
        test_array[18] = self.peak_rpm
        test_array[19] = self.city_mpg
        test_array[20] = self.highway_mpg
        
        test_array[body_style_index] = 1
        test_array[engine_type_index] = 1
        test_array[fuel_system_index] = 1
        test_array[make_index] = 1
        test_array
        print("Test Array: ", test_array)

        charges = round(self.model.predict([test_array])[0],2)

        return charges

if __name__ == "__main__":
    symboling = 3.00
    normalized_losses = 118.00
    fuel_type = "gas"
    aspiration = "turbo"
    num_of_doors = "four"
    drive_wheels = "4wd"
    engine_location = "rear"
    wheel_base = 88.60
    length = 170.80
    width = 64.10
    height = 50.80
    curb_weight = 2600.00
    num_of_cylinders = "five"
    engine_size = 130.00
    bore = 3.47
    stroke = 2.68
    compression_ratio = 9.00
    horsepower = 111.00
    peak_rpm = 6000.00
    city_mpg = 21.00
    highway_mpg = 27.00
    # onehot encoded columns
    engine_type = "ohc"
    body_style = "sedan"
    fuel_system = "mpfi"
    make = "audi" 

    car_charges = CarPrice(symboling, normalized_losses,fuel_type, aspiration, num_of_doors, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, num_of_cylinders, engine_size, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, engine_type, body_style , fuel_system, make)
    charges = car_charges.get_predicted_car_price() 
    print("Predicted Car Prize is:", charges, "/- Rs.")