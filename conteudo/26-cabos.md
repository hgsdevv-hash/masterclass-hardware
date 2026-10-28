## O que são

**Cabos** são os condutores que **levam energia ou dados** entre os componentes internos e entre o computador e os periféricos. Cada cabo segue um **padrão** que define o **conector**, o **número de fios**, a **velocidade** e a **potência** suportadas.

## Para que servem: função no computador

| Tipo | Função | Exemplo de impacto |
|---|---|---|
| **Cabos de energia** | Levar a energia da fonte até as peças | Um cabo de GPU mal encaixado = PC desligando em jogo |
| **Cabos de dados internos** | Ligar o armazenamento e o painel frontal à placa-mãe | Um cabo SATA ruim = HD "sumindo" e arquivos corrompidos |
| **Cabos de vídeo** | Levar a imagem até o monitor | Um HDMI antigo = monitor de 144 Hz preso a 60 Hz |
| **Cabos de periféricos (USB)** | Teclado, mouse, celular, SSD externo, impressora | Um cabo USB-C "só de carga" = celular que carrega mas não transfere fotos |
| **Cabos de rede** | Conectar à internet | Um cabo Cat5 danificado = internet presa em 100 Mbps |
| **Cabos de áudio** | Fones, microfones, caixas | Um P2 com mau contato = chiado |

## Do que são feitos (material)

| Parte | Material |
|---|---|
| **Condutores** | **Cobre** (os de qualidade); os baratos usam **CCA** (alumínio revestido de cobre), que esquenta mais, quebra mais e perde sinal |
| **Isolamento** | PVC, polietileno, teflon (FEP) em cabos de alta frequência |
| **Blindagem** | Malha de cobre e/ou folha de alumínio, contra interferência |
| **Conectores** | Metal (cobre, latão) com banho de **ouro** ou **estanho**; invólucro plástico |
| **Capa externa** | PVC, TPE ou nylon trançado |
| **Fibra óptica** | Núcleo de **vidro** (sílica) ou plástico |

## Cabos internos de energia (da fonte)

| Conector | Pinos | Tensões | Alimenta | Observação |
|---|---|---|---|---|
| **ATX 24 pinos (20+4)** | 24 | 3,3 / 5 / 12 V | **Placa-mãe** | O maior conector; tem trava |
| **EPS / CPU 8 pinos (4+4)** | 8 | 12 V | **Processador** | Fica perto do soquete; placas topo têm 2 (8 + 8 ou 8 + 4) |
| **PCIe 6+2 pinos** | 6 ou 8 | 12 V | **Placa de vídeo** | Até **150 W** por conector de 8 pinos (mais 75 W do slot) |
| **12VHPWR / 12V-2x6 (16 pinos)** | 12 + 4 sensores | 12 V | **GPUs modernas** | Até **600 W** num conector; encaixe até o fim |
| **SATA power (15 pinos)** | 15 | 3,3 / 5 / 12 V | **HDs, SSDs SATA**, drives, alguns hubs de ventoinha e RGB | Conector achatado em "L" |
| **Molex (4 pinos)** | 4 | 5 / 12 V | Periféricos antigos, ventoinhas, bombas | Herança dos anos 1980–2000 |
| **Berg / floppy (4 pinos, pequeno)** | 4 | 5 / 12 V | Drives de disquete, alguns acessórios | Quase extinto |

:::atencao O "EPS" e o "PCIe" parecem iguais, mas não são
Os dois têm 8 pinos e cabem fisicamente em lugares parecidos, mas **a pinagem é invertida** (os 12 V e o terra ficam em lados opostos). Os encaixes têm formatos de pino diferentes para impedir o erro, mas **forçar** o cabo PCIe na tomada EPS (ou vice-versa) pode causar **curto e queima**. Leia a etiqueta do cabo: "CPU" ou "PCIe/VGA".
:::

## Cabos internos de dados

| Cabo | Velocidade | Uso | Observação |
|---|---|---|---|
| **SATA (7 pinos)** | SATA I: 1,5 Gb/s; II: 3 Gb/s; **III: 6 Gb/s (≈ 600 MB/s)** | HDs, SSDs SATA, drives ópticos | Conector em "L"; prefira os com **trava metálica** |
| **IDE / PATA (40 ou 80 vias)** | Até 133 MB/s | HDs e drives antigos (até ≈ 2008) | Cabo "flat" largo, com jumpers master/slave |
| **Cabo do painel frontal (F_PANEL)** | — | Botões Power e Reset, LEDs | Fios finos de 1 ou 2 pinos: **POWER SW, RESET SW, HDD LED (+/−), POWER LED (+/−)** |
| **USB 2.0 interno (9 pinos)** | 480 Mb/s | USB frontal | — |
| **USB 3.0 interno (19 pinos)** | 5 Gb/s | USB frontal azul | Conector grande e frágil (pinos entortam fácil) |
| **USB-C interno (Key-A)** | 10–20 Gb/s | USB-C frontal | — |
| **HD Audio (9 pinos)** | — | Fone e microfone frontais | — |
| **Cabos de ventoinha (3 ou 4 pinos)** | — | Coolers | — |
| **ARGB (3 pinos, 5 V) / RGB (4 pinos, 12 V)** | — | Iluminação | Não inverta |

