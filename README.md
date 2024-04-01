# Timer

Simple example of creating a timer with Tkinter in Python.

## Presentation of the application

This code creates a small Tkinter application with an input field where you can enter the number of seconds for the timer, and a button to start the timer. Once the timer has started, the number of seconds remaining is displayed, and it updates every second until the time is up.  
<div style="display:flex">
    <img src="/test_img/error.png" alt="Screenshot of the error page" style="width:200px" />&nbsp;
    <img src="/test_img/ok.png" alt="Screenshot of the timer ending"style="width:200px" />
</div>

## Interesting features

 - The size of the window is fixed by `root.resizable(False, False)`
 - The keyboard \<enter\> button is equivalent to start up by `self.entry.bind("<Return>", self.start_timer_enter)`

## Installation

Download `main.py` then launch the command `python main.py`