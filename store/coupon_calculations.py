

def calculate_price(price, cash_coupon, percent_coupon):
    total_after_savings =  price - cash_coupon
    coupon_savings = total_after_savings * percent_coupon
    total_after_coupon = total_after_savings - coupon_savings
    tax = total_after_coupon * .6
    total_after_tax = total_after_coupon + tax
    if price < 10:
        shipping = 5.95
    else:
        shipping = 0
    return total_after_tax + shipping


def main():
    calculate_price(23, 3, 30)


if __name__== "__main__":
    main()