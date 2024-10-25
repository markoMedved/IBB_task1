@echo off
setlocal enabledelayedexpansion

set input_folder=images_out
set results_file=bozorth_scores.txt


echo Bozorth3 Comparison Results >> "%results_file%"

rem position of name in filepath
set start_position=11
set length=9

rem go through all combinations of folders
for %%f in ("%input_folder%\*.xyt") do (
    for %%g in ("%input_folder%\*.xyt") do (
            set file1=%%f
            set file2=%%g
            rem take only names of files in filepath
            set sub1=!file1:~%start_position%,%length%!
            set sub2=!file2:~%start_position%,%length%!
            rem write names of files in the results file
            echo !sub1! !sub2! >> "%results_file%"
            rem write bozorth scores in the results file
            bozorth3 !file1! !file2! >> "%results_file%"
    )
)

endlocal
