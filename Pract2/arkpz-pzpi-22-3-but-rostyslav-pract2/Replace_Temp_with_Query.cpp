//До рефакторингу
double calculateOrderTotal(const Order& order) {
    double subTotal = 0.0;
    for (const auto& item : order.items) {
        subTotal += item.price * item.quantity;
    }

    double discount = (order.isVip) ? subTotal * 0.1 : 0.0;
    double tax = subTotal * 0.2;
    return subTotal - discount + tax;
}

//Після рефакторингу
double calculateSubTotal(const Order& order) {
    double subTotal = 0.0;
    for (const auto& item : order.items) {
        subTotal += item.price * item.quantity;
    }
    return subTotal;
}

double calculateDiscount(const Order& order) {
    return (order.isVip) ? calculateSubTotal(order) * 0.1 : 0.0;
}

double calculateTax(const Order& order) {
    return calculateSubTotal(order) * 0.2;
}

double calculateOrderTotal(const Order& order) {
    return calculateSubTotal(order) - calculateDiscount(order) + calculateTax(order);
}
