def arithmetic_arranger(problems, display_answers=False):
  list_of_top_nums = []
  list_of_operators = []
  list_of_bottom_nums = []
  list_of_dashes = []

  if len(problems) > 5:
    return "Error: Too many problems."


  if display_answers:
    list_of_answers = []
    for i in problems:
      plus_index = i.find("+")
      minus_index = i.find("-")
      if plus_index != -1:
        split_values = i.split("+")
        operator = "+"
        list_of_operators.append("+")
      elif minus_index != -1:
        split_values = i.split("-")
        operator = "-"
        list_of_operators.append("-")
      else:
        return "Error: Operator must be '+' or '-'."
  
      left_value = split_values[0].rstrip()
      right_value = split_values[1].lstrip()
      

      try:
        left_value = int(left_value)
        right_value = int(right_value)
      except Exception as e:
        return f"Error: Numbers must only contain digits. \n\n{e}"
    
      
      if len(str(left_value)) > 4 or len(str(right_value)) > 4:
        return "Error: Numbers cannot be more than four digits."
      
      if len(str(left_value)) > len(str(right_value)):
        top_value = f"  {left_value}"
        length_of_spaces = (len(top_value) - len(str(right_value))) - 1
        bottom_value = " "*length_of_spaces + f"{right_value}"
        dashes = "-"*len(top_value)
        list_of_dashes.append(dashes)
  
      if len(str(right_value)) > len(str(left_value)):
        bottom_value = f" {right_value}"
        length_of_spaces = (len(bottom_value) - len(str(left_value))) + 1
        top_value = " "*length_of_spaces + f"{left_value}"
        dashes = "-"*(len(bottom_value) + 1)
        list_of_dashes.append(dashes)
  
      if len(str(right_value)) == len(str(left_value)):
        top_value = f"  {left_value}"
        bottom_value = f" {right_value}"
        dashes = "-"*len(top_value)
        list_of_dashes.append(dashes)

      
      if operator == "+":
        answer = left_value + right_value
      else:
        answer = left_value - right_value
        

      ans_list = [" "] * len(dashes)

      answer_index = -1
      answer = str(answer)
      for i in range(len(answer)-1,-1,-1):
        ans_list[answer_index] = answer[i]
        answer_index -= 1 
        
      answer = "".join(ans_list)
        
      
      list_of_top_nums.append(top_value)
      list_of_bottom_nums.append(bottom_value)
      list_of_answers.append(answer)
      
    arranged_problems = """"""
    for i in list_of_top_nums:
      arranged_problems = arranged_problems + str(i) + "    "

    arranged_problems += "\n"

    count = 0
    for i in list_of_operators:
      arranged_problems  += i
      arranged_problems += str(list_of_bottom_nums[count])
      arranged_problems += "    "
      count += 1

    arranged_problems += "\n"

    for i in list_of_dashes:
      arranged_problems = arranged_problems + str(i) + "    "

    arranged_problems += "\n"

    for i in list_of_answers:
      arranged_problems += str(i)
      arranged_problems += "    "
  else:
    for i in problems:
      plus_index = i.find("+")
      minus_index = i.find("-")
      if plus_index != -1:
        split_values = i.split("+")
        list_of_operators.append("+")
      elif minus_index != -1:
        split_values = i.split("-")
        list_of_operators.append("-")
      else:
        return "Error: Operator must be '+' or '-'."
  
      left_value = split_values[0].rstrip()
      right_value = split_values[1].lstrip()
      
      if len(left_value) > 4 or len(right_value) > 4:
        return "Error: Numbers cannot be more than four digits."

      try:
        left_value = int(left_value)
        right_value = int(right_value)
      except Exception as e:
        return f"Error: Numbers must only contain digits. \n\n{e}"
      
      left_value = str(left_value)
      right_value = str(right_value)
      
      if len(left_value) > len(right_value):
        top_value = f"  {left_value}"
        length_of_spaces = (len(top_value) - len(right_value)) - 1
        bottom_value = " "*length_of_spaces + f"{right_value}"
        dashes = "-"*len(top_value)
        list_of_dashes.append(dashes)
  
      if len(right_value) > len(left_value):
        bottom_value = f" {right_value}"
        length_of_spaces = (len(bottom_value) - len(left_value)) + 1
        top_value = " "*length_of_spaces + f"{left_value}"
        dashes = "-"*(len(bottom_value) + 1)
        list_of_dashes.append(dashes)
  
      if len(right_value) == len(left_value):
        top_value = f"  {left_value}"
        bottom_value = f" {right_value}"
        dashes = "-"*len(top_value)
        list_of_dashes.append(dashes)
      
      list_of_top_nums.append(top_value)
      list_of_bottom_nums.append(bottom_value)

    
    arranged_problems = """"""
    for i in list_of_top_nums:
      arranged_problems = arranged_problems + str(i) + "    "

    arranged_problems += "\n"

    count = 0
    for i in list_of_operators:
      arranged_problems  += i
      arranged_problems += str(list_of_bottom_nums[count])
      arranged_problems += "    "
      count += 1

    arranged_problems += "\n"

    for i in list_of_dashes:
      arranged_problems = arranged_problems + str(i) + "    "

    arranged_problems += "\n"
    

  return arranged_problems
