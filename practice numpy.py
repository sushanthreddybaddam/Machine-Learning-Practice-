import numpy as np

number = [8, 9, 9, 1, 6, 9, 5, 7, 3, 9, 7, 3, 4, 8, 3, 5, 8, 4, 8, 7, 5, 7, 3, 6, 1, 2, 7, 4, 7, 7, 8, 4, 3, 4, 2, 2, 2, 7, 3, 5, 6, 1, 1, 3, 2, 1, 1, 7, 7, 1, 4, 4, 5, 6, 1, 2, 7, 4, 5, 8, 1, 4, 8, 6, 2, 4, 3, 7, 3, 6, 2, 3, 3, 3, 2, 4, 6, 8, 9, 3, 9, 3, 1, 8, 6, 6, 3, 3, 9, 4, 6, 4, 9, 6, 7, 1, 2, 8, 7, 8, 1, 4]
price = [195, 225, 150, 150, 90, 60, 75, 255, 270, 225, 135, 195, 30, 15, 210, 105, 15, 30, 180, 60, 165, 60, 45, 225, 180, 90, 30, 210, 150, 15, 270, 60, 210, 180, 60, 225, 150, 150, 120, 195, 75, 240, 60, 45, 30, 180, 240, 285, 135, 165, 180, 240, 60, 105, 165, 240, 120, 45, 120, 165, 285, 225, 90, 105, 225, 45, 45, 45, 75, 180, 90, 240, 30, 30, 60, 135, 180, 15, 255, 180, 270, 135, 105, 135, 210, 180, 135, 195, 225, 75, 225, 15, 240, 60, 15, 180, 255, 90, 15, 150, 230, 150]

#total number of products 
total_prodcts=len(number)
print(total_prodcts)

#items sold 
total_items_sold=sum(number)
print(total_items_sold)

#revenue of company 
total_revenue = 0
for i in range(len(number)):
    total_revenue += number[i] * price[i]
print(total_revenue)

#average price 
avg_price=np.mean(price)
print (int(avg_price))

#specific product is popular than other specific product
popular_product=number[19]>number[49]
print(popular_product)

#greater than average price 
count=0
for i in range( len(price)):
    if price[i]>avg_price:
        count+=1
print(count)


