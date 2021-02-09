from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests
from urllib.request import urlopen, Request
import re

def elimLetters(str):
    return re.sub(r'[a-z]+', '', str, re.I) 

#Location object will store 
class Location:
    def __init__(self, link, foods):
        self.link = link
        self.foods = foods

class foodStuffs:
#Constructor
    def __init__(self, foodName, cal, protein, fats, carbs, chol, sodium, dailyFats, 
                 dailyCarbs, dailyChol, dailySodium):
        self.foodName = foodName
        self.cal = cal

        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.chol = chol
        self.sodium = sodium
        self.dailyFats = dailyFats
        self.dailyCarbs = dailyCarbs
        self.dailyChol = dailyChol 
        self.dailySodium = dailySodium

#Getters
    def get_foodName(self):
        return self.foodName
    def get_cal(self):
        return self.cal
    def get_protein(self):
        return self.protein
    def get_fats(self):
        return self.fats
    def get_carbs(self):
        return self.carbs
    def get_chol(self):
        return self.chol
    def get_sodium(self):
        return self.sodium
    def get_dailyFats(self):
        return self.dailyFats
    def get_dailyCarbs(self):
        return self.dailyCarbs
    def get_dailyChol(self):
        return self.dailyChol
    def get_dailySodium(self):
        return self.dailySodium

#Setters
    def set_foodName(self, newfoodName):
        self.foodName = newfoodName
    def set_cal(self, newCal):
        self.cal = newCal
    def set_protein(self, newProtein):
        self.protein = newProtein
    def set_fats(self, newFats):
        self.fats = newFats
    def set_carbs(self, newCarbs):
        self.carbs = newCarbs
    def set_chol(self, newChol):
        self.chol = newChol
    def set_sodium(self, newSodium):
        self.sodium = newSodium
    def set_dailyFats(self, newDailyFats):
        self.dailyFats =  newDailyFats
    def set_dailyCarbs(self, newDailyCarbs):
        self.dailyCarbs = newDailyCarbs
    def set_dailyChol(self, newDailyChol):
        self.dailyChol = newDailyChol
    def set_dailySodium(self, newDailySodium):
        self.dailySodium = newDailySodium

locations = {}

locations.update({"Berkshire Dining Commons": Location("https://umassdining.com/locations-menus/berkshire/menu", {})})
locations.update({"Worcester Dining Commons": Location("https://umassdining.com/locations-menus/worcester/menu", {})})
locations.update({"Franklin Dining Commons": Location("https://umassdining.com/locations-menus/franklin/menu", {})})
locations.update({"Hampshire Dining Commons": Location("https://umassdining.com/locations-menus/hampshire/menu", {})})
locations.update({"Blue Wall - Harvest": Location("https://umassdining.com/menu/harvest-blue-wall-menu", {})})
locations.update({"Blue Wall - Tavola": Location("https://umassdining.com/menu/tavola", {})})
locations.update({"Blue Wall - Green Fields": Location("https://umassdining.com/menu/green-fields-blue-wall", {})})
locations.update({"Blue Wall- Tamales" : Location("https://umassdining.com/menu/tamales-blue-wall-menu", {})})
locations.update({"Blue Wall - Wasabi": Location("https://umassdining.com/menu/wasabi-blue-wall", {})})
locations.update({"Blue Wall - Deli Delish": Location("https://umassdining.com/menu/deli-delish-blue-wall", {})})
locations.update({"Blue Wall - Star Ginger": Location("https://umassdining.com/menu/star-ginger-blue-wall-menu", {})})
locations.update({"Blue Wall - The Grill": Location("https://umassdining.com/menu/grill-blue-wall-menu", {})})
locations.update({"Blue Wall - Bamboo": Location("https://umassdining.com/menu/bamboo-at-chefs-table-menu", {})})

allFoods = {}
jsonFile = {}
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
for location in locations:
    jsonFile[location] = {"foods": []}
    url = locations[location].link
    hdr = {"User-Agent": "Mozilla/5.0"}
    req = Request(url, headers = hdr)
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
        #jsonFile[location]["foods"].append(jsonData)
        allFoods.update(jsonData)

# Back-End Website Set Up
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def foodCalc():
    if request.method == "POST":
        result = request.form['food']
        totals["totalCal"] += int(allFoods[result]['calories'])
        totals["totalProt"] += float(elimLetters(allFoods[result]['protein']))
        totals["totalFat"] += float(elimLetters(allFoods[result]['fat']))
        totals["totalCarbs"] += float(elimLetters(allFoods[result]['carbs']))
        totals["totalChol"] += float(elimLetters(allFoods[result]['cholesterol']))
        totals["totalSodium"] += float(elimLetters(allFoods[result]['sodium']))
        totals["dailyFat"] += int(allFoods[result]['fat-dv'])
        totals["dailyCarbs"] += int(allFoods[result]['carbs-dv'])
        totals["dailyChol"] += int(allFoods[result]['cholesterol-dv'])
        totals["dailySodium"] += int(allFoods[result]['sodium-dv'])
    sortedFoods = sorted(allFoods)
    return render_template("index.html", allFoods = sortedFoods)

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
    return render_template("results.html", totals=totals)

if __name__ == "__main__":
    app.run()