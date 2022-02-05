import functions
import players


if __name__ == '__main__':
    functions.homeWindow()
    try:
        ans1=functions.ob1.x
        print(ans1)
        if (ans1 == 1):
            print("Help clicked")

        elif (ans1 == 2):
            print("ABout us clicked")
        elif (ans1==3):
            print("Single Player clicked")
        else:
            print("Double Player clicked")
    except:

        print("Thanks for visiting")
