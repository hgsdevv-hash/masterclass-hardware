Se você abrir **qualquer** computador de hoje (o seu PC, o notebook, o celular, o servidor do banco), vai encontrar por dentro a mesma ideia organizadora, descrita em **1945**. Ela se chama **Arquitetura de Von Neumann**, e entendê-la é entender como o computador "pensa".

## Quem foi John von Neumann

**John von Neumann** (1903–1957) foi um matemático húngaro-americano, considerado um dos maiores gênios do século XX. Contribuiu para a mecânica quântica, a teoria dos jogos, a economia, o Projeto Manhattan e, claro, a computação. Ele se juntou como consultor ao grupo do ENIAC em **1944**.

Em **30 de junho de 1945**, circulou o documento **"First Draft of a Report on the EDVAC"** (*Primeiro Rascunho de um Relatório sobre o EDVAC*), assinado só por von Neumann. Ele descrevia como deveria ser o sucessor do ENIAC.

:::atencao Justiça histórica
As ideias do relatório nasceram de discussões com **Eckert e Mauchly**, que já pensavam em programa armazenado, e o próprio Turing havia descrito a máquina universal em 1936. Como o rascunho circulou só com o nome de von Neumann, ele levou a fama e a arquitetura ganhou o nome dele. Muitos historiadores preferem o termo **"arquitetura de programa armazenado"**.
:::

## A ideia central: o programa armazenado

No ENIAC, o **programa** ficava nos **cabos** (para mudar a tarefa, era preciso religar fios por dias), e os **dados** ficavam nos acumuladores eletrônicos.

A grande sacada de von Neumann foi: **"Coloque as instruções do programa na mesma memória que os dados, como se fossem números."** Consequências:

1. Trocar de programa passa a ser **só carregar outros números na memória**, em segundos, não em dias.
2. Um programa pode **ler, criar e modificar outros programas**. É isso que torna possíveis compiladores, sistemas operacionais e instaladores.
3. A máquina vira **realmente universal**: o mesmo hardware serve para planilha, jogo, música ou IA.

## Os cinco componentes

```
            ┌───────────────────────────────────────┐
            │      UNIDADE CENTRAL DE PROCESSAMENTO │
            │  ┌──────────────┐  ┌───────────────┐  │
 ENTRADA ──►│  │  UNIDADE DE  │  │  UNIDADE      │  │──► SAÍDA
            │  │  CONTROLE    │◄►│  LÓGICA E     │  │
            │  │  (UC)        │  │  ARITMÉTICA   │  │
            │  └──────┬───────┘  │  (ULA)        │  │
            │         │          └───────┬───────┘  │
            │         │   Registradores  │          │
            └─────────┼──────────────────┼──────────┘
                      │   BARRAMENTO     │
            ┌─────────▼──────────────────▼──────────┐
            │      MEMÓRIA PRINCIPAL                │
            │  (instruções + dados, juntos)         │
            └───────────────────────────────────────┘
```

| Componente | Função | Equivalente no seu PC |
|---|---|---|
| **Unidade de Controle (UC)** | O "maestro": busca cada instrução, decodifica e manda as outras partes agirem | Parte interna da CPU |
| **Unidade Lógica e Aritmética (ULA / ALU)** | A "calculadora": soma, subtrai, compara, faz AND, OR, NOT | Parte interna da CPU (cada núcleo tem várias) |
| **Registradores** | Memória minúscula e ultrarrápida dentro da CPU | Registradores da CPU (ex.: RAX, RIP no x86-64) |
| **Memória** | Guarda instruções e dados | Memória RAM (com caches L1/L2/L3 no meio do caminho) |
| **Entrada e Saída (E/S)** | Comunicação com o mundo | Teclado, mouse, monitor, SSD, rede |
| **Barramentos** | As "estradas" que ligam tudo: endereço, dados e controle | Trilhas da placa-mãe, PCIe, canais de memória |

## O ciclo de instrução: buscar → decodificar → executar

A CPU repete este ciclo **bilhões de vezes por segundo**:

1. **Busca (*fetch*)**: a UC lê no registrador **PC** (*Program Counter*, ou contador de programa) o endereço da próxima instrução e a busca na memória.
2. **Decodificação (*decode*)**: a UC interpreta o que a instrução pede (por exemplo, "some o conteúdo de A com B").
3. **Execução (*execute*)**: a ULA faz a operação.
4. **Escrita (*write-back*)**: o resultado vai para um registrador ou para a memória. O PC avança para a próxima instrução, e o ciclo recomeça.

