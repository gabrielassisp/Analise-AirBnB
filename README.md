# 📊 Análise Exploratória de Dados Airbnb

Bem-vindo(a) ao repositório do projeto de Análise Exploratória de Dados do Airbnb!

Este projeto tem como objetivo principal extrair insights valiosos de um dataset de anúncios do Airbnb, focando em padrões de preços, disponibilidade e características dos imóveis. Através de análises estatísticas e visualizações de dados, buscamos entender melhor o comportamento do mercado de aluguel por temporada.

## 🎯 Objetivo do Projeto

Realizar uma análise exploratória aprofundada nos dados de imóveis do Airbnb para identificar tendências, relações e padrões que possam fornecer inteligência de negócio. O foco está em:
* Preços médios por localização e tipo de imóvel.
* Disponibilidade dos imóveis ao longo do ano.
* Correlações entre diferentes variáveis (e.g., preço e avaliações).
* Perfil predominante das acomodações oferecidas.

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Python:** Linguagem de programação principal para análise de dados.
    * **Pandas:** Para manipulação e tratamento de dados.
    * **Matplotlib:** Para criação de gráficos estáticos.
    * **Seaborn:** Para visualizações estatísticas atraentes e informativas.
* **Jupyter Notebook / Ambiente de Desenvolvimento Integrado (IDE):** Para o desenvolvimento e execução do código (e.g., VS Code).

## 🗃️ Base de Dados

O dataset utilizado neste projeto é o `listings.csv`, contendo informações detalhadas sobre os anúncios do Airbnb, incluindo:
* `price`: Preço por noite.
* `neighbourhood`: Bairro do imóvel.
* `room_type`: Tipo de acomodação (e.g., casa/apartamento inteiro, quarto privado).
* `minimum_nights`: Número mínimo de noites para reserva.
* `reviews_per_month`: Média de avaliações por mês.
* `availability_365`: Dias disponíveis no ano.
* E muitas outras colunas relevantes para a análise.

**Fonte:** Os dados foram obtidos do **Inside Airbnb**, uma iniciativa que fornece dados abertos sobre listagens do Airbnb em diversas cidades ao redor do mundo.
* **Link para a fonte dos dados:** [https://insideairbnb.com/get-the-data.html](https://insideairbnb.com/get-the-data.html)
* **Cidade utilizada na análise: Rio de Janeiro

## 🚀 Etapas da Análise

O projeto seguiu as seguintes etapas principais:

1.  **Limpeza e Preparação dos Dados:**
    * Remoção de registros com preços inválidos (zero).
    * Tratamento de valores ausentes, como o preenchimento de `reviews_per_month` com 0.
    * Conversão de tipos de dados (e.g., `last_review` para formato de data).
    * Renomeação de colunas para maior clareza e padronização em português.
2.  **Análise Exploratória e Geração de Insights:**
    * Segmentação e agrupamento dos dados para responder a perguntas de negócio relevantes.
    * Criação de visualizações de dados diversas (gráficos de barras, dispersão, histogramas, boxplots) para ilustrar os padrões encontrados.

## 💡 Principais Insights e Descobertas

A análise dos dados do Airbnb revelou os seguintes insights chave:

* **Disparidade de Preços por Bairro:** Identificou-se uma significativa variação nos preços médios entre diferentes bairros, destacando regiões premium e outras mais acessíveis, o que pode guiar decisões estratégicas de precificação e investimento.
    * ![Gráfico Top 10 Bairros Mais Caros](link/para/sua/imagem/top_10_bairros_caros.png)
    * ![Gráfico Top 10 Bairros Mais Baratos](link/para/sua/imagem/top_10_bairros_baratos.png)
* **Pouca Correlação Preço-Avaliações:** A análise demonstrou uma relação fraca entre o preço do imóvel e o número de avaliações, sugerindo que um custo mais elevado não garante um volume maior de reviews, indicando que outros fatores influenciam a reputação.
    * ![Gráfico Correlação Preço vs Reviews](link/para/sua/imagem/correlacao_preco_reviews.png)
* **Alta Disponibilidade Predominante:** A maioria dos imóveis na base de dados apresenta alta disponibilidade anual (próximo a 365 dias), indicando uma oferta considerável de aluguéis de longo prazo ou imóveis dedicados exclusivamente à plataforma.
    * ![Gráfico Distribuição Disponibilidade](link/para/sua/imagem/distribuicao_disponibilidade.png)
* **Diferenciais em Imóveis de Alto Custo:** Os imóveis classificados como mais caros (top 5% do preço) não necessariamente se destacam em volume de reviews ou disponibilidade, apontando que seu valor premium pode residir em outros atributos não explorados pelo dataset (e.g., luxo, amenidades específicas, localização).
    * ![Gráfico Boxplot Disponibilidade Mais Caros](link/para/sua/imagem/boxplot_disponibilidade_caros.png)
* **Domínio de "Entire Home/Apt":** A maior parte da oferta no dataset consiste em aluguéis de casas/apartamentos inteiros, seguidos por quartos privados, definindo o perfil predominante das acomodações na plataforma e o foco do mercado.
    * ![Gráfico Distribuição Tipo de Acomodação](link/para/sua/imagem/distribuicao_tipo_acomodacao.png)

**(Lembre-se de substituir `link/para/sua/imagem/*.png` pelos caminhos reais das imagens dos seus gráficos. Recomendo criar uma pasta `images/` ou `plots/` no seu repositório para guardá-las.)**

## ⚙️ Como Executar o Código

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/airbnb_data_analysis.git](https://github.com/SeuUsuario/airbnb_data_analysis.git)
    cd airbnb_data_analysis
    ```
2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install pandas matplotlib seaborn
    ```
4.  **Baixe o dataset:**
    * Acesse o link [https://insideairbnb.com/get-the-data.html](https://insideairbnb.com/get-the-data.html).
    * Selecione a cidade desejada (ex: **[Nome da Cidade que você usou]**) e baixe o arquivo `listings.csv`.
    * Coloque o arquivo `listings.csv` na pasta `data/` dentro do diretório do projeto.
        **(Ou atualize o caminho do arquivo no script `airbnb_analysis.py`, se você o colocou em outro lugar).**
5.  **Execute o script Python (ou o Jupyter Notebook):**
    * Se estiver usando o script `.py`:
        ```bash
        python airbnb_analysis.py
        ```
    * Se estiver usando um Jupyter Notebook (`.ipynb`), inicie o Jupyter e abra o notebook:
        ```bash
        jupyter notebook
        ```

## 🤝 Contato

Conecte-se comigo!

* **Gabriel Assis Pereira**
* www.linkedin.com/in/gabriel-assis-pereira-858b24280
* https://github.com/gabrielassisp

---
