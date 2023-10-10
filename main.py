from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from plyer.platforms.win.libs.batterystatus import battery_status
from plyer.facades import Battery
from ctypes.wintypes import BYTE

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    
    def show_battery_state(self):
        charging = BYTE(8).value
        unknown_status = BYTE(255).value
        status = {"isCharging": None, "percentage": None}

        my_battry_status = battery_status()

        if not my_battry_status:
            return status

        status["isCharging"] = (my_battry_status["BatteryFlag"] != unknown_status) and \
                               (my_battry_status["BatteryFlag"] & charging > 0)
        status["percentage"] = my_battry_status["BatteryLifePercent"]

        return status 

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()

MainApp().run()
