from django.core.mail import send_mail

send_mail(
    subject='Message Test 1 Subject',
    message='Message Test 1 Body',
    from_email='admin@waynelambert.dev',
    recipient_list=['wayne.a.lambert@gmail.com'],
)
