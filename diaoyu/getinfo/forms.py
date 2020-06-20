from django import forms
from django.forms import widgets


class InfoForm(forms.Form):
    name = forms.CharField(widget=widgets.TextInput(attrs={'class': "span12", 'type': "Text", 'id': "userName",  'name':"userName", 'placeholder': "输入您的用户名"}))
    pwd = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'span12', 'type': "password", 'id': 'pwd', 'name': 'pwd', 'placeholder': '请输入您的密码'}))
    attrs = {'class': "span12", 'type': "password", 'id': "pwd",  'name':"pwd", 'placeholder': "输入您的密码"}