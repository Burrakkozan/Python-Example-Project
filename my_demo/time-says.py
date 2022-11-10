import datetime  


while (True):
  ## get the name of the country from the user
  country = input("Enter country: ")

  ## get the current time 
  current_time = datetime.datetime.now()

  ## save hours, minutes and second of the current time 
  ## in their corresponding variables 
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  ## check for case 1: the learner has typed Boston
  if country == "USA":
    hour = hour - 4 
    minute = minute - 30
  ## check for case 2: the learner has typed Tokyo
  elif country == "Japan":
    hour = hour + 9

  ## check for case 3: the learner has typed Chicago
  elif country == "china":
    hour = hour - 5 

  ## check for case 4: the learner has typed Seattle
  elif country == "Turkey":
    hour = hour - 7
    minute = minute + 30
  
  ## check for case 5: the learner has typed exit
  elif country == "exit": 
    break

  ## if all cases fail, show the time for GMT    
  else:
    print(country, "is not added")
    country = "GMT" 

  # print the name of the country and the its corresponding time
  print(country, str(hour) + ":" + str(minute) + ":" + str(second))
