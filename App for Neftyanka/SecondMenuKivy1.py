import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

kivy.require('2.1.0')  # Убедитесь, что у вас установлена соответствующая версия Kivy

# Функция для обработки нажатия кнопки
def button_press(instance):
    print(f"Нажата кнопка: {instance.text}")

class WellControlApp(App):
    def build(self):
        # Главный макет приложения
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Прокручиваемый виджет для кнопок
        scrollview = ScrollView(size_hint=(1, None), size=(800, 500))
        button_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))

        # Текст кнопок
        button_texts = [
            "СНИЖЕНИЕ ДЕБИТА\n(СКВАЖИНА ПОПАЛА В КРАСНУЮ ЗОНУ)",
            "ОСТАНОВ УЭЦН ПО ЗСП\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
            "ОСТАНОВ УЭЦН+ПАКЕР ПО ЗСП\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
            "ОСТАНОВ УЭЦН ПО ЗП\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
            "ОСТАНОВ УЭЦН ПО ОТСУТСТВИЮ ПОДАЧИ\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
            "ОСТАНОВ УЭЦН ПО R-0\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
            "ОСТАНОВ УЭЦН ПО ТОКУ Х.Х.\n(СКВАЖИНА ВО ВНУТРИСМЕННОМ ПРОСТОЕ)",
        ]

        # Создание и размещение кнопок
        for text in button_texts:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=100,
                on_press=button_press
            )
            button_layout.add_widget(btn)

        # Добавление кнопок в прокручиваемый виджет
        scrollview.add_widget(button_layout)
        main_layout.add_widget(scrollview)

        # Создание и размещение метки версии
        version_label = Label(
            text="Версия 1.0",
            size_hint=(1, None),
            height=50,
            halign='right',
            valign='middle'
        )
        version_label.bind(size=version_label.setter('text_size'))
        main_layout.add_widget(version_label)

        return main_layout

if __name__ == '__main__':
    WellControlAppWellControlApp().run()
