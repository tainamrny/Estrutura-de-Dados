# Entrelinhas — base da aula de JavaScript

O HTML e o CSS já estão prontos. Durante nossa aula, vamos escrever o JavaScript juntos: criar um objeto, organizar uma coleção, construir elementos HTML e consultar uma API.

## Estrutura

```text
projeto/
├── readme.md
├── index.html
├── style/
│   └── style.css
└── script/
    └── .gitkeep
```

`.gitkeep` é um arquivo vazio usado apenas para manter a pasta no GitHub. Não contém JavaScript. O Git não versiona diretórios vazios.

## Abrir

Baixe ou clone o repositório e abra `index.html` no navegador. Não há instalação de pacotes, dependências ou build. Para acompanhar as requisições em aula, abra o projeto com Live Server no VS Code.

O catálogo inicial tem oito cards escritos no HTML. O botão da API começa sem comportamento: sua integração será feita em sala.

## O que vamos construir

1. Criar `script/app.js` e descomentar sua tag `script` no `index.html`.
2. Criar um objeto com `titulo`, `autor`, `categoria` e `status`.
3. Selecionar `#catalogo` com `document.querySelector`.
4. Construir um card com `createElement`, `textContent`, `className` e `append`.
5. Colocar os livros em um array e renderizar a coleção com uma função e uma repetição.
6. Ligar o botão `#carregar-api` a uma função com `addEventListener`.
7. Fazer GET no JSONPlaceholder, interpretar o JSON e adaptar os dados para os cards.
8. Mostrar mensagens em `#mensagem` durante o carregamento e em caso de erro.

As classes usadas pelo card estão prontas no CSS: `livro`, `livro-capa`, `livro-info`, `livro-categoria`, `livro-titulo`, `livro-autor` e `status`.

## API de exercício

Usaremos `https://jsonplaceholder.typicode.com/posts?_limit=8`.

O [JSONPlaceholder](https://jsonplaceholder.typicode.com/) oferece **posts de teste**, com campos como `title`, `body` e `userId`. Não é uma API de biblioteca. Na aula, cada post será adaptado para um card de demonstração, claramente identificado. O número `userId` será usado como identificador de autor simulado, sem representar uma pessoa real. Esses exemplos não têm disponibilidade de empréstimo.

## Resultado esperado

O visual funciona desde o início. Ao terminar o JavaScript, os oito livros locais serão gerados a partir de dados. O botão buscará exemplos na API e atualizará os cards, sem recarregar a página. Se a consulta falhar, a tela mostrará uma mensagem e manterá os cards anteriores.

Busca por título e filtros ficam como possíveis próximos exercícios.

## GitHub

Publique o conteúdo **desta pasta** como raiz do repositório. Ela contém apenas a base da aula e não traz a solução JavaScript. No GitHub Pages, o `index.html` já abre com o layout e os oito cards estáticos.

## Créditos

Projeto didático de Modelagem de Sites Básicos — Prof. Matheus Ribeiro Ávila.

Identidade visual, resumos e capas tipográficas autorais em HTML/CSS. Pequenos Recomeços é uma obra fictícia criada para a atividade. As categorias são escolhas didáticas. Os status locais são ilustrativos, sem empréstimo real.
