from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from spam_classifier.utils import email_check, ip_check, word_check, get_ip
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact


def contact(request):
	template = "contact.html"

	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.ip_address = get_ip(request)
			if email_check(instance.email) or ip_check(instance.ip_address) or word_check(instance.message):
				messages.success(request,"You are considered a spammer and do not like you.")
			else:
				instance.save()
				messages.success(request, "We have received your message and will respond within 24 hours.")
	else:
		form = ContactForm()

	context = {
        'form' : form,
    }
	return render(request, template, context)




class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('first_name', 'last_name','email', 'ip_address' ,'message')
    serializer_class = ContactSerializer
