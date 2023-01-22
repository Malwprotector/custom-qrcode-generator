# custom-qrcode-generator
*Many services offer qrcode with customised images, but there is a charge for this. Well, with this project, you will be able to achieve your goal very easily!*

**Differences between `generator1.py` and `generator2.py`:**
You can choose which type of qrcode you want to generate. The first file allows you to generate qrcodes with a chosen image in the centre, and the second with an image implanted directly into the qrcode. Here are some examples (the qrcodes in the examples link to my website): <br> <br>
**qrcode generated with `generator1.py`:** <br>
<img src="https://raw.githubusercontent.com/Malwprotector/custom-qrcode-generator/main/examples/logo.jpg" width="100"/>
<br>
<img src="https://raw.githubusercontent.com/Malwprotector/custom-qrcode-generator/main/examples/output1.png" width="100"/>
<br>
**qrcode generated with `generator2.py`:**<br>
<img src="https://raw.githubusercontent.com/Malwprotector/custom-qrcode-generator/main/examples/logo.png" width="100"/>
<br>
<img src="https://raw.githubusercontent.com/Malwprotector/custom-qrcode-generator/main/examples/output2.png" width="100"/>
<br><br>
**How to use it?** <br>
It is very simple. First, download the files `generator1.py` and `generator2.py`. Then, check that python is installed on your computer, if not download it <a href='https://www.python.org/'>from the official website</a>. Check that the images you want to appear in the qrcode are in the same directory as the files you downloaded (`logo.jpg` and `logo.png`).<br>
Then right-click in the directory where the file is, select "open in command prompt" (or similar), and write `python3 filename.py`; in this case, if you don't rename the files, the command will be `python3 generator1.py` to run the first type of qrcode and `python3 generator2.py` to run the second type of qrcode. <br>
And that's it, your qrcode magically appears in your file folder as `output.png`! 
If this doesn't work, check that you have the latest version of python. It's also possible that you don't have the required libraries: in that case, open the command prompt and run the command `pip install Pillow && pip install qrcode`. <br>
If this still doesn't work, feel free to contact me so I can help you solve your problem! <br><br>
**advanced settings**<br>
For the more adventurous among you, you can have fun modifying the code of the file to be able to modify parameters, like the colour of the qrcode! Don't worry, each piece of code is commented to help you as much as possible.




