## O que é

A **CPU** (*Central Processing Unit*, ou Unidade Central de Processamento), o **processador**, é o chip que **executa as instruções dos programas**. É o "cérebro" do computador: faz contas, toma decisões (comparações) e coordena todas as outras peças.

## Para que serve: sua função no computador

| Tarefa | O que a CPU faz |
|---|---|
| **Abrir abas e navegar** | Interpreta o HTML e o CSS, executa o **JavaScript** das páginas e gerencia cada aba como um processo. Mais núcleos = mais abas pesadas sem travar |
| **Editar e exportar vídeo** | Codifica e decodifica (com ajuda da GPU), aplica efeitos, organiza a linha do tempo. A exportação usa **todos os núcleos** |
| **Jogos** | Física, inteligência dos personagens, lógica do jogo e o envio de comandos para a GPU (as *draw calls*). Uma CPU fraca limita o FPS: é o famoso **"gargalo"** |
| **Gerar imagens com IA** | Prepara os dados e coordena; o trabalho pesado vai para a **GPU** (ou para a **NPU**, em notebooks novos) |
| **Office, planilhas** | Cálculos de fórmulas, macros |
| **Compactar arquivos, antivírus, compilar código** | Trabalho intenso da CPU |

## Onde fica e como é

- **Onde**: no **soquete da placa-mãe**, sob o **dissipador / cooler**.
- **Como é**: um quadrado de ≈ **3,75 × 3,75 cm** (Intel LGA1700/1851: 3,75 × 4,5 cm; AMD AM5: 4 × 4 cm), com:
  - **IHS** (*Integrated Heat Spreader*): a **tampa metálica** por cima, que espalha o calor.
  - **Substrato**: a placa verde ou marrom por baixo, que liga o chip aos contatos.
  - **Contatos ou pinos**: na parte de baixo.
  - Por dentro, sob o IHS, um ou mais **dies** (pedaços de silício), que são o processador de verdade.

## Do que é feita (material)

| Parte | Material |
|---|---|
| **Die (núcleo)** | **Silício** ultrapuro (99,9999999%, os "nove noves"), com bilhões de transistores feitos por **fotolitografia** |
| **Interconexões internas** | **Cobre** (desde 1997, IBM) em até 15–20 camadas microscópicas |
| **IHS (tampa)** | **Cobre niquelado** |
| **Material de interface (die → IHS)** | **Solda de índio** (modelos melhores) ou pasta térmica |
| **Substrato** | Fibra de vidro/resina e camadas de cobre |
| **Contatos** | Cobre com banho de **ouro** |

:::curiosidade Da areia ao processador
O silício vem da **areia de quartzo** (SiO₂). Ele é purificado, derretido e transformado num **lingote cilíndrico** monocristalino (pelo **método Czochralski**), cortado em **wafers** de 300 mm. Cada wafer passa por **centenas de etapas** de fotolitografia ao longo de **cerca de 3 meses**, em fábricas (*fabs*) que custam mais de **US$ 20 bilhões**. As máquinas mais avançadas, de **litografia EUV (ultravioleta extremo)**, são feitas por uma única empresa no mundo: a holandesa **ASML**. Cada uma custa de US$ 200 a 400 milhões.
:::

## Como funciona

### Os blocos internos de um núcleo
| Bloco | Função |
|---|---|
| **Unidade de busca e decodificação** | Lê as instruções da memória e as traduz em micro-operações |
| **Previsor de desvios** | "Adivinha" o caminho do programa (if/else) para não perder tempo |
| **Unidades de execução (ALUs, FPUs, unidades vetoriais AVX)** | Fazem as contas (inteiros, ponto flutuante, vetores) |
| **Registradores** | Memória dentro do núcleo, a mais rápida que existe |
| **Cache L1 e L2** | Memória ultrarrápida de cada núcleo |
| **Cache L3** | Memória compartilhada entre os núcleos |
| **Controlador de memória** | Conversa com a RAM (antes ficava no chipset da placa) |
| **Controlador PCIe** | Linhas para a GPU e o SSD |
| **iGPU** (quando há) | Gráfico integrado |
| **NPU** (nos chips para notebooks recentes) | Acelerador de IA |

