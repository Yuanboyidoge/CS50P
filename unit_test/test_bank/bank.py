def main():
    greet=input("Greeting:").strip().lower()
    print(f"${value(greet)}")


def value(greeting):
    if greeting.startswith("hello"):
        res=0
    elif greeting.startswith("h"):
        res=20
    else :
        res=100
    return res


if __name__ == "__main__":
    main()