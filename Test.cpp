#include <iostream>
#include <assert.h>

using namespace std;

// 基类
class Shape
{
public:
    void setWidth(int w) {
        width = w;
    }
    void setHeight(int h) {
        height = h;
    }

protected:
    int width;
    int height;
};

// 派生类
class Rectangle: public Shape
{
public:
    int getArea() {
        return (width * height);
    }
};


// int main(void) 
// {
//     Rectangle rect;
//     rect.setHeight(5);
//     rect.setWidth(6);

//     cout << "Total area: " << rect.getArea() << endl;

//     return 0;
// }

class Line
{
public:
    double length;
    void setLength(double len);
    double getLength(void);
};

void Line::setLength(double len) 
{
    lenght = len;
}

double Line::getLength(void)
{
    return length;
}

int main()
{
    Line line;

    line.setLength(6.0);
    
    line.length = 10.0;

    cout << "length: " << line.length << endl;

    system("pause");
    return 0;
}

class Shape {
protected:
    int width, height;
public:
    Shape(int a = 0, int b = 0) 
    {
        width = a;
        height = b;
    }

    virtual int area()
    {
        cout << "Parent class " << endl;
        return 0;
    }

    // virtual int area() = 0; // 纯虚函数
};

# Python

class Animal(object):
    def run(self):
        print("Animal")

class Dog(Animal):
    def eat(self):
        print("Dog eat")

dog = Dog()
dog.run()
