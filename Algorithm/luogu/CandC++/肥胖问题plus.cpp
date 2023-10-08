#include <iostream>

using namespace std;

int main() {
	double weight;
	double height;
	cin >> weight >> height;
	double BMI = weight / (height * height);
	if (BMI < 18.5)
		cout << "Underweight";
	if (BMI >= 18.5 && BMI < 24)
		cout << "Normal";
	if (BMI >= 24) {
		cout <<  BMI << "\n" << "Overweight";
	}
	return 0;
}