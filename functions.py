def get_car(filepath="cars.txt"):
    """"
    Read a text file and return the list of cars
    """
    with open(filepath, 'r') as file_local:
        cars = file_local.readlines()
    return cars


def write_cars(cars_argument, filepath="cars.txt"):
    """"
    Write cars name in the text file.
    """
    with open(filepath, 'w') as file_write:
        file_write.writelines(cars_argument)

if __name__ == "__main__":
    print("Hello")
    print(get_car())