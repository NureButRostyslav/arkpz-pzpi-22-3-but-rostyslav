// Поганий приклад
for (int i = 0; i < 10; i++)cout << i << endl;

// Гарний приклад
for (int index = 0; index < 10; ++index) {
    cout << index << endl;
}

// Поганий приклад
void calculate(int y, int z) {
    int x = y + z;
    cout << "Sum: " << x << endl;
}

// Гарний приклад
void calculateSum(int firstValue, int secondValue) {
    int sumResult = firstValue + secondValue;
    cout << "Sum: " << sumResult << endl;
}

// Поганий приклад
void process(BankAccount * account) {
    if (account != nullptr) {
        account->performAction();
    }
}

// Гарний приклад
void executeTransaction(BankAccount & bankAccount) {
    bankAccount.performAction();
}

// Поганий приклад
int result;

void calculate(int operand1, int operand2) {
    result = operand1 + operand2;
    cout << "Sum: " << result << endl;
}

// Гарний приклад
void calculateSum(int firstOperand, int secondOperand) {
    int sumResult = firstOperand + secondOperand;
    cout << "Sum: " << sumResult << endl;
}

// Поганий приклад
int area1 = width * height;
int area2 = length * width;
int area3 = height * depth;

// Гарний приклад
int calculateArea(int width, int height) {
    return width * height;
}

int area1 = calculateArea(width, height);
int area2 = calculateArea(length, width);
int area3 = calculateArea(height, depth);

// Поганий приклад
int addAndMultiply(int value1, int value2) {
    int sum = value1 + value2;
    int product = value1 * value2;
    cout << "Sum: " << sum << endl;
    cout << "Product: " << product << endl;
    return sum;
}

// Гарний приклад
int calculateAddition(int firstNumber, int secondNumber) {
    return firstNumber + secondNumber;
}

// Поганий приклад
if (dataSize == 0) return;
for (int i = 0; i < 10; i++) cout << "ok" << endl;

// Гарний приклад
if (dataSize == 0) {
    return;
}
for (int index = 0; index < 10; ++index) {
    cout << "ok" << endl;
}

// Поганий приклад
if (a == b) {
    return true;
}
else {
    return false;
}

// Гарний приклад
return a == b;

// Поганий приклад
int array[100];
for (int i = 0; i < 100; ++i) {
    array[i] = i;
}

// Гарний приклад
const int arraySize = 100;

int processArray() {
    int dataArray[arraySize];
    for (int index = 0; index < arraySize; ++index) {
        dataArray[index] = index;
    }
    return 0;
}

// Поганий приклад
void readFile() {
    FILE* file = fopen("data.txt", "r");
    if (file) {
        char buffer[256];
        while (fgets(buffer, sizeof(buffer), file)) {
            cout << buffer;
        }
        fclose(file);
    }
    else {
        cerr << "Error opening file" << endl;
    }
}

// Гарний приклад
void readFile() {
    ifstream file("data.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return;
    }

    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }
}

// Поганий приклад
int main() {
    int dividend, divisor;
    cout << "Enter dividend: ";
    cin >> dividend;
    cout << "Enter divisor: ";
    cin >> divisor;
    if (divisor == 0) {
        cout << "Error: Division by zero." << endl;
        return 1;
    }
    cout << "Result: " << dividend / divisor << endl;
    return 0;
}

// Гарний приклад
int divideNumbers() {
    int dividend, divisor;
    cout << "Enter dividend: ";
    cin >> dividend;
    cout << "Enter divisor: ";
    cin >> divisor;
    try {
        if (divisor == 0) {
            throw runtime_error("Error: Division by zero.");
        }
        cout << "Result: " << dividend / divisor << endl;
    }
    catch (runtime_error& err) {
        cout << err.what() << endl;
    }
    return 0;
}
