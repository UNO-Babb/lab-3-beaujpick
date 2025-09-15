#TempConvert.py
#Name: Beau Pick
#Date:9-14-25
#Assignment:Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter a Fahrenheiht temp: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((5/9) * (tempF - 32),1)
  #Output converted temperature.


  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
