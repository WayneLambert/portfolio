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

    def clean_title(self):
        starting_title = self.cleaned_data['title']
        words = starting_title.split(' ')
        capitalized_exceptions = ('why', 'how', 'tip')
        uncapitalized_exceptions = ('with', 'them')
        updated_words = []
        for word in words:
            if not word.isupper():
                if (len(word.strip()) >= 4 or word in capitalized_exceptions) and \
                    word not in uncapitalized_exceptions:
                    updated_words.append(word.title())
                elif (len(word.strip()) < 4 or word in uncapitalized_exceptions) and \
                    word not in capitalized_exceptions:
                    updated_words.append(word.lower())
            else:
                updated_words.append(word)
        new_title = ' '.join(updated_words).replace("&", "and").strip()
        if new_title[0].islower():
            new_title = f"{new_title[0].capitalize()}{new_title[1:]}"
        return new_title[:-1] if new_title.endswith('.') else new_title
