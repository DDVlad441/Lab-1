inventory = {
    "яблука": 10,
    "банани": 3,
    "молоко": 7,
    "хліб": 2,
    "сир": 5,
}

def update_inventory(inventory, product, quantity):

    if product in inventory:
        inventory[product] += quantity
        if inventory[product] <= 0:
            del inventory[product]
    elif quantity > 0:
        inventory[product] = quantity
    else:
        print(f"Продукту «{product}» немає на складі, видаляти нічого.")



update_inventory(inventory, "апельсини", 8)   # додаємо новий продукт
update_inventory(inventory, "яблука", 5)      # збільшуємо кількість
update_inventory(inventory, "банани", -3)     # видаляємо продукт повністю
update_inventory(inventory, "молоко", -2)     # зменшуємо кількість
update_inventory(inventory, "сік", -1)        # такого продукту немає

print("Інвентар:", inventory)

# Список продуктів, кількість яких менша за 5
low_stock = [name for name, qty in inventory.items() if qty < 5]
print("Продукти з кількістю менше 5:", low_stock)