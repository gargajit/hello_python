def main():
    rad = float(input("Radius: "))
    volume = vol_of_sphere(rad)
    print(f"Volume of sphere: {volume:.2f}")

def vol_of_sphere(r):
    vol = (4/3) * (22/7) * (r ** 3)
    return vol


if __name__ == "__main__":
    main()
