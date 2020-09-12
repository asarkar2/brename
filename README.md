# brename
Python script to bulk rename files and folders

## Example:

    ls *.mp3 > inputlist.txt
    ls *.mp3 > outputlist.txt

Open outputlist.txt in your favorite text editor and edit the filenames
as per your wish. Make sure not to change the order of the files. Then
run the code.
    
    brename.py -i inputlist.txt -o outputlist.txt

All filenames in inputlist.txt will get changed to filenames given in 
outputlist.txt sequentially.
