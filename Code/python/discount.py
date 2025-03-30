def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount percentage is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply (e.g., 20 for 20%).

    Returns:
        float: The final price after applying the discount, or the original price if the discount
               percentage is less than 20%.

    Example:
        >>> calculate_discount(100, 25)
        75.0
        >>> calculate_discount(100, 15)
        100.0
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage (e.g., 20 for 20%): "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"After applying a {discount_percentage}% discount, the final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied (discount percentage is less than 20%). The final price is: ${final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numerical values for the price and discount percentage.")