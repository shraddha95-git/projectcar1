from flask import Flask, jsonify, render_template, request

from project_app.utils import CarPrice

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Welcome to Car Price Prediction System") 
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_Car_charges():
    if request.method == "GET":
        print("We are in a GET Method")

        symboling = float(request.args.get("symboling"))
        normalized_losses =float( request.args.get("normalized_losses"))
        fuel_type = (request.args.get("fuel_type"))
        aspiration = (request.args.get("aspiration"))
        num_of_doors = request.args.get("num_of_doors")
        drive_wheels = (request.args.get("drive_wheels"))
        engine_location = (request.args.get("engine_location"))
        wheel_base = float(request.args.get("wheel_base"))
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        height = float(request.args.get("height"))
        curb_weight = float(request.args.get("curb_weight"))
        num_of_cylinders = (request.args.get("num_of_cylinders"))
        engine_size = float(request.args.get("engine_size"))
        bore = float(request.args.get("bore"))
        stroke = float(request.args.get("stroke"))
        compression_ratio = float(request.args.get("compression_ratio"))
        horsepower = float(request.args.get("horsepower"))
        peak_rpm = float(request.args.get("peak_rpm"))
        city_mpg = float(request.args.get("city_mpg"))
        highway_mpg = float(request.args.get("highway_mpg"))
        engine_type = (request.args.get("engine_type"))
        body_style = (request.args.get("body_style"))
        fuel_system = (request.args.get("fuel_system"))
        make = (request.args.get("make"))

        car_charges = CarPrice(symboling, normalized_losses,fuel_type, aspiration, num_of_doors, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, num_of_cylinders, engine_size, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, engine_type, body_style , fuel_system, make)
        charges = car_charges.get_predicted_car_price() 

        return render_template("index.html", prediction = charges)

if __name__ == "__main__":
    app.run()
