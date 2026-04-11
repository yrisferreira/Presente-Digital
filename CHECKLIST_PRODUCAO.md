# Checklist de Produção - Surpresas Românticas

## **1. Dependências do Sistema**

### **Python e Pacotes**
- [ ] Python 3.8+ instalado
- [ ] Virtual environment criado
- [ ] Requirements.txt instalado:
  ```
  Flask==2.3.3
  Werkzeug==2.3.7
  Jinja2==3.1.2
  Flask-Login==0.6.3
  Flask-SQLAlchemy==3.0.5
  bcrypt==4.0.1
  stripe==7.8.0
  python-dotenv==1.0.0
  email-validator==2.1.0
  Flask-Mail==0.9.1
  ```

### **Servidor Web**
- [ ] Servidor web (Nginx/Apache) configurado
- [ ] WSGI (Gunicorn/uWSGI) instalado
- [ ] Certificado SSL instalado
- [ ] Domínio configurado

## **2. Banco de Dados**

### **Configuração**
- [ ] Banco de dados criado (SQLite/PostgreSQL/MySQL)
- [ ] Variável DATABASE_URL configurada
- [ ] Tabelas criadas (db.create_all())
- [ ] Migrações aplicadas

### **Modelos**
- [ ] User: id, username, email, password_hash, plano, data_cadastro, creditos, stripe_customer_id
- [ ] Surprise: id, id_unico, seu_nome, nome_parceiro, mensagem, musica, imagens, data_criacao, usuario_id, status
- [ ] Pagamento: id, usuario_id, stripe_payment_id, valor, plano, status, data_pagamento

## **3. Variáveis de Ambiente (.env)**

### **Obrigatórias**
- [ ] `FLASK_SECRET_KEY`: Chave secreta única
- [ ] `STRIPE_SECRET_KEY`: Chave secreta do Stripe
- [ ] `STRIPE_PUBLISHABLE_KEY`: Chave pública do Stripe
- [ ] `EMAIL_USER`: Email para envio
- [ ] `EMAIL_PASSWORD`: Senha do email

### **Configurações**
- [ ] `DATABASE_URL`: URL do banco de dados
- [ ] `BASE_URL`: URL base do aplicativo
- [ ] `FLASK_ENV=production`
- [ ] `DEBUG=False`
- [ ] `SESSION_COOKIE_SECURE=True`

### **Opcionais**
- [ ] `STRIPE_WEBHOOK_SECRET`: Webhook do Stripe
- [ ] `RATELIMIT_STORAGE_URL`: Rate limiting
- [ ] `MAX_CONTENT_LENGTH`: 16MB
- [ ] `UPLOAD_FOLDER`: uploads

## **4. Integrações Externas**

### **Stripe (Pagamentos)**
- [ ] Conta Stripe criada
- [ ] Chaves de API configuradas
- [ ] Webhook configurado
- [ ] Planos criados no dashboard
- [ ] Testes de pagamento realizados

### **Email (Gmail/Outlook)**
- [ ] App password gerada
- [ ] Configuração SMTP testada
- [ ] Templates de email funcionando
- [ ] Envio de recuperação de senha

### **Armazenamento**
- [ ] Pasta uploads criada
- [ ] Permissões configuradas
- [ ] Limite de upload (16MB)
- [ ] Backup automático

## **5. Estrutura de Arquivos**

```
/app
  app_meupresente.py
  requirements.txt
  .env
  /templates
    index_meupresente.html
    dashboard_v4.html
    surpresa_v4.html
    auth/login_v3.html
    auth/cadastro_v3.html
    planos_v2.html
  /static
    /css
    /js
    /images
    /music
  /uploads
  /instance
```

## **6. Segurança**

### **Aplicação**
- [ ] HTTPS configurado
- [ ] Cookies seguros
- [ ] CSRF tokens
- [ ] Rate limiting
- [ ] Input sanitization
- [ ] SQL injection protection

### **Dados**
- [ ] Hash de senhas (bcrypt)
- [ ] Validação de email
- [ ] Sanitização de uploads
- [ ] Backup diário
- [ ] Logs de acesso

## **7. Performance**

### **Otimização**
- [ ] Cache configurado
- [ ] Compressão Gzip
- [ ] CDN para assets
- [ ] Lazy loading
- [ ] Minificação CSS/JS

### **Monitoramento**
- [ ] Logs de erro
- [ ] Monitoramento de uptime
- [ ] Analytics configurado
- [ ] Alertas de falha

## **8. Funcionalidades**

### **Core**
- [ ] Login/Cadastro funcionando
- [ ] Dashboard operacional
- [ ] Criação de surpresas
- [ ] Upload de imagens
- [ ] Visualização de surpresas

### **Pagamentos**
- [ ] Planos funcionando
- [ ] Stripe integration
- [ ] Webhook recebendo
- [ ] Créditos sendo creditados

### **Email**
- [ ] Confirmação de cadastro
- [ ] Recuperação de senha
- [ ] Notificações

## **9. Deploy**

### **Servidor**
- [ ] Firewall configurado
- [ ] Portas abertas (80, 443)
- [ ] Process manager (systemd)
- [ ] Log rotation
- [ ] Backup automatizado

### **Domínio**
- [ ] DNS configurado
- [ ] SSL certificado
- [ ] WWW redirect
- [ ] Email MX records

## **10. Testes Finais**

### **Funcional**
- [ ] Cadastro de usuário
- [ ] Login/logout
- [ ] Compra de plano
- [ ] Criação de surpresa
- [ ] Compartilhamento
- [ ] Visualização mobile

### **Técnico**
- [ ] Load test
- [ ] Security scan
- [ ] Performance test
- [ ] Error handling
- [ ] 404 pages

## **11. Manutenção**

### **Rotina**
- [ ] Backup diário
- [ ] Monitoramento de logs
- [ ] Atualização de dependências
- [ ] Limpeza de uploads antigos
- [ ] Verificação de pagamentos

### **Suporte**
- [ ] Canal de suporte
- [ ] FAQ atualizado
- [ ] Tutoriais
- [ ] Contato configurado

---

## **Comandos Úteis**

### **Setup Inicial**
```bash
# Criar virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Criar banco de dados
python -c "from app_meupresente import app, db; app.app_context().push(); db.create_all()"

# Iniciar aplicação
gunicorn -w 4 -b 0.0.0.0:5000 app_meupresente:app
```

### **Manutenção**
```bash
# Backup do banco
cp site.db backup/site_$(date +%Y%m%d).db

# Limpar uploads antigos
find uploads/ -mtime +30 -delete

# Atualizar dependências
pip install --upgrade -r requirements.txt
```

### **Monitoramento**
```bash
# Verificar logs
tail -f /var/log/app.log

# Verificar processos
ps aux | grep gunicorn

# Testar SSL
openssl s_client -connect dominio.com:443
```

---

## **Contatos de Emergência**

- **Hospedagem**: [Contato da provedora]
- **Stripe**: [Dashboard de suporte]
- **Email**: [Configuração SMTP]
- **Domínio**: [Registro do domínio]

---

**Status**: ____
**Responsável**: ____
**Data**: ____
