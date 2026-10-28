## O que é

O **SSD** (*Solid State Drive*, ou unidade de estado sólido) é um dispositivo de **armazenamento permanente** que guarda os dados em **chips de memória flash NAND**, **sem nenhuma parte móvel**. "Estado sólido" quer dizer justamente isso: tudo é **eletrônico**, sem motores, pratos ou braços.

## Para que serve: sua função no computador

O SSD faz o mesmo trabalho do HD (guardar o sistema, os programas e os arquivos), só que **dezenas ou centenas de vezes mais rápido** no acesso.

| Atividade | Impacto do SSD |
|---|---|
| **Ligar o PC** | Boot em **10–20 s** (contra 60–120 s no HD) |
| **Abrir programas e abas** | Programas abrem quase instantaneamente; abas descarregadas voltam rápido; o arquivo de paginação fica muito menos doloroso quando a RAM acaba |
| **Editar vídeo** | Prévia e *scrubbing* (arrastar a linha do tempo) fluidos em 4K; cache de mídia rápido. O ideal é um **NVMe para projetos** |
| **Jogos** | Carregamentos curtos; jogos modernos usam **DirectStorage**, que leva dados direto do NVMe para a GPU; muitos **exigem SSD** |
| **Gerar imagens e rodar IA localmente** | Carrega **modelos de vários GB** (de 4 a mais de 40 GB) em segundos |
| **Uso geral** | O computador "parece novo" |

## Onde fica e como é

