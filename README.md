# Documentação do Atualizador de Versão

Este código é um atualizador de aplicativos que utiliza a biblioteca `urllib` para verificar e baixar atualizações e a biblioteca `tqdm` para exibir uma barra de progresso no terminal enquanto baixa as atualizações.

## Requisitos

Você precisará das seguintes bibliotecas para executar este código:

- urllib
- tqdm

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```sh
pip install tqdm
```

## Como usar

O código é um script que, quando executado, verifica se há atualizações disponíveis para um aplicativo e, se houver, exibe informações sobre a atualização e pergunta ao usuário se deseja atualizar.

### Verificação de atualizações e atualização

O script verifica se há atualizações disponíveis comparando a versão atual do aplicativo (definida no código) com a versão mais recente disponível em um arquivo online. Se houver uma atualização disponível, o script exibe informações sobre a atualização e pergunta ao usuário se deseja atualizar. Se o usuário decidir atualizar, o aplicativo baixa a atualização, descompacta o arquivo e instala a atualização.

## Exemplo de uso

Antes de usar o atualizador, é necessário inserir os links corretos nos seguintes lugares do código:

- Link do RAW do arquivo contendo a versão: `versao = urllib.request.urlopen('Insira aqui o link').read().decode('utf8').splitlines()[0]`
- Link do RAW do arquivo contendo o changelog: `changelogs = urllib.request.urlopen('Insira aqui o link').read().decode('utf8')`
- Link do download no GitHub: `link = 'Insira aqui o link'`

Para usar o atualizador, siga estas etapas:

1. Salve o código em um arquivo chamado, por exemplo, `atualizador.py`.
2. Execute o script `atualizador.py`:

```sh
python atualizador.py
```

O script verificará se há atualizações disponíveis. Se houver uma atualização, exibirá informações sobre a atualização e perguntará se você deseja atualizar. Se você decidir atualizar, o aplicativo baixará e instalará a atualização.
