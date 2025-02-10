Projeto: Baixar Imagens e Organizar por Tombamento
Objetivo
Este script foi desenvolvido como parte de um projeto de estágio na área de desenvolvimento com o objetivo de automatizar o processo de download de imagens hospedadas no Google Drive. Ele organiza as imagens em pastas específicas, nomeadas de acordo com o número de tombamento. O processo de organização visa facilitar o gerenciamento e a localização das imagens relacionadas a diferentes objetos ou arquivos na empresa.

A automação utiliza um arquivo Excel para determinar os links das imagens e a estrutura de pastas onde as imagens serão armazenadas. O script foi pensado para ser uma solução simples e eficaz, especialmente em ambientes corporativos onde muitos documentos e imagens precisam ser organizados.

Funcionamento
Entrada de Dados:

O script começa com a leitura de um arquivo Excel (planilha_path) que contém os links para as imagens.
O arquivo deve ter uma coluna chamada "TOMBAMENTO", que é usada para nomear as pastas onde as imagens serão salvas.
Outras colunas (como "", "", "" ) contêm os links do Google Drive para as imagens correspondentes.
Processamento:

Para cada linha do arquivo Excel:
O código verifica o link do Google Drive para cada coluna de imagem.
Se o link for válido, o script extrai o ID do arquivo do Google Drive (usando a função extrair_id_do_link).
Uma pasta específica para o "tombamento" é criada (caso ainda não exista).
As imagens são baixadas da URL do Google Drive e salvas com o nome correspondente à coluna de imagem (por exemplo, TOM123456.(NOME DA COLUNA ESCOLHIDA).png).
Estrutura de Pastas:

O script cria uma estrutura de pastas onde cada "tombamento" é representado por uma pasta numerada.
As imagens baixadas para cada tombamento são salvas dentro da respectiva pasta.
Baixando as Imagens:

O script utiliza a biblioteca requests para fazer o download das imagens diretamente dos links fornecidos no Google Drive.
Em caso de erro durante o download (por exemplo, se o link estiver quebrado), o script exibirá uma mensagem de erro.
Requisitos
Bibliotecas Python: O script requer as seguintes bibliotecas:

os: Para manipulação de arquivos e diretórios.
pandas: Para ler e processar o arquivo Excel.
requests: Para realizar o download das imagens da web.
openpyxl: Para garantir a leitura adequada de arquivos Excel (.xlsx).
Arquivo Excel: O arquivo Excel deve ter uma coluna chamada "TOMBAMENTO" e outras colunas (por exemplo, "Item", "Plaqueta_Atual", etc.) com os links das imagens hospedadas no Google Drive.

Configurações
Caminho da Planilha: Defina o caminho completo para o arquivo Excel que contém os dados (modifique planilha_path).

Pasta de Destino: Defina o caminho onde as imagens serão salvas (modifique pasta_destino).

Como Usar
Prepare o arquivo Excel com os links das imagens no formato adequado.
Atualize o caminho para o arquivo Excel e a pasta de destino no código.
Execute o script Python. O processo de download será iniciado automaticamente, e as imagens serão organizadas em pastas conforme os "tombamentos".

Considerações Finais
O script facilita o gerenciamento de imagens associadas a diferentes "tombamentos", baixando-as automaticamente de links do Google Drive e organizando-as em pastas estruturadas.
O processo de erro (como links inválidos ou indisponíveis) é tratado para evitar que o script falhe abruptamente.
