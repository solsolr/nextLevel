from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['area', 'user_id', 'user_pwd', 'user_name']
        labels = {
            'area': '담당 구',
            'user_id': '사용할 아이디',
            'user_pwd': '사용할 비밀번호',
            'user_name': '이름',
        }