def add_time(start, duration, day=None):
  hour = 0
  min = 0
  
  week_days = {"Monday":1,
   "Tuesday":2,
   "Wednesday":3,
   "Thursday":4,
   "Friday":5,
   "Saturday":6,
   "Sunday":7}
  
  num_of_days = 0

  start_time_split = start.split(' ')
  time_of_day = start_time_split[1]
  start_hour_and_min = start_time_split[0].split(":")
  start_hour = int(start_hour_and_min[0])
  start_min = int(start_hour_and_min[1])

  duration_split = duration.split(":")
  duration_hour = int(duration_split[0])
  duration_min = int(duration_split[1])
  
  hour_already_set = False
  
  if day!=None:
      day = day.title()
      curr_day_value = week_days[day]

  if (start_min + duration_min) > 60:
    result = (start_min + duration_min) - 60
    hour += 1
    min = result
  else:
    min = (start_min + duration_min)
    
   
  if (start_hour + duration_hour + hour) == 12:
    if time_of_day == "AM":
      time_of_day = "PM"
    else:
      time_of_day = "AM"
      num_of_days += 1
      if day != None:
          curr_day_value += 1
          if curr_day_value > 7:
              curr_day_value - 7
              
            
  if (start_hour + duration_hour + hour) > 12:
    hour_already_set = True
    hour += (start_hour + duration_hour)
    while hour > 12:
      hour -= 12
      if time_of_day == "AM":
        time_of_day = "PM"
      else:
        time_of_day = "AM"
        num_of_days += 1
        if day != None:
          curr_day_value += 1
          if curr_day_value > 7:
              curr_day_value - 7
    
  if hour == 12:
      if time_of_day == "AM":
          time_of_day = "PM"
      else:
          time_of_day = "AM"
          num_of_days += 1
          if day != None:
            curr_day_value += 1
            if curr_day_value > 7:
                curr_day_value - 7
  
  if not hour_already_set:
    hour += (start_hour + duration_hour)

  min = str(min)
  if len(min) < 2:
    min = f"0{min}"



  if day != None:   
    for key, value in week_days.items():
        if value == curr_day_value:
            day = key
            
    new_time = f"{hour}:{min} {time_of_day}, {day}"
  else:
    new_time = f"{hour}:{min} {time_of_day}"
    
  if num_of_days == 1:
      new_time += " (Next Day)"
  if num_of_days > 1:
      new_time += f" ({num_of_days} days later)"

  return new_time
