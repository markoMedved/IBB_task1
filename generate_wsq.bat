@echo off
setlocal enabledelayedexpansion

set "base=%1"
echo %base%

set input_folder=images
set output_folder=images_out_2

rem generate wsq of images
for %%f in ("%input_folder%\*") do (
    set "filename=%%~nf"
  
    magick %%f -depth 8 -type Grayscale -compress none -colorspace Gray -strip "%output_folder%\!filename!.gray"

    cwsq 1 wsq "%output_folder%\!filename!.gray" -raw_in 640,480,8,500
 
)

endlocal


