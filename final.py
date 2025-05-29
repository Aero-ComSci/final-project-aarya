

total_destinations = []
church_list = []
museum_list = []
palace_list = []
price = 0

print("you are going to a vaccation in Paris this summer: plan the tourist attractions you will visit")

church_options = ["the sacre coure","the notre damn","the sainte-chapelle","no church"]

def church_option(choice):
    if choice == "the sacre coure":
        church_list.append("the sacre coure")
        ask = input ("would you like to go up the stairs?\n")
        while ask not in ("yes", "no"):
            ask = input("would you like to go up the stairs?\n")
        if ask == "yes": 
            print("Congrats! you get to see a very nice view (make time in your scedule for a couple hours after visiting the church)")
        elif ask == "no": 
            print("ok")
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
print(",".join(church_list))
total_destinations.append(church_list)



musem_options = ["The Louvre","The Musée d'Orsay","The Centre Pompidou", "no museum"]


def museums_option(choice1):
    if choice1 == "the louvre":
        museum_list.append("The Louvre")
        return "The Louvre"
    elif choice1 == "the musee d'orsay":
        museum_list.append("The Musee d'Orsay")
        return "The Musee d'Orsay"
    elif choice1 == "the centre pompidou":
        museum_list.append("The Centre Pompidou")
        return "The Centre Pompidou"
    elif choice1 == "no church":
        museum_list.append("")
        return "no musuem"


museums_option(input("Which museum would you like to visit?: The Louvre, The Musee d'Orsay, The Centre Pompidou, or no museum\n")).lower
print(",".join(museum_list))
total_destinations.append(museum_list)
print(total_destinations)


palace_options = ["Versailles","Luxembourg Palace","no palace"]


def palace_option(choice2):
    global price
    if choice2 == "versailles":
        palace_list.append("Versailles")
        ticketprice = input("how many tickets would you like? it costs 26€\n")
        price = float(ticketprice)*float(26)
        print("$" + str(price) + " " + "is your price")
    elif choice2 == "luxembourg palace":
        palace_list.append("Luxembourg Palace")
        ticketprice = input("how many tickets would you like? it costs 14€\n")
        price = float(ticketprice)*float(14)
        print("$" + str(price) + " "+ "is your price")
    elif choice2 == "no palace":
        palace_list.append("no palace")
        return "no palace"


palace_option(input("Which palace would you like to visit?: Versailles, Luxembourg Palace, or no palace\n"))
total_destinations.append(palace_list)
print("you are going to visit" + " "+ str(total_destinations) + " " + "this SUMMER")











