1. // Поганий приклад
2. int x; 
3. 
4. // Поганий приклад
5. void calculate(int y, int z) {
6.     x = y + z;
7.     cout << "Sum: " << x << endl;
8. }
9. 
10. // Гарний приклад
11. void calculateSum(int firstValue, int secondValue) {
12.     int sumResult = firstValue + secondValue;
13.     cout << "Sum: " << sumResult << endl;
14. }
15. 
16. // Поганий приклад
17. int main() {
18.     int a = 25;
19.     int b = 7;
20.     string c = "John";
21.     return 0;
22. }
23. 
24. // Гарний приклад
25. int userInterface() {
26.     int userAge = 25;
27.     const int daysInWeek = 7;
28.     string userName = "John";
29.     return 0;
30. }
31. 
32. // Поганий приклад
33. for (int i = 0; i < 10; i++) {
34.     cout << i << endl;
35. }
36. 
37. // Гарний приклад
38. for (int index = 0; index < 10; ++index) {
39.     cout << index << endl;
40. }
41. 
42. // Поганий приклад
43. int main() {
44.     int dividend, divisor;
45.     cout << "Enter dividend: ";
46.     cin >> dividend;
47.     cout << "Enter divisor: ";
48.     cin >> divisor;
49.     if (divisor == 0) {
50.         cout << "Error: Division by zero." << endl;
51.         return 1;
52.     }
53.     cout << "Result: " << dividend / divisor << endl;
54.     return 0;
55. }
56. 
57. // Гарний приклад
58. int divideNumbers() {
59.     int dividend, divisor;
60.     cout << "Enter dividend: ";
61.     cin >> dividend;
62.     cout << "Enter divisor: ";
63.     cin >> divisor;
64.     try {
65.         if (divisor == 0) {
66.             throw runtime_error("Error: Division by zero.");
67.         }
68.         cout << "Result: " << dividend / divisor << endl;
69.     } catch (runtime_error &err) {
70.         cout << err.what() << endl;
71.     }
72.     return 0;
73. }
74. 
75. // Поганий приклад
76. int addAndMultiply(int value1, int value2) {
77.     int sum = value1 + value2;
78.     int product = value1 * value2;
79.     cout << "Sum: " << sum << endl;
80.     cout << "Product: " << product << endl;
81.     return sum;
82. }
83. 
84. // Гарний приклад
85. int calculateAddition(int firstNumber, int secondNumber) {
86.     return firstNumber + secondNumber;
87. }
88. 
89. // Поганий приклад
90. int main() {
91.     int array[100];
92.     for (int i = 0; i < 100; ++i) {
93.         array[i] = i;
94.     }
95.     return 0;
96. }
97. 
98. // Гарний приклад
99. const int arraySize = 100;
100.
101. int processArray() {
102.     int dataArray[arraySize];
103.     for (int index = 0; index < arraySize; ++index) {
104.         dataArray[index] = index;
105.     }
106.     return 0;
107. }
108. 
109. // Поганий приклад
110. int main() {
111.     ifstream file("data.txt");
112.     file.close();
113.     return 0;
114. }
115. 
116. // Гарний приклад
117. int readFile() {
118.     ifstream fileInput("data.txt");
119.     if (!fileInput.is_open()) {
120.         cerr << "Error: Failed to open file." << endl;
121.         return 1;
122.     }
123.     fileInput.close();
124.     return 0;
125. }
126. 
127. // Поганий приклад
128. if (a == b) {
129.     return true;
130. } else {
131.     return false;
132. }
133. 
134. // Гарний приклад
135. return a == b;
136. 
137. // Поганий приклад
138. if (dataSize == 0) {
139.     return;
140. } else {
141.     for (int i = 0; i < 10; i++) cout << "ok" << endl;
142. }
143. 
144. // Гарний приклад
145. if (dataSize == 0) {
146.     return;
147. } else {
148.     for (int index = 0; index < 10; ++index) {
149.         cout << "ok" << endl;
150.     }
151. }
152. 
153. // Поганий приклад
154. void process(BankAccount* account) {
155.     if (account != nullptr) {
156.         account->performAction();
157.     }
158. }
159. 
160. // Гарний приклад
161. void executeTransaction(BankAccount& bankAccount) {
162.     bankAccount.performAction();
163. }
