from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.anchorlayout import AnchorLayout

if __name__ == '__main__' and __package__ is None:
    from os import sys, path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

root = Builder.load_string("""

#:import MapView kivy.garden.mapview.MapView
<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'

    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

RelativeLayout:

    MapView:
        id: mapview
        lat: 55.34321886123324
        lon: 86.06356764514878
        zoom: 15
        #size_hint: .5, .5
        #pos_hint: {"x": .25, "y": .25}

        #on_map_relocated: mapview2.sync_to(self)
        #on_map_relocated: mapview3.sync_to(self)

        MapMarkerPopup:
            lat: 55.375711
            lon: 86.071539
            source: "Infocard/mapMarker.png"
            Image:
                canvas:
                    Color:
                        rgb: (1, 1, 1)
                    Rectangle:
                        texture: self.texture
                        size: self.width + 300, self.height + 300
                        pos: self.x - 150, self.y - 40
                        source: "Infocard/MuzeyKrasniyGorka.png"
        MapMarkerPopup:
            lat: 55.37458689218019
            lon: 86.07826716927184
            source: "Infocard/mapMarker.png"
            Image:
                canvas:
                    Color:
                        rgb: (1, 1, 1)
                    Rectangle:
                        texture: self.texture
                        size: self.width + 300, self.height + 300
                        pos: self.x - 150, self.y - 40
                        source: "Infocard/PamytnicShahery.png"
        MapMarkerPopup:
            lat: 55.36092555961332
            lon: 86.07843404247674
            source: "Infocard/mapMarker.png"
            Image:
                canvas:
                    Color:
                        rgb: (1, 1, 1)
                    Rectangle:
                        texture: self.texture
                        size: self.width + 300, self.height + 300
                        pos: self.x - 150, self.y - 40
                        source: "Infocard/ParkChudes.png"                
    
    Toolbar:
        top: root.top
        Button:
            text: "Мувай на парк лп"
            on_release: mapview.center_on(55.419672, 86.239627)
        Button:
            text: "Мувай в Калугу"
            on_release: mapview.center_on(54.511785, 36.265093)
        Spinner:
            values: 'Музей <<Красная Горка>>', 'Памятник Погибшим Шахтерам', 'Парк Чудес', 'Custom'
            on_text:    
                if self.text == "Музей <<Красная Горка>>":   mapview.center_on(55.375711, 86.071539) 
                elif self.text == "Памятник Погибшим Шахтерам": mapview.center_on(55.37458686095922, 86.07869197494216)
                elif self.text == "Парк Чудес": mapview.center_on(55.361071919148706, 86.07845550832407)






    Toolbar:
        Label:
            text: "Longitude: {}".format(mapview.lon)
        Label:
            text: "Latitude: {}".format(mapview.lat)
    """)

runTouchApp(root)
