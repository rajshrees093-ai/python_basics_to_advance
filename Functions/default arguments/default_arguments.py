# default arguments= a default value for certaim parameters
#                    default is used when that argument is omitted
#                     make function to work more flexibly reduces # of argument
#                     1.positional 2. DEFAULT 3. keyword 4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price*(1-discount)*(1+tax)

print(net_price(500))