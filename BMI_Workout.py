import json
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# JSON 파일에서 BMI 운동 계획 불러오기
def load_bmi_plans():
    with open("bmi_exercise_plans.json", "r", encoding="utf-8") as file:
        return json.load(file)

bmi_plans = load_bmi_plans()

class BMIScreen(Screen):
    def __init__(self, weight, height, gender, **kwargs):
        super().__init__(**kwargs)
        self.weight = weight
        self.height = height
        self.gender = gender
        
        bmi = self.calculate_bmi()
        category = self.get_bmi_category(bmi)
        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        bmi_label = Label(text=f'당신의 BMI: {bmi:.2f}', font_size='24sp')
        result_label = Label(text=f'분류: {category}', font_size='28sp', bold=True)
        
        self.layout.add_widget(bmi_label)
        self.layout.add_widget(result_label)
        
        if category in bmi_plans:
            for key, value in bmi_plans[category].items():
                self.layout.add_widget(Label(text=f"{key}: {value}", font_size='18sp'))
        
        back_button = Button(text='뒤로 가기', size_hint=(1, 0.2), on_press=self.go_back)
        self.layout.add_widget(back_button)
        
        self.add_widget(self.layout)
    
    def calculate_bmi(self):
        return self.weight / (self.height / 100) ** 2
    
    def get_bmi_category(self, bmi):
        if self.gender == "남성":
            if bmi < 18.5:
                return "저체중"
            elif 18.5 <= bmi < 24.9:
                return "정상 체중"
            elif 25 <= bmi < 29.9:
                return "과체중"
            else:
                return "비만"
        elif self.gender == "여성":
            if bmi < 18.0:
                return "저체중"
            elif 18.0 <= bmi < 23.9:
                return "정상 체중"
            elif 24 <= bmi < 28.9:
                return "과체중"
            else:
                return "비만"
        return "알 수 없음"
    
    def go_back(self, instance):
        self.manager.current = 'height_weight_screen'

