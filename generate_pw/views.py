from django.shortcuts import render
import random
import string


# Create your views here.
def home(request):

    if request.method == 'POST':
        length = int(request.POST['length'])
        use_symbols = request.POST.get('use_symbols', False)
        use_numbers = request.POST.get('use_numbers', False)
        use_uppercase = request.POST.get('use_uppercase', False)

        password = ''
        pw_characters = string.ascii_lowercase

        if use_uppercase:
            pw_characters += string.ascii_uppercase

        if use_symbols:
           pw_characters += string.punctuation
        
        if use_numbers:
            pw_characters += string.digits


        for i in range(length):
            password += random.choice(pw_characters)

        context = {
            "password": password,
            "length": length,
            "use_symbols": use_symbols,
            "use_numbers": use_numbers,
            "use_uppercase": use_uppercase 
        }


        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
    