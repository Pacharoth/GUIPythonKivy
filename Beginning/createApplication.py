#!/usr/bin/python3
import kivy
kivy.require('1.10.1') # replace with your current kivy version
from kivy.app import App    #import library file to compile app
from kivy.uix.label import Label    #Label from kivy to show display

class MyApp(App): 

    def build(self):
        return Label(text='Hello world')

if __name__=='__main__':
    MyApp().run()