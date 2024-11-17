#pragma once
#include "Shape.h"

class Circle : public Shape {
public:
    explicit Circle(double radius);
    double area() const override;

private:
    double radius;
};
