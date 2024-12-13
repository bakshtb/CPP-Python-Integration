#pragma once
#include <cstdint>
#include <cstddef>

class DataStreamExample {
public:
    explicit DataStreamExample(size_t size);
    uint32_t* getDataBuffer() const;
    void printDataBuffer() const;
    size_t getBufferSize() const;
    ~DataStreamExample();

private:
    uint32_t* buffer;
    size_t bufferSize;
};
