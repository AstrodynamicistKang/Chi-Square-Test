#This is a Chi-Squared Test Python Program.
#Currently accepted distribution functions are: Geometric Distribution

test = (69,32,17,12,9,11)

def Geo(p,r):
    'Geometric Distribution function'
    geo_array = ()
    for a in range (1, r + 1 , 1):
        geo_pn = ((1-p)**(a-1))*(p)
        geo_array = geo_array + (geo_pn,)
    return geo_array

def E_chi(total, a):
    'Expected Value function'
    new_tuple = ()
    for element in a:
        if (total * element) >= 5: 
            new_tuple = new_tuple + ((total * element),)
        else:
            print()
            print(str(total * element) + " < 5, chi_squared not valid for small E_i.")
            new_tuple = new_tuple + ((total - sum(new_tuple)),)
            break    
    return new_tuple

def chi_square():
    'Chi-Square test function'
    while True:
        print("Please enter the observed values, O_i when prompted below.")
        print()
        x = eval(input())
        print()
        print(x)
        print()
        print("Is this the correct input? y/n")
        print()
        ans = input()

        if ans.lower() == "n":
            print("Please reenter your value.")
            print()
            continue
        elif ans.lower() == "y":
            break
        else:
            continue

    print()

    while True:
        print("Please enter the expected values, E_i when prompted below.")
        print()
        y = eval(input())
        print()
        print(y)
        print()
        print("Is this the correct input? y/n")
        print()
        ans = input()

        if len(y) != len(x):
            print("Number of E_i is different from number of O_i. Please reenter your E_i values.")
            continue
        elif ans.lower() == "n":
            print("Please reenter your value.")
            print()
            continue
        elif ans.lower() == "y":
            break
        else:
            continue

    final_array = ()

    for a, b in zip(x,y):
        chi_squared = ((a-b)**2)/b
        final_array = final_array + (chi_squared, )

    return(sum(final_array))
