from .models import BlockedEmails, BlockedIps, BlockedWords

def email_check(email):
	return 	BlockedEmails.objects.filter(email=email).exists()

def ip_check(ip):	
	return BlockedIps.objects.filter(ip_address=ip).exists()

def get_ip(request):
	ip = request.META.get('HTTP_X_FORWARDED_FOR')
	if ip:
		ip = ip.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def word_check(message):
	blocked_words = BlockedWords.objects.all()
	for item in blocked_words:
		if item.word.lower() in message.lower():
			return True
		else:
			return False