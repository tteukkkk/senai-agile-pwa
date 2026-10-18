# Revisão para portfólio

## Alterações comuns

- Removidos ambientes virtuais, arquivos compilados, bancos SQLite, uploads locais e estáticos coletados.
- Configuração de credenciais por variáveis de ambiente; arquivo `.env.example` sem senha real.
- SQLite como padrão para demonstração e MySQL opcional.
- Dependências e instruções de instalação documentadas.
- DEFAULT_AUTO_FIELD alinhado às migrações existentes.

## Alterações específicas

Corrigida a relação aluno.curso na matrícula e o nome do template de sucesso. Service worker servido na raiz para escopo correto, sem cache de páginas de perfis; limpeza de versões antigas do cache.

## Verificação executada

Python 3.12.14 / Django 5.2.18 / SQLite. 4 testes passaram; check, conferência de migrações e migrate concluíram com sucesso. Testes novos cobrem fluxos alterados e se somam aos testes originais. Não houve teste de MySQL, concorrência real, implantação ou inspeção visual em navegador da aplicação local.

## Limitações

Protótipo acadêmico: perfis e matrículas ainda não possuem controle de acesso por aluno. Use somente dados fictícios. O PWA tem cache básico da página inicial e do CSS; a instalação e o modo offline completo não foram testados em navegador. A presença de serializers não significa que exista uma API REST publicada.

## Modelos principais

- `Curso`
- `Noticia`
- `Aluno`
- `Contato`

A carga original foi substituída integralmente por dados sintéticos (domínio example.com e telefone composto por zeros).
