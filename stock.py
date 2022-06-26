from tabulate import tabulate
import random
import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost", user="root",
                       password="Home@253144", database="stock")
cursor = mycon.cursor()
x = ("select * from stock")
cursor.execute(x)
z = cursor.fetchall()
headers = ["Sno", "Comp_Name", "Price_per_Stock", "Price_invested",
           "Stocks_owned", "Comp_status", "Gain_or_Loss", "Final_price"]

table = (tabulate(z, headers=headers, tablefmt="pretty"))
mycon.commit()

'''def table():
    cursor.execute('select * from stock;')
    data=cursor.fetchall()
    for row in data:
        print(row)'''
comp = {1: 10000, 2: 250000, 3: 2000, 4: 16000, 5: 130000}
list = ["P", "L"]
dmat = 0


def original():
    for i in range(1, 6):
        k = "update stock set price_per_stock=%s where srno=%s" % (comp[i], i)
        cursor.execute(k)
        mycon.commit()
        m = "update stock set stocks_owned=%s where srno=%s" % (0, i)
        m1 = "update stock set comp_status=NULL where srno=%s" % (i)
        m2 = "update stock set gain_or_loss=%s where srno=%s" % (0, i)
        m3 = "update stock set price_invested=%s where srno=%s" % (0, i)
        m4 = "update stock set final_price=%s where srno=%s" % (0, i)
        cursor.execute(m)
        cursor.execute(m1)
        cursor.execute(m2)
        cursor.execute(m3)
        cursor.execute(m4)
        mycon.commit()
        return 0


def bal():
    print("Available balance is", dmat)
    return 0


print("welcome.....")
name = input("enter your name:")
b = 0
while b == 0:
    print("hello", name, "what do you want to do??")
    print("1.Check balance(DMAT ACC)")
    print("2.Withdraw to DMAT ACC")
    print("3.Deposit from DMAT ACC")
    choice = int(input("enter here:"))
    if choice == 1:
        if dmat == 0:
            print("oops,seems like your dmat account is empty")
            ans = int(
                input("would you like to withdraw some amount(1.yes/2.no):"))
            if ans == 1:
                amu = int(input("how much amount would  you like to withdraw:"))
                dmat += amu
                b = +1
            elif ans == 2:
                print('nevermind,have a nice day')
                print("bye")
                break
    elif choice == 2:
        mon = int(
            input("how much money would you like to withdraw(min(Rs10,00,000)):"))
        dmat += mon
        print("TRANSACTION SUCCESSFUL !!!")
        b += 1

    elif choice == 3:
        if dmat == 0:
            print("you can't deposit you balance is empty")
        else:
            dep = int(
                input("how much money do you want to deposit Current balance:", dmat, ":"))
            dmat = dmat-dep
            b += 1
