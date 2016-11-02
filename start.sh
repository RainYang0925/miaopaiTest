#!/bin/bash

rm test.log
rm ./errorScreenShot/*
python startTest.py | tee test.log

