bill = int(input())
dis1= bill * 10/100
dis2 = 100
max_discount =  max(dis1,dis2)
pay = bill - max_discount
print(pay)
