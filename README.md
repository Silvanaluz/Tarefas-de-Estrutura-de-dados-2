Índice Remissivo utilizando Árvore AVL

Introdução

Este trabalho tem como objetivo a implementação de um índice remissivo a partir de um arquivo de texto, utilizando como estrutura de dados principal a Árvore AVL. O problema consiste em armazenar palavras extraídas de um texto e associá-las às linhas em que aparecem, permitindo uma organização eficiente e balanceada dos dados.

Para resolver o problema, foi feita a leitura de um arquivo `.txt`, no qual cada linha é processada individualmente. As palavras são normalizadas (convertidas para letras minúsculas e sem pontuação) e inseridas na árvore AVL. Cada nó da árvore representa uma palavra distinta, armazenando também um conjunto de números de linhas onde essa palavra ocorre.

A escolha da Árvore AVL se justifica pela necessidade de manter a árvore sempre balanceada, garantindo eficiência nas operações de inserção e busca, mesmo para arquivos de texto extensos. Dessa forma, o índice remissivo é construído de maneira organizada, evitando degradação de desempenho.


Estruturas de Dados Utilizadas

- Árvore AVL: estrutura principal para armazenar as palavras do texto de forma ordenada e balanceada.
- Conjunto (set): utilizado para armazenar as linhas em que cada palavra aparece, evitando duplicidades.
- Recursão: aplicada no processo de inserção e balanceamento da árvore.

## Documentação do Código

### Classe `No`

A classe `No` representa cada nó da árvore AVL. Ela contém:
- `palavra`: a palavra armazenada no nó.
- `linhas`: conjunto de números das linhas em que a palavra aparece.
- `esquerda` e `direita`: referências para os filhos do nó.
- `altura`: altura do nó, utilizada no cálculo do balanceamento da árvore.

Cada nó é criado quando uma nova palavra é encontrada no texto.

Classe `AVL`

A classe `AVL` é responsável por gerenciar toda a árvore e implementar suas operações.

Construtor `__init__`
Inicializa a árvore com:
- raiz vazia
- contador de rotações
- contador de palavras inseridas
- contador de palavras descartadas (repetidas na mesma linha)

Método `altura(no)`
Retorna a altura de um nó. Caso o nó seja nulo, retorna zero.

Método `fator_balanceamento(no)`
Calcula a diferença entre a altura da subárvore esquerda e direita, permitindo identificar se o nó está balanceado.

Método `rotacao_direita(y)`
Executa uma rotação simples à direita para corrigir desbalanceamentos do tipo esquerda-esquerda.

Método `rotacao_esquerda(x)`
Executa uma rotação simples à esquerda para corrigir desbalanceamentos do tipo direita-direita.

Método `inserir(no, palavra, linha)`
Responsável por inserir uma palavra na árvore:
- Se o nó for nulo, cria um novo nó.
- Se a palavra já existir, adiciona o número da linha ao conjunto.
- Caso contrário, insere recursivamente à esquerda ou à direita.
- Após a inserção, atualiza a altura do nó e aplica rotações quando necessário.

Esse método garante que a árvore permaneça balanceada após cada inserção.


Exemplos de Uso

Exemplo de entrada (arquivo texto)
A sabedoria clama nas ruas
A inteligência levanta a sua voz


Código para processar o texto

avl = AVL()
avl.raiz = avl.inserir(avl.raiz, "sabedoria", 1)
avl.raiz = avl.inserir(avl.raiz, "inteligência", 2)

saída esperada
Exemplo de entPalavra: sabedoria → Linhas: {1}
Palavra: inteligência → Linhas: {2}
Total de rotações: 0
rada (arquivo texto)
Esses resultados demonstram a correta associação das palavras às linhas correspondentes, bem como o funcionamento do balanceamento automático da árvore.

Observações Finais

O código foi testado com diferentes arquivos de texto para garantir o correto funcionamento das operações de inserção e balanceamento da árvore AVL. Foram adotadas boas práticas de programação, como modularização, uso de nomes de variáveis claros e comentários explicativos ao longo do código.

A utilização da Árvore AVL mostrou-se eficiente para a construção do índice remissivo, garantindo organização, desempenho e escalabilidade, mesmo para grandes volumes de dados.
