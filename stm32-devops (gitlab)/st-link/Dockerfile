FROM ubuntu:18.04
RUN mkdir build
RUN apt-get update && apt-get install git build-essential cmake rpm libusb-1.0-0-dev libusb-1.0 -y
RUN git clone https://github.com/stlink-org/stlink.git && cd stlink && make clean && make release && cd build/Release && make install . && ldconfig

WORKDIR /build
