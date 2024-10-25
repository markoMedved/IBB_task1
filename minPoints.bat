@echo off
setlocal enabledelayedexpansion

set input_folder=images
set output_folder=images_out

rem make folder on the first run
if not exist "%output_folder%" mkdir "%output_folder%"

rem go through entire input folder 
for %%f in ("%input_folder%\*") do (
    rem only take filename without file-type
    set filename=%%~nf
    mindtct %%f "%output_folder%\!filename!"
)