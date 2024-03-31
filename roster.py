#https://goheels.com/sports/mens-basketball/roster


import pandas as pd


player = {"Last Name": ["Bacot", "Davis", "Cadeau", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
          "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
          "height": [83, 72, 73, 81, 77, 75, 77, 82, 73, 76],
          "weight": [240, 180, 180, 225, 195, 195, 195, 230, 180, 190]
          }
data = pd.DataFrame(player)

data["bmi"] = ((data["weight"]/2.205)/((data["height"]/39.37)**2)).round(2)
print(data)

data.to_csv("bmi.csv")
