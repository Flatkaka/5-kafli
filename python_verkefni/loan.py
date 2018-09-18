lan = float(input("Input the cost of the item in $: "))
if lan < 1000:
    vex = 1.5
else:
    vex = 2.0
n= 0
pay = 50.0
total = 0.0
while lan > 0.0:
    if lan < 0.00000001:
        break
    n += 1
    interest = lan * (vex / 100)
    if pay > (interest + lan):
        pay = (interest + lan)
    lan = lan - pay + interest
    print("Month:", n, "Payment:", round(pay, 2), "Interest paid:", round(interest, 2), "Remaining debt:", round(lan, 2))
    total += interest
print()
print("Number of months:" , n)
print("Total interest paid:" , round(total, 2))