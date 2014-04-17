from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'contaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'contaEditar'),
    url(r'^salvar/$', 'contaSalvar'),
    url(r'^pesquisar/$', 'contaPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'contaExcluir'),
    url(r'^$', 'contaListar'),
)