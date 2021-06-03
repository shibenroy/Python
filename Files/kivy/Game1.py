
# Program to explain how to creat drop-down in kivy 
     
# import kivy module    
import kivy  
from kivy.app import App 
kivy.require('1.9.0') 
     
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
  
# create a dropdown with 10 buttons
dropdown = DropDown()
mylist = ['Rock','Paper','Scissor']
for index in range(3):
  
    # Adding button in drop down list
    btn = Button(text =mylist[index], size_hint_y = None, height = 40)
  
    # binding the button to show the text when selected
    btn.bind(on_release = lambda btn: dropdown.select(btn.text))
  
    # then add the button inside the dropdown
    dropdown.add_widget(btn)
  
# create a big main button
mainbutton = Button(text ="User Selection !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(52, 20),
                   size_hint =(.2, .2),
                   pos =(50, 350))

mainbutton.bind(on_release = dropdown.open)

dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
  

runTouchApp(mainbutton)
print(mainbutton.text)