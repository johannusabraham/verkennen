month_discount_brands = "Vespa,Kymco,Puch"
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands.split(','):
        korting = price * MONTH_DISCOUNT_PERC / 100
    else:
        korting = 0
    return korting

korting = calc_discount(1000, "Vespa", month_discount_brands)
print(f"{korting:.2f}")