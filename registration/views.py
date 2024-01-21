from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm
from django.views.generic import TemplateView
from .forms import activate_user

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)
        

from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)