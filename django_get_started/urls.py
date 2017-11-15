"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'app.views.pagina_inicial', name='pagina_inicial'),

    url(r'^listar_alunos', 'app.views.listar_alunos', name='listar_alunos'),
    url(r'^novo_aluno', 'app.views.novo_aluno', name='novo_aluno'),
    url(r'^editar_aluno/(?P<pk>\d+)$', 'app.views.editar_aluno', name='editar_aluno'),
    url(r'^apagar_aluno/(?P<pk>\d+)$', 'app.views.apagar_aluno', name='apagar_aluno'),

    url(r'^listar_professor', 'app.views.listar_professor', name='listar_professor'),
    url(r'^novo_professor', 'app.views.novo_professor', name='novo_professor'),
    url(r'^editar_professor/(?P<pk>\d+)$', 'app.views.editar_professor', name='editar_professor'),
    url(r'^apagar_professor/(?P<pk>\d+)$', 'app.views.apagar_professor', name='apagar_professor'),

    url(r'^listar_colaborador', 'app.views.listar_colaborador', name='listar_colaborador'),
    url(r'^novo_colaborador', 'app.views.novo_colaborador', name='novo_colaborador'),
    url(r'^editar_colaborador/(?P<pk>\d+)$', 'app.views.editar_colaborador', name='editar_colaborador'),
    url(r'^apagar_colaborador/(?P<pk>\d+)$', 'app.views.apagar_colaborador', name='apagar_colaborador'),

    url(r'^listar_usuarios', 'app.views.listar_usuarios', name='listar_usuarios'),
    url(r'^novo_usuario', 'app.views.novo_usuario', name='novo_usuario'),
    url(r'^editar_usuario/(?P<pk>\d+)$', 'app.views.editar_usuario', name='editar_usuario'),
    url(r'^apagar_usuario/(?P<pk>\d+)$', 'app.views.apagar_usuario', name='apagar_usuario'),

    url(r'^listar_cursos', 'app.views.listar_cursos', name='listar_cursos'),
    url(r'^novo_curso', 'app.views.novo_curso', name='novo_curso'),
    url(r'^editar_curso/(?P<pk>\d+)$', 'app.views.editar_curso', name='editar_curso'),
    url(r'^apagar_curso/(?P<pk>\d+)$', 'app.views.apagar_curso', name='apagar_curso'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

)
