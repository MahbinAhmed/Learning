# class store:
#     def __init__(self,item_input,item_price):
#         self.item_counter = item_input
#         self.item_price = item_price

#     def buy(self,item_quantity,money):
#         if item_quantity == self.item_counter or item_quantity < self.item_counter:
#             if money >= item_quantity * self.item_price:
#                 print("Thanks for your purchase !")
#                 self.item_counter = self.item_counter-item_quantity
#             else:
#                 print(f"Sorry! You need {self.item_counter*self.item_price - money} tk more.")
#         else:
#             print(f"Sorry! We have only {self.item_counter} piece remaining.")

# shop = store(50,5)

# if __name__ == "__main__":
#     print("Welcome to our Shop\n")
#     print("1. Buy item")
#     user_input = int(input("Enter your choice : "))
#     if user_input == 1 :
#         quantity_input = int(input("Enter your quantity : "))
#         money_input = int(input("Please give your money : "))
#         shop.buy(quantity_input,money_input)
#         print(shop.item_counter)

for i in range(5):
    print(i+1)