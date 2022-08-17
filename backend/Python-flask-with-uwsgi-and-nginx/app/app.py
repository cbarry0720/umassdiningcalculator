from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from urllib.request import urlopen, Request

def elimLetters(str):
    return re.sub(r'[a-z]+', '', str, re.I) 


locations = {}

locations.update({"Berkshire Dining Commons": "https://umassdining.com/locations-menus/berkshire/menu"})
locations.update({"Worcester Dining Commons": "https://umassdining.com/locations-menus/worcester/menu"})
locations.update({"Franklin Dining Commons": "https://umassdining.com/locations-menus/franklin/menu"})
locations.update({"Hampshire Dining Commons": "https://umassdining.com/locations-menus/hampshire/menu"})
locations.update({"Blue Wall - Harvest": "https://umassdining.com/menu/harvest-blue-wall-menu"})
locations.update({"Blue Wall - Tavola": "https://umassdining.com/menu/tavola"})
locations.update({"Blue Wall - Green Fields": "https://umassdining.com/menu/green-fields-blue-wall"})
locations.update({"Blue Wall - Tamales" : "https://umassdining.com/menu/tamales-blue-wall-menu"})
locations.update({"Blue Wall - Wasabi": "https://umassdining.com/menu/wasabi-blue-wall"})
locations.update({"Blue Wall - Deli Delish": "https://umassdining.com/menu/deli-delish-blue-wall"})
locations.update({"Blue Wall - Star Ginger": "https://umassdining.com/menu/star-ginger-blue-wall-menu"})
locations.update({"Blue Wall - The Grill": "https://umassdining.com/menu/grill-blue-wall-menu"})
locations.update({"Blue Wall - Bamboo": "https://umassdining.com/menu/bamboo-at-chefs-table-menu"})

totals = {
          "totalCal" : 0,
          "totalProt" : 0,
          "totalFat" : 0,
          "totalCarbs" : 0,
          "totalChol" : 0,
          "totalSodium": 0,
          "dailyFat" : 0, 
          "dailyCarbs" : 0,
          "dailyChol" : 0,
          "dailySodium" : 0}


# Back-End Website Set Up
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/foods", methods=["GET"])
@cross_origin()
def foodCalc():
    jsonFile = {}
    args = request.args
    if "loc" not in args:
        return "NOT FOUND"
    locs = []
    if "Berkshire Dining Commons" == args["loc"]:
        locs.append({"Berkshire Dining Commons": locations.get("Berkshire Dining Commons")})
    elif "Franklin Dining Commons" == args["loc"]:
        locs.append({"Franklin Dining Commons": locations.get("Franklin Dining Commons")})
    elif "Hampshire Dining Commons" == args["loc"]:
        locs.append({"Hampshire Dining Commons": locations.get("Hampshire Dining Commons")})
    elif "Worcester Dining Commons" == args["loc"]:
        locs.append({"Worcester Dining Commons": locations.get("Worcester Dining Commons")})
    else:
        for k in locations.keys():
            if "Blue Wall" in k:
                locs.append({k: locations.get(k)})

    for location in locs:
        location = list(location.items())[0]
        jsonFile[location[0]] = {}
        hdr = {"User-Agent": "Mozilla/5.0"}
        req = Request(location[1], headers = hdr)
        client = urlopen(req)
        html = client.read()
        client.close()
        soup = BeautifulSoup(html, "html.parser")
        
        foods = soup.findAll("li", {"class": "lightbox-nutrition"})
        for food in foods:
            if(len(food) == 0):
                continue
            #foodDict = {food.a.text: foodStuffs(food.a.text, food.a["data-calories"], food.a["data-protein"], food.a["data-total-fat"], food.a["data-total-carb"], food.a["data-cholesterol"], food.a["data-sodium"], food.a["data-protein-dv"], food.a["data-total-fat-dv"], food.a["data-total-carb-dv"], food.a["data-cholesterol_dv"], food.a["data-sodium-dv"])}
            #locations[location].foods.update(foodDict)
            
            jsonData = {food.a.text: {
                "calories": food.a["data-calories"],
                "servingSize": food.a["data-serving-size"],
                "protein": food.a["data-protein"],
                "fat": food.a["data-total-fat"],
                "carbs": food.a["data-total-carb"],
                "cholesterol": food.a["data-cholesterol"],
                "sodium": food.a["data-sodium"],
                "fat-dv": food.a["data-total-fat-dv"],
                "carbs-dv": food.a["data-total-carb-dv"],
                "cholesterol-dv": food.a["data-cholesterol_dv"],
                "sodium-dv": food.a["data-sodium-dv"]
            }}
            jsonFile[location[0]].update(jsonData)
    return jsonFile

@app.route("/results", methods = ["GET", "POST"])
def results():
    totals["totalProt"] = format(totals["totalProt"], '.2f') + "g"
    totals["totalFat"] = format(totals["totalFat"], '.2f') + "g"
    totals["totalCarbs"] = format(totals["totalCarbs"], '.2f') + "g"
    totals["totalChol"] = format(totals["totalChol"], '.2f') + "mg"
    totals["totalSodium"] = format(totals["totalSodium"], '.2f') + "mg"
    totals["dailyFat"] = str(totals["dailyFat"]) + "%"
    totals["dailyCarbs"] = str(totals["dailyCarbs"]) + "%"
    totals["dailyChol"] = str(totals["dailyChol"]) + "%"
    totals["dailySodium"] = str(totals["dailySodium"]) + "%"
    return totals

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
