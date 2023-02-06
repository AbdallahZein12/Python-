import os, time, random, sys

main_list = []
while True: 
    try:
        f = open("calendar.txt", "r")
        main_list = eval(f.read())
        f.close()
        break
    except:
        break


def colors(col):
  if col.strip().lower() == 'red':
    return "\033[31m"
  elif col.strip().lower() == 'green':
    return "\033[32m"
  elif col.strip().lower() == 'yellow':
    return "\033[33m"
  elif col.strip().lower() == 'magenta':
    return "\033[35m"
  elif col.strip().lower() == 'blue':
    return "\033[34m"
  else:
    return "\033[0m"


def letterbyletter(string):
  colors1 = ['red', 'green', 'yellow', 'magenta', 'blue']
  for i in string:
    color = random.choice(colors1)
    print(f"{colors(color)}{i}", end='')
    sys.stdout.flush()
    time.sleep(0.1)


def editor():
  time.sleep(0.2)
  print(
    f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
  )
  time.sleep(0.2)
  print("-------------------------------------------------------")
  print()
  for i in range(len(main_list)):
    if main_list[i][2] == 'HIGH':
      print(f"{colors('red')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'MEDIUM':
      print(f"{colors('yellow')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'LOW':
      print(f"{colors('green')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
  print("\033[0m")
  print()
  while True:
    try:
      item_ = input("Input item # you would like to edit>> ")
      item_1 = int(item_.strip())
      break

    except:
      print()
      print(f"{colors('red')}Error please try again!{colors('reset')}")
      print()
      continue
  while True:
    if int(item_1) in range(len(main_list)):
      print()
      name_ = input(f"Input name of item {item_1} > ")
      main_list[item_1][0] = name_
      os.system('cls')
      time.sleep(0.2)
      print(
        f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
      )
      time.sleep(0.2)
      print("-------------------------------------------------------")
      print()
      for i in range(len(main_list)):
        if main_list[i][2] == 'HIGH':
          print(f"{colors('red')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'MEDIUM':
          print(f"{colors('yellow')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'LOW':
          print(f"{colors('green')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
      print("\033[0m")
      print()
      while True:
        due_ = input("Due Date(mmddyyyy)> ")
        if len(due_) > 8 or len(due_) < 8:
          print()
          print(
            f"{colors('red')}Please follow correct format!! (mmddyyyy){colors('reset')}"
          )
          print()
          continue
        else:
          new1 = due_[:2] + "/" + due_[2:]
          new2 = new1[:5] + "/" + new1[5:]
          main_list[item_1][1] = new2
          break
      os.system('cls')
      time.sleep(0.2)
      print(
        f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
      )
      time.sleep(0.2)
      print("-------------------------------------------------------")
      print()
      for i in range(len(main_list)):
        if main_list[i][2] == 'HIGH':
          print(f"{colors('red')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'MEDIUM':
          print(f"{colors('yellow')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'LOW':
          print(f"{colors('green')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
      print("\033[0m")

      print()
      while True:
        priority = input("Priority level(Low , Medium, High)> ")
        if priority.lower().strip() != 'low' and priority.lower().strip(
        ) != 'medium' and priority.lower().strip() != 'high':
          print()
          print(f"{colors('red')}Error, Please try again!{colors('reset')}")
          print()
          continue
        else:
          real_priority = priority.strip().upper()
          main_list[item_1][2] = real_priority
          os.system('cls')
          time.sleep(0.2)
          print(
            f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
          )
          time.sleep(0.2)
          print("-------------------------------------------------------")
          print()
          for i in range(len(main_list)):
            if main_list[i][2] == 'HIGH':
              print(f"{colors('red')}", end='')
              print(
                i, "      {:<16} {:<21} {}".format(main_list[i][0],
                                                   main_list[i][1],
                                                   main_list[i][2]), "\n")
              print(f"{colors('reset')}", end="")
            elif main_list[i][2] == 'MEDIUM':
              print(f"{colors('yellow')}", end='')
              print(
                i, "      {:<16} {:<21} {}".format(main_list[i][0],
                                                   main_list[i][1],
                                                   main_list[i][2]), "\n")
              print(f"{colors('reset')}", end="")
            elif main_list[i][2] == 'LOW':
              print(f"{colors('green')}", end='')
              print(
                i, "      {:<16} {:<21} {}".format(main_list[i][0],
                                                   main_list[i][1],
                                                   main_list[i][2]), "\n")
              print(f"{colors('reset')}", end="")
          print("\033[0m")

        while True:
          more_ = input("Edit more?(y/n)> ")
          if more_.strip().lower() == 'y':
            os.system('cls')
            editor()
          elif more_.strip().lower() == 'n':
            os.system('cls')
            home()
          else:
            print()
            print(f"{colors('red')}Error, Please try again!{colors('reset')}")
            print()
            continue
    else:
      print()
      while True:
        again_1 = input(
          f"{colors('red')}Looks like this wasn't on the list! Try again?(y/n)> {colors('reset')}"
        )
        if again_1.lower().strip() == 'y':
          os.system('cls')
          editor()
        elif again_1.lower().strip() == 'n':
          os.system('cls')
          home()
        else:
          print()
          print(f"{colors('red')}Error, Please try again!{colors('reset')}")
          print()
          continue


def priority_viewer(priority):
  if priority == 'HIGH':
    time.sleep(0.2)
    print(
      f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
    )
    time.sleep(0.2)
    print("-------------------------------------------------------")
    for i in range(len(main_list)):
      if main_list[i][2] == 'HIGH':
        print(f"{colors('red')}", end='')
        print(
          i, "      {:<19} {:<18} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")
    print("\033[0m")
    input("Press enter to go back to home")
    os.system('cls')
    home()

  elif priority == 'MEDIUM':
    time.sleep(0.2)
    print(
      f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
    )
    time.sleep(0.2)
    print("-------------------------------------------------------")
    for i in range(len(main_list)):
      if main_list[i][2] == 'MEDIUM':
        print(f"{colors('yellow')}", end='')
        print(
          i, "      {:<19} {:<18} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")
    print("\033[0m")
    input("Press enter to go back to home")
    os.system('cls')
    home()

  elif priority == 'LOW':
    time.sleep(0.2)
    print(
      f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
    )
    time.sleep(0.2)
    print("-------------------------------------------------------")
    for i in range(len(main_list)):
      if main_list[i][2] == 'LOW':
        print(f"{colors('green')}", end='')
        print(
          i, "      {:<19} {:<18} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")

    print("\033[0m")
    input("Press enter to go back to home")
    os.system('cls')
    home()


def adder():

  task_name = input("Task Name> ")
  print()
  print()
  while True:
    due_date = input("Due Date(mmddyyyy)> ")
    if len(due_date) > 8 or len(due_date) < 8:
      print()
      print(
        f"{colors('red')}Please follow correct format!! (mmddyyyy){colors('reset')}"
      )
      print()
      continue
    else:
      new1 = due_date[:2] + "/" + due_date[2:]
      new2 = new1[:5] + "/" + new1[5:]
      break
  print()
  print()
  while True:
    priority = input("Priority level(Low , Medium, High)> ")
    if priority.lower().strip() != 'low' and priority.lower().strip(
    ) != 'medium' and priority.lower().strip() != 'high':
      print()
      print(f"{colors('red')}Error, Please try again!{colors('reset')}")
      print()
      continue
    else:
      real_priority = priority.strip().upper()
      row = [task_name, new2, real_priority]
      main_list.append(row)
      f = open("calendar.txt", "w")
      f.write(str(main_list))
      f.close()
      os.system('cls')
      time.sleep(0.2)
      print(
        f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
      )
      time.sleep(0.2)
      print("-------------------------------------------------------")
      print()
      for i in range(len(main_list)):
        if main_list[i][2] == 'HIGH':
          print(f"{colors('red')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'MEDIUM':
          print(f"{colors('yellow')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        elif main_list[i][2] == 'LOW':
          print(f"{colors('green')}", end='')
          print(
            i,
            "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                            main_list[i][2]), "\n")
          print(f"{colors('reset')}", end="")
        print("\033[0m")
      print()
      print(f"{colors('green')}Added successfully!{colors('reset')}")
      print()
      print()
      while True:
        more = input("Add more?(y/n)> ")
        if more.lower().strip() == 'y':
          os.system('cls')
          adder()
        elif more.lower().strip() == 'n':
          os.system('cls')
          home()
        else:
          print()
          print(f"{colors('red')}Error, Please try again!{colors('reset')}")
          print()
          continue


def remover():
  time.sleep(0.2)
  print(
    f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
  )
  time.sleep(0.2)
  print("-------------------------------------------------------")
  print()
  for i in range(len(main_list)):
    if main_list[i][2] == 'HIGH':
      print(f"{colors('red')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'MEDIUM':
      print(f"{colors('yellow')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'LOW':
      print(f"{colors('green')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
  print("\033[0m")

  which = input("Input item number you would like to remove>> ")
  if int(which) in range(len(main_list)):
    main_list.remove(main_list[int(which)])
    os.system('cls')
    time.sleep(0.2)
    print(
      f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
    )
    time.sleep(0.2)
    print("-------------------------------------------------------")
    print()
    for i in range(len(main_list)):
      if main_list[i][2] == 'HIGH':
        print(f"{colors('red')}", end='')
        print(
          i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")
        print(f"{colors('reset')}", end="")
      elif main_list[i][2] == 'MEDIUM':
        print(f"{colors('yellow')}", end='')
        print(
          i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")
        print(f"{colors('reset')}", end="")
      elif main_list[i][2] == 'LOW':
        print(f"{colors('green')}", end='')
        print(
          i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                             main_list[i][2]), "\n")
        print(f"{colors('reset')}", end="")
    print("\033[0m")
    print()
    print(f"{colors('green')}Item removed successfully!{colors('reset')}")
    print()
    print()
    while True:
      remove_again = input("Remove another(y/n)>> ")
      if remove_again.lower().strip() == 'y':
        os.system('cls')
        remover()
      elif remove_again.lower().strip() == 'n':
        os.system('cls')
        home()
      else:
        print()
        print(f"{colors('red')}Error, Please try again!!{colors('reset')}")
        print()
        continue

  else:
    print()
    print(
      f"{colors('red')}Looks like this wasn't on the list!{colors('reset')}")
    print()
    while True:
      again11 = input("Try again(y/n)>> ")
      if again11.lower().strip() == 'y':
        os.system('cls')
        remover()
      elif again11.lower().strip() == 'n':
        os.system('cls')
        home()
      else:
        print()
        print(f"{colors('red')}Error, Please try again!!{colors('reset')}")
        print()
        continue


def viewer():
  time.sleep(0.2)
  print(
    f"{colors('reset')}NUM     {colors('blue')}TASK                {colors('yellow')}DUE                {colors('magenta')}PRIORITY{colors('reset')}"
  )
  time.sleep(0.2)
  print("-------------------------------------------------------")
  print()
  for i in range(len(main_list)):
    if main_list[i][2] == 'HIGH':
      print(f"{colors('red')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'MEDIUM':
      print(f"{colors('yellow')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
    elif main_list[i][2] == 'LOW':
      print(f"{colors('green')}", end='')
      print(
        i, "      {:<16} {:<21} {}".format(main_list[i][0], main_list[i][1],
                                           main_list[i][2]), "\n")
      print(f"{colors('reset')}", end="")
  print("\033[0m")
  input("Press enter to go back to home")
  os.system('cls')
  home()


def view_options():
  print("\033[?25l", end='')
  option1 = f"{colors('blue')}1 - View all"
  option2 = f"{colors('yellow')}2 - View by Priority"
  print()
  time.sleep(0.2)
  print(f"{option1:>10}", end="")
  sys.stdout.flush()
  time.sleep(0.2)
  print(f"        {option2:>15}")
  time.sleep(0.2)
  print("\033[0m")
  while True:
    print("\033[?25h", end="")
    user_option = input("Option #> ")
    if user_option.lower().strip() == '1':
      os.system('cls')
      print("\033[?25l")
      viewer()
    elif user_option.lower().strip() == '2':
      os.system('cls')
      p_option1 = f"{colors('greem')}1 - LOW"
      p_option2 = f"{colors('yellow')}2 - MEDIUM"
      p_option3 = f"{colors('red')}3 - HIGH"
      os.system('cls')
      print("\033[?25l")
      print(f"{p_option1}", end='')
      sys.stdout.flush()
      time.sleep(0.2)
      print(f"       {p_option2}", end='')
      sys.stdout.flush()
      time.sleep(0.2)
      print(f"        {p_option3:}")
      print(f"{colors('reset')}")
      print("\033[?25h")

      while True:
        user_option2 = input("Option #> ")
        if user_option2.lower().strip() == '1':
          os.system('cls')
          print("\033[?25l")
          priority_viewer('LOW')
        elif user_option2.lower().strip() == '2':
          os.system('cls')
          print("\033[?25l")
          priority_viewer('MEDIUM')
        elif user_option2.lower().strip() == '3':
          os.system('cls')
          print("\033[?25l")
          priority_viewer('HIGH')
        else:
          print()
          print(f"{colors('red')}Error, Please try again!!{colors('reset')}")
          print()
          continue

    else:
      print()
      print(f"{colors('red')}Error, Please try again!!{colors('reset')}")
      print()
      continue


def home():
  print("\033[?25l", end='')
  letterbyletter("⭐Life Organizer!⭐")
  print()
  print()
  view = f"{colors('blue')}View"
  add = f"{colors('green')}Add"
  remove = f"{colors('red')}Remove"
  edit = f"{colors('magenta')}Edit"
  print(f"{view}")
  print(f"{add:>15}")
  print(f"{remove:>25}")
  print(f"{edit:>32}")
  print()
  print("\033[0m")
  print("\033[?25h", end="")
  while True:
    user = input(">> ")
    if user.lower().strip() == 'view':
      os.system('cls')
      view_options()
    elif user.lower().strip() == 'add':
      os.system('cls')
      adder()
    elif user.lower().strip() == 'remove':
      os.system('cls')
      remover()
    elif user.lower().strip() == 'edit':
      os.system('cls')
      editor()
    else:
      print()
      print(f"{colors('red')}Error, Please try again!{colors('reset')}")
      print()
      continue


home()
