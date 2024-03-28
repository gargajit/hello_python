def main():
    number = int(input("Number: "))
    hundreds_place, tens_place, ones_place = extract_places(number)
    print("Hundreds place:", hundreds_place)
    print("Tens place:", tens_place)
    print("Ones place:", ones_place)


def extract_places(number):
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10
    return hundreds, tens, ones


if __name__ == "__main__":
    main()
