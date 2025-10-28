sales = [
    {"product": "laptop", "amount": 3, "price": 20000},
    {"product": "keyboard", "amount": 10, "price": 300},
    {"product": "mouse", "amount": 20, "price": 200},
    {"product": "monitor", "amount": 5, "price": 5000},
    {"product": "PC", "amount": 2, "price": 50000},
    {"product": "headphones", "amount": 7, "price": 250},
    {"product": "microphone", "amount": 1, "price": 350},
]
def calculate_income(sale_list):
    income = {}
    for item in sale_list:
        product = item["product"]
        total = item["amount"] * item["price"]
        income[product] = income.get(product, 0) + total
    return income
incomes = calculate_income(sales)
print("total income")
for product, total in incomes.items():
    print(f"{product}: {total} uah")
highest_income = [p for p, t in incomes.items() if t>1000]
print("products with income more than 1000: ")
print(highest_income)