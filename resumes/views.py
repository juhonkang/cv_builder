from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .models import CV
from .serializers import CVSerializer
from .utils import render_to_pdf  # we'll create this utility function later

from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import CVForm


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def home_view(request):
    if request.user.is_authenticated:
        cvs = CV.objects.filter(user=request.user)
        form = CVForm()

        if request.method == 'POST':
            form = CVForm(request.POST)
            if form.is_valid():
                cv = form.save(commit=False)
                cv.user = request.user
                cv.save()
                form = CVForm()

        return render(request, 'cv_list.html', {'cvs': cvs, 'form': form})
    else:
        # redirect to login page if user is not logged in
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'  # redirect to login page after successful registration
    template_name = 'registration/signup.html'  # template for the signup form



class CVViewSet(viewsets.ModelViewSet):
    serializer_class = CVSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CV.objects.none()  # Add this line


    def get_queryset(self):
        # Filter CVs by logged-in user
        return CV.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set user of CV to current user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        cv = self.get_object()
        pdf = render_to_pdf('pdf_template.html', {'cv': cv})  # render CV to PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "CV_%s.pdf" % (cv.name)
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
