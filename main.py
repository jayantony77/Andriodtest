from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.tab import MDTabsBase
#from kivy.core.window import Window


import csv
import os
import sys




#Window.size = (300,600)

Builder.load_file("FirstScreen.kv")
Builder.load_file("AnalyzeScreen.kv")
Builder.load_file("AnalysisScreen.kv")
           

class FirstScreen(MDScreen):
    pass

class TeamScreen(MDScreen):
    pass

class AnalyzeScreen(MDScreen):
    pass


class Data(GridLayout):
    pass

class ScoreCardItem(RelativeLayout):
    pass

class ScoreCardBowlItem(RelativeLayout):
    pass

class Tab(FloatLayout, MDTabsBase):
    pass
        
class Scores(Tab):
    pass

class General(Tab):
    pass


class FirstScreen1(MDApp):
    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='firstScreen'))
        sm.add_widget(AnalyzeScreen(name='analyzeScreen'))
                                            
         
        return sm


    def on_press(self):

        print("clicking the listitems")

class AnalyzeScreen(MDScreen):

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        path = os.path.dirname(os.path.abspath(__file__))
     
        path = path + '/data/ss/'


        if instance_tab_label.text == "General":
            pass
        
        if instance_tab_label.text == "Scores-Batting":
            self.ids.sc_bat.ids.scorelist.clear_widgets(children=None)
            
            for f_name in os.listdir(path):
                if f_name.startswith('bat'):
                    print(f_name)
                    scorecarditem = self.buildscorecard(path + f_name, "bat",f_name)
                    self.ids.sc_bat.ids.scorelist.add_widget(scorecarditem)

        if instance_tab_label.text == "Scores-Bowling":
            self.ids.sc_bowl.ids.scorelist.clear_widgets(children=None)
            for f_name in os.listdir(path):
                if f_name.startswith('bowl'):
                    print(f_name)
                    scorecarditem = self.buildscorecard(path + f_name,"bowl",f_name)
                    self.ids.sc_bowl.ids.scorelist.add_widget(scorecarditem)   

        if instance_tab_label.text == "Prediction":
            print("instance_tab_label", instance_tab_label.text)
            

    def buildscorecard(self, filename, id_string,match):

        if id_string == "bat":
            scorecard = ScoreCardItem()
        if id_string == "bowl":
            scorecard = ScoreCardBowlItem()
        scorecard.ids.matchlbl.text=match      
        k = 0
        
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
    

            for row in csv_reader:

                for columns in row:
                    if k == 0:
                        label = MDLabel(text=columns,    
                        theme_text_color = "Custom",
                        text_color = (1/255, 1/255, 255/255, 1),
                        font_style="Overline",
                        width=100)
                        scorecard.ids.data.add_widget(label)
                    if k == 1:
                        label = MDLabel(text=columns, 
                        bold = True,
                        theme_text_color = "Custom",
                        text_color = (252/255, 142/255, 2/255, 1),
                        font_style="Caption")
                        scorecard.ids.data.add_widget(label)
                    if k == 2:
                        label = MDLabel(text=columns, 
                        text_color = (252/255, 142/255, 144/255, 1),
                        font_style="Caption")
                        scorecard.ids.data.add_widget(label)
                    if k == 3:
                        label = MDLabel(text=columns,
                        font_style="Caption")
                        scorecard.ids.data.add_widget(label)
                    if k == 4:
                        label = MDLabel(text=columns, 
                        font_style="Caption")
                        scorecard.ids.data.add_widget(label)
                    
                k += 1
        return scorecard 



FirstScreen1().run()