#pragma once
#include <vector>
#include <memory>
#include "Shape.h"

class ShapeManager {
public:
    void addShape(std::shared_ptr<Shape> shape);
    double totalArea() const;
    std::shared_ptr<Shape> getShape(size_t index) const;

private:
    std::vector<std::shared_ptr<Shape>> shapes;
};
