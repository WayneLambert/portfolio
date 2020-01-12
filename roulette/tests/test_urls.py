from django.urls import resolve, reverse

class TestUrls:

    def test_holiday_roulette(self):
        path = reverse('holiday-roulette')
        assert resolve(path).view_name == 'holiday-roulette'

    def test_holiday_destination(self):
        path = reverse('holiday-destination')
        assert resolve(path).view_name == 'holiday-destination'

    def test_destination_log_file(self):
        path = reverse('destination-log-file')
        assert resolve(path).view_name == 'destination-log-file'
