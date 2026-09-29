def laptop_advisor(turn_on,internet,slow):
  if turn_on == "no":
    print("Ceck the charger and power cable")
  elif internet=="no":
    print("Check the wifi connection")
  elif slow =="yes":
    print("Restart the laptopand close the unused programs")
  else:
    print("The system does not find any problems")
turn_on=input("Does the laptop turn on?yes/no:")
internet=input("Is there any internet connection?yes/no:")
slow=input("Is the laptop slow?yes/no:")
advise=laptop_advisor(turn_on,internet,slow)
print("Export system advise")
print(advise)