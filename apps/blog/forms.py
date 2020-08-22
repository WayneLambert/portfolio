from django import forms

from apps.blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'categories', 'reference_url', 'status', 'image')

        widgets = {
            'status': forms.RadioSelect(attrs={
                'class': 'custom-control-inline'}),
            'title': forms.TextInput(attrs={
                'id': 'id_post_title',
                'onkeyup': 'character_count()',
                'class': 'col-sm-8',
                'placeholder': 'Post Title...'
            })
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
