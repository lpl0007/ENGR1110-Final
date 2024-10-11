import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

countryList = ['Singapore', 'Bangladesh', 'India', 'Japan', 'England']
graphData = {"Year": [], "Singapore": [], "Bangladesh": [], "India": [], "Japan": [], "England": []}

#User input
print("Pick a month to use for graphing purposes (1-12): ", end = "")
month = int(input("\nMonth: "))

if (month < 1) or (month > 12):
  print("That is not an option")
  exit()

print("\nHow many countries would you like to view? (1-5): ", end = "")
countryAmount = int(input("\nNumber: "))
countriesChosen = []

if countryAmount == 1:
  print("\nChoose a country from the following list:", end = "")
  for i in countryList:
    print("\n\t" + i, end = "")
  countriesChosen.append(input("\nCountry: ").title())
  if countriesChosen[0] not in countryList:
    print('Country is not in list :(')
    exit()
elif countryAmount == 2:
  print("\nChoose a country from the following list:", end = "")
  for i in countryList:
    print("\n\t" + i, end = "")
  countriesChosen.append(input("\nCountry: ").title())
  if countriesChosen[0] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[0])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nSecond Country: ").title())
  if countriesChosen[1] not in countryList:
    print('Country is not in list :(')
    exit()
elif countryAmount == 3:
  print("\nChoose a country from the following list:", end = "")
  for i in countryList:
    print("\n\t" + i, end = "")
  countriesChosen.append(input("\nCountry: ").title())
  if countriesChosen[0] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[0])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nSecond Country: ").title())
  if countriesChosen[1] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[1])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nThird Country: ").title())
  if countriesChosen[2] not in countryList:
    print('Country is not in list :(')
    exit()
elif countryAmount == 4:
  print("\nChoose a country from the following list:", end = "")
  for i in countryList:
    print("\n\t" + i, end = "")
  countriesChosen.append(input("\nCountry: ").title())
  if countriesChosen[0] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[0])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nSecond Country: ").title())
  if countriesChosen[1] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[1])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nThird Country: ").title())
  if countriesChosen[2] not in countryList:
    print('Country is not in list :(')
    exit()
  countryList.remove(countriesChosen[2])
  print("\nChoose another country from the list:", end = "")
  countriesChosen.append(input("\nFourth Country: ").title())
  if countriesChosen[3] not in countryList:
    print('Country is not in list :(')
    exit()
elif countryAmount == 5:
  countriesChosen = countryList
else:
  print("That is not an option")
  exit()
countriesChosen = sorted(countriesChosen)

#Singapore
f = open("Singapore.csv", "r")
data = f.read()
data2 = data.split("\n")
num = 0
for i in data2:
  if num == month:
    data3 = i.split(",")
    graphData["Year"].append(str(data3[0][:4]))
    graphData["Singapore"].append(float(data3[1]))
  if num == 12:
    num = 0
  num += 1

#Bangladesh
f = open("Bangladesh.csv", "r")
data = f.read()
data2 = data.split("\n")
num = 0
missingDates = []
for i in data2:
  if num == month:
    data3 = i.split(",")
    if data3[2] not in graphData["Year"]:
      missingDates.append([data3[2], data3[0]])
    else:
      graphData["Bangladesh"].append(float(data3[0]))
  if num == 12:
    num = 0
  num += 1

#Add empty values for years after the Bangladesh data set
if (len(graphData["Singapore"]) > len(graphData["Bangladesh"])):
  for i in range(len(graphData["Singapore"]) - len(graphData["Bangladesh"])):
    graphData["Bangladesh"].append(np.nan)

#Add empty values for years before the Singapore data set
count = 0
for i in missingDates:
  graphData["Year"].insert(count, i[0])
  graphData["Singapore"].insert(count, np.nan)
  graphData["Bangladesh"].insert(count, float(i[1]))
  count += 1

#India
f = open("India.csv", "r")
data = f.read()
data2 = data.split("\n")
bool = False
for i in data2:
  if not(bool):
    bool = True
  else:
    data3 = i.split(",")
    graphData["India"].append(float(data3[1]))

