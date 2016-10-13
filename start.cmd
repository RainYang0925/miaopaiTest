@echo off

del test.log

rem 只输出到命令行
rem python startTest.py

rem 只输出到文件
rem python startTest.py >> test.log 2>&1 

rem 同时输出到命令行和文件
powershell "python startTest.py 2>&1 | tee test.log" 

pause