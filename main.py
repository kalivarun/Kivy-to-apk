import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

import socket
ip = ''
port = 0
kivy.require('2.0.0')

#Video Logo

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from kivy.core.window import Window

class ConnectPage(Screen):
    def __init__(self, **kwargs):
        super(ConnectPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Add a Video widget as the background
        video = Video(source='https://pouch.jumpshare.com/preview/SlxcZjtXAl37pwxXLx2l7cEF1soQOFnG8nVnmdYGM4d0SAvTBgUpZY-lKbQmTkwz7l3WM4PG73VpYPe6AU7aweC0bLQtJmp2j3uzxJf5hP_U4xn-bMw_c7Z6qTLjU03i--TP3Q3kcfwKdWaayQp8J26yjbN-I2pg_cnoHs_AmgI.mp4', state='play', opacity=0.9 ,options={'eos': 'loop'})
        video.size_hint = (1, 0.2)
        video.allow_stretch = True
        layout.add_widget(video)

        # Add overlay for inputs
        overlay = BoxLayout(orientation='vertical', size_hint=(1, 0.1), padding=20, spacing=10)
        
        self.ip_input = TextInput(hint_text='Enter IP', multiline=False, font_size=18, size_hint=(1, 0.2))
        overlay.add_widget(self.ip_input)

        self.port_input = TextInput(hint_text='Enter Port', multiline=False, font_size=18, size_hint=(1, 0.2))
        overlay.add_widget(self.port_input)

        btn_connect = Button(text='Connect', size_hint=(1, 0.2))
        btn_connect.bind(on_press=self.connect_to_server)
        overlay.add_widget(btn_connect)

        layout.add_widget(overlay)
        self.add_widget(layout)

    def connect_to_server(self, instance):
        global ip, port
        ip = self.ip_input.text
        try:
            port = int(self.port_input.text)
            # Check connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(5)  # Set a timeout for the connection attempt
                client.connect((ip, port))
                # If we reach this point, the connection is successful
                print(f"Connected to {ip}:{port}")
                self.manager.current = 'main_menu'
        except (ValueError, socket.error) as e:
            # Show error popup with a "Try Again" button
            self.show_error_popup(f"Connection failed: {str(e)}")

    def show_error_popup(self, message):
        popup = ErrorPopup(on_try_again=self.retry_connection)
        popup.message_label.text = message
        popup.open()

    def retry_connection(self):
        # Reset inputs and focus the user back to ConnectPage
        self.ip_input.text = ''
        self.port_input.text = ''
        self.manager.current = 'connect'

class ErrorPopup(Popup):
    def __init__(self, on_try_again, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        self.on_try_again = on_try_again
        layout = BoxLayout(orientation='vertical', padding=10)
        
        self.message_label = Label(size_hint_y=0.8)
        layout.add_widget(self.message_label)

        btn_try_again = Button(text='Try Again', size_hint_y=0.2)
        btn_try_again.bind(on_press=self.try_again)
        layout.add_widget(btn_try_again)

        self.add_widget(layout)

    def try_again(self, instance):
        self.dismiss()
        self.on_try_again()



#Image Logo 
"""
#Connect Page Menu
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from io import BytesIO
import requests

# URL of the image
IMAGE_URL = "https://www.obrela.com/wp-content/uploads/2023/12/advisory3.png"

def load_image_from_url(url):
    try:
        # Download the image from the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Load image data into Kivy
        image_data = BytesIO(response.content)
        return CoreImage(image_data, ext='jpg')
    except Exception as e:
        print(f"Failed to load image: {e}")
        return None

class ConnectPage(Screen):
    def __init__(self, **kwargs):
        super(ConnectPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Load image from URL
        logo_image = load_image_from_url(IMAGE_URL)
        if logo_image:
            logo = Image(texture=logo_image.texture, size_hint=(1, 1.4))
            layout.add_widget(logo)
        else:
            # Fallback if image cannot be loaded
            logo = Label(text='Image Load Failed', size_hint=(1, 1), font_size=32)
            layout.add_widget(logo)

        self.ip_input = TextInput(hint_text='Enter IP', multiline=False, font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.ip_input)

        self.port_input = TextInput(hint_text='Enter Port', multiline=False, font_size=18, size_hint=(1, 0.2))
        layout.add_widget(self.port_input)

        btn_connect = Button(text='Connect', size_hint=(1, 0.2))
        btn_connect.bind(on_press=self.connect_to_server)
        layout.add_widget(btn_connect)

        self.add_widget(layout)

    def connect_to_server(self, instance):
        global ip, port
        ip = self.ip_input.text
        try:
            port = int(self.port_input.text)
            # Check connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(5)  # Set a timeout for the connection attempt
                client.connect((ip, port))
                # If we reach this point, the connection is successful
                print(f"Connected to {ip}:{port}")
                self.manager.current = 'main_menu'
        except (ValueError, socket.error) as e:
            # Show error popup with a "Try Again" button
            self.show_error_popup(f"Connection failed: {str(e)}")

    def show_error_popup(self, message):
        popup = ErrorPopup(on_try_again=self.retry_connection)
        popup.message_label.text = message
        popup.open()

    def retry_connection(self):
        # Reset inputs and focus the user back to ConnectPage
        self.ip_input.text = ''
        self.port_input.text = ''
        self.manager.current = 'connect'
"""
#Error Popup in connect page 
        
class ErrorPopup(Popup):
    def __init__(self, on_try_again, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Error message label
        self.message_label = Label(text='', size_hint=(1, 0.8))
        layout.add_widget(self.message_label)
        
        # Try Again button
        try_again_button = Button(text='Try Again', size_hint=(1, 0.2))
        try_again_button.bind(on_press=self.on_try_again_button_press)
        layout.add_widget(try_again_button)
        
        self.on_try_again = on_try_again
        self.content = layout

    def on_try_again_button_press(self, instance):
        if self.on_try_again:
            self.on_try_again()
            self.dismiss()
# Continue with the rest of your classes


#Main menu all pages will be redirected to this page 

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = GridLayout(cols=2, rows=2, padding=20, spacing=20, size_hint=(1, 1))
        self.add_widget(layout)

        btn_mouse_pad = Button(text='Mouse Pad', size_hint=(0.9, 0.9))
        btn_mouse_pad.bind(on_press=self.go_to_mouse_pad)
        layout.add_widget(btn_mouse_pad)

        btn_game_mode = Button(text='Game Mode', size_hint=(0.9, 0.9))
        btn_game_mode.bind(on_press=self.go_to_game_mode)
        layout.add_widget(btn_game_mode)

        btn_full_keyboard = Button(text='Full Keyboard', size_hint=(0.9, 0.9))
        btn_full_keyboard.bind(on_press=self.go_to_full_keyboard)
        layout.add_widget(btn_full_keyboard)

        btn_lock_screen = Button(text='Lock Screen', size_hint=(0.9, 0.9))
        btn_lock_screen.bind(on_press=self.lock_screen)
        layout.add_widget(btn_lock_screen)

    def go_to_mouse_pad(self, instance):
        self.manager.current = 'mouse_pad'

    def go_to_game_mode(self, instance):
        self.manager.current = 'game_mode'

    def go_to_full_keyboard(self, instance):
        self.manager.current = 'full_keyboard'

    def lock_screen(self, instance):
        self.send_message('LOCK_SCREEN')

    def send_message(self, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((ip, port))
                client.send(message.encode('utf-8'))
        except ConnectionRefusedError:
            print(f"Error: Could not connect to the server at {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")


#Mousepad has buttons to move the cursor 

class MousePad(Screen):
    def __init__(self, **kwargs):
        super(MousePad, self).__init__(**kwargs)
        layout = GridLayout(cols=3, padding=10, spacing=10)
        self.add_widget(layout)

        btn_up = Button(text='Up')
        btn_up.bind(on_press=self.send_up)
        layout.add_widget(btn_up)

        btn_left = Button(text='Left')
        btn_left.bind(on_press=self.send_left)
        layout.add_widget(btn_left)

        btn_down = Button(text='Down')
        btn_down.bind(on_press=self.send_down)
        layout.add_widget(btn_down)

        btn_right = Button(text='Right')
        btn_right.bind(on_press=self.send_right)
        layout.add_widget(btn_right)

        btn_left_click = Button(text='Left Click')
        btn_left_click.bind(on_press=self.send_left_click)
        layout.add_widget(btn_left_click)

        btn_right_click = Button(text='Right Click')
        btn_right_click.bind(on_press=self.send_right_click)
        layout.add_widget(btn_right_click)

        btn_main_menu = Button(text='Main Menu')
        btn_main_menu.bind(on_press=self.go_to_main_menu)
        layout.add_widget(btn_main_menu)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'

    def send_message(self, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((ip, port))
                client.send(message.encode('utf-8'))
        except ConnectionRefusedError:
            print(f"Error: Could not connect to the server at {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

    def send_up(self, instance):
        self.send_message('MOVE_UP')

    def send_left(self, instance):
        self.send_message('MOVE_LEFT')

    def send_down(self, instance):
        self.send_message('MOVE_DOWN')

    def send_right(self, instance):
        self.send_message('MOVE_RIGHT')

    def send_left_click(self, instance):
        self.send_message('LEFT_CLICK')

    def send_right_click(self, instance):
        self.send_message('RIGHT_CLICK')

class GameMode(Screen):
    def __init__(self, **kwargs):
        super(GameMode, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=10, spacing=10)
        self.add_widget(layout)

        buttons = {
            'Go': 'GO',
            'Stop': 'STOP',
            'Change': 'CHANGE',
            'Esc': 'ESC',
            'Shift': 'SHIFT',
            'Left': 'LEFT',
            'Right': 'RIGHT',
            'Space': 'SPACE',
        }

        for text, action in buttons.items():
            btn = Button(text=text, size_hint=(0.9, 0.3))
            btn.bind(on_press=lambda btn, act=action: self.send_message(f'BUTTON_PRESS {act}'))
            btn.bind(on_release=lambda btn, act=action: self.send_message(f'BUTTON_RELEASE {act}'))
            layout.add_widget(btn)

        btn_main_menu = Button(text='Main Menu', size_hint=(0.9, 0.3))
        btn_main_menu.bind(on_press=self.go_to_main_menu)
        layout.add_widget(btn_main_menu)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'

    def send_message(self, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((ip, port))
                client.send(message.encode('utf-8'))
        except ConnectionRefusedError:
            print(f"Error: Could not connect to the server at {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")



#Keyboard menu has all the buttons of numbers and letters
            
class FullKeyboard(Screen):
    def __init__(self, **kwargs):
        super(FullKeyboard, self).__init__(**kwargs)
        layout = GridLayout(cols=4, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        keys = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '~','!','@','#','$','%','^','&','*','(',')','_','+','?', 'spacebar' 
        ]

        for key in keys:
            btn = Button(text=key, size_hint=(0.2, 0.2))
            btn.bind(on_press=lambda btn, k=key: self.send_message(f'KEY_PRESS {k}'))
            btn.bind(on_release=lambda btn, k=key: self.send_message(f'KEY_RELEASE {k}'))
            layout.add_widget(btn)

        btn_main_menu = Button(text='Main Menu', size_hint=(0.2, 0.2))
        btn_main_menu.bind(on_press=self.go_to_main_menu)
        layout.add_widget(btn_main_menu)

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'

    def send_message(self, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((ip, port))
                client.send(message.encode('utf-8'))
        except ConnectionRefusedError:
            print(f"Error: Could not connect to the server at {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ConnectPage(name='connect'))
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(MousePad(name='mouse_pad'))
        sm.add_widget(GameMode(name='game_mode'))
        sm.add_widget(FullKeyboard(name='full_keyboard'))
        return sm

if __name__ == '__main__':
    MyApp().run()


