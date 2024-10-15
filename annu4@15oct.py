"""
author name:annu james
python program to check discount amount
"""
purchase_amount=int(input('enter the purchase amount'))
if purchase_amount>500:
    discount=purchase_amount*0.20
    final_amount=purchase_amount-discount
    print("final amount=",final_amount)
elif(purchase_amount>=200) and (purchase_amount<500):
    discount=purchase_amount*0.10
    final_amount=purchase_amount-discount
    print("final amount:",purchase_amount)
else:
    print("final amount:",purchase_amount)