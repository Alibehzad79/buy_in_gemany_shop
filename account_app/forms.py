from django import forms
from django.core import validators


class ResetPasswordFrom(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="رمز عبور جدید",
        validators=[
            validators.MinLengthValidator(6, "تعداد کارکتر نباید کمتر از 6 باشد"),
            validators.MaxLengthValidator(12, 'تعداد کاراکتر نباید بیشتر از 12 باشد'),
        ],
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="تایید رمز عبور",
        validators=[
            validators.MinLengthValidator(6, "تعداد کارکتر نباید کمتر از 6 باشد"),
            validators.MaxLengthValidator(12, 'تعداد کاراکتر نباید بیشتر از 12 باشد'),
        ],
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("رمز عبور ها یکسان نیست")
        return password1
