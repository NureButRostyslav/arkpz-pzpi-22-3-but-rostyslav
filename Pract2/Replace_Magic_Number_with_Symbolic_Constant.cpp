//До рефакторингу
if (employee.age >= 18 && employee.age <= 65) {
    employee.salary = employee.hoursWorked * 20.5;
    if (employee.salary > 5000) {
        employee.salary -= employee.salary * 0.15;
    }
}

//Після рефакторингу
const int MIN_WORKING_AGE = 18;
const int MAX_WORKING_AGE = 65;
const double HOURLY_RATE = 20.5;
const double TAX_RATE = 0.15;

if (employee.age >= MIN_WORKING_AGE && employee.age <= MAX_WORKING_AGE) {
    employee.salary = employee.hoursWorked * HOURLY_RATE;
    if (employee.salary > 5000) {
        employee.salary -= employee.salary * TAX_RATE;
    }
}