| Formato | Onde fica | Como é |
|---|---|---|
| **SATA 2,5"** | Baia de 2,5" (ou 3,5" com adaptador), com cabo SATA de dados e de energia | Caixinha leve de plástico ou metal, de 100 × 70 × 7 mm |
| **M.2** (o mais comum hoje) | **Encaixado direto na placa-mãe**, no slot M.2, preso por parafuso ou trava | "Pente" de 22 mm de largura com chips. Tamanhos: **2280** (22 × 80 mm, o padrão), 2242, 2230 (Steam Deck, notebooks finos), 22110 |
| **mSATA** | Notebooks antigos | Placa pequena (obsoleto) |
| **U.2 / U.3 / E1.S / E3.S** | Servidores | Formatos empresariais |
| **SSD externo** | USB-C | Caixinha do tamanho de um cartão de crédito |
| **BGA (soldado)** | Placa-mãe de ultrabooks e Macs | Chip soldado, **não trocável** |

## Do que é feito (material)

| Parte | Material e função |
|---|---|
| **Chips NAND flash** | Silício; onde os dados ficam (Samsung, Kioxia, SK Hynix, Micron, WD/SanDisk, YMTC) |
| **Controlador** | Processador do SSD (Phison, Silicon Motion, Samsung, Maxio); gerencia tudo |
| **Cache DRAM** | Chip de memória que guarda o **mapa** de onde está cada dado (nos SSDs melhores) |
| **PCB** | Fibra de vidro e cobre |
| **Dissipador** (opcional) | Alumínio ou cobre, essencial nos NVMe PCIe 5.0 |
| **Capacitores (SSDs empresariais)** | Proteção contra queda de energia (*power-loss protection*) |

## Como funciona

### A célula de memória flash
1. Cada célula é um **transistor especial** com uma **porta flutuante** (*floating gate*) ou uma **camada de armadilha de carga** (*charge trap*), cercada de isolante.
2. **Gravar**: uma tensão alta "empurra" elétrons para dentro dessa porta (por **tunelamento quântico**, o efeito *Fowler-Nordheim*), onde eles ficam **presos** mesmo sem energia.
3. **Ler**: o controlador mede o nível de carga para saber qual valor está guardado.
4. **Apagar**: só pode ser feito em **blocos** grandes (de vários MB), não byte a byte. É por isso que o SSD precisa de "faxina" interna (a **coleta de lixo**, *garbage collection*) e do comando **TRIM**.

### Tipos de célula: quantos bits por célula
| Tipo | Bits por célula | Níveis de carga | Durabilidade (ciclos P/E aprox.) | Velocidade | Custo | Uso |
|---|---|---|---|---|---|---|
| **SLC** | 1 | 2 | ≈ 50.000–100.000 | ⭐⭐⭐⭐⭐ | $$$$$ | Indústria, cache |
| **MLC** | 2 | 4 | ≈ 3.000–10.000 | ⭐⭐⭐⭐ | $$$$ | Antigos SSDs premium |
| **TLC** | 3 | 8 | ≈ 1.000–3.000 | ⭐⭐⭐ | $$$ | **O mais comum hoje** |
| **QLC** | 4 | 16 | ≈ 500–1.000 | ⭐⭐ | $$ | SSDs baratos e de grande capacidade |
| **PLC** | 5 | 32 | Ainda menor | ⭐ | $ | Em desenvolvimento |

- **3D NAND**: as células são **empilhadas em camadas verticais** (de 200 a mais de 300 camadas nos chips de 2025–2026), como um **prédio** em vez de casas térreas. Isso aumentou muito a capacidade e reduziu o custo.
- **Cache SLC**: os SSDs TLC e QLC usam parte das células como se fossem SLC, para gravar rápido. Quando esse cache **enche** (numa cópia de 100 GB, por exemplo), a velocidade de escrita **despenca**. Isso é normal nos modelos baratos.

### Interfaces e protocolos: SATA × NVMe
| | **SSD SATA** | **SSD NVMe PCIe 3.0** | **NVMe PCIe 4.0** | **NVMe PCIe 5.0** |
|---|---|---|---|---|
| Barramento | SATA III (6 Gb/s) | PCIe 3.0 x4 | PCIe 4.0 x4 | PCIe 5.0 x4 |
| Protocolo | AHCI (feito para HDs) | **NVMe** (criado para flash, em **2011**) | NVMe | NVMe |
| Leitura sequencial máxima | ≈ **550 MB/s** | ≈ **3.500 MB/s** | ≈ **7.000–7.450 MB/s** | ≈ **12.000–15.000 MB/s** |
| Formato | 2,5" ou M.2 SATA | M.2 | M.2 | M.2 (com dissipador grande) |
| Calor | Baixo | Baixo-médio | Médio | **Alto** |

:::atencao Nem todo M.2 é NVMe
Existem SSDs **M.2 SATA** (com **dois** entalhes no conector, *B+M key*), que são limitados a ≈ 550 MB/s, e SSDs **M.2 NVMe** (com **um** entalhe, *M key*). Alguns slots M.2 de placas antigas ou baratas aceitam **só um dos tipos**. **Confira o manual da placa-mãe** antes de comprar.
:::

### Com DRAM × sem DRAM (DRAM-less / HMB)
- **Com cache DRAM**: o "mapa" dos dados fica numa memória própria e rápida, com melhor desempenho em uso intenso e mais consistência.
- **Sem DRAM (*DRAM-less*)**: mais barato. Os NVMe usam o **HMB** (*Host Memory Buffer*), que "empresta" um pouco da RAM do PC. Para uso doméstico, os bons modelos HMB são suficientes.

## Durabilidade: TBW e o mito de que "SSD estraga rápido"
- **TBW** (*Terabytes Written*): quantos **terabytes** podem ser gravados antes que o fabricante deixe de garantir o SSD. Exemplo: um SSD de 1 TB com **600 TBW**.
- **DWPD** (*Drive Writes Per Day*): quantas vezes por dia o disco inteiro pode ser regravado durante a garantia (usado em SSDs empresariais).

:::exemplo Exemplo: quanto tempo dura um SSD de 600 TBW
Um usuário comum grava ≈ **20–50 GB por dia** (sistema, atualizações, navegação, downloads):
600 TB = 600.000 GB → 600.000 ÷ 50 = **12.000 dias ≈ 33 anos**.
Na prática, **o SSD fica obsoleto antes de se desgastar**. O que realmente mata SSDs é **falha do controlador, queda de energia ou firmware com defeito**, e não o desgaste das células.
:::

## TRIM, desfragmentação e otimização
- **TRIM**: comando em que o sistema avisa o SSD quais blocos foram apagados, para ele limpá-los antecipadamente. O Windows faz isso automaticamente (**"Otimizar unidades"**).
- **Nunca desfragmente um SSD**: a desfragmentação não traz ganho (não há braço mecânico) e **gasta ciclos de escrita**. O Windows já sabe disso e, no SSD, executa o TRIM em vez de desfragmentar.
- **Deixe 10–20% livre**: SSDs quase cheios ficam mais lentos (sobra menos espaço para o cache SLC e a coleta de lixo).

## Preço médio (Brasil, out/2026)

:::atencao Preços de SSD em alta
Assim como a RAM, a **memória NAND** subiu muito entre o fim de 2025 e 2026 por causa da demanda dos data centers de IA. Os valores abaixo são de out/2026.
:::

| Produto | Faixa de preço (out/2026) |
|---|---|
| SSD SATA 480–512 GB | R$ 350–600 (estimativa) |
| SSD SATA 1 TB | R$ 800–1.200 (estimativa) |
| **NVMe PCIe 4.0 1 TB de entrada** (Kingston NV3) | **≈ R$ 1.150 (Pix)** |
| NVMe PCIe 4.0 1 TB intermediário (WD SN7100) | ≈ R$ 1.560–1.750 |
| NVMe PCIe 4.0 1 TB topo (Samsung 990 Pro, WD Black SN850X) | R$ 1.700–2.300 (estimativa) |
| NVMe PCIe 4.0 2 TB | R$ 2.500–4.000 (estimativa) |
| NVMe PCIe 5.0 2 TB | R$ 4.000–6.000 (estimativa) |

*Fontes: menores preços à vista em agregadores, out/2026. Para comparar, o mesmo Kingston NV3 1 TB custava ≈ R$ 919 em junho de 2026, e a alta reflete a crise da NAND (a TrendForce previu **+70–75%** só no 2º trimestre de 2026). As linhas marcadas como estimativa não tinham preço datado nas fontes consultadas.*

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **SSD não aparece** | Não está na BIOS nem no Windows | Ver a compatibilidade do slot M.2 (SATA × NVMe); o parafuso | Reencaixar; testar outro slot; no Windows, **Gerenciamento de Disco** → inicializar (GPT) e criar volume |
| **Instalação do Windows não encontra o SSD** | "Nenhuma unidade encontrada" | — | Carregar o **driver Intel RST/VMD** na instalação ou **desativar o VMD/RAID** na BIOS |
| **Superaquecimento (NVMe 4.0/5.0)** | Velocidade cai muito em cópias longas, temperatura acima de 70–80 °C | Usar o **dissipador** da placa-mãe (e **retirar a película plástica do pad térmico**) | Instalar dissipador; melhorar o fluxo de ar |
| **Lentidão com o disco cheio** | Escritas lentas | Manter 10–20% livre | Liberar espaço |
| **Queda de velocidade em cópias grandes** | Começa a 3.000 MB/s e cai para 100–500 MB/s | Saber que é o **cache SLC** acabando (normal em TLC/QLC) | Para gravações enormes e constantes, preferir SSDs TLC com DRAM |
| **Firmware com defeito** | Desaparecimento, perda de dados, desgaste anormal (casos reais: Samsung 980/990 Pro em 2023) | Atualizar o firmware pelo software oficial (Samsung Magician, WD Dashboard, Crucial Storage Executive) | Atualizar o firmware; acionar a garantia |
| **Falha súbita** | O SSD "morre" sem aviso (diferente do HD, que costuma dar sinais) | **Backup!** Nobreak | Garantia; recuperação de dados em SSD é **muito difícil** (TRIM e criptografia interna) |
| **SSD falso / capacidade falsa** | "2 TB" baratíssimo que corrompe dados depois de alguns GB | Comprar em lojas confiáveis | Testar com o **H2testw** ou o **ValiDrive** |
| **Saúde do SSD** | — | Acompanhar | **CrystalDiskInfo** mostra a **% de vida útil**, as horas ligadas e o total gravado |

## HD × SSD: comparativo final

| Critério | **HD** | **SSD** |
|---|---|---|
| Tecnologia | Magnética, com partes móveis | Eletrônica (flash NAND) |
| Velocidade sequencial | 80–280 MB/s | 550–15.000 MB/s |
| Tempo de acesso | 5–15 ms | 0,02–0,1 ms |
| Ruído | Sim (giro e cliques) | Silencioso |
| Resistência a impactos | **Baixa** | **Alta** |
| Consumo | 5–10 W | 2–9 W |
| Custo por TB (out/2026) | **Menor** (≈ R$ 280–360 no 4–8 TB) | Mais alto (≈ R$ 1.000–1.500) |
| Capacidade máxima comum | **Até 30+ TB** | 1–8 TB (consumidor) |
| Melhor uso | **Backup, arquivo, NAS, vigilância** | **Sistema, programas, jogos, projetos** |

:::dica A configuração ideal em 2026
**SSD NVMe de 1–2 TB** para o sistema, os programas e os jogos + **HD de 2–8 TB** para backup e arquivos grandes (ou backup em nuvem). É o melhor dos dois mundos.
:::
