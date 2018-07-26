#This is a Chi-Squared Test Python Program.
#Accepted distribution functions are: Geometric Distribution

#confirm_inputs = ("yes" , "no" , "y" , "n" )\

test = (69,32,17,12,9,11)

def Geo(p,r):
    'Geometric Distribution'
    geo_array = ()
    for a in range (1, r + 1 , 1):
        geo_pn = ((1-p)**(a-1))*(p)
        geo_array = geo_array + (geo_pn,)
    return geo_array

def E_chi(total, a):
    'Expected Value'
    new_tuple = ()
    for element in a:
        new_tuple = new_tuple + ((total * element),)
    for y in range (1, len(a)):
        if new_tuple[y - 1] < 5:
            print(str(new_tuple[y]) + " < 5, chi_squared not valid for small E_i.")
            store_value = y
            break
    new_list = list(new_tuple)
    for n in range(store_value, len(a) + 1):
        print(n)
        new_list = new_list.pop(new_list[n])
    new_list.extend([total - sum(new_list)])
                
    return new_list

def chi_squared():
    'Chi-squared test'
    while True:
        print("Please enter the observed values, O_i when prompted below.")
        print()
        x = eval(input())
        print()
        print(x)
        print()
        print("Is this the correct input?")
        print()
        ans = input()

        if ans.lower() == ("no" or "n"):
            print("Please reenter your value.")
            continue
        elif ans.lower() == ("yes" or "no" or "y" or "n"):
            print("Please enter yes or no only.")
            continue
        else:
            break

    print()

    while True:
        print("Please enter the expected values, E_i when prompted below.")
        print()
        y = eval(input())
        print()
        print(y)
        print()
        print("Is this the correct input?")
        print()
        ans = input()

        if len(y) != len(x):
            print("Number of E_i is different from number of O_i. Please reenter your E_i values.")
            continue
        elif ans.lower() == ("no" or "n"):
            print("Please reenter your value.")
            continue
        elif ans.lower() == ("yes" or "no" or "y" or "n"):
            print("Please enter yes or no only.")
            continue
        else:
            break

    final_array = ()

    for a in x:
        for b in y:
            chi_squared = ((a-b)**2)/b
            final_array = final_array + (chi_squared, )
            break
        break

    print(final_array)
