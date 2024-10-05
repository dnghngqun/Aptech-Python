from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu và xác nhận mật khẩu không khớp.")
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class TaskForm(forms.Form):
    task_name = forms.CharField(label="Tên công việc", max_length=255)
    description = forms.CharField(label="Mô tả", widget=forms.Textarea, required=False)
    # deadline = forms.DateField(label="Ngày hết hạn", widget=forms.SelectDateWidget())
    deadline = forms.DateTimeField(label="Ngày hết hạn", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    priority = forms.ChoiceField(
        label="Mức độ ưu tiên",
        choices=[('Cao', 'Cao'), ('Trung bình', 'Trung bình'), ('Thấp', 'Thấp')]
    )
    completed = forms.BooleanField(required=False)

class EditTaskForm(forms.Form):
    task_name = forms.CharField(label="Tên công việc", max_length=255)
    description = forms.CharField(label="Mô tả", widget=forms.Textarea, required=False)
    # deadline = forms.DateField(label="Ngày hết hạn", widget=forms.SelectDateWidget())
    deadline = forms.DateTimeField(label="Ngày hết hạn", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    priority = forms.ChoiceField(
        label="Mức độ ưu tiên",
        choices=[('Cao', 'Cao'), ('Trung bình', 'Trung bình'), ('Thấp', 'Thấp')]
    )
    completed = forms.BooleanField(required=False)
    
