from kivymd.uix.screen import MDScreen

from kivymd.uix.label import MDLabel

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.gridlayout import GridLayout

from kivymd.uix.tab import MDTabsBase 

from kivymd.uix.button import MDFillRoundFlatButton, MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.widget import Widget
from kivymd.uix.card import MDSeparator
from kivymd.theming import ThemableBehavior
import globalvar


import csv
import os
import sys
from pathlib import Path


class ScoreCardItem(MDCard):
    pass

"""
class ScoreCardBowlItem(MDCard):
    pass
"""
class DataBat(GridLayout):
    pass

class DataBowl(GridLayout):
    pass

class DataLabel(MDLabel):
    pass

class ScoresScreenBowl(MDScreen):

    def on_pre_enter(self):
        
        cluetext = str(self.ids.scorestbb.cluetxt)
        teamclue = cluetext.partition("-")[0]
        inngclue = cluetext.partition("-")[2]

        print("Teamclue",teamclue,"inningsclue",inngclue)
        #rendering of prev scores starts
        #
        path = os.path.dirname(os.path.abspath(__file__))
        if teamclue == "CSK":
            path = path + '/data/ss/'
        else:
            path = path + '/data/ps/'

        if inngclue == "bowl":
           
            self.ids.scorestbb.title=teamclue + " Bowling "
            if globalvar.current_team_bowling == teamclue:
                print("Children Bowl Populated")
            else:
                #if len(self.ids.scorelist.children) < 1:
                con = 1
                self.ids.scorelist.clear_widgets()
                for f_name in os.listdir(path):
                    if f_name.startswith('bowl'):
                        print(f_name)
                        scorecarditem = self.buildscorecard(path + f_name, "bowl",con)
                        self.ids.scorelist.add_widget(scorecarditem)
                        con += con
                        globalvar.current_team_bowling=teamclue


    def buildscorecard(self, filename, id_string,con):

        scorecard = ScoreCardItem()
                
        k = 0
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            data = DataBowl()
            textmatch="CSK/RCB-09-04-2021"
            matlbl = MDLabel(text=textmatch, adaptive_size=True)
            scorecard.add_widget(matlbl)
            sep = MDSeparator(height="1dp")
            scorecard.add_widget(sep)

            for row in csv_reader:

                for columns in row:
                    if k == 0:
                        lbl1 = MDLabel(text=columns, font_style="Overline")
                        data.add_widget(lbl1)
                    if k == 1:
                        lbl1 = MDLabel(text="[b]"+columns+"[b]",markup=True, font_style="Caption")
                        data.add_widget(lbl1)
                    if k == 2:
                        lbl1 = MDLabel(text=columns, font_style="Caption")
                        data.add_widget(lbl1)
                    if k == 3:
                        lbl1 = MDLabel(text=columns, font_style="Caption")
                        data.add_widget(lbl1)
                    if k == 4:
                        lbl1 = MDLabel(text=columns, font_style="Caption")
                        data.add_widget(lbl1)
                k += 1
        scorecard.add_widget(data)
        return scorecard 




