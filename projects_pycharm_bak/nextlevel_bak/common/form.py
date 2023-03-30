from django import forms
from common.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['area','user_id', 'user_pwd', 'user_name']
        labels = {
            'area': '지역',
            'user_id': '사용자 아이디',
            'user_pwd': '사용자 비밀번호',
            'user_name': '사용자 이름',
        }