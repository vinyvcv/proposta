import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------- CONFIGURAÇÃO DA PÁGINA ----------------------
st.set_page_config(
    page_title="Proposta de Manutenção e Evolução Mensal",
    page_icon="🛠️",
    layout="wide"
)

# ---------------------- CABEÇALHO ----------------------
st.title("🛠️ Proposta de Manutenção e Evolução Mensal")
st.subheader("Projeto: Sistema de Vistorias Online (App + Painel + Integrações)")
st.write("**Responsável técnico:** Vinicius Cavalcante Viana")

st.markdown("---")

# ---------------------- MENU INTERATIVO ----------------------
with st.sidebar:
    selected = option_menu(
        "Planos de Manutenção",
        ["📘 Escopo de Responsabilidade", "🔹 Plano Básico", "🔹 Plano Intermediário", "🔹 Plano Avançado", "ℹ️ Observações"],
        icons=["list-task", "star", "trophy", "gem", "info-circle"],
        menu_icon="tools",
        default_index=0
    )

# ---------------------- CONTEÚDOS ----------------------
if selected == "📘 Escopo de Responsabilidade":
    st.header("📘 Escopo Técnico do Sistema Atual")
    st.markdown("""
    O sistema de **Vistorias Online** é composto por múltiplos módulos, integrações e camadas de infraestrutura.  
    Abaixo está um detalhamento técnico do que já está em produção e sob minha responsabilidade:

    ## 🌐 Infraestrutura e Hospedagem
    - **Servidor Hostinger** rodando aplicações Node.js (backends e APIs).  
    - **Banco de Dados SQL Server** hospedado em instância dedicada, armazenando dados de:
      - Usuários, veículos, vistorias, fotos, vídeos, laudos, selos.  
      - Controle de acessos, permissões e tokens de autenticação.  
      - Logs de auditoria e histórico de operações.  
    - **Armazenamento em AWS S3**:
      - Fotos de vistorias (upload pelo app).  
      - Vídeos de vistorias.  
      - Arquivos de laudos e selos em PDF.  
    - Monitoramento de disponibilidade, performance e segurança de todos os serviços.

    ## 📱 Aplicações (Quasar + Node.js)
    ### 1. **App Cliente (Quasar + Node.js)**
    - Cadastro de usuários (com validação de CPF e e-mail).  
    - Upload de fotos da vistoria (enviadas direto para S3).  
    - Integração com **Mercado Pago API** para pagamentos (checkout, notificações, webhooks).  
    - Consulta de placa veicular via API externa.  
    - Consulta de CEP (endereço automático).  
    - Recebimento de notificações por WhatsApp e e-mail (boas-vindas, confirmação, laudos e selos).  
    - Tokens de redefinição de senha gerados e enviados por **Amazon SES**.  

    ### 2. **App Vistoriadores (Quasar + Node.js)**
    - Login seguro com tokens.  
    - Acesso às fotos enviadas pelo cliente (via S3).  
    - Análise técnica das imagens para validar ou reprovar itens.  
    - Conclusão do **laudo digital** a partir das evidências enviadas.  
    - Integração com 2 APIs externas:  
        - **Envio do laudo** para empresa responsável.  
        - **Recebimento do laudo** de volta para armazenar no sistema.  
    - Emissão e envio automático de **PDFs de laudo e selo digital**.  

    ## 🤖 Integrações e Automação
    - **Mercado Pago** → Processamento de pagamentos e notificações.  
    - **API de Placa** → Identificação automática de veículos.  
    - **API de CEP** → Preenchimento automático de endereço.  
    - **APIs de Laudo** → Envio e retorno dos laudos oficiais.  
    - **WhatsApp Bot**:
      - Atendimento automatizado para dúvidas comuns.  
      - Envio de laudos e selos assim que ficam prontos.  
      - Fluxo de boas-vindas para novos clientes.  
    - **Amazon SES** → E-mails automáticos:
      - Boas-vindas no cadastro.  
      - Redefinição de senha.  
      - Confirmações de laudos emitidos.  

    ## 📊 Relatórios e Gestão
    - SQL Server armazena dados de auditoria, métricas de uso e históricos de vistorias.  
    - Relatórios técnicos e administrativos exportáveis.  
    - Logs de erros e eventos integrados para análise de falhas.  

    ---
    Esse é o **escopo técnico atual**, englobando infraestrutura, aplicações, integrações e automações que garantem o funcionamento do sistema de vistorias digitais.
    """)

elif selected == "🔹 Plano Básico":
    st.header("🔹 Plano Básico – R$ 3.000/mês")
    st.success("""
    ### O que está incluso no Plano Básico
    - Manutenção **corretiva** do sistema completo (apps, APIs e banco SQL Server).  
    - **Infraestrutura:** monitoramento contínuo da Hostinger e AWS S3.  
    - **Banco de Dados:** suporte ao SQL Server (usuários, veículos, vistorias, fotos, vídeos, laudos e selos).  
    - **Aplicações (Quasar + Node.js):**
      - App Cliente: cadastro, envio de fotos, integração com Mercado Pago, APIs de Placa e CEP, redefinição de senha via SES.  
      - App Vistoriadores: análise de fotos, emissão de laudos, envio e recebimento via APIs.  
    - **Integrações:** Mercado Pago, Placa, CEP, APIs de Laudo.  
    - **WhatsApp Bot:** ativo para dúvidas básicas e envio de laudos/selos.  
    - **Amazon SES:** envio de e-mails automáticos (boas-vindas, redefinição de senha, notificações).  
    - Correções de bugs e falhas de integração.  
    - Atendimento de até **15 horas/mês** para ajustes e pequenas melhorias.  
    - Suporte em horário comercial (segunda a sexta).  
    - **Atendimento eventual aos sábados ou domingos em casos de urgência, desde que haja notificação prévia de 1 dia.**  
    """)


elif selected == "🔹 Plano Intermediário":
    st.header("🔹 Plano Intermediário – R$ 5.000/mês")
    st.info("""
    ### O que está incluso no Plano Intermediário
    Inclui **tudo do Plano Básico**, mais:
    - Atendimento de até **30 horas/mês** para evoluções e novas funcionalidades.  
    - **Atualizações preventivas:** bibliotecas Node.js, dependências Quasar, pacotes de segurança.  
    - **Infraestrutura:** ajustes pró-ativos em Hostinger e AWS S3 para otimizar performance.  
    - **Banco de Dados:** melhorias em consultas SQL Server e relatórios administrativos.  
    - **Aplicações (Quasar + Node.js):**
      - Evolução de telas, relatórios e fluxos do App Cliente e App Vistoriadores.  
      - Ajustes em integrações de laudos e fluxo de pagamentos via Mercado Pago.  
    - **WhatsApp Bot:** manutenção evolutiva para fluxos mais inteligentes e customizados.  
    - **APIs externas:** revisões contínuas de integração para evitar quebras.  
    - Prioridade em chamados críticos.  
    - Suporte emergencial fora do horário comercial (plantão).  
    """)

elif selected == "🔹 Plano Avançado":
    st.header("🔹 Plano Avançado – R$ 7.000/mês")
    st.warning("""
    ### O que está incluso no Plano Avançado
    Inclui **tudo do Plano Intermediário**, mais:
    - Atendimento de até **50 horas/mês** para melhorias, evoluções robustas e novas features.  
    - **Evoluções planejadas:** desenvolvimento de novos módulos, relatórios estratégicos e integrações adicionais.  
    - **Infraestrutura:** monitoramento ativo 24/7 de servidores, logs e integrações (Hostinger + S3).  
    - **Banco de Dados:** otimização contínua de queries no SQL Server e relatórios estratégicos.  
    - **Aplicações (Quasar + Node.js):**
      - Novas telas, dashboards e recursos de análise para clientes e vistoriadores.  
      - Implementação de funcionalidades complexas sob demanda.  
    - **WhatsApp Bot:** evolução para agente virtual mais completo (fluxos de dúvidas, notificações personalizadas, relatórios).  
    - **Governança:** reuniões mensais de alinhamento estratégico e definição de roadmap de produto.  
    - Garantia de **resposta imediata** em incidentes críticos.  
    """)

elif selected == "ℹ️ Observações":
    st.header("Observações Importantes")
    st.markdown("""
    - Horas excedentes: serão cobradas à parte, no valor de **R$120/hora**.  
    - Evoluções grandes (novos módulos, integrações adicionais, refatorações completas) serão orçadas como projetos independentes.  
    - Os valores **não incluem custos de infraestrutura** (Hostinger, AWS S3, APIs de terceiros, Mercado Pago etc.), que permanecem sob responsabilidade do cliente.  
    """)

# ---------------------- RODAPÉ ----------------------
st.markdown("---")
st.caption("© 2025 - Proposta de Manutenção • Desenvolvido por Vinicius Cavalcante Viana")
