# color-picker-from-image
This is a simple python program that opens an image and on left click it shows the hex color code of the pixel where the mouse is clicked and also copies the hex color code to clipboard.

It is useful when you want to choose a hex color code from an image instantly. 
(I am working to improve it and I would be glad if anyone can contribute to it :)

### Requirements 

* OpenCV
* Numpy
* Pyperclip
* A working PC


Linux users need to install a copy/paste mechanism like ``xclip`` for Color Picker to run.

### How to use?

1] Clone the repo.

2] Install the dependencies.

All the dependencies are listed in the ``requirements.txt`` file.

* Installing on Windows:

  ```pip install -r requirements.txt```


* Installing on Linux:

  ```pip3 install -r requirements.txt```


Linux users also need to install ``xclip``.


* Using ``apt``:

  ```sudo apt install xclip```


* Using ``pacman``:

  ```sudo pacman -S xclip```

3] Run the program.

Running the program will open up the default ``Just Slide.png`` image. Different image can be opened by supplying it as an argument.

Use ``python`` on Windows and ``python3`` on Linux.

**Usage**:

```python main.py <address_to_the_desired_image>```
