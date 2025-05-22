# forms.py

from django import forms
from django.contrib.auth import authenticate
from .models import Department, Course, HashTag, CustomUser, Questions, Answers, Replies, PaymentSwitch

from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254)

# Then, use this form in your PasswordResetView
# views.py

from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    
    

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'  # Include all fields

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course', 'department')  # Explicit field selection

class HashTagForm(forms.ModelForm):
    class Meta:
        model = HashTag
        fields = '__all__'  # Include all fields

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "status",'first_name', 'last_name','profile_pic'] # Customize user fields

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [ 'password', 'first_name', 'last_name', 'email', 'department']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Perform custom validation for email format if needed
        # You can add additional validation logic here
        return email

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = (  'course', 'question', 'hashtags')
        widgets = {
            'question': forms.Textarea(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}),
            'hashtags': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}),
            'course': forms.Select(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('user', 'answer', 'verified')
        exclude = ['date'] 

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Replies
        fields = ('user', 'reply', 'date')
        exclude = ['date'] 
        
        
        
        
class PaymentSwitchForm(forms.ModelForm):
    class Meta:
        model = PaymentSwitch
        fields = ['is_on']
