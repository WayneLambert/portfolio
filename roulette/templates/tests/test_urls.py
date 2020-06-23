from django.urls import resolve, reverse

class TestUrls:

    def test_holiday_roulette(self):
        path = reverse('roulette:holiday_roulette')
        assert resolve(path).view_name == 'holiday_roulette'

    def test_holiday_destination(self):
        path = reverse('roulette:holiday_destination')
        assert resolve(path).view_name == 'holiday_destination'

    def test_destination_log_file(self):
        path = reverse('roulette:destination_log_file')
        assert resolve(path).view_name == 'destination_log_file'
