from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
import os

STREAM_URL = "https://qurango.net/radio/tarateel"

KV = r"""
<RadioUI>:
    orientation: "vertical"
    padding: dp(24)
    spacing: dp(16)
    canvas.before:
        Color:
            rgba: 0.04, 0.08, 0.12, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "📻  Mp3Quran Tarateel"
        font_size: "25sp"
        bold: True
        color: 1,1,1,1
        size_hint_y: None
        height: dp(65)

    Label:
        text: root.status
        font_size: "17sp"
        color: 0.75,0.9,1,1
        halign: "center"
        text_size: self.width, None
        size_hint_y: None
        height: dp(55)

    Button:
        text: "▶  PLAY RADIO"
        font_size: "19sp"
        size_hint_y: None
        height: dp(58)
        on_release: root.play()

    Button:
        text: "⏸  PAUSE"
        font_size: "19sp"
        size_hint_y: None
        height: dp(58)
        on_release: root.pause()

    Button:
        text: "⏹  STOP"
        font_size: "19sp"
        size_hint_y: None
        height: dp(58)
        on_release: root.stop()

    Label:
        text: "Volume"
        color: 1,1,1,1
        size_hint_y: None
        height: dp(30)

    Slider:
        min: 0
        max: 1
        value: 1
        on_value: root.volume(self.value)

    Label:
        text: "Background playback is supported. Lock-screen controls appear in the Android media notification."
        color: 0.65,0.7,0.75,1
        font_size: "13sp"
        halign: "center"
        text_size: self.width, None
"""

Builder.load_string(KV)

class RadioUI(BoxLayout):
    status = StringProperty("Ready")

    def service_path(self):
        return os.path.join(os.path.dirname(__file__), "service.py")

    def start_service(self, command):
        if platform != "android":
            self.status = "Android service controls are available on Android."
            return
        try:
            from jnius import autoclass
            RadioService = autoclass("org.mp3quran.radio.RadioService")
            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            if command == "play":
                RadioService.startService(PythonActivity.mActivity, STREAM_URL)
            elif command == "pause":
                PythonService.pausePlayer()
            elif command == "stop":
                PythonService.stopPlayer()
            elif command == "volume":
                pass
        except Exception as e:
            self.status = "Service error: " + str(e)[:70]

    def play(self):
        self.status = "Connecting to Mp3Quran Tarateel…"
        self.start_service("play")
        Clock.schedule_once(lambda dt: setattr(self, "status", "Playing — background mode enabled"), 1)

    def pause(self):
        self.start_service("pause")
        self.status = "Paused"

    def stop(self):
        self.start_service("stop")
        self.status = "Stopped"

    def volume(self, value):
        # Volume is controlled by Android media volume in this version.
        pass

class RadioApp(App):
    title = "Mp3Quran Tarateel"
    def build(self):
        Window.softinput_mode = "below_target"
        return RadioUI()

if __name__ == "__main__":
    RadioApp().run()
