A evolução do computador costuma ser ensinada em **gerações**. Cada geração é definida pela **tecnologia do componente que faz a comutação**, ou seja, o "liga/desliga" que representa os bits. Quando essa peça muda, tudo muda junto: tamanho, preço, consumo, velocidade e quem consegue ter um computador.

## As gerações do computador

| Geração | Período | Tecnologia-chave | Exemplos | Velocidade típica | Programação |
|---|---|---|---|---|---|
| **Geração 0** | até 1940 | Mecânica e eletromecânica (engrenagens, relés) | Pascalina, Z3, Harvard Mark I | Poucas operações por segundo | Cartões, chaves, fitas |
| **1ª geração** | 1946–1958 | **Válvulas termiônicas** | ENIAC, UNIVAC I, IBM 701 | Milhares de operações/s | Linguagem de máquina, cabos |
| **2ª geração** | 1958–1964 | **Transistores** | IBM 1401, IBM 7090 | Centenas de milhares de operações/s | Assembly, FORTRAN (1957), COBOL (1959) |
| **3ª geração** | 1964–1971 | **Circuitos integrados (CIs)** | IBM System/360, PDP-8 | Milhões de operações/s | Sistemas operacionais, BASIC |
| **4ª geração** | 1971–hoje | **Microprocessadores (VLSI)** | Intel 4004, IBM PC, Apple II, smartphones | Bilhões de operações/s | Linguagens de alto nível, interfaces gráficas |
| **5ª geração** | 1980s–hoje | **Processamento paralelo, IA, GPUs, nuvem** | Supercomputadores, NVIDIA H100/B200 | Quatrilhões ou mais de operações/s (peta/exa) | IA, aprendizado de máquina |
| **Fronteira** | 2019– | **Qubits** (computação quântica) | Google Willow, IBM Heron | Outra lógica (não se mede da mesma forma) | Algoritmos quânticos |

### 1ª geração: válvulas (1946–1958)
- **Como era**: salas inteiras, toneladas de peso, ar-condicionado industrial, válvulas queimando com frequência.
- **Memória**: linhas de atraso de mercúrio, tubos de Williams (tubos de raios catódicos) e, no fim da geração, **memória de núcleos magnéticos** (anéis de ferrite atravessados por fios).
- **Quem usava**: governos, exército, universidades e grandes empresas.

### 2ª geração: transistores (1958–1964)
- O transistor tornou os computadores **menores, mais baratos, mais frios e muito mais confiáveis**.
- Surgiram as **linguagens de alto nível**: **FORTRAN** (IBM, John Backus, 1957) para ciência e **COBOL** (1959, com forte influência de **Grace Hopper**) para negócios. O COBOL ainda roda em muitos bancos.
- O **IBM 1401** (1959) vendeu mais de 10 mil unidades, um sucesso enorme para a época.

### 3ª geração: circuitos integrados (1964–1971)
- Vários transistores num único chip de silício.
- O **IBM System/360 (1964)** criou a ideia de **família de computadores compatíveis**: o mesmo software rodava do modelo mais barato ao mais caro. Foi também ele que **padronizou o byte de 8 bits**.
- Nasce a **multiprogramação**, com vários programas compartilhando a máquina, e os **minicomputadores** (DEC PDP-8, 1965) chegam a laboratórios e empresas médias.

### 4ª geração: microprocessadores (1971–hoje)
- **VLSI** (*Very Large Scale Integration*): milhões e depois bilhões de transistores num chip.
- A CPU inteira cabe num chip (Intel 4004, 1971), o que tornou possível o **computador pessoal**, depois o notebook e o smartphone.
- Chegam as interfaces gráficas, o mouse, as redes locais e a internet.

### 5ª geração: paralelismo e inteligência artificial
- O termo nasceu do **projeto japonês de "computadores de quinta geração" (1982–1992)**, voltado à IA lógica. O projeto não atingiu as metas, mas o nome pegou.
- Hoje a 5ª geração é associada a **processamento massivamente paralelo** (CPUs com dezenas de núcleos e GPUs com milhares), **IA e aprendizado de máquina** e **computação em nuvem**.

## A evolução de cada peça (antes → hoje)

