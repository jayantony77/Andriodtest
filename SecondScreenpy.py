from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.label import MDLabel
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout

class Data(GridLayout):
    pass

class ScoreCardItem(RelativeLayout):
    pass


class SecondScreen(MDScreen):

    def on_pre_enter(self, *args):
        
        #not working 
        
        for i in range(4):
            #text1 =  "CSK Vs RCB" + str(i)
            #oneLine = OneLineListItem(text= text1)
            scorecarditem = self.buildscorecard()
            self.ids.scorelist.add_widget(scorecarditem)
    
    def on_leave(self, *args):
        self.ids.scorelist.clear_widgets(children=None)
        

    def buildscorecard(self):

        #for matches in the list , u try to add matches as indivial score 

        list1 = [ 
            ("Batsman","R","B","S/R","4s","6s"),
            ("KLRahul",25,25,123.23,4,0),
            ("Myank",54,65,93.23,7,0),
            ("Kholi",75,65,93.23,11,2),
            ("Hardik",45,25,123.23,12,12)
            ]
        scorecard = ScoreCardItem()
        #matchLabel = MDLabel(text="")
        #matchlabel = ObjectProperty(None)
        #scorecard.ids.matchlabel.text="India vs Australia 2st ODI"
            
        k = 0
        for tup in list1:
            for i in tup:
                if k == 0:
                    label = MDLabel(text=str(i),    
                    theme_text_color = "Custom",
                    text_color = (1/255, 1/255, 255/255, 1),
                    font_style="Overline")
                    scorecard.ids.data.add_widget(label)
                if k == 1:
                    label = MDLabel(text=str(i), 
                    bold = True,
                    theme_text_color = "Custom",
                    text_color = (252/255, 142/255, 2/255, 1),
                    font_style="Caption")
                    scorecard.ids.data.add_widget(label)
                if k == 2:
                    label = MDLabel(text=str(i), text_color = (252/255, 142/255, 144/255, 1),
                    font_style="Caption")
                    scorecard.ids.data.add_widget(label)
                if k == 3:
                    label = MDLabel(text=str(i),
                    font_style="Caption")
                    scorecard.ids.data.add_widget(label)
                if k == 4:
                    label = MDLabel(text=str(i), 
                    font_style="Caption")
                    scorecard.ids.data.add_widget(label)
            k += 1
        return scorecard 
            