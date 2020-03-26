from django.urls import path
from .views import home, login, contato, mensagem, pedido_novo



urlpatterns =[
    path('', home, name='core_home'),
    path('login', login, name='core_login'),
    path('contato', contato, name='core_contato'),
    path('mensagem', mensagem, name='core_mensagem'),
    path('pedido-novo', pedido_novo, name='core_pedido_novo'),
]