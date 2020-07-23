from django.urls import resolve, reverse


class TestUserURLs:
    def test_register(self):
        """ Verify that the `register` url invokes intended view """
        resolver = resolve(reverse('blog:users:register'))
        assert resolver.view_name, 'register'

    def test_profile_screen(self):
        """ Verify that the `profile` url invokes intended view """
        resolver = resolve(reverse(
            'blog:users:profile', kwargs={'username': 'wayne-lambert'}))
        assert resolver.view_name, 'profile'

    def test_profile_update_screen(self):
        """ Verify that the `profile update` url invokes intended view """
        resolver = resolve(reverse(
            'blog:users:profile_update', kwargs={'username': 'wayne-lambert'}))
        assert resolver.view_name, 'profile_update'
