#pragma once
#include "Shape.h"

class Rectangle : public Shape {
public:
    Rectangle(double width, double height);
    double area() const override;

private:
    double width;
    double height;
};