:::exemplo Exemplo: o computador calculando 2 + 3
Imagine que a memória tem este conteúdo:

| Endereço | Conteúdo | Significado |
|---|---|---|
| 100 | `CARREGA A, [200]` | Instrução: ponha em A o valor do endereço 200 |
| 101 | `SOMA A, [201]` | Instrução: some a A o valor do endereço 201 |
| 102 | `GUARDA A, [202]` | Instrução: guarde A no endereço 202 |
| 200 | `2` | Dado |
| 201 | `3` | Dado |
| 202 | `?` | Resultado |

1. PC = 100 → busca, decodifica e executa: A = 2.
2. PC = 101 → A = 2 + 3 = 5 (trabalho da ULA).
3. PC = 102 → grava 5 no endereço 202.

Repare que **instruções e dados moram na mesma memória**, lado a lado. Isso é Von Neumann.
:::

## O gargalo de Von Neumann

Como instruções e dados passam pelo **mesmo barramento** entre CPU e memória, a CPU muitas vezes fica **esperando** a memória entregar as informações. O termo **"gargalo de Von Neumann"** (*Von Neumann bottleneck*) foi popularizado por **John Backus** (criador do FORTRAN) na palestra do Prêmio Turing em **1977**.

Hoje o problema é ainda maior, porque a CPU ficou muito mais rápida que a RAM (o chamado *memory wall*). As soluções modernas:

| Solução | Como ajuda |
|---|---|
| **Memória cache (L1, L2, L3)** | Memória rápida dentro da CPU guarda o que foi usado recentemente; a CPU vai à RAM bem menos |
| **Cache separado de instruções e dados (L1i / L1d)** | Dentro do núcleo, usa a ideia de Harvard (veja abaixo) |
| **Pré-busca (*prefetch*) e previsão de desvio** | A CPU adivinha o que vai precisar e busca antes |
| **Dual/quad channel de memória** | Mais "estradas" em paralelo até a RAM |
| **Cache 3D (AMD X3D)** | Empilha cache extra em cima do chip, o que ajuda muito em jogos |
| **HBM (*High Bandwidth Memory*)** | Memória empilhada ao lado da GPU, usada em IA |
| **Computação perto da memória** | Pesquisa atual para processar dentro da própria memória |

:::exemplo Exemplo do gargalo no dia a dia
Um processador gamer com **mais cache** (como o Ryzen 7 9800X3D, com 96 MB de L3) pode ganhar **10% a 30% de FPS** em alguns jogos em relação a um modelo com clock parecido e menos cache. A ULA é a mesma; o ganho vem de **não esperar a RAM**.
:::

## Von Neumann x Harvard

| | **Von Neumann** | **Harvard** |
|---|---|---|
| Memória | **Uma** só, para instruções e dados | **Duas** separadas |
| Barramento | Compartilhado | Separados (busca instrução e dado ao mesmo tempo) |
| Vantagem | Simples, flexível, programa pode virar dado | Mais rápida e previsível |
| Desvantagem | Gargalo | Mais complexa, menos flexível |
| Origem do nome | Relatório do EDVAC (1945) | Harvard Mark I (1944), que lia instruções de fita perfurada separada dos dados |
| Onde se usa hoje | PCs, servidores, celulares (no nível da RAM) | Microcontroladores (Arduino/AVR, PIC), DSPs e o cache L1 das CPUs modernas |

:::dica Resposta de prova
"Os computadores modernos usam uma **arquitetura Harvard modificada**: por fora (RAM) são Von Neumann, com uma memória única, e por dentro do núcleo (cache L1) são Harvard, com caches separados de instruções e de dados."
:::

## Por que isso importa para quem trabalha com hardware

- Explica por que **mais RAM** e **RAM mais rápida** fazem diferença: a memória é a "mesa de trabalho" da CPU.
- Explica por que **SSD** deixa o PC muito mais rápido que HD: o programa precisa ser **carregado na memória** antes de rodar, e o SSD entrega os dados dezenas de vezes mais rápido.
- Explica por que **cache** aparece em destaque nas fichas técnicas de processadores.
- Explica a lógica do **POST** (próximos módulos): se a RAM falha, a CPU não tem onde buscar instruções, e o PC não liga a imagem.
