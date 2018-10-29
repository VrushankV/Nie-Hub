from django.shortcuts import render
# Create your views here.
def logout(request):
	fmt = getattr(settings, 'LOG_FORMAT', None)
	lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

	logging.basicConfig(format=fmt, level=lvl)
	logging.debug("Logging started on ")	
	try:
		if(request.session['usn'] == "4NI16CS500"):
			del request.session['usn']
			request.session.modified = True
			return render("login")
		
		
	except:
		return render("signup")
	
	return render("home")