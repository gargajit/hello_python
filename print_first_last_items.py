def main():
    color_list = ["Red","Green","White" ,"Black"]
    total_items = len(color_list)
    for i in range(total_items):
        if i == 0 or i == total_items - 1:
            print(color_list[i])

if __name__ == "__main__":
    main()
