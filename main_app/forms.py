from django import forms
class MyForm(forms.Form):
    email = forms.EmailField(error_messages={"invalid":"请输入正确的邮箱"})