:::dica Ligando o painel frontal sem errar
No manual da placa-mãe há o diagrama do **F_PANEL**. Os **botões** (Power SW, Reset SW) **não têm polaridade**. Os **LEDs têm** (+ e −); se um LED não acender, inverta o conector. Na falta do manual, os pinos costumam vir impressos na própria placa.
:::

## Cabos de vídeo

| Cabo | Tipo | Resolução e taxa máximas típicas | Áudio? | Situação em 2026 |
|---|---|---|---|---|
| **VGA (D-Sub 15 pinos, azul)** | **Analógico** (1987) | Até ≈ 2048 × 1536 (com perda de qualidade) | ❌ | Obsoleto; ainda em projetores e monitores antigos |
| **DVI (D, I, A)** | Digital (DVI-D) e/ou analógico | 1920 × 1200 a 60 Hz (single link); 2560 × 1600 (dual link) | ❌ | Obsoleto |
| **HDMI 1.4** | Digital | 4K a 30 Hz; 1080p a 120 Hz | ✅ | Comum em equipamentos antigos |
| **HDMI 2.0** | Digital (18 Gb/s) | **4K a 60 Hz**; 1080p a 240 Hz | ✅ | Comum |
| **HDMI 2.1** | Digital (**48 Gb/s**) | **4K a 120–144 Hz**, 8K a 60 Hz, VRR | ✅ | Padrão de TVs e consoles atuais (cabo "**Ultra High Speed**") |
| **HDMI 2.2** | Digital (**96 Gb/s**) | 4K a 480 Hz, 8K a 240 Hz, 12K e 16K | ✅ | Apresentado na CES (janeiro de 2025) e com especificação **finalizada em junho de 2025** (cabo certificado "**Ultra96**"); produtos chegando |
| **DisplayPort 1.4** | Digital (32,4 Gb/s) | 4K a 120 Hz, 1440p a 240 Hz (com DSC, mais) | ✅ | Padrão dos monitores gamer |
| **DisplayPort 2.0 / 2.1** | Digital (até **80 Gb/s**, UHBR20, desde o DP 2.0 de 2019) | 4K a 240 Hz+, 8K | ✅ | GPUs RTX 50 e RX 9000 |
| **USB-C (DP Alt Mode / Thunderbolt)** | Digital | Igual ao DisplayPort que carrega | ✅ | Notebooks e monitores modernos |

:::exemplo Exemplo: o monitor de 165 Hz que fica em 60 Hz
O cliente comprou um monitor gamer de 165 Hz e ligou com o **HDMI 1.4** que tinha em casa. Em 1080p, o cabo até passaria de 60 Hz, mas a combinação de cabo e porta limitou a taxa. Solução: usar o **cabo DisplayPort** que vem na caixa do monitor e configurar em **Configurações → Sistema → Tela → Configurações avançadas → Taxa de atualização: 165 Hz**.
:::

## Cabos USB e o "caos do USB-C"

| Versão | Nome atual (USB-IF) | Velocidade | Ano |
|---|---|---|---|
| USB 1.0 / 1.1 | Low / Full Speed | 1,5 / **12 Mb/s** | 1996 / 1998 |
| USB 2.0 | High Speed | **480 Mb/s** | 2000 |
| USB 3.0 = 3.1 Gen 1 = **3.2 Gen 1** | USB 5Gbps | **5 Gb/s** | 2008 |
| USB 3.1 Gen 2 = **3.2 Gen 2** | USB 10Gbps | **10 Gb/s** | 2013 |
| **USB 3.2 Gen 2x2** | USB 20Gbps | **20 Gb/s** | 2017 |
| **USB4** (v1) | USB 40Gbps | **40 Gb/s** | 2019 |
| **USB4 v2** | USB 80Gbps | **80 Gb/s** (até 120 Gb/s num sentido) | 2022 |
| **Thunderbolt 3 / 4** | — | 40 Gb/s | 2015 / 2020 |
| **Thunderbolt 5** | — | **80 Gb/s** (até 120 Gb/s) | 2023–2024 |

**Tipos de conector**: **Tipo A** (o retangular), **Tipo B** (impressoras), **Mini-USB**, **Micro-USB** (celulares antigos) e **Tipo C** (reversível, desde **2014**; obrigatório em celulares na União Europeia desde dezembro de 2024).