### Conceitos de ficha técnica
| Termo | O que é | Exemplo prático |
|---|---|---|
| **Núcleos (*cores*)** | Processadores independentes dentro do chip | 6 núcleos = 6 tarefas pesadas em paralelo |
| **Threads** | Fluxos de execução. Com **SMT/Hyper-Threading**, cada núcleo atende **2 threads** | 6 núcleos / 12 threads |
| **Núcleos P e E (Intel, desde a 12ª geração)** | **P-cores** (*Performance*, fortes) e **E-cores** (*Efficient*, econômicos) | Core i5-14600K: 6P + 8E = 14 núcleos |
| **Clock base / boost (turbo)** | Frequência garantida / máxima temporária | 3,8 GHz base, 5,1 GHz boost |
| **Cache L3** | Memória interna compartilhada | 32 MB; nos **X3D**, 96 MB ou mais |
| **TDP / PPT / PBP** | Potência térmica de referência (para escolher o cooler) | 65 W, 105 W, 125 W |
| **Litografia (nó de processo)** | "Tamanho" do processo de fabricação (hoje é um **nome comercial**, não uma medida real) | TSMC N4, N3; Intel 7, Intel 18A |
| **IPC** | Instruções por ciclo, a "eficiência" da arquitetura | Zen 5 tem IPC ≈ 16% maior que o Zen 4 (segundo a AMD) |
| **Arquitetura (conjunto de instruções)** | A "língua" do processador | **x86-64** (Intel, AMD) × **ARM** (celulares, Apple M, Snapdragon X) |

### Chiplets × monolítico
- **Monolítico**: tudo num único pedaço de silício.
- **Chiplets**: vários pedaços menores, ligados dentro do mesmo pacote. A AMD popularizou isso com o Ryzen 3000 (2019): um ou dois **CCDs** (núcleos) + um **IOD** (entrada e saída). A Intel adotou o empilhamento **Foveros** nos Core Ultra. Vantagem: **custo menor** e mais flexibilidade.

## Intel × AMD: tipos e nomenclatura

### Como ler o nome de um processador Intel
**Intel Core i5-14600KF** (modelos até a 14ª geração):
- **Core i5**: a faixa. i3 (entrada), **i5** (intermediário, o mais vendido), i7 (alto), i9 (topo).
- **14**: a **geração** (14ª).
- **600**: o modelo dentro da faixa (maior = melhor).
- **K**: **desbloqueado para overclock**.
- **F**: **sem gráfico integrado** (precisa de placa de vídeo).

**Intel Core Ultra 7 265K** (nova nomenclatura, de 2024):
- **Core Ultra 5 / 7 / 9**: a faixa.
- **2xx**: a série (200 = Arrow Lake para desktop; nos notebooks, Lunar Lake e, em 2026, a série 300 Panther Lake).
- **K, F, KF, T**: como antes; **T** = baixo consumo.

| Sufixo Intel | Significado |
|---|---|
| **K** | Overclock liberado |
| **F** | Sem vídeo integrado |
| **KF** | Overclock liberado e sem vídeo |
| **T** | Baixo consumo (35 W) |
| **H / HX** | Notebook de alto desempenho |
| **U / P** | Notebook de baixo consumo |
| **V** | Notebook com memória no pacote (Lunar Lake) |

### Como ler o nome de um processador AMD
**AMD Ryzen 7 9800X3D**:
- **Ryzen 3 / 5 / 7 / 9**: a faixa (como o i3/i5/i7/i9).
- **9**: a **série/geração** (9000 = **Zen 5**).
- **8**: o nível dentro da faixa.
- **00**: variação do modelo.
- **X3D**: **cache 3D V-Cache** empilhado, o melhor para jogos.

