from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class GenderSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 배경색 설정
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # 연한 회색 배경
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # 레이아웃 설정
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.size_hint = (0.8, 0.8)
        self.layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # 이미지 추가
        image = Image(source="images/성별.png", size_hint=(0.6, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.layout.add_widget(image)

        # 남성 버튼 생성
        male_button = self.create_gender_button(
            "남성",
            bg_color=(169/255, 206/255, 229/255, 1),
            text_color=(11/255, 18/255, 142/255, 1),
            gender="남성"
        )
        self.layout.add_widget(male_button)

        # 여성 버튼 생성
        female_button = self.create_gender_button(
            "여성",
            bg_color=(244/255, 194/255, 194/255, 1),
            text_color=(200/255, 0, 0, 1),
            gender="여성"
        )
        self.layout.add_widget(female_button)

        # 레이아웃을 화면에 추가
        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def create_gender_button(self, text, bg_color, text_color, gender):
        # 성별 선택 버튼 생성 함수
        btn = Button(
            text=text,
            size_hint=(1, 0.15),
            font_name="malgun.ttf",
            color=text_color,
            background_color=(0, 0, 0, 0),  # 배경 투명
            background_normal=''  # 기본 스타일 제거
        )

        # 버튼 배경색 설정
        with btn.canvas.before:
            btn.bg_color = Color(*bg_color)
            btn.rect = Rectangle(size=btn.size, pos=btn.pos)

        # 버튼 크기와 위치 바인딩
        btn.bind(size=lambda instance, value: setattr(btn.rect, 'size', value))
        btn.bind(pos=lambda instance, value: setattr(btn.rect, 'pos', value))
        btn.bind(on_press=lambda instance: self.on_gender_select(gender))
        return btn

    def on_gender_select(self, gender):
        # 성별 선택 후 화면 전환
        print(f"선택된 성별: {gender}")
        self.manager.current = 'height_weight_screen'  # height_weight_screen으로 화면 전환
