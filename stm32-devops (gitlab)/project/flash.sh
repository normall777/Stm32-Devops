#!/bin/bash
st-flash erase 
st-flash --reset write *.bin 0x08000000
