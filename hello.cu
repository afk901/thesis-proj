#include <stdio.h>

__global__ void sayHello() {
  printf("Hello from GPU!\n");
}

int main() {
  printf("Hello from CPU!\n");

  sayHello<<<1,1>>>();
  cudaDeviceSynchronize();
}