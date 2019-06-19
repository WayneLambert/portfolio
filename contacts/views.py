from django.shortcuts import render, redirect
from contacts.forms import ContactForm


def contact(request):
    contact_form_template = 'contacts/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact-submitted')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, contact_form_template, context)


def contact_submitted(request):
    return render(request, 'contact_submitted.html')
