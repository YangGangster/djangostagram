from django import forms

from dsuser.models import Dsuser

class PostForm(forms.Form):

    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=200,
        label="제목"
    )
    img_url = forms.CharField(
        required=True,
        error_messages={'required': '이미지 주소를 업로드해주세요.'},
        label="이미지 주소"
    )
    contents= forms.CharField(
        required=True,
        error_messages={'required': '내용을 입력 해주세요.'},
        widget=forms.Textarea(attrs={"rows":5, "cols":20}),
        label="내용"
    )
    tags = forms.CharField(required = False, label = "태그")
    

    def clean(self):
        
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        img_url = cleaned_data.get('img_url')
        contents = cleaned_data.get('contents')
        tags = cleaned_data.get('tags').split(',')

        if not(cleaned_data) or not(title and img_url and contents):
            self.add_error('contents','모든 값을 입력해야 합니다.')
        
        

  
            
            
            
 


    