| Sufixo AMD | Significado |
|---|---|
| **X** | Clock mais alto |
| **X3D** | Cache L3 extra (3D V-Cache) |
| **G** | Com gráfico integrado forte (APU) |
| **F** | Sem gráfico integrado |
| **HS / HX / U** (notebook) | Desempenho / alto desempenho / baixo consumo |

Os notebooks da AMD também usam nomes como **Ryzen AI 9 HX 370** (série Strix Point, com NPU).

### Outras famílias
| Família | Uso |
|---|---|
| **Intel Xeon / AMD EPYC** | Servidores (até 128–192 núcleos por chip) |
| **AMD Threadripper / Intel Xeon W** | Workstations |
| **Intel Celeron, Pentium, Intel N100/N150 / AMD Athlon** | Entrada, mini PCs |
| **Apple M1–M5** | Macs (ARM, SoC com memória unificada) |
| **Qualcomm Snapdragon X** | Notebooks Windows com ARM |
| **Snapdragon, MediaTek Dimensity, Apple A, Samsung Exynos** | Celulares |

## Gerações recentes (referência out/2026)

| Fabricante | Família | Soquete | Destaques |
|---|---|---|---|
| AMD | **Ryzen 5000** (Zen 3, 2020) | AM4 | Ainda ótimo custo-benefício com DDR4 (Ryzen 5 5600, Ryzen 7 5700X3D) |
| AMD | **Ryzen 7000** (Zen 4, 2022) | AM5 | DDR5, PCIe 5.0 |
| AMD | **Ryzen 9000** (Zen 5, 2024) | AM5 | Ryzen 5 9600X, Ryzen 7 9800X3D (referência para jogos) |
| Intel | **Core 12ª a 14ª geração** (2021–2023) | LGA1700 | Núcleos P + E; aceitam DDR4 ou DDR5 |
| Intel | **Core Ultra 200S** (Arrow Lake, 2024) | LGA1851 | Mais eficiência, NPU, sem Hyper-Threading |
| Intel | **Core Ultra Série 3** (Panther Lake, jan. 2026) | Notebooks (BGA) | Primeiro chip no processo **Intel 18A** |

:::curiosidade O que vem por aí
Em out/2026, os próximos desktops ainda **não foram lançados**. A AMD **Zen 6** (no mesmo soquete AM5) e a Intel **Nova Lake** (novo soquete LGA1954) são esperadas para **2027**, segundo relatos da imprensa especializada. A crise de preços de memória é apontada como um dos motivos dos atrasos.
:::

:::atencao Instabilidade dos Intel de 13ª e 14ª geração
Em 2024, a Intel confirmou que muitos **Core i7 e i9 de 13ª e 14ª geração** sofriam **degradação** por receberem **tensão acima do necessário** (o problema *Vmin shift*). Os sintomas eram travamentos e erros em jogos. A Intel liberou **microcódigos** corretivos (0x12B em 2024 e 0x12F em 2025) e **estendeu a garantia** dos modelos afetados. **Ao montar ou atender um PC com esses processadores, atualize a BIOS.**
:::

## Preço médio (Brasil, out/2026)

| Processador | Menor preço à vista (out/2026) |
|---|---|
| Core Ultra 5 225F | ≈ R$ 580 |
| Core i3-14100F | ≈ R$ 660 |
| Ryzen 5 5600 | ≈ R$ 930 |
| Ryzen 5 7600 | ≈ R$ 940 |
| Core i5-14400F | ≈ R$ 980 |
| Ryzen 5 9600X | ≈ R$ 1.150 |
| Core i5-14600KF | ≈ R$ 1.335 |
| Core Ultra 7 265K | ≈ R$ 1.780 |
| Ryzen 7 9800X3D | ≈ R$ 2.130 (com cupom) a R$ 2.500 |
| Ryzen 9 9950X | ≈ R$ 3.100 |
| Core Ultra 9 285K | ≈ R$ 3.100 |

*Fonte: menores preços à vista (Pix/boleto) verificados em 28/10/2026 em agregadores (hardwarebarato.com). No parcelado, some de 5% a 17%. Em lojas comuns, os preços costumam ser mais altos que o menor preço do dia.*

## Diferenças de um para outro: como escolher

| Perfil | O que priorizar | Sugestão |
|---|---|---|
| Escritório, estudos, internet | Núcleos suficientes (4–6) e **vídeo integrado** | Ryzen 5 8500G / 5600G, Core i3-14100 (sem F) |
| Jogos | **Clock alto + cache grande** (X3D), 6–8 núcleos | Ryzen 5 7600 / 9600X; Ryzen 7 9800X3D para o topo |
| Edição de vídeo, 3D, programação pesada | **Mais núcleos e threads** | Ryzen 9 9900X / 9950X, Core Ultra 7 265K / Ultra 9 285K |
| Notebook com bateria longa | Eficiência, NPU | Intel Core Ultra (série V), Snapdragon X, Apple M |

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Causa | Como evitar | Como resolver |
|---|---|---|---|---|
| **Superaquecimento** | Temperatura acima de 90–100 °C, *throttling*, desligamento | Cooler fraco, pasta seca, cooler mal instalado, poeira | Cooler adequado ao TDP; pasta trocada a cada 2–3 anos | Limpar, trocar a pasta, reinstalar o cooler com pressão uniforme |
| **Pinos tortos** (AMD AM4 e anteriores) | CPU não reconhecida, falta memória ou USB | Queda, manuseio | Segurar pelas bordas; guardar no estojo | Desentortar com cuidado (cartão de crédito ou agulha, com lupa) |
| **Incompatibilidade** | PC não dá imagem | Soquete ou chipset errados, BIOS antiga | Conferir a **CPU Support List** da placa-mãe | Atualizar a BIOS (Flashback) |
| **Sem imagem com CPU "F"** | Sem vídeo pela placa-mãe | O processador **não tem** vídeo integrado | Ler o sufixo antes de comprar | Instalar uma placa de vídeo |
| **Instabilidade (tela azul, travamentos)** | Erros WHEA, crashes em jogos | Overclock ou *undervolt* instável, degradação (Intel 13/14), BIOS antiga | Não exagerar no overclock; atualizar a BIOS | Restaurar o padrão da BIOS; atualizar o microcódigo; testar com OCCT, Prime95 ou Cinebench |
| **Gargalo** | GPU com uso abaixo de 90% em jogos, FPS baixo | CPU fraca para a GPU | Equilibrar CPU e GPU | Fazer upgrade da CPU; aumentar a resolução e a qualidade gráfica (desloca a carga para a GPU) |
| **Dano físico ao instalar o cooler** | Trinca no die (CPUs antigas sem IHS) | Pressão excessiva | Apertar em "X", aos poucos | — |

### Temperaturas de referência
| Situação | Temperatura típica | Alerta |
|---|---|---|
| Ociosa (sem fazer nada) | 30–50 °C | > 60 °C |
| Jogando | 55–80 °C | > 90 °C |
| Carga máxima (renderização) | 70–90 °C | Nos Ryzen 7000/9000 e Intel 13/14, **até 95–100 °C pode ser comportamento normal de projeto** sob carga extrema, mas não deveria ocorrer em jogos |
| Limite de proteção (TjMax) | ≈ 95–105 °C | A CPU reduz o clock ou desliga |

:::dica Ferramentas para monitorar a CPU
**HWiNFO64** (o mais completo), **HWMonitor**, **CPU-Z** (identifica modelo, soquete, clock e memória), **Core Temp**, **Ryzen Master** (AMD) e **Intel XTU**. Para testes de estresse: **Cinebench R23/2024**, **OCCT**, **Prime95**, **AIDA64**.
:::
