

def calculate_price(price, cash_coupon, percent_coupon):
    total_after_savings = price - cash_coupon
    coupon_savings = total_after_savings * (percent_coupon / 100)
    total_after_coupon = total_after_savings - coupon_savings
    tax = total_after_coupon * .06
    total_after_tax = total_after_coupon + tax
    if price < 10:
        shipping = 5.95
    elif price < 30:
        shipping = 7.95
    elif price < 50:
        shipping = 11.95
    else:
        shipping = 0
    return round(total_after_tax + shipping, 2)


def main():
    print(calculate_price(25, 15, 20))


if __name__== "__main__":
    main()