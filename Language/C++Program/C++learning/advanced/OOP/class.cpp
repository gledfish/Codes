#include <iostream>

using namespace std;

class Person
{
public:
    int age;
    string name;

    // 构造函数
    Person(int age, string name)
    {
        this->age = age;
        this->name = name;
    }

    ~Person()
    {
    }
};
int main()
{
    Person* person = new Person(25, "张三");
    cout << person->age << endl;
    cout << person->name << endl;

    delete person;
    return 0;
}