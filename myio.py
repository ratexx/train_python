#input
#name = input("input name please")
name = "pong pong"
print("Hello " +name + " testttt")
print("Hello {}, feel Good".format(name) )


money = 10044.5678
#money =float(input("input money >"))
print("{:,.2f}".format(money))
print("{:10,.2f}".format(money))
print("{:<10,.2f}".format(money))
print("{:>10,.2f}".format(money))
print("{:>10,.2f}".format(money*100//1/100))
#multiple
n = int(input("multiple "))
for i in range(1,13):
    print("{} x {:2d} = {:>2d}".format(n,i,i*n))


