def calculate_discount(price, discount_percent):
    
    if discount_percent >= 0:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
