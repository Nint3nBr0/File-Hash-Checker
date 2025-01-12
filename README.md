# File-Hash-Checker
** # The Future Of This Project **

I have recently just finished my first version of the file hash checker, I have two other updates that will be coming out. My plan for this project will be to have a selection screen that will choose between whether you want to check for a file, an entire directory and a full backup. I will also improve the performance of the speed for checking the hashes and I would like for it to check different hashing algorithms. Currently it only checks SHA256 as that is the most common one.
There is a couple things I would like to touch on before explaining what the code does. 

** # What is a Hash? **

First I would like to explain what a hash is so you get a better idea as to why I made this project. Hashing means transforming any piece of data into a unique, fixed length output. It looks something like 
"44524f1abd1ac0f550e77516527d70a2ab4a1d88273947608e3200a42f792f2c"

** # Reason you should check hashes **

Hashing is a good way to check if a file has been changed. This ties into the CIA triad(confidently, integrity, availability) as this checks the integrity of the file to make sure no malicious code or data has been changed. This project was an excellent way for me to get myself into understanding Cybersecurity concepts through coding.

** # Options for an explanation **

Now to explain how the code works, I will have a canvas explain what each section of this code does, but for a more in-depth understanding and explanation on how to use this code, please read here.

** # Full explanation of what the program does and how to use it **

First you are prompted to put the file path you would like to check for example you would input a path like so "path/to/file/file.exe" For the end when you reach the file, make sure to put in the .exe or . extension for whatever file you would like to check, then you will be prompted to give the original hash. If you don't have the original hash that is okay, I plan on making it so you can save the hash in a file so you can check it with that file but that's for later. You can find the original hash when you download certain applications online. Sometimes you may have to do a little digging to find it though. After that, my program will hash the file you chose and check it with the original hash which will then print out a message saying "The hashes are the same" or "The hashes are different" if the hashes are different, you can check https://www.virustotal.com/gui/home/upload to see if the file got maliciously changed. Alternatively, if the file does not exist or if the program doesn't have access to the directory to the file it will print out "File can not be accessed or does not exist" You may come into this issue if you are trying to access the C: directory, your best option will be to move the file to a more public directory like your Documents folder or C:\Users\Public.
