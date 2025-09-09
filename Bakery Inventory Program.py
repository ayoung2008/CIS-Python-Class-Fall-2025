# Initial inventory
muffins = 10
cupcakes = 10

while True:
    item = input("What would you like to buy (muffin/cupcake)? Enter 0 to stop: ").strip().lower()
    
    if item == "0":
        break
    elif item == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    else:
        print("Invalid input")

# Print remaining inventory
print(f"muffins: {muffins} cupcakes: {cupcakes}")
