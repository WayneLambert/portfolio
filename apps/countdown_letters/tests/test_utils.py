from apps.countdown_letters import utils


class TestURL:
    def test_build_game_screen_url(self):
        """ Tests that the game screens' URL is built correctly """
        game_screen_url = utils.build_game_screen_url(num_vowels_selected=3)
        path = 'countdown-letters/game/?letters_chosen='
        assert path in game_screen_url, \
            'specified path including query param should be within the URL'
        letters_chosen_in_url = game_screen_url[-9:]
        full_url = f"{path}{letters_chosen_in_url}"
        assert full_url in game_screen_url

    def test_build_results_screen_url(self):
        """ Tests that the results screens' URL is built correctly """
        results_screen_url = utils.build_results_screen_url(
            letters_chosen='ABCDEFGHI', players_word='BAD')
        path = 'countdown-letters/results/?letters_chosen='
        assert path in results_screen_url
        assert 'players_word=' in results_screen_url
        assert 'ABCDEFGHI' in results_screen_url
        assert 'BAD' in results_screen_url