#Add empty values for years after the India data set
if (len(graphData["Singapore"]) > len(graphData["India"])):
  for i in range(len(graphData["Singapore"]) - len(graphData["India"])):
    graphData["India"].append(np.nan)

#Japan
f = open("Japan.csv", "r")
data = f.read()
data2 = data.split("\n")
num = 0
missingDates = []
for i in data2:
  if num == month:
    data3 = i.split(",")
    if data3[0] not in graphData["Year"]:
      missingDates.append([data3[0], data3[2]])
    else:
      graphData["Japan"].append(float(data3[2]))
  if num == 12:
    num = 0
  num += 1

#Add empty values for years before the Singapore, Bangladesh, and India data sets
count = 0
for i in missingDates:
  graphData["Year"].insert(count, i[0])
  graphData["Singapore"].insert(count, np.nan)
  graphData["Bangladesh"].insert(count, np.nan)
  graphData["India"].insert(count, np.nan)
  graphData["Japan"].insert(count, float(data3[2]))
  count += 1

#England
f = open("England.csv", "r")
data = f.read()
data2 = data.split("\n")
num = 0
leap = 3
if month == 1:
  month = 1
elif month == 2:
  month = 32
elif month == 3:
  month = 60
elif month == 4:
  month = 91
elif month == 5:
  month = 121
elif month == 6:
  month = 152
elif month == 7:
  month = 182
elif month == 8:
  month = 213
elif month == 9:
  month = 244
elif month == 10:
  month = 274
elif month == 11:
  month = 305
elif month == 12:
  month = 334
for i in data2:
  if num == month:
    data3 = i.split(",")
    graphData["England"].append(float(data3[5]))
  if leap == 4:
    if num == 366:
      num = 0
      leap = 0
  else:
    if num == 365:
      num = 0
      leap += 1
  num += 1

#Add empty values for years before the England data set
if (len(graphData["Singapore"]) > len(graphData["England"])):
  for i in range(len(graphData["Singapore"]) - len(graphData["England"])):
    graphData["England"].insert(0, np.nan)

#Display solutions or comparisons
if countryAmount == 1:
  if countriesChosen[0] == "Singapore":
    print('Since Singapore is a developed country, it is working to swap from fuel oil to natural gas.')
  elif countriesChosen[0] == "Bangladesh":
    print('Bangladesh is not a very developed country, most of its resources have been put to builing dams and construction roadside plantations for fruit trees')
  elif countriesChosen[0] == "India":
    print('India is quite developed and has worked to protect regional glaciers and reduce single-use plastic.')
  elif countriesChosen[0] == "Japan":
    print('Japan is a very developed country and has introduced renewable energy, like solar, biomass and geothermal.')
  elif countriesChosen[0] == "England":
    print('Since England is well developed, it has launched a goal to reach a net zero for greenhouse gas emissions')
