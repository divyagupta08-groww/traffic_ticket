ticket_price = 30
print("welcome to parking ticket ")
print(f"pay this much:{ticket_price}\n")
print("accepted coins-1,2,5,10\n")
def calculator(price,paid):
    change = price-paid
    return change
coins_inserted= 0
total_inserted= 0
while True:
 coin=(int(input("insert a coin")))
 if coin != 1 and coin != 2 and coin != 5 and coin != 10 :
    print("wrong input try again")
    continue 
 total_inserted += coin
 coins_inserted += 1
 print(f"inserted_coin {coin} total so far {total_inserted}")
 if total_inserted>ticket_price:
    print("enough given")
    break
change_due = calculator(ticket_price,total_inserted)
print("giving your ticket")
if change_due==0:
   pass
else:
   print(f"here is your change:{change_due}")
print("bill")
print(f"total inserted:{total_inserted}")
print(f"coins given:{coins_inserted}")
print(f"change given,{change_due}")
print("bye")