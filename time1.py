#Gulzat Kaipova
#7/27/2023

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")  # Added a closing parenthesis
currentTimeInt = int(currentTimeStr)  # Corrected variable names to match the ones above
waitTimeInt = int(waitTimeStr)  # Corrected variable names to match the ones above
finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)  # Corrected variable name to match the one above
