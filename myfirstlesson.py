shop_description = 'Over 20 Years of Experience To Give You Great Deals on Quality Home Products and More. Shop ' \
                   'MacBooks You Love at Overstock, with Free Shipping on Everything* and Easy Returns. '

mac_book_pro15_description = 'Configure to Order. Configure your MacBook Pro with these options, only at apple.com: ' \
                             '2.4GHz 8-core Intel Core i9, Turbo Boost '
mac_book_pro15_price = 1000

mac_book_pro13_description = 'Configure to Order. Configure your MacBook Pro with these options, only at apple.com: ' \
                             '2.1GHz 4-core Intel Core i5, Turbo Boost '
mac_book_pro13_price = 800

total_price = 0

item_description = " "

total_price += mac_book_pro15_price

item_description += mac_book_pro15_description

total_price += mac_book_pro13_price

item_description += mac_book_pro13_description

sale_tax = total_price + total_price * 0.2

print("Customer One Total:" + str(sale_tax))
print("Customer One Description:" + item_description)
