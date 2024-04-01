# Timer

Simple example of creating a timer with Tkinter in Python.

## Presentation of the application

This code creates a small Tkinter application with an input field where you can enter the number of seconds for the timer, and a button to start the timer. Once the timer has started, the number of seconds remaining is displayed, and it updates every second until the time is up.  
<img src="/test_img/error.png" alt="Screenshot of the error page" style="float: left;" />
<img src="/test_img/ok.png" alt="Screenshot of the timer ending" />
![Screenshot of the error page.](/test_img/error.png =250x)
![Screenshot of the timer ending.](/test_img/ok.png)

## Interesting features

 - The size of the window is fixed by `root.resizable(False, False)`
 - The keyboard \<enter\> button is equivalent to start up by `self.entry.bind("<Return>", self.start_timer_enter)`

## Installation

Download `main.py` then launch the command `python main.py`