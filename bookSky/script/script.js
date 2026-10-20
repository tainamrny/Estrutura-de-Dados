const livro =  [
    { titulo: "A Metamorfose",
      autor: "Franz Kafka",
      categoria: "Ficção", status: "Disponível"},

    { titulo: "Dom Casmurro",
      autor: "Machado de Assis",
      categoria: "Romance", status: "Emprestado"},
]

const catalogo =
    document.querySelector('#catalogo');
const mensagem =
    document.querySelector('#mensagem');
const botao =
    document.querySelector('#carregar-api')

mensagem.textContent = "JavaScript Conectado!"

const tituloTeste =
    document.createElement('h3');

tituloTeste.className = 'livro-titulo';
tituloTeste.textContent = livro.titulo;

catalogo.append(tituloTeste);

const card = document.createElement('article');
card.className = 'livro';
const capa = document.createElement('div');
capa.className = 'livro-capa';
const textoCapa = document.createElement('span');
textoCapa.textContent = livro.titulo;
capa.append(textoCapa);
const info = document.createElement('div');
info.className = 'livro-info';
const titulo = document.createElement('h3');
titulo.className = 'livro-titulo';
titulo.textContent = livro.titulo;
const categoria = document.createElement('p')
categoria.className ='livro-categoria';
categoria.textContent = livro.categoria;

console.log(livro[0].titulo);
console.log(livro.lenght);