#!/usr/bin/python3
#import library
#what we need input widget app grid

from kivy.app import App    #import the app
from kivy.uix.gridlayout import GridLayout  #we got grid
from kivy.uix.label import Label        #we got label
from kivy.uix.textinput import TextInput    #we got input
from kivy.uix.button import Button

#create class app
class LoginAccount(GridLayout):

    def __init__(self,**kwargs):    
        super(LoginAccount,self).__init__(**kwargs)     #oop class use to implement
        self.cols = 2
        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline = False)    #when we type make text visible
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password = True, multiline = False) # we set them as password
        self.add_widget(self.password) #set as password
        self.add_widget(Button(text='Login'))
        self.add_widget(Button(text='Register'))
#building app
class MyApp(App):

    def build(self):
        return LoginAccount()
# run the app
if __name__ == '__main__':
    MyApp().run()