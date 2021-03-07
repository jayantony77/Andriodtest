from kivymd.uix.screen import MDScreen

from kivymd.uix.label import MDLabel

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.gridlayout import GridLayout

from kivymd.uix.tab import MDTabsBase 

from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatButton, MDRectangleFlatButton
from kivymd.app import MDApp

import csv
import os
import sys
from pathlib import Path

#File last modified 07-03-2021 at 5:15PM


class Tab(FloatLayout, MDTabsBase):
    pass
        
class Scores(Tab):
    pass

class General(Tab):
    pass

class ScoreCardItem(RelativeLayout):
    pass

class ScoreCardBowlItem(RelativeLayout):
    pass

class Data(GridLayout):
    pass

class DataLabel(MDLabel):
    pass

class Prediction(Tab):
    def on_press(self, text):
        if text == "bat":
            self.ids.img.source= "battingheavy.jpg"
        if text == "bal":
            self.ids.img.source= "balancedteam.jpg"
        if text == "bowl":
            self.ids.img.source= "bowlingheavy.jpg"

    pass

class AnalyzeScreen(MDScreen):

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        path = os.path.dirname(os.path.abspath(__file__))
     
        path = path + '/data/ss/'

        if instance_tab_label.text == "General":
            pass
        
        if instance_tab_label.text == "Scores-Batting":
            #self.ids.sc_bat.ids.scorelist.clear_widgets(children=None)
            
            if len(self.ids.sc_bat.ids.scorelist.children) < 1: 
                con = 1
                for f_name in os.listdir(path):
                    if f_name.startswith('bat'):
                        print(f_name)
                        scorecarditem = self.buildscorecard(path + f_name, "bat",con)
                        self.ids.sc_bat.ids.scorelist.add_widget(scorecarditem)
                        con += con
            else:
                print("Children Bat Populated")        


        if instance_tab_label.text == "Scores-Bowling":
            #self.ids.sc_bowl.ids.scorelist.clear_widgets(children=None)
            if len(self.ids.sc_bowl.ids.scorelist.children) < 1: 
                con = 1
                for f_name in os.listdir(path):
                    if f_name.startswith('bowl'):
                        print(f_name)
                        scorecarditem = self.buildscorecard(path + f_name,"bowl",con)
                        self.ids.sc_bowl.ids.scorelist.add_widget(scorecarditem)   
                        con += con
            else:
                print("Children Bowl Populated")        


        if instance_tab_label.text == "Prediction":
            print("instance_tab_label", instance_tab_label.text)
            

    def buildscorecard(self, filename, id_string,con):

        if id_string == "bat":
            scorecard = ScoreCardItem()
        if id_string == "bowl":
            scorecard = ScoreCardBowlItem()
        scorecard.ids.matchlbl.text=str(con)+"st Match CSK vs Other"   
        
        k = 0
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
    

            for row in csv_reader:

                for columns in row:
                    if k == 0:
                        label = DataLabel(
                        text="[u]"+columns+"[/u]",
                        markup=True,
                        font_size=8)
                                               
                        scorecard.ids.data.add_widget(label)
                    if k == 1:
                        label = DataLabel(
                        text="[b]"+columns+"[/b]",
                        markup=True,
                        font_size="10sp")
                        
                        scorecard.ids.data.add_widget(label)
                    if k == 2:
                        label = DataLabel(text=columns, 
                        font_size="10sp")
                        scorecard.ids.data.add_widget(label)
                    if k == 3:
                        label = DataLabel(text=columns,
                        font_size="10sp")
                        scorecard.ids.data.add_widget(label)
                    if k == 4:
                        label = DataLabel(text=columns, 
                        font_size="10sp")
                        scorecard.ids.data.add_widget(label)
                    
                k += 1
        return scorecard 
    
    
    


class RoundFlatToggleButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.accent_color
        super().__init__(**kwargs)