:::atencao USB-C é só o formato do conector
Um cabo **USB-C** pode ser:
- **Só de carga** (USB 2.0 com pouquíssima velocidade de dados, ou nenhuma);
- USB 2.0 (480 Mb/s), USB 5, 10 ou 20 Gbps;
- **USB4 / Thunderbolt** (40–80 Gb/s, com vídeo);
- De **60 W** ou de **240 W** (USB **Power Delivery** 3.1, com chip **e-marker**).

**Olhe a especificação na embalagem** ou os logos do USB-IF ("USB 40Gbps", "240W"). O cabo errado explica o SSD externo "lento" e o notebook que "não carrega".
:::

## Cabos de rede

| Categoria | Velocidade máxima | Frequência | Uso recomendado (2026) |
|---|---|---|---|
| Cat5 | 100 Mb/s | 100 MHz | Obsoleto |
| **Cat5e** | **1 Gb/s** (2,5 Gb/s em distâncias curtas) | 100 MHz | Mínimo aceitável |
| **Cat6** | 1 Gb/s (**10 Gb/s até ≈ 55 m**) | 250 MHz | **O mais recomendado** para casa e escritório |
| **Cat6a** | **10 Gb/s até 100 m** | 500 MHz | Redes de 10G |
| Cat7 / Cat8 | 10–40 Gb/s | 600–2.000 MHz | Data centers (Cat8 até 30 m) |
| **Fibra óptica** | Até centenas de Gb/s | — | Backbones; **FTTH** (*fibra até a casa*) |

- Conector: **RJ-45** (8 vias). Padrões de crimpagem: **T568A** e **T568B** (o mais usado no Brasil é o **T568B**: branco-laranja, laranja, branco-verde, azul, branco-azul, verde, branco-marrom, marrom).
- Distância máxima do cabo de par trançado: **100 metros**.
- **UTP** (sem blindagem, o comum) × **STP/FTP** (blindado, para ambientes com interferência).

## Cabos de áudio

| Conector | Uso |
|---|---|
| **P2 (3,5 mm)** | Fones e microfones. Cores no PC: **verde** = saída (fone/caixa), **rosa** = microfone, **azul** = entrada de linha |
| **P2 TRRS (4 polos)** | Fone com microfone (celular, headsets) |
| **P10 (6,35 mm)** | Instrumentos e áudio profissional |
| **RCA** | Som e vídeo antigos, caixas de som |
| **Óptico (Toslink / S/PDIF)** | Áudio digital para home theater |
| **XLR** | Microfones profissionais |

## Preço médio (Brasil, out/2026)

| Cabo | Faixa de preço |
|---|---|
| SATA de dados (com trava) | R$ 8–25 |
| HDMI 2.0 (1,5–2 m) | R$ 20–50 |
| HDMI 2.1 Ultra High Speed **certificado** | R$ 60–180 |
| DisplayPort 1.4 / 2.1 | R$ 40–200 |
| Cabo de rede Cat6 (patch cord 2–5 m) | R$ 15–50 |
| Caixa de cabo Cat6 (305 m) | R$ 400–1.000 |
| USB-C 2.0 (carga) | R$ 15–40 |
| USB-C 240 W / USB4 40 Gbps | R$ 80–300 |
| Cabo de força (tripolar, padrão novo) | R$ 15–40 |
| Extensões ou adaptadores de cabos de fonte (*sleeved*) | R$ 80–300 o kit |

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **Cabo SATA solto ou ruim** | HD sumindo, "*CRC errors*" no CrystalDiskInfo, travamentos | Cabos com trava; não dobrar demais | Trocar o cabo (é a primeira suspeita quando o atributo **C7 / UDMA CRC Error Count** sobe) |
| **Cabo de vídeo com defeito** | Imagem piscando, "sem sinal" intermitente, cores erradas | Cabos certificados; não dobrar perto do conector | Trocar o cabo; testar outra porta |
| **Cabo USB "só carga"** | Carrega, mas o PC não reconhece o dispositivo | Comprar cabos de dados | Trocar o cabo |
| **Conector de energia mal encaixado** | PC desligando, cheiro de queimado (12VHPWR) | Encaixar até o "clique" | Reencaixar; inspecionar se há derretimento |
| **Cabo de rede rompido** | Link a 100 Mb/s ou sem link | Não passar sob portas nem esmagar | Testar com um **testador de cabo**; refazer o RJ-45 |
| **Cabos de fonte de marcas diferentes** | Peças queimadas | **Nunca misturar** cabos modulares | — |
| **Fluxo de ar bloqueado pelos cabos** | Temperaturas altas | *Cable management* atrás da bandeja | Organizar com abraçadeiras e velcro |
| **Chiado no áudio** | Ruído e zumbido | Cabos blindados; afastar dos cabos de força | Usar a porta traseira (mais blindada); testar *ground loop* |
| **Mau contato por oxidação** | Funciona "às vezes" | Ambiente seco; conectores dourados | Limpar com isopropílico ou limpa-contatos |
