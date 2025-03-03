def get_car():
    with open('cars.txt', 'r') as file_local:
        cars = file_local.readlines()
    return cars

while True:
    user_action = input("Add new car, show, edit, complete or exit: ")
    name_car = user_action.strip()


    if user_action.startswith("add"):
        car_name = user_action[4:]

        cars = get_car()

        cars.append(car_name + '\n')

        with open('cars.txt', 'w') as file:
            file.writelines(cars)

    elif user_action.startswith("show"):

        cars = get_car()

        for index, item in enumerate(cars):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)


    elif user_action.startswith("edit"):
       try:

            number = int(user_action[5:])
            print(number)

            number -= 1

            cars = get_car()

            new_car = input("Enter new car: ")
            cars[number] = new_car + '\n'

            with open('cars.txt', 'w') as file:
                file.writelines(cars)

       except ValueError:
           print("Your command is not valid!")
           continue

    elif user_action.startswith("complete"):
        try:

            number = int(user_action[9:])

            cars = get_car()

            index = number - 1
            cars_remove = cars[index].strip('\n')
            cars.pop(index)

            with open('cars.txt', 'w') as file:
                file.writelines(cars)

            messages = f" This car {cars_remove} was remove from the list."
            print(messages)
        except ValueError:
            print("There is no car with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command isn't valid.")



print("Have a great day!")