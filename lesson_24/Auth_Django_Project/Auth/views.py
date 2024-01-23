from django.shortcuts import render
from django.views import View
from .models import Users


class UsersView(View):
    def get(self, request):
        users = Users.objects.all()
        private_emails = []
        for user in users:
            mod = str(user).split('@')
            modded_username = mod[0][:2] + "*" * (len(mod[0]) - 2)
            domain = mod[1]
            modded_email = modded_username + '@' + domain
            private_emails.append(modded_email)
        users_count = len(users)
        last_10_emails = private_emails[-10:]
        return render(request, 'main.html',
                      {'count': users_count, 'users': last_10_emails})


class SignupView(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        for user in Users.objects.all():
            if user.email == email:
                return render(request, 'reg_decline.html',
                              {'error_message': 'User already exists!'})
            else:
                if password == repeat_password:
                    user = Users(email=email, password=password)
                    user.save()
                    return render(request, 'reg_success.html')
                else:
                    return render(request, 'reg_decline.html',
                                  {'error_message': 'Passwords do not match'})


class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user_found = False
        for user in Users.objects.all():
            if user.email == email and user.password == password:
                user_found = True
                return render(request, 'signin_success.html', {'message': 'Success!'})
        if not user_found:
            return render(request, 'signin_decline.html', {'error_message': 'Invalid email or password!'})
