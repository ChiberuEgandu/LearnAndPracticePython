#Example: we wanna our customers to make a choice on our menu on our website.

def choose_menu():
    print("L -- Login\n"
          "R -- Register\n")

    choice = input("Pick your Choice:")
    return choice


def main():
    option = choose_menu()
    print("Your Choice is:", option)
main()
