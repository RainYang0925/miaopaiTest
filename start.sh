#!/bin/bash

rm test.log
python startTest.py | tee test.log