original()
x = 0
while x == 0:
    print("What do you want to do next?")
    print("1.Buy shares")
    print("2.Sell shares(You can't sell if you didn't buy the shares)")
    print("3.EXIT")
    choice1 = int(input("enter your choice:"))
    if choice1 == 1:
        t = 0
        while t == 0:
            print(table)
            print("1. Apple  2. Amazon  3. JIO  4. Microsoft  5. Google")
            w = int(input("Which company do you want to invest in:"))
            pur = int(input("How many stocks do you want to buy:"))
            w1 = "update stock set stocks_owned=%s where srno=%s" % (pur, w)
            cursor.execute(w1)
            mycon.commit()
            c = comp[w]*pur
            dmat -= c
            c1 = "update stock set price_invested=%s where srno=%s" % (c, w)
            cursor.execute(c1)
            mycon.commit()
            for a in range(1, 6):
                index = random.choice([0, 1])
                per = round(random.random(), 3)
                if index == 0:
                    z = comp[a]+((per/100)*comp[a])
                    z1 = "update stock set price_per_stock=%s where srno=%s" % (
                        z, a)
                    cursor.execute(z1)
                    mycon.commit()
                    g = (z-comp[a])*pur
                    g1 = "update stock set gain_or_loss=%s where srno=%s" % (
                        g, a)
                    fp = z*pur
                    fp1 = "update stock set final_price=%s where srno=%s" % (
                        fp, a)
                    f = "("+"+"+str(per)+"%"+")"
                    f1 = "update stock set comp_status='%s' where srno=%s" % (
                        list[index]+f, a)
                    cursor.execute(f1)
                    mycon.commit()
                else:
                    z2 = comp[a]-((per/100)*comp[a])
                    z3 = "update stock set price_per_stock=%s where srno=%s" % (
                        z2, a)
                    cursor.execute(z3)
                    mycon.commit()
                    l = (comp[a]-z2)*pur
                    l1 = "update stock set gain_or_loss=%s where srno=%s" % (
                        l, a)
                    cursor.execute(l1)
                    mycon.commit()
                    fp2 = z2*pur
                    fp3 = "update stock set final_price=%s where srno=%s" % (
                        fp2, a)
                    cursor.execute(fp3)
                    mycon.commit()
                    f2 = "("+"-"+str(per)+"%"+")"
                    f3 = "update stock set comp_status='%s' where srno=%s" % (
                        list[index]+f2, a)
                    cursor.execute(f3)
                    mycon.commit()
            print(table)
            v = int(input("DO YOU WANT TO BUY MORE SHARES(1.YES/2.NO):"))
            if v == 1:
                print("OK,YOU CAN PROCEED")
            else:
                t += 1

    elif choice1 == 2:
        r = 0
        while r == 0:
            print = (table)
            print("1.Apple  2.Amazon  3.JIO  4.MICROSOFT  5.Google")
            iu = int(input("which company's share do you want to sell?:"))
            it = int(input("How many:"))
            ca = "select stocks_owned from stock where srno=%s" % (iu)
            cursor.execute(ca)
            da = cursor.fetchone()
            in1 = "update stock set stocks_owned=%s where srno=%s" % (
                da[0]-it, iu)
            cursor.execute(in1)
            mycon.commit()
            fa = "select price_per_stock from stock where srno=%s" % (iu)
            cursor.execute(fa)
            fe = cursor.fetchone()
            fe1 = fe[0]*it
            dmat += fe1
            ta = "select price_invested from stock where srno=%s" % (iu)
            cursor.execute(ta)
            ta1 = cursor.fetchone()
            if fe[0] > comp[iu]:
                xa = fe1-(comp[iu]*it)
                print("Hurraaaaahhh,You gained rupees", xa, ".")

            else:
                xe = (comp[iu]*it)-fe1
                print("Alaas,you lost rupeess", xe, ".")
            dr = fe[0] * (da[0] - it)
            dr1 = "update stock set final_price=%s where srno=%s" % (dr, iu)
            cursor.execute(dr1)
            mycon.commit()
            for a in range(1, 6):
                index = random.choice([0, 1])
                per = round(random.random(), 3)
                if a == iu:
                    if index == 0:
                        z = comp[a] + ((per / 100) * comp[a])
                        z1 = "update stock set price_per_stock=%s where srno=%s" % (
                            z, a)
                        cursor.execute(z1)
                        mycon.commit()
                        g = (z - comp[a]) * it
                        g1 = "update stock set gain_or_loss=%s where srno=%s" % (
                            g, a)
                        f = "(" + "+" + str(per) + "%" + ")"
                        f1 = "update stock set comp_status='%s' where srno=%s" % (
                            list[index] + f, a)
                        cursor.execute(f1)
                        mycon.commit()
                    else:
                        z2 = comp[a] - ((per / 100) * comp[a])
                        z3 = "update stock set price_per_stock=%s where srno=%s" % (
                            z2, a)
                        cursor.execute(z3)
                        mycon.commit()
                        l = (comp[a] - z2) * it
                        l1 = "update stock set gain_or_loss=%s where srno=%s" % (
                            l, a)
                        cursor.execute(l1)
                        mycon.commit()
                        f2 = "(" + "-" + str(per) + "%" + ")"
                        f3 = "update stock set comp_status='%s' where srno=%s" % (
                            list[index] + f2, a)
                        cursor.execute(f3)
                        mycon.commit()
                else:
                    if index == 0:
                        z = comp[a] + ((per / 100) * comp[a])
                        z1 = "update stock set price_per_stock=%s where srno=%s" % (
                            z, a)
                        cursor.execute(z1)
                        mycon.commit()
                        g = (z - comp[a]) * it
                        g1 = "update stock set gain_or_loss=%s where srno=%s" % (
                            g, a)
                        f = "(" + "+" + str(per) + "%" + ")"
                        f1 = "update stock set comp_status='%s' where srno=%s" % (
                            list[index] + f, a)
                        cursor.execute(f1)
                        mycon.commit()
                        fp = z * pur
                        fp1 = "update stock set final_price=%s where srno=%s" % (
                            fp, a)
                        cursor.execute(fp1)
                        mycon.commit()
                    else:
                        z2 = comp[a] - ((per / 100) * comp[a])
                        z3 = "update stock set price_per_stock=%s where srno=%s" % (
                            z2, a)
                        cursor.execute(z3)
                        mycon.commit()
                        l = (comp[a] - z2) * pur
                        l1 = "update stock set gain_or_loss=%s where srno=%s" % (
                            l, a)
                        cursor.execute(l1)
                        mycon.commit()
                        fp2 = z2 * pur
                        fp3 = "update stock set final_price=%s where srno=%s" % (
                            fp2, a)
                        cursor.execute(fp3)
                        mycon.commit()
                        f2 = "(" + "-" + str(per) + "%" + ")"
                        f3 = "update stock set comp_status='%s' where srno=%s" % (
                            list[index] + f2, a)
                        cursor.execute(f3)
                        mycon.commit()

            print(table)
            choice2 = int(
                input("Do you want to sell more shares ??(1.YES/2.NO): "))
            if choice2 == 1:
                print("OK,GO AHEAD")
            else:
                r += 1
    elif choice1 == 3:
        print("GOOD BYE,Have a nice richful day")
        break
original()
