hello = input("Enter Your message: ")
if hello == "Hello":
    help_user = input("Please choose the office by the number:"
                      "\n1) google_kazakstan.txt"
                      "\n2) google_paris.txt"
                      "\n3) google_uar.txt"
                      "\n4) google_kyrgyzstan.txt"
                      "\n5) google_san_francisko.txt"
                      "\n6) google_germany.txt"
                      "\n7) google_moscow.txt"
                      "\n8) google_sweden.txt"
                      "\n"
                      "\nEnter the number of the office here: ")
    complain = input("Please write Your message: ")
    if help_user == "1":
        filename = "google_kazakstan.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "2":
        filename = "google_paris.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "3":
        filename = "google_uar.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "4":
        filename = "google_kyrgyzstan.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "5":
        filename = "google_san_francisco.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "6":
        filename = "google_germany.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "7":
        filename = "google_moscow.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
    elif help_user == "8":
        filename = "google_sweden.txt"
        file = open(filename, "a")
        file.writelines("\n" + "We have a new complain: " + complain)
        file.close()
else:
    print("Try again!")