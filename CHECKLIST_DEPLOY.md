# ✅ Checklist de Deploy - Grava Perfumes

## 📋 Antes do Deploy

- [ ] Código testado localmente
- [ ] Todas as funcionalidades funcionando
- [ ] Logo.jpg na pasta correta
- [ ] Arquivo .env.example criado
- [ ] README.md atualizado

## 🔧 Preparação

- [ ] Repositório Git criado
- [ ] Código commitado
- [ ] Repositório no GitHub criado
- [ ] Código enviado para GitHub (`git push`)

## 🗄️ Banco de Dados

- [ ] PostgreSQL criado no Easypanel
- [ ] Nome do banco: `gravaperfumes`
- [ ] Senha anotada em local seguro
- [ ] Banco está rodando (status: running)

## 🚀 Aplicação

- [ ] App criado no Easypanel
- [ ] Repositório GitHub conectado
- [ ] Build Type: Dockerfile
- [ ] Port: 8000
- [ ] App linkado ao banco de dados

## 🔐 Variáveis de Ambiente

- [ ] SECRET_KEY gerada e configurada
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS com seu domínio
- [ ] DB_ENGINE=django.db.backends.postgresql
- [ ] DB_NAME=gravaperfumes
- [ ] DB_USER=postgres
- [ ] DB_PASSWORD configurada
- [ ] DB_HOST=gravaperfumes-db
- [ ] DB_PORT=5432

## 📦 Deploy

- [ ] Deploy iniciado
- [ ] Build concluído sem erros
- [ ] Container rodando
- [ ] Logs sem erros críticos

## ⚙️ Configuração Pós-Deploy

- [ ] `python manage.py migrate` executado
- [ ] `python manage.py createsuperuser` executado
- [ ] `python manage.py collectstatic` executado
- [ ] Superusuário criado (anote usuário e senha!)

## 🌐 Domínio

- [ ] Domínio adicionado no Easypanel
- [ ] DNS configurado (A record)
- [ ] SSL ativo (Let's Encrypt)
- [ ] Site acessível via HTTPS

## 🧪 Testes Finais

- [ ] Site carrega corretamente
- [ ] Tela de login aparece
- [ ] Login funciona
- [ ] Dashboard carrega
- [ ] Logo aparece corretamente
- [ ] Cores da marca aplicadas
- [ ] Navegação entre páginas funciona
- [ ] Criar cliente funciona
- [ ] Criar perfume funciona
- [ ] Criar venda funciona

## 📊 Monitoramento

- [ ] Logs verificados
- [ ] Uso de CPU normal
- [ ] Uso de RAM normal
- [ ] Backup automático configurado

## 📝 Documentação

- [ ] Credenciais anotadas em local seguro:
  - [ ] Superusuário Django
  - [ ] Senha do PostgreSQL
  - [ ] SECRET_KEY
  - [ ] URL do site
  - [ ] Acesso Easypanel

## 🎉 Finalização

- [ ] Cliente notificado
- [ ] Treinamento realizado (se necessário)
- [ ] Documentação entregue
- [ ] Sistema em produção!

---

## 📞 Contatos de Emergência

**Hostinger Suporte**: https://www.hostinger.com.br/contato
**Easypanel Docs**: https://easypanel.io/docs

## 🔄 Atualizações Futuras

Para atualizar o sistema:

```bash
# No seu computador
git add .
git commit -m "Atualização: descrição"
git push

# No Easypanel
# Clique em "Redeploy" no app
```

## 🐛 Se algo der errado

1. Verifique os logs no Easypanel
2. Confirme variáveis de ambiente
3. Teste conexão com banco
4. Verifique ALLOWED_HOSTS
5. Reinicie o app se necessário

---

**Data do Deploy**: ___/___/______
**Responsável**: _________________
**Status**: ⬜ Pendente | ⬜ Em Progresso | ⬜ Concluído