| Componente | Antes | Hoje (2026) | Salto |
|---|---|---|---|
| **Processador** | Intel 4004 (1971): 2.300 transistores, 740 kHz | CPUs com dezenas de bilhões de transistores, 5–6 GHz, 16–24 núcleos (desktop) | ≈ 10 milhões de vezes mais transistores |
| **Memória RAM** | Altair 8800 (1975): 256 **bytes** | PCs com 16–64 **GB** de DDR5 | ≈ 100 milhões de vezes mais |
| **Armazenamento** | IBM 350 RAMAC (1956): **3,75 MB** em 50 discos de 61 cm, ≈ 1 tonelada | HDs de 30+ TB; cartões microSD de 1–2 TB | Milhões de vezes mais, num espaço milhões de vezes menor |
| **Disquete** | 8" (1971): 80 KB → 5,25" → 3,5" (1,44 MB) | Pen drive de 256 GB | ≈ 180 mil disquetes num pen drive |
| **Tela** | Teletipo (papel), depois CRT monocromático | OLED 4K a 240 Hz | — |
| **Rede** | Modem acústico de 300 bps | Fibra de 1 Gbps em casa | ≈ 3 milhões de vezes mais rápida |
| **Litografia (tamanho do transistor)** | 10 µm (1971) | Processos "3 nm" e "2 nm" (nomes comerciais) | Transistores milhares de vezes menores |

:::exemplo Exemplo: quanto cabe hoje no espaço de antes
Uma foto de celular de 2026 (≈ 4 MB) **não caberia** no IBM 350 RAMAC de 1956, que tinha 3,75 MB, pesava uma tonelada e o sistema completo em que ele funcionava (o IBM 305 RAMAC) era alugado por cerca de US$ 3.200 por mês. O disco sozinho saía por ≈ US$ 650–750 por mês. Hoje, um microSD do tamanho de uma unha guarda 1 TB, ou seja, umas **250 mil dessas fotos**.
:::

## As grandes forças da evolução

1. **Miniaturização (Lei de Moore)**: transistores menores são mais rápidos, gastam menos energia e custam menos por unidade.
2. **Paralelismo**: desde cerca de **2005**, o clock parou de subir muito por causa do calor (o chamado *power wall*). A indústria passou a colocar **vários núcleos** num chip, em vez de um núcleo cada vez mais rápido.
3. **Especialização**: em vez de uma CPU que faz tudo, surgiram chips especialistas: **GPU** (gráficos e IA), **NPU** (redes neurais em notebooks e celulares), **DSP** (áudio), **codificadores de vídeo**.
4. **Integração (SoC)**: o *System on a Chip* coloca CPU, GPU, NPU, controladores e às vezes até a RAM num só pacote (Apple M-series, Snapdragon, chips de celular).
5. **Conectividade**: o computador deixou de ser uma ilha e virou um ponto de uma rede mundial.

:::especialista O fim da Lei de Moore?
Muitos especialistas, inclusive o CEO da NVIDIA, **Jensen Huang**, dizem que a Lei de Moore "desacelerou" ou "acabou" no sentido econômico, porque transistores menores não ficam mais baratos como antes. Já a Intel e a TSMC continuam anunciando processos mais densos (2 nm, 18A, 1.4 nm). O consenso: **o ganho de desempenho agora vem mais da arquitetura, do empilhamento 3D de chips (*chiplets*, cache 3D) e da especialização** do que apenas de encolher transistores.
:::

## Evolução da tecnologia em geral: as ondas

| Onda | Período | Tecnologia dominante | O que mudou na vida das pessoas |
|---|---|---|---|
| Mainframe | 1950–1970 | Um computador gigante para muitos usuários | Bancos, censos e companhias aéreas automatizados |
| Minicomputador | 1965–1985 | Computadores de laboratório | Universidades e indústrias |
| PC | 1977–2005 | Um computador por pessoa | Escritório, escola, jogos em casa |
| Internet | 1995–hoje | Tudo conectado | E-mail, sites, comércio eletrônico |
| Mobile | 2007–hoje | Um computador no bolso | Apps, redes sociais, Pix, GPS |
| Nuvem | 2006–hoje | Computadores alugados em data centers | Streaming, backup, empresas sem servidor próprio |
| IA | 2012–hoje | Redes neurais em GPUs | Assistentes, geração de imagem e texto, tradução |
| Quântica | 2019– | Qubits | Ainda experimental: química, criptografia, otimização |
