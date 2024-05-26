size=input("what size pizza do u want S/M/L?")
add_pepperoni=input("DO u want pepperoni (Y/N)?")
add_cheese=input("Do you want cheese (Y/N)?")
bill=0
if size=='S'  or size=='s':
    bill+=100
    print("small pizza price is Rs.100.")
elif size=='M'  or size=='m':
    bill+=200
    print("medium  pizza price is Rs.200.")
else:
    bill+=300
    print("large pizza price is Rs.300.")


if add_pepperoni== 'Y'  or add_pepperoni=='y':
    if size=='S'  or size=='s':
        bill+=30
    else:
        bill+=50

if add_cheese =='Y'or add_cheese=='y':
    bill+=20
else:
    bill+=40    
print(f"Your bill is Rs.{bill}")

 