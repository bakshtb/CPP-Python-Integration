#include "ShapeManager.h"

void ShapeManager::addShape(std::shared_ptr<Shape> shape) {
    shapes.push_back(shape);
}

double ShapeManager::totalArea() const {
    double total = 0.0;
    for (const auto& shape : shapes) {
        total += shape->area();
    }
    return total;
}

std::shared_ptr<Shape> ShapeManager::getShape(size_t index) const {
    return shapes.at(index);
}
