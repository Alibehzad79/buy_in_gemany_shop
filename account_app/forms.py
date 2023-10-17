from django import forms


class ResetPasswordFrom(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور جدید")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="تایید رمز عبور")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('رمز عبور ها یکسان نیست')
        return password1