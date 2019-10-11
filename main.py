import sqlite3
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class Input(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit(self):
        name = self.name.text
        email = self.email.text
        print("Name:", name, "email:", email)
        self.writing(name,email)
        self.name.text = ""
        self.email.text = ""

#funcao de escrita num ficheiro 

    def writing(self, name, email):
        file1 = open("MyFile.txt","a")
        file1.write(str(name)+ ";" + str(email)+ "\n")
        file1.close()

class AgendaApp(App):
    def build(self):
       return Input()

if __name__ == "__main__":
    AgendaApp().run()
