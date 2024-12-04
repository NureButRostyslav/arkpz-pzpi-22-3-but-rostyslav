//До рефакторингу
double calculateFinalPrice(double price, double taxRate, int quantity) {
    if (price < 500) {
        price += 50;
    }
    double discount = (quantity > 10) ? price * 0.1 : 0;
    double tax = price * taxRate;
    return (price - discount + tax);
}

//Після рефакторингу
const double LOW_PRICE_SURCHARGE = 50.0;
const double DISCOUNT_RATE = 0.1;

double applySurcharge(double price) {
    return (price < 500) ? price + LOW_PRICE_SURCHARGE : price;
}

double calculateDiscount(double price, int quantity) {
    return (quantity > 10) ? price * DISCOUNT_RATE : 0;
}

double calculateTax(double price, double taxRate) {
    return price * taxRate;
}

double calculateFinalPrice(double price, double taxRate, int quantity) {
    double adjustedPrice = applySurcharge(price);
    double discount = calculateDiscount(adjustedPrice, quantity);
    double tax = calculateTax(adjustedPrice, taxRate);
    return (adjustedPrice - discount + tax);
}

