# ** Surpresas Românticas - Plataforma Comercial **

Uma plataforma completa para criação de surpresas românticas personalizadas com sistema de pagamentos e assinaturas.

## ** Sobre o Projeto **

Transformamos sentimentos em experiências digitais inesquecíveis! Nossa plataforma permite que usuários criem surpresas românticas personalizadas com fotos, mensagens e música, tudo com um design moderno e experiência de usuário excepcional.

## ** Recursos Principais **

### ** Para Usuários **
- ** Sistema de Cadastro/Login ** - Gestão completa de usuários
- ** Planos Flexíveis ** - Gratuito, Básico (R$ 19,90), Premium (R$ 39,90), Ilimitado (R$ 79,90)
- ** Créditos de Surpresas ** - Sistema de créditos por plano
- ** Upload de Fotos ** - Até 3 fotos por surpresa
- ** Mensagens Personalizadas ** - Editor de texto romântico
- ** Trilha Sonora ** - Múltiplas opções de música romântica
- ** Compartilhamento ** - WhatsApp, Facebook, link direto
- ** Dashboard Pessoal ** - Acompanhamento de surpresas criadas

### ** Para Administradores **
- ** Painel Administrativo ** - Gestão completa da plataforma
- ** Análise de Dados ** - Estatísticas e relatórios
- ** Gestão de Usuários ** - Visualização e edição de contas
- ** Histórico de Pagamentos ** - Controle financeiro
- ** Sistema de Backup ** - Segurança dos dados

### ** Técnico **
- ** Flask Framework ** - Backend robusto e escalável
- ** SQLAlchemy ** - Banco de dados relacional
- ** Stripe Integration ** - Pagamentos seguros
- ** Sistema de Autenticação ** - Login seguro com Flask-Login
- ** Design Responsivo ** - Mobile-first approach
- ** Animações Modernas ** - Experiência visual rica

## ** Estrutura do Projeto **

```
surpresas-romanticas/
|
|-- app_comercial.py              # Aplicação Flask principal
|-- requirements.txt              # Dependências Python
|-- .env                         # Variáveis de ambiente
|-- README_COMERCIAL.md          # Este arquivo
|
|-- templates/                   # Templates HTML
|   |-- index_comercial.html     # Página inicial comercial
|   |-- planos.html              # Planos e preços
|   |-- dashboard.html           # Dashboard do usuário
|   |-- criar.html               # Formulário de criação
|   |-- surpresa_comercial.html  # Página de visualização
|   |-- 404.html                 # Página de erro
|   |-- auth/                    # Autenticação
|   |   |-- login.html           # Login
|   |   |-- cadastro.html        # Cadastro
|   |-- admin/                   # Admin
|       |-- dashboard.html       # Painel admin
|
|-- static/                      # Arquivos estáticos
|   |-- css/
|   |   |-- style_comercial.css  # Estilos comerciais
|   |-- js/                      # JavaScript (se necessário)
|   |-- music/                   # Arquivos de música
|   |-- images/                  # Imagens estáticas
|
|-- uploads/                     # Uploads de usuários
|-- data/                        # Dados da aplicação
|   |-- site.db                 # Banco de dados SQLite
|
|-- venv/                        # Ambiente virtual
```

## ** Instalação e Configuração **

### ** Pré-requisitos **
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Conta Stripe (para pagamentos)
- Conta Gmail (para emails - opcional)

### ** Passo 1: Clonar o Projeto **
```bash
# Se estiver usando Git
git clone <repositorio-url>
cd surpresas-romanticas

# Ou baixe os arquivos manualmente
```

### ** Passo 2: Ambiente Virtual **
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar (macOS/Linux)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### ** Passo 3: Instalar Dependências **
```bash
pip install -r requirements.txt
```

### ** Passo 4: Configurar Variáveis de Ambiente **
Edite o arquivo `.env` com suas configurações:

```env
# Chave Secreta Flask
FLASK_SECRET_KEY=sua_chave_secreta_aqui_mude_isso

# Configurações do Stripe
STRIPE_SECRET_KEY=sk_test_sua_chave_secreta_aqui
STRIPE_PUBLISHABLE_KEY=pk_test_sua_chave_publica_aqui
STRIPE_WEBHOOK_SECRET=whsec_seu_webhook_secret_aqui

# Configurações de Email (opcional)
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_app_google

# Configurações do Banco de Dados
DATABASE_URL=sqlite:///site.db

# Ambiente
FLASK_ENV=development
DEBUG=True
BASE_URL=http://localhost:5002
```

