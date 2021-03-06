from django import  forms
# from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password =  forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))

    # captcha = CaptchaField(label="验证码")
    

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    real_name= forms.CharField(label="真实姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    phone_number = forms.CharField(label="手机号码", max_length=32,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Id_number = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control'}), label="身份证号")
    birthday = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control'}), label="出生日期")
    # captcha = CaptchaField(label='验证码')


class PersonnalInformationForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    new_username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="手机号码", max_length=32,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    sex =forms.ChoiceField(label='性别', choices=gender)
    birthday =forms.CharField(label="生日", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    perfession =forms.CharField(label="职业", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))



class usernameForm(forms.Form):

    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))