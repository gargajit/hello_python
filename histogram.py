def main():
    s = input("Enter a character: ")
    print(f"Enter 4 numbers to create the histogram for {s}")

    input_list = []
    for i in range(4):
        element = int(input(f"Number {i+1}: "))
        
        input_list.append(element)

    print(f"Histogram for {s} in the format {input_list}")
    
    for i in input_list:
        for j in range(i):
            print(f"{s}", end="")

        print()


if __name__ == "__main__":
    main()
        
