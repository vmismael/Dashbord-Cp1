import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import kagglehub

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Portfólio | Vitor Montemor Ismael",
    page_icon="📊",
    layout="wide"
)

# ---------------- BARRA LATERAL ----------------
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/163008825?v=4", width=160)
    st.markdown("### Vitor Montemor Ismael")
    st.caption("Estudante de Engenharia de Software")
    
    pagina_selecionada = st.radio(
        "Navegação",
        ("Home", "Formação & Experiência", "Skills", "Análise de Dados"),
        key="navigation"
    )
    
    st.write("---")
    st.caption("Projeto CP1 - Dashboard Individual com Análise de Dados  - FIAP")   
    st.caption("© 2025 - Vitor Montemor Ismael")   

# ---------------- PÁGINAS ----------------
def pagina_home():
    st.title("Bem-vindo ao meu Portfólio")
    st.markdown("### Olá! Eu sou o **Vitor Montemor Ismael**")
    st.write("Aqui você encontrará informações sobre minha trajetória acadêmica, experiências, habilidades e alguns exemplos de análise de dados.")
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
    onde possa aplicar e expandir meus conhecimentos em **programação, engenharia de software e análise de dados**, 
    contribuindo para o desenvolvimento de soluções inovadoras e para a melhoria contínua dos processos da organização.   
    Tenho interesse em atuar em projetos de **transformação digital**, automação e inovação tecnológica, agregando valor 
    à equipe e à empresa, enquanto construo uma trajetória de crescimento profissional consistente.
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
        - **Design Thinking** - FIAP (2024)   
        - **Gestão Financeira de Empresas** - FIAP (2024)   
        - **Formação Full stack JavaScript** - ALURA (2024)   
        - **Formação Social e Sustentabilidade** - FIAP (2024)   
        - **Formação Python com Orientação a Objetos** - ALURA (2024)   
        """)

def pagina_skills():
    st.title("Competências e Habilidades")
    st.markdown("---")
    
    st.subheader("Tecnologias e Programação")
    st.caption("Principais linguagens e frameworks que utilizo")
    
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
    
    st.subheader("Ferramentas, Frameworks e Metodologias")
    st.caption("Ambientes, frameworks e conceitos que domino")
    
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
    st.caption("Níveis de proficiência")
    
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
    st.caption("Competências interpessoais e características profissionais")
    
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

# ---------------- PÁGINA DE ANÁLISE DE DADOS (COM CORREÇÕES) ----------------
def pagina_analise_dados():
    st.title("Análise de Dados - Airlines Flights Data")
    st.markdown("---")
    
    # Baixar dataset do Kaggle
    try:
        caminho_arquivo = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")
        caminho_csv = f"{caminho_arquivo}/airlines_flights_data.csv"
        dataframe = pd.read_csv(caminho_csv).sample(10000, random_state=42)
        st.success("✅ Dataset 'Airlines Flights Data' carregado com 10.000 amostras.")
    except Exception as erro:
        st.error(f"Erro ao carregar dataset: {erro}")
        return
    
    dataframe.columns = [coluna.strip() for coluna in dataframe.columns]
    
    # Identificar colunas principais
    coluna_preco = next((c for c in dataframe.columns if "price" in c.lower()), None)
    coluna_companhia = next((c for c in dataframe.columns if "airline" in c.lower()), None)
    
    if coluna_preco:
        dataframe[coluna_preco] = pd.to_numeric(dataframe[coluna_preco], errors="coerce")
    if coluna_companhia:
        dataframe[coluna_companhia] = dataframe[coluna_companhia].astype(str).str.strip()
    
    st.subheader("📄 Visão Geral do Dataset")
    st.dataframe(dataframe.head())
    
    secao_analise = st.selectbox(
        "Escolha a análise que deseja visualizar:",
        ["Estatísticas Descritivas", "Visualização de Dados", "Correlação", "Teste de Hipótese"]
    )

    # ---------------- ESTATÍSTICAS DESCRITIVAS ----------------
    if secao_analise == "Estatísticas Descritivas":
        st.subheader("📊 Estatísticas Descritivas")
        st.write(dataframe.describe())
        if coluna_preco:
            st.write(f"Média de Preços: {dataframe[coluna_preco].mean():.2f}, Mediana: {dataframe[coluna_preco].median():.2f}, Desvio: {dataframe[coluna_preco].std():.2f}")

    # ---------------- VISUALIZAÇÃO DE DADOS ----------------
    elif secao_analise == "Visualização de Dados":
        st.subheader("📈 Visualização de Dados")
        colunas_numericas = dataframe.select_dtypes(include=["int64","float64"]).columns.tolist()
        colunas_categoricas = dataframe.select_dtypes(include=["object"]).columns.tolist()
        
        tipo_visualizacao = st.radio("Tipo de visualização:", ["Numérica", "Categórica", "Comparativa", "Resumo por Companhia"])
        
        # Numérica
        if tipo_visualizacao == "Numérica" and colunas_numericas:
            coluna_selecionada = st.selectbox("Escolha uma variável numérica", colunas_numericas)
            figura, eixo = plt.subplots()
            sns.histplot(dataframe[coluna_selecionada].dropna(), kde=True, color="skyblue", ax=eixo)
            eixo.set_title(f"Distribuição de {coluna_selecionada}")
            eixo.set_xlabel(coluna_selecionada)
            eixo.set_ylabel("Frequência")
            st.pyplot(figura)
        
        # Categórica
        elif tipo_visualizacao == "Categórica" and colunas_categoricas:
            coluna_selecionada = st.selectbox("Escolha uma variável categórica", colunas_categoricas)
            figura, eixo = plt.subplots(figsize=(10,4))
            sns.countplot(x=dataframe[coluna_selecionada], order=dataframe[coluna_selecionada].value_counts().index, palette="Set2", ax=eixo)
            eixo.set_title(f"Contagem por {coluna_selecionada}")
            eixo.set_xlabel(coluna_selecionada.replace('_', ' ').title())
            eixo.set_ylabel("Contagem")
            plt.xticks(rotation=45)
            st.pyplot(figura)
        
        # Comparativa
        elif tipo_visualizacao == "Comparativa":
            if coluna_preco and coluna_companhia:
                df_comparacao = dataframe.dropna(subset=[coluna_preco, coluna_companhia])
                companhias_selecionadas = st.multiselect("Companhias para comparação", df_comparacao[coluna_companhia].unique(), default=df_comparacao[coluna_companhia].unique()[:3])
                if companhias_selecionadas:
                    df_selecionado = df_comparacao[df_comparacao[coluna_companhia].isin(companhias_selecionadas)]
                    figura, eixo = plt.subplots()
                    sns.boxplot(x=coluna_companhia, y=coluna_preco, data=df_selecionado, palette="Pastel1", ax=eixo)
                    eixo.set_title("Comparação de Preços por Companhia")
                    eixo.set_xlabel("Companhia")
                    eixo.set_ylabel("Preço")
                    plt.xticks(rotation=45)
                    st.pyplot(figura)
        
        # Resumo por Companhia
        elif tipo_visualizacao == "Resumo por Companhia":
            if coluna_preco and coluna_companhia:
                resumo_companhias = dataframe.groupby(coluna_companhia)[coluna_preco].agg(['mean','median','std']).reset_index()
                resumo_companhias.rename(columns={'mean':'Média','median':'Mediana','std':'Desvio Padrão', coluna_companhia:'Companhia'}, inplace=True)
                st.write("📋 Resumo estatístico por Companhia:")
                st.dataframe(resumo_companhias)
                figura, eixo = plt.subplots()
                sns.barplot(x='Companhia', y='Média', data=resumo_companhias, palette="Set2", ax=eixo)
                eixo.set_title("Preço Médio por Companhia")
                eixo.set_xlabel("Companhia")
                eixo.set_ylabel("Preço Médio")
                plt.xticks(rotation=45)
                st.pyplot(figura)

    # ---------------- CORRELAÇÃO ----------------
    elif secao_analise == "Correlação":
        st.subheader("📉 Correlação entre Variáveis Numéricas")
        matriz_correlacao = dataframe.select_dtypes(include=["int64","float64"]).corr()
        st.write(matriz_correlacao)
        figura, eixo = plt.subplots(figsize=(8,6))
        sns.heatmap(matriz_correlacao, annot=True, cmap="coolwarm", fmt=".2f", ax=eixo)
        eixo.set_title("Mapa de Correlação")
        st.pyplot(figura)

    # ---------------- TESTE DE HIPÓTESE ----------------
    elif secao_analise == "Teste de Hipótese":
        st.subheader("🧪 Teste de Hipótese - Diferença de Preço entre Companhias")
        if coluna_preco and coluna_companhia:
            df_teste = dataframe.dropna(subset=[coluna_preco, coluna_companhia])
            selecao_companhias = st.multiselect(
                "Selecione companhias para comparar (mínimo 2)",
                df_teste[coluna_companhia].unique(),
                default=df_teste[coluna_companhia].unique()[:2]
            )
            
            if len(selecao_companhias) >= 2:
                grupos_para_teste = [df_teste[df_teste[coluna_companhia]==c][coluna_preco] for c in selecao_companhias]
                
                # Teste ANOVA
                estatistica_f, valor_p = stats.f_oneway(*grupos_para_teste)
                
                st.write(f"**F-statístico (medida da diferença entre grupos):** {estatistica_f:.2f}")
                st.write(f"**p-valor (probabilidade da diferença ocorrer por acaso):** {valor_p:.5f}")
                
                st.markdown("""
                **Interpretação:**
                - Se o **p-valor < 0.05**, existe evidência estatística de que pelo menos uma companhia tem preço médio diferente.
                - Se o **p-valor ≥ 0.05**, não há evidência estatística de diferença significativa entre as companhias selecionadas.
                """)
                
                # Mostrar boxplot para visualização
                df_selecionado = df_teste[df_teste[coluna_companhia].isin(selecao_companhias)]
                figura, eixo = plt.subplots()
                sns.boxplot(x=coluna_companhia, y=coluna_preco, data=df_selecionado, palette="Pastel2", ax=eixo)
                eixo.set_title("Distribuição de Preços por Companhia")
                eixo.set_xlabel("Companhia")
                eixo.set_ylabel("Preço")
                plt.xticks(rotation=45)
                st.pyplot(figura)
            else:
                st.info("Selecione pelo menos duas companhias para realizar o teste.")
        else:
            st.warning("⚠️ O dataset não contém colunas de preço ou companhia aérea compatíveis para o teste de hipótese.")

# ---------------- ROTEAMENTO ----------------
if pagina_selecionada == "Home":
    pagina_home()
elif pagina_selecionada == "Formação & Experiência":
    pagina_formacao_experiencia()
elif pagina_selecionada == "Skills":
    pagina_skills()
elif pagina_selecionada == "Análise de Dados":
    pagina_analise_dados()