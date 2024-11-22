print("")
print("")
print("                      //  ) ) //  ) )              ")
print("    ___      ___   __//__  __//__  ___      ___    ")
print("  //   ) ) //   ) ) //      //   //___) ) //___) ) ")
print(" //       //   / / //      //   //       //        ")
print("((____   ((___/ / //      //   ((____   ((____     ")
print("")
print("")
print("wona brew -h")
answer = input("Enter command: ")

if answer == "-h":
    print("coffee   - brews a coffee")
    answer = input("Enter command: ")

    if answer == "-h":
        print("not agen you fucker just read the shite above dumb ass")
        wait = input(" ")

    elif answer == "coffee":
        print("Brewing coffee... ☕")
        print("")
        print("   ( (")
        print("    ) )")
        print("  ........")
        print("  |      |]")
        print("  \\      /")
        print("   `----'")
        wait = input(" ")
    else:
        print("Invalid command. Try again.")
        wait = input(" ")
elif answer == "coffee":
    print("Brewing coffee... ☕")
    print("")
    print("   ( (")
    print("    ) )")
    print("  ........")
    print("  |      |]")
    print("  \\      /")
    print("   `----'")
    wait = input(" ")
else:
    print("Invalid command. Try again.")
    wait = input(" ")
# got a lil bit of help from chat gpt just with the == and the ""