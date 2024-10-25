@echo off
setlocal enabledelayedexpansion

set input_folder=images_out_2
set output_file=paths_to_your_fingerprints_for_pcasys.txt

rem generate list of paths to wsq images
for %%f in ("%input_folder%\*.wsq") do (
    
    echo %%f A >> "%output_file%"
    
)