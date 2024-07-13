<h1>Etl com Python, dbt-core e MySQL</h1>
<h2>Descrição do Projeto</h2>
<p>
    Este projeto tem como objetivo a criação de um data warehouse para análise de commodities usando dbt (data build tool) e MySQL. Ele inclui a extração de dados de preços de commodities e movimentações de commodities, transformação dos dados usando modelos dbt, e carregamento dos dados transformados em um banco de dados MySQL.
</p>


<h2>Pré-requisitos</h2>
<ul>
    <li>Python 3.8 ou superior</li>
    <li>pip</li>
    <li>MySQL</li>
    <li>dbt</li>
</ul>

<h2>Configuração do Ambiente</h2>

<h3>Instalação de Dependências</h3>
<ol>
    <li>Clone o repositório:
        <pre>
git clone &lt;https://github.com/ArthurCoutinho15/Commodities-Python-dbt&gt;
cd ETL-dbt
        </pre>
    </li>
    <li>Crie um ambiente virtual e instale as dependências:
        <pre>
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
        </pre>
    </li>
</ol>

<h3>Configuração do dbt</h3>
<ol>
    <li>Inicialize o projeto dbt:
        <pre>dbt init datawarehouse</pre>
    </li>
    <li>Configure o arquivo <code>profiles.yml</code>:
        <pre>
datawarehouse:
  target: dev
  outputs:
    dev:
      type: mysql
      server: localhost
      port: 3306
      database: commodities
      schema: public
      username: username
      password: password
      driver: MySQL ODBC 8.0 ANSI Driver
        </pre>
    </li>
</ol>

<h3>Configuração do Banco de Dados MySQL</h3>
<ol>
    <li>Crie um banco de dados chamado <code>commodities</code> no MySQL.</li>
    <li>Crie as tabelas necessárias:
        <pre>
CREATE TABLE movimentacao_commodities (
    date DATE,
    symbol VARCHAR(10),
    action VARCHAR(10),
    quantity INT
);

CREATE TABLE commodities (
    Date DATE,
    Close DECIMAL(10, 2),
    simbolo VARCHAR(10)
);
        </pre>
    </li>
</ol>

<h2>Execução do Projeto</h2>
<ol>
    <li>Execute as seeds para carregar os dados do iniciais:
        <pre>dbt seed</pre>
    </li>
    <li>Execute os modelos dbt:
        <pre>dbt run</pre>
    </li>
    <li>Verifique os resultados no MySQL:
        <pre>
SELECT * FROM public.dm_commodities;
        </pre>
    </li>
</ol>

<h2>Estrutura dos Modelos dbt</h2>

<h3>staging</h3>
<ul>
    <li><code>stg_commodities.sql</code>: Modelo de staging para os dados de commodities.</li>
    <li><code>st_movimentacao_commodities.sql</code>: Modelo de staging para os dados de movimentação de commodities.</li>
</ul>

<h3>datamart</h3>
<ul>
    <li><code>dm_commodities.sql</code>: Modelo de data mart que junta os dados de commodities e movimentações, calculando valores e ganhos.</li>
</ul>
<img src='https://github.com/ArthurCoutinho15/Commodities-Python-dbt/blob/main/img/Captura%20de%20tela%202024-07-13%20162123.png'>
<h2>Utilização do Streamlit</h2>
<p>
    O Streamlit é utilizado para criar um dashboard interativo que mostra os dados das commodities e suas transações.
</p>

<h3>Execução do Streamlit</h3>
<ol>
    <li>Certifique-se de que o ambiente virtual está ativado.</li>
    <li>Execute o comando para iniciar o Streamlit:
        <pre>
streamlit run script.py
        </pre>
        <p>Substitua <code>script.py</code> pelo nome do arquivo Python que contém o código acima.</p>
    </li>
    <li>Abra o navegador e acesse <a href="http://localhost:8501">http://localhost:8501</a> para visualizar o dashboard.</li>
</ol>





