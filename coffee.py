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

    elif answer == "coffee":
        print("Brewing coffee... ☕")
        print("")
        print("   ( (")
        print("    ) )")
        print("  ........")
        print("  |      |]")
        print("  \\      /")
        print("   `----'")
    else:
        print("Invalid command. Try again.")
elif answer == "coffee":
    print("Brewing coffee... ☕")
    print("")
    print("   ( (")
    print("    ) )")
    print("  ........")
    print("  |      |]")
    print("  \\      /")
    print("   `----'")
else:
    print("Invalid command. Try again.")
# got a lil bit of help from chat gpt just with the == and the ""