#include "DataStreamExample.h"

DataStreamExample::DataStreamExample(size_t size) : bufferSize(size) {
    buffer = new uint32_t[bufferSize];
    for (size_t i = 0; i < bufferSize; ++i) {
        buffer[i] = static_cast<uint32_t>(i * 10);
    }
}

uint32_t* DataStreamExample::getDataBuffer() const {
    return buffer;
}

size_t DataStreamExample::getBufferSize() const {
    return bufferSize;
}

DataStreamExample::~DataStreamExample() {
    delete[] buffer;
}
