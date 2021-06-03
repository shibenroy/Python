from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random


Builder.load_file('spin.kv')

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"You Selected : {value}"
    
    def comp_result(self):
        mylist = ['Rock','Paper','Scissor']
        comp_input = random.choice(mylist)
        self.ids.comp_label.text = comp_input # f"And, Computer Selected : {comp_input}"

    def show_result(self, userinput, comp_input):
        res = ""
        if  userinput == 'Paper' and comp_input == 'Rock':
            res ='User Win!!!'
        elif userinput == 'Paper' and comp_input == 'Scissor':
            res ='Computer Wins'
        elif userinput == 'Paper' and comp_input == 'Paper':
            res ='Draw!!'
        # Rock       
        elif userinput == 'Rock' and comp_input == 'Paper':
            res ='Computer Win!!!'
        elif userinput == 'Rock' and comp_input == 'Rock':
            res ='Draw!!!'
        elif userinput == 'Rock' and comp_input == 'Scissor':
            res ='User Win !!!'      
        # Scissor  
        elif userinput == 'Scissor' and comp_input == 'Rock':
            res ='Computer Win !!!'
        elif userinput == 'Scissor' and comp_input == 'Scissor':
            res ='Draw!!!'
        elif userinput == 'Scissor' and comp_input == 'Paper':
            res ='User Win !!!' 

        self.ids.res_label.text = f"Result is: {res}"

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()

