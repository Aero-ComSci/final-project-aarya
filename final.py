

total_destinations = []
church_list = []


print("you are going to a vaccation in Paris this summer: plan the tourist attractions you will visit")

church_options = ["the sacre coure","the notre damn","the sainte-chapelle","no church"]

def church_option(choice):
    if choice == "the sacre coure":
        church_list.append("the sacre coure")
        return "the sacre coure"
    elif choice == "the notre damn":
        church_list.append("the notre damn")
        #print(church_list)
        return "the notre damn"
    elif choice == "the sainte-chapelle":
        church_list.append("the sainte-chapelle")
        return "the sainte-chapelle"
    elif choice == "no church":
        church_list.append("")
        return "no church "
    else:
        return None


church_option(input("which church would you like to visit?: the sacre coure, the notre damn, the sainte-chapelle, or no church\n"))
if church_option not in church_options:
    church_option(input("which church would you like to visit?: the sacre coure, the notre damn, the sainte-chapelle, or no church\n"))
else: 
    print(",".join(church_list))
    total_destinations.append(church_list)




