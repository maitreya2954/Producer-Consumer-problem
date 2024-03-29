# Producer Consumer Problem - A classic synchronization problem in operating system

## Group : Leela Krishna (coe15b004@iiitdm.ac.in), Maitreya Rayabharam (coe15b040@iiitdm.ac.in)

## Introduction

![Screenshot](https://github.com/maitreya2954/Producer-Consumer-problem/blob/master/image.png)

The producer-consumer problem is an example of a multi-process synchronization problem. The problem describes two processes, the producer and the consumer that shares a common fixed-size buffer use it as a queue.

* The producer’s job is to generate data, put it into the buffer, and start again.

* At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time.

The solution is that the producer is to either go to sleep or discard data if the buffer is full. The next time the consumer removes an item from the buffer, it notifies the producer, who starts to fill the buffer again. In the same manner, the consumer can go to sleep if it finds the buffer to be empty. The next time the producer puts data into the buffer, it wakes up the sleeping consumer.

In our demonstration, the producer is represented by the mother, the buffer is represented by the refridgerator and the consumer is the child. The mother produces apples into the refridgerator whereas the children consume the apples from the refrigerator.

## Codestack

* Python

* Pygame library

