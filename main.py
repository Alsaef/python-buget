while True:
    try:
        bg = float(input("Enter your budget: "))
        s = bg
    except ValueError:
        print("Ammount The Number")
        continue
    else:
        break

a = {"name": [], 'quantity': [], 'price': []}
b = list(a.values())

na = b[0]
qu = b[1]
pr = b[2]

while True:
    try:
        ch = int(input("1. ADD\n2. EXIT\nEnter your choice: "))
    except ValueError:
        print("\nERROR: chose only digit from given option")
        continue
    else:
        if ch == 1 and s > 0:
            pn = input('enter product name: ')
            q = input('enter quantity: ')
            p = float(input('enter price of the product: '))

            if p > s:

                print("\nNeed Much Money")

            else:
                if pn in na:
                    ind = na.index(pn)

                    qu.remove(qu[ind])

                    pr.remove(pr[ind])

                    qu.insert(ind, q)

                    pr.insert(ind, p)

                    s = bg-sum(pr)

                    print("\namount left", s)

                else:

                    na.append(pn)
                    pr.append(p)
                    qu.append(q)
                    s = bg-sum(pr)

                    print('\nammount left', s)