elif countryAmount == 2:
  if countriesChosen == ["Bangladesh", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; Singapore: 0.25C.')
  if countriesChosen == ["India", "Singapore"]:
    print('India: 0.7C avg. increase per decade; Singapore: 0.25C.')
  if countriesChosen == ["Japan", "Singapore"]:
    print('Japan: 0.22C avg. increase per decade; Singapore: 0.25C.')
  if countriesChosen == ["England", "Singapore"]:
    print('England: 0.8C avg. increase per decade; Singapore: 0.25C.')
  if countriesChosen == ["Bangladesh", "England"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C')
  if countriesChosen == ["Bangladesh", "India"]:
    print('Bangladesh: 0.07C avg. increase per decade; India: 0.7C')
  if countriesChosen == ["Bangladesh", "Japan"]:
    print('Bangladesh: 0.07C avg. increase per decade; Japan: 0.22C')
  if countriesChosen == ["India", "Japan"]:
    print('India: 0.7C avg. increase per decade; Japan: 0.22C')
  if countriesChosen == ["England", "India"]:
    print('England: 0.8C avg. increase per decade; India: 0.7C')
  if countriesChosen == ["England", "Japan"]:
    print('England: 0.8C avg. increase per decade; Japan: 0.22C')
elif countryAmount == 3:
  if countriesChosen == ["Bangladesh", "England", "India"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; India: 0.7C')
  elif countriesChosen == ["Bangladesh", "England", "Japan"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; Japan: 0.22C')
  elif countriesChosen == ["Bangladesh", "England", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; Singapore: 0.25C')
  elif countriesChosen == ["Bangladesh", "India", "Japan"]:
    print('Bangladesh: 0.07C avg. increase per decade; India: 0.7C; Japan: 0.22C')
  elif countriesChosen == ["Bangladesh", "India", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; India: 0.7C; Singapore: 0.25C')
  elif countriesChosen == ["Bangladesh", "Japan", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; Japan: 0.22C; Singapore: 0.25C')
  elif countriesChosen == ["England", "India", "Japan"]:
    print('England: 0.8C avg. increase per decade; India: 0.7C; Japan: 0.22C')
  elif countriesChosen == ["England", "India", "Singapore"]:
    print('England: 0.8C avg. increase per decade; India: 0.7C; Singapore: 0.25C')
  elif countriesChosen == ["England", "Japan", "Singapore"]:
    print('England: 0.8C avg. increase per decade; Japan: 0.22C; Singapore: 0.25C')
  elif countriesChosen == ["India", "Japan", "Singapore"]:
    print('India: 0.7C avg. increase per decade; Japan: 0.22C; Singapore: 0.25C')
elif countryAmount == 4:
  if countriesChosen == ["Bangladesh", "England", "India", "Japan"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; India: 0.7C; Japan: 0.22C')
  elif countriesChosen == ["Bangladesh", "England", "India", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; India: 0.7C; Singapore: 0.25C')
  elif countriesChosen == ["Bangladesh", "England", "Japan", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; England: 0.8C; Japan: 0.22C; Singapore: 0.25C')
  elif countriesChosen == ["Bangladesh", "India", "Japan", "Singapore"]:
    print('Bangladesh: 0.07C avg. increase per decade; India: 0.7C; Japan: 0.22C; Singapore: 0.25C')
  elif countriesChosen == ["England", "India", "Japan", "Singapore"]:
    print('England: 0.8C avg. increase per decade; India: 0.7C; Japan: 0.22C; Singapore: 0.25C')
else:
  print('England: 0.8C avg. increase per decade; India: 0.7C; Japan: 0.22C; Singapore: 0.25C; Bangladesh: 0.07C')

#Create and display graph
df = pd.DataFrame(graphData)
df.head()
if countryAmount == 1:
  df2 = df[["Year", countriesChosen[0]]]
  df2.plot(x = 'Year', ylabel = 'Temperature (°C)', title = countriesChosen[0])
elif countryAmount == 2:
  df2 = df[["Year", countriesChosen[0], countriesChosen[1]]]
  df2.plot(x = 'Year', ylabel = 'Temperature (°C)', title = countriesChosen[0] + " vs " + countriesChosen[1])
elif countryAmount == 3:
  df2 = df[["Year", countriesChosen[0], countriesChosen[1], countriesChosen[2]]]
  df2.plot(x = 'Year', ylabel = 'Temperature (°C)', title = countriesChosen[0] + " vs " + countriesChosen[1] + " vs " + countriesChosen[2])
elif countryAmount == 4:
  df2 = df[["Year", countriesChosen[0], countriesChosen[1], countriesChosen[2], countriesChosen[3]]]
  df2.plot(x = 'Year', ylabel = 'Temperature (°C)', title = countriesChosen[0] + " vs " + countriesChosen[1] + " vs " + countriesChosen[2] + " vs " + countriesChosen[3])
else:
  df2 = df[["Year", countriesChosen[0], countriesChosen[1], countriesChosen[2], countriesChosen[3], countriesChosen[4]]]
  df2.plot(x = 'Year', ylabel = 'Temperature (°C)', title = countriesChosen[0] + " vs " + countriesChosen[1] + " vs " + countriesChosen[2] + " vs " + countriesChosen[3] + " vs " + countriesChosen[4])
plt.show()