### ** Passo 5: Configurar Stripe **
1. Crie uma conta em [Stripe](https://stripe.com)
2. Obtenha suas chaves de API
3. Configure webhooks no dashboard Stripe
4. Adicione as chaves no arquivo `.env`

### ** Passo 6: Adicionar Músicas **
Adicione arquivos MP3 em `static/music/`:
- `romantic1.mp3` - Piano Romântico
- `romantic2.mp3` - Melodia Doce  
- `romantic3.mp3` - Sinfonia do Amor

### ** Passo 7: Iniciar a Aplicação **
```bash
python app_comercial.py
```

A aplicação estará disponível em `http://localhost:5002`

## ** Funcionalidades Detalhadas **

### ** Sistema de Planos **

| Plano | Preço | Créditos | Recursos |
|-------|-------|----------|----------|
| Gratuito | R$ 0 | 1/mês | 1 surpresa, design básico |
| Básico | R$ 19,90 | 5/mês | 5 surpresas, todos os designs |
| Premium | R$ 39,90 | 15/mês | 15 surpresas, recursos exclusivos |
| Ilimitado | R$ 79,90 | 999/mês | Surpresas ilimitadas, suporte VIP |

### ** Fluxo do Usuário **

1. **Cadastro** - Usuário cria conta gratuita
2. **Escolha do Plano** - Seleciona plano adequado
3. **Pagamento** - Processamento via Stripe
4. **Criação** - Formulário passo a passo
5. **Compartilhamento** - WhatsApp, redes sociais

### ** Fluxo de Pagamento **

1. **Seleção** - Usuário escolhe plano
2. **Redirect** - Redirecionado para Stripe Checkout
3. **Pagamento** - Processamento seguro
4. **Webhook** - Confirmação automática
5. **Créditos** - Adicionados à conta

### ** Sistema de Upload **

- **Formatos**: PNG, JPG, JPEG, GIF, WebP
- **Tamanho máximo**: 16MB por arquivo
- **Quantidade**: Até 3 fotos por surpresa
- **Segurança**: Validação de arquivo e sanitização

## ** Personalização **

### ** Alterar Cores e Design **
Edite `static/css/style_comercial.css`:

```css
/* Cores principais */
:root {
    --primary-color: #ff6b9d;
    --secondary-color: #ffc3d8;
    --accent-color: #d63384;
    --text-color: #e91e63;
}
```

### ** Adicionar Novos Planos **
1. Atualize `app_comercial.py` (função `pagamento`)
2. Modifique templates (`planos.html`)
3. Atualize preços no frontend

### ** Personalizar Músicas **
1. Adicione novos arquivos MP3 em `static/music/`
2. Atualize opções no formulário
3. Modifique nomes no template

### ** Configurar Email **
Configure no `.env`:
```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_app_google
MAIL_DEFAULT_SENDER=seu_email@gmail.com
```

## ** Implantação em Produção **

### ** Ambiente de Produção **
```env
FLASK_ENV=production
DEBUG=False
SESSION_COOKIE_SECURE=True
```

### ** Servidor WSGI **
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app_comercial:app
```

### ** Configurações Nginx **
```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### ** HTTPS com Let's Encrypt **
```bash
sudo certbot --nginx -d seu-dominio.com
```

## ** Manutenção **

### ** Backup do Banco de Dados **
```bash
# Backup
cp data/site.db data/backup_$(date +%Y%m%d).db

# Restaurar
cp data/backup_20241201.db data/site.db
```

### ** Logs e Monitoramento **
- Logs de erro em `/var/log/`
- Monitoramento com Uptime Robot
- Alertas por email

### ** Atualizações **
```bash
# Atualizar dependências
pip install -r requirements.txt --upgrade

# Reiniciar aplicação
sudo systemctl restart gunicorn
```

## ** Segurança **

### ** Medidas Implementadas **
- **Hash de senhas** com bcrypt
- **CSRF protection** do Flask
- **Validação de uploads** de arquivos
- **Sanitização de inputs** do usuário
- **HTTPS obrigatório** em produção
- **Rate limiting** (opcional)

### ** Recomendações **
- Manter dependências atualizadas
- Usar senhas fortes
- Monitorar atividades suspeitas
- Backup regular dos dados

## ** Suporte e Contato **

### ** Problemas Comuns **

**Q: A música não toca automaticamente**
A: Navegadores modernos bloqueiam autoplay. A música tocará após primeira interação do usuário.

**Q: Upload de fotos não funciona**
A: Verifique permissões da pasta `uploads/` e tamanho máximo do arquivo (16MB).

**Q: Pagamento não é confirmado**
A: Verifique configuração do Stripe e webhooks no dashboard.

### ** Obtendo Ajuda **
1. Verifique logs de erro
2. Teste com usuário de teste
3. Confirme configurações do `.env`
4. Entre em contato: suporte@surpresasromanticas.com.br

## ** Monetização **

### ** Receitas **
- **Planos de assinatura** (R$ 19,90 - R$ 79,90)
- **Upsells** futuros (templates premium)
- **Parcerias** com serviços românticos

### ** Custos **
- **Hospedagem**: ~R$ 50/mês
- **Stripe**: 2.9% + R$ 0,30 por transação
- **Domínio**: ~R$ 50/ano
- **Email**: Gratuito (Gmail) ou R$ 10/mês

### **Projeção Financeira**
Com 100 usuários no plano Básico:
- **Receita**: R$ 1.990/mês
- **Custos**: ~R$ 100/mês  
- **Lucro**: ~R$ 1.890/mês

## ** Roadmap Futuro **

### ** Versão 2.0 **
- [ ] Templates de surpresas customizáveis
- [ ] Integração com redes sociais
- [ ] Sistema de avaliações
- [ ] App mobile (React Native)
- [ ] API para desenvolvedores

### ** Versão 3.0 **
- [ ] Inteligência artificial para sugestões
- [ ] Vídeos nas surpresas
- [ ] Chat romântico integrado
- [ ] Gamificação
- [ ] Marketplace de produtos

## ** Licença **

Este projeto está sob licença MIT. Sinta-se livre para usar, modificar e distribuir conforme necessário.

---

## ** Comece Agora! **

1. **Clone** o repositório
2. **Configure** seu ambiente
3. **Personalize** com suas cores e marca
4. **Lance** sua plataforma de surpresas românticas

**Transforme amor em negócio! **

---

*Criado com ** por desenvolvedores apaixonados por experiências digitais emocionantes.*
