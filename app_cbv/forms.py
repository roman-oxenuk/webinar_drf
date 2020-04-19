from django import forms
from posts_models.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'author']

    def clean_text(self):
        text_value = self.cleaned_data['text']
        if 'fuck' in text_value:
            raise forms.ValidationError('Недопустимое слово в тексте')
        return text_value
