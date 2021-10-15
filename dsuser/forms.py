from django import forms


class RegisterForm(forms.Form):
    userId = forms.CharField(
        required=True,
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=200,
        label="아이디"
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        widget=forms.EmailInput,
        label="이메일"
    )
    password = forms.CharField(
        required=True,
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label="비밀번호"
    )
    confirmPassword = forms.CharField(
        required=True,
        error_messages={
            'required': '비밀번호 확인을 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label="비밀번호 확인"
    )

    def clean(self):
        
        cleaned_data = super().clean()

        userId = cleaned_data.get('userId')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')

        if not(cleaned_data) or not(userId and email and password and confirmPassword):
            self.add_error('confirmPassword','모든 값을 입력해야 합니다.')
        
        
        
        if password and confirmPassword:
            if password != confirmPassword:
                self.add_error('password','비밀번호가 서로 다릅니다.')
                self.add_error('confirmPassword','비밀번호가 서로 다릅니다.')

    


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=200,
        label="아이디"
    )
