from .models import Post, Comment, Contact, Members
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ContactForm(forms.Form):
    Your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('Title', 'Gender', 'First_Name', 'Last_Name', 'Mobile_Number', 'Email', 'Nationality', 'Occupation', 'Interested_PBC_Faculty', 'Agree_to_Terms_and_Conditions')


    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)

        self.fields['Agree_to_Terms_and_Conditions'].required = True
        

        
            