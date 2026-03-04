import streamlit as st

st.set_page_config(
    page_title="Portfólio | Vitor Montemor Ismael",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    try:
        st.image("WhatsApp Image 2026-03-04 at 16.59.02.jpeg", width=200)
    except:
        st.error("⚠️ Erro ao carregar imagem.")
        
    st.markdown("### Vitor Montemor Ismael")
    st.caption("Estudante de Engenharia de Software")
    
    pagina_selecionada = st.radio(
        "Navegação",
        ("Home", "Formação & Experiência", "Skills"),
        key="navigation"
    )
    
    st.write("---")
    st.caption("© 2026 - Vitor Montemor Ismael")   

def pagina_home():
    st.title("Bem-vindo ao meu Portfólio")
    st.markdown("### Olá! Eu sou o **Vitor Montemor Ismael**")
    st.write("Aqui você encontrará informações sobre minha trajetória acadêmica, experiências e competências técnicas no desenvolvimento de software.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Contato")
        st.write("📍 São Paulo, Aclimação")
        st.write("📧 vitor.montemor.ismael@gmail.com")
        st.write("📞 +55 (19) 98105-7925")
    with col2:
        st.subheader("Presença Online")
        st.markdown("[GitHub](https://github.com/vmismael)")
    
    st.markdown("---")
    st.subheader("Objetivo Profissional")
    st.info("""
    Busco uma oportunidade desafiadora como **Analista Júnior, Trainee ou Estagiário em TI**, 
    onde possa aplicar e expandir meus conhecimentos em **programação e engenharia de software**, 
    contribuindo para o desenvolvimento de soluções inovadoras e para a melhoria contínua dos processos da organização.   
    Tenho interesse em atuar em projetos de **transformação digital**, automação e inovação tecnológica.
    """)

def pagina_formacao_experiencia():
    st.title("Formação Acadêmica e Experiência")
    st.markdown("---")
    
    st.subheader("Formação Acadêmica")
    st.markdown("- **Engenharia de Software** - FIAP *(Cursando)*")   
    st.markdown("- **EB-24 - Intensive 24 Business** - LSI Auckland *(Jan/2024)*")   
    st.markdown("- **Curso de Francês** - France Langue, Paris *(Jan/2023)*")   
    st.markdown("- **Business Course** - Cats Academy Boston *(Dez/2019)*")   
    st.markdown("- **Ensino Médio** - Koelle *(Dez/2018)*")   
    
    st.markdown("---")
    st.subheader("Cursos de Aprimoramento")
    with st.expander("Ver cursos concluídos"):
        st.markdown("""
        - **Design Thinking** (2024)   
        - **Gestão Financeira de Empresas** (2024)   
        - **Formação Full stack JavaScript** (2024)   
        - **Formação Social e Sustentabilidade** (2024)   
        - **Formação Python com Orientação a Objetos** (2024)   
        """)

def pagina_skills():
    st.title("Competências e Habilidades")
    st.markdown("---")
    
    st.subheader("Tecnologias e Programação")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Python**")
        st.progress(85)
        st.write("**Java**")
        st.progress(75)
        st.write("**JavaScript**")
        st.progress(70)
    with col2:
        st.write("**C**")
        st.progress(60)
        st.write("**HTML & CSS**")
        st.progress(80)
        st.write("**SQL (Oracle / SQLite)**")
        st.progress(65)
    
    st.markdown("---")
    st.subheader("Ferramentas e Metodologias")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("Frameworks & Bibliotecas")
        st.markdown("- React.js\n- Node.js")
        st.success("Controle de Versão")
        st.markdown("- Git & GitHub")
    with col2:
        st.success("Ferramentas & IDEs")
        st.markdown("- VSCode, IntelliJ, Figma")
        st.success("Conceitos & Metodologias")
        st.markdown("- Programação Orientada a Objetos\n- Design Thinking\n- Metodologias Ágeis (Scrum)")
    
    st.markdown("---")
    st.subheader("Idiomas")
    
    st.write("**Português (Nativo)**")
    st.progress(100)
    st.write("**Inglês (Avançado - C1)**")
    st.progress(85)
    st.write("**Espanhol (Intermediário)**")
    st.progress(60)
    st.write("**Francês (Básico)**")
    st.progress(40)
    
    st.markdown("---")
    st.subheader("Soft Skills")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("Proatividade")
    with c2:
        st.info("Criatividade")
    with c3:
        st.info("Responsabilidade")
    
    c4, c5, c6 = st.columns(3)
    with c4:
        st.info("Disciplina")
    with c5:
        st.info("Respeito")
    with c6:
        st.info("Trabalho em equipe")

if pagina_selecionada == "Home":
    pagina_home()
elif pagina_selecionada == "Formação & Experiência":
    pagina_formacao_experiencia()
elif pagina_selecionada == "Skills":
    pagina_skills()
