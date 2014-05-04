from django import forms


SUBJECTS = ('Appointment', 'Question',
            'Feedback', 'Request')
SUBJECTS = (
    ('Appointment', 'Appointment'),
    ('Question', 'Question'),
    ('Feedback', 'Feedback'),
    ('Request', 'Request'),
)


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter name',
        'required': 'required'}))
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter email',
        'pattern': '[^@]+@[^@]+\.[a-zA-Z]{2,6}', 'required': 'required'}))
    subject = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=SUBJECTS)
    telephone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Phone number',
            'pattern': '(\+?\d[- .]*){7,13}'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '6', 'required': 'required'}))
