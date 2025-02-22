
list_cars = []

while True:
    user_action = input("Add new car, show, edit, complate or exit:")
    name_car = user_action.strip()

    match name_car:
        case 'add':
            car_name = input("Enter a car: ")
            list_cars.append(car_name)
        case 'show':
            for index, item in enumerate(list_cars):
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input("Number of the car to edit: "))
            number -= 1
            new_car = input("Enter new car: ")
            list_cars[number] = new_car
        case 'complete':
            number = int(input("Number of the car to complete: "))
            list_cars.pop(number)
        case 'exit':
            break


print("Have a great day!")