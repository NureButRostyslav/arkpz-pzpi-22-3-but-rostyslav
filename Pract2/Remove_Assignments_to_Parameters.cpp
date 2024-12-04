//До рефакторингу
void applyDiscount(Order& order) {
    if (order.totalPrice > 1000) {
        order.totalPrice -= order.totalPrice * 0.1;
    }
    order.totalPrice -= order.loyaltyPoints * 0.05;
}

//Після рефакторингу
double calculateDiscountedPrice(const Order& order) {
    double discount = 0.0;
    if (order.totalPrice > 1000) {
        discount += order.totalPrice * 0.1;
    }
    discount += order.loyaltyPoints * 0.05;
    return order.totalPrice - discount;
}

