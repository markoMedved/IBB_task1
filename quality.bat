@echo off
setlocal enabledelayedexpansion

rem calculating quality of all samples

rem input images
set input_folder=images
rem output text file
set results_file=quality.txt

rem loop through the whole images folder and calculate quality for each sample
for %%f in ("%input_folder%\*") do (
            set file=%%f
            nfiq !file! >> "%results_file%"

)