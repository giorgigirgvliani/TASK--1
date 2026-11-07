name = input("what is your name?: ")
age = input("what is your age?: ")

NumberOfProducts = int(input("how many different products you want?: "))
PriceOfProducts = 0
NumberOfProduct = 0
PriceOfProduct = 0
DiscountCounter = 0
PriceWithoutDiscount = 0

for index in range(NumberOfProducts + 1):
    print(index)
    NameOfProduct = input("name of product: ")
    while NumberOfProduct < 1:
          NumberOfProduct = int(input("number of product: "))
    while PriceOfProduct < 1:
         PriceOfProduct = int(input("price of product: ")) 
    

    
    PriceOfProducts = PriceOfProduct * NumberOfProduct
    PriceWithoutDiscount = PriceOfProducts
    
    if(NumberOfProduct > 4):
        PriceOfProducts = PriceOfProducts - ((PriceOfProducts / 100) * 10) 
        DiscountCounter = 10


Disscount = 0
if ( PriceOfProducts > 99 and PriceOfProducts < 201 ):
    Disscount = 5
    DiscountCounter = DiscountCounter + 5
elif( PriceOfProducts > 200 ):
    Disscount = 10
    DiscountCounter = DiscountCounter + 10
PriceOfProducts = PriceOfProducts - ((PriceOfProducts / 100) * Disscount) 


Delivery = ""
while Delivery !="yes" or Delivery !="no":
     input("would you like fast delivery?: ")

promocode ="" 
while promocode !="yes" or Delivery !="no":
     promocode = input("do you have PROMOCODE?: ")

if(promocode == "yes"):
     promocode = input("write your prmocode: ")
     if(promocode == "PYTHON10"):
         PriceOfProducts = PriceOfProducts - ((PriceOfProducts / 100) * 10) 


DeliveryPrice = 0

if( Delivery =="no"):
     DeliveryPrice  = 5
     PriceOfProducts = PriceOfProducts + 5
if( Delivery =="yes"):
     DeliveryPrice  = 15
     PriceOfProducts = PriceOfProducts + 15


ClientMoney = int(input("how many you want to pay?: "))
ChangedMoney = 0
PayedStatus ="no"
if(ClientMoney >= PriceOfProducts):
     ChangedMoney  = ClientMoney - PriceOfProducts
     print(f"changed:{ChangedMoney} lari")
     PayedStatus ="yes"
elif(ClientMoney < PriceOfProducts):
     ChangedMoney = PriceOfProducts - ClientMoney
     print(f"you need:{ChangedMoney} lari")

print(f"name of Client{name}")
if(PayedStatus == "yes" ):
     print(f"number of products you bought:{NumberOfProduct}")
else:
     print("number of products you bought: 0")
print(f"price of products until discount:{PriceWithoutDiscount} lari ")
print(f"used discount:{DiscountCounter}%")
print(f"price of delivery:{DeliveryPrice} lari ")
print(f"payed money:{PriceOfProducts} lari")
print(f"did eveything go well:{PayedStatus}")

