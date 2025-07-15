🚀 Projeto de Demonstração: Couchbase com Python

Este projeto é uma demonstração prática de como utilizar o Couchbase, um banco de dados NoSQL multi-modelo, com Python para gerenciar um simples catálogo de produtos. O objetivo é apresentar os conceitos básicos, a configuração do ambiente e a execução de operações fundamentais como inserção, consulta e atualização de dados.

📖 O que este projeto faz?

O script app_couchbase.py se conecta a uma instância local do Couchbase (rodando via Docker) e executa as seguintes ações:

Insere ou atualiza dois produtos no catálogo com dados em formato JSON.

Consulta o estoque de um dos produtos antes de uma atualização.

Simula uma venda, atualizando o estoque de forma otimizada com uma operação de sub-documento.

Consulta novamente o estoque do produto para provar que a alteração foi efetivada.

🛠️ Pré-requisitos

Para executar este projeto na sua máquina, você precisará ter os seguintes softwares instalados:

Docker Desktop

Usado para criar e gerenciar o contêiner do banco de dados Couchbase.

Faça o download aqui

Python 3.9

A biblioteca do Couchbase usada neste projeto tem melhor compatibilidade com esta versão do Python.

Faça o download do Python 3.9.13 (Windows Installer 64-bit)

Durante a instalação, marque a caixa "Add Python 3.9 to PATH".

⚙️ Instalação e Configuração

Siga estes passos para deixar o ambiente pronto para execução.

1. Clone o Repositório

git clone https://github.com/arthurv10/Trabalho-Final---NOSQL.git
cd Trabalho-Final---NOSQL

2. Inicie o Servidor Couchbase

Com o Docker Desktop já rodando, abra um terminal (PowerShell, CMD, etc.) e execute:

docker run -d --name db-couchbase -p 8091-8094:8091-8094 -p 11210:11210 couchbase

Aguarde um ou dois minutos para o serviço iniciar completamente.

3. Configure o Couchbase pela Primeira Vez

Esta etapa só precisa ser feita uma vez:

Abra seu navegador e acesse http://localhost:8091

Clique em "Setup New Cluster"

Defina um nome de usuário como Administrador e uma senha como 123456

Clique em "Accept Terms" e finalize a configuração com as opções padrão

Na interface principal, vá para a aba "Buckets" e clique em "ADD BUCKET"

Dê o nome ao bucket de trabalho_final e clique em "ADD BUCKET"

4. Instale as Dependências do Python

Crie um arquivo chamado requirements.txt na pasta do seu projeto com o seguinte conteúdo:

couchbase

Em seguida, instale a dependência:

py -3.9 -m pip install -r requirements.txt

▶️ Executando a Aplicação

No terminal, dentro da pasta do projeto, rode:

py -3.9 app_couchbase.py

Você verá no terminal a saída do programa, mostrando a conexão bem-sucedida e a demonstração de "antes e depois" da atualização do estoque. Também é possível verificar os dados diretamente na interface web do Couchbase em http://localhost:8091.

Exemplo de Saída no Terminal

✅ Conexão com Couchbase estabelecida!

📝 Inserindo/Resetando produtos no catálogo...
   - Produtos inseridos com sucesso.

===== DEMONSTRAÇÃO DA ATUALIZAÇÃO =====
📈 ANTES: O estoque do notebook é: 80

🔄 Simulando uma venda e atualizando o estoque...
   - Operação de atualização enviada.
📉 DEPOIS: O novo estoque do notebook é: 75
==========================================
