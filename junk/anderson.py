from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.slider import MDSlider


class MySlider(MDSlider):
    sound = ObjectProperty(None)

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            # call super method and save its return
            ret_val = super(MySlider, self).on_touch_up(touch)

            # adjust position of sound
            self.sound.seek(self.max * self.value_normalized)

            # if sound is stopped, restart it
            if self.sound.state == 'stop':
                MDApp.get_running_app().start_play()

            # return the saved return value
            return ret_val
        else:
            return super(MySlider, self).on_touch_up(touch)


class MusicApp(MDApp):

    def build(self):
        self.a = SoundLoader.load('test.mp3')

        # create slider and pass the sound to it
        self.slider = MySlider(min=0, max=self.a.length, value=0, sound=self.a,
                          pos_hint={'center_x': 0.50, 'center_y': 0.6},
                          size_hint=(0.6, 0.1))

        screen = Screen()

        screen.add_widget(self.slider)

        self.updater = None

        # start the sound
        self.start_play()

        return screen

    def start_play(self, *args):
        # play the sound
        self.a.play()

        if self.updater is None:
            # schedule updates to the slider
            self.updater = Clock.schedule_interval(self.update_slider, 0.5)

    def update_slider(self, dt):
        # update slider
        self.slider.value = self.a.get_pos()

        # if the sound has finished, stop the updating
        if self.a.state == 'stop':
            self.updater.cancel()
            self.updater = None


MusicApp().run()
