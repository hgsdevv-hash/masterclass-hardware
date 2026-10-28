## O que é

A **placa-mãe** (*motherboard* ou *mainboard*, e em Portugal, "motherboard") é a **placa de circuito impresso principal** do computador. É nela que **todos os componentes se conectam e se comunicam**. Se o processador é o cérebro, a placa-mãe é o **sistema nervoso e o esqueleto ao mesmo tempo**.

## Para que serve: sua função no computador

1. **Conectar** todos os componentes: CPU, RAM, GPU, armazenamento, fonte, periféricos.
2. **Distribuir energia** com precisão: transforma os 12 V da fonte nas tensões baixas que a CPU e a memória exigem (pelo **VRM**).
3. **Transportar dados** entre as peças, pelos **barramentos** (PCIe, canais de memória, DMI/Infinity Fabric, USB, SATA).
4. **Coordenar** o funcionamento com o **chipset** e o **firmware (BIOS/UEFI)**.
5. **Oferecer recursos integrados (onboard)**: áudio, rede, Wi-Fi, USB, vídeo (se a CPU tiver gráfico integrado).

:::exemplo Exemplo: o papel da placa-mãe ao abrir 30 abas e editar um vídeo
- Ao abrir abas, a **CPU** pede espaço à **RAM**. Quem leva esses dados são os **canais de memória**, trilhas da placa-mãe. Uma placa com **4 slots** permite chegar a 64–256 GB de RAM.
- Ao editar vídeo, o arquivo sai do **SSD M.2** por **linhas PCIe** da placa, vai para a RAM e para a **GPU** (no slot PCIe x16). Ao exportar, a CPU trabalha em 100% por minutos, e um **VRM fraco** esquenta e **reduz o clock** (*throttling*). A mesma CPU fica mais lenta numa placa-mãe barata.
- Ao gerar imagens com IA localmente, a GPU precisa do slot **PCIe x16** em velocidade total (Gen 4 ou 5).
:::

## Onde fica e como é

- **Onde**: presa à **bandeja lateral do gabinete**, sobre espaçadores, com o **painel traseiro de I/O** voltado para trás.
- **Como é**: uma placa geralmente **preta** (antigamente verde), com trilhas de cobre, slots, soquete e dissipadores metálicos.

### Do que é feita (material)
| Parte | Material |
|---|---|
| **PCB (placa de circuito impresso)** | Camadas de **fibra de vidro com resina epóxi (FR-4)**, intercaladas com **camadas de cobre** (de 4 a 12 camadas; placas melhores têm mais camadas e cobre mais espesso) |
| **Trilhas** | Cobre |
| **Máscara de solda** | Verniz polimérico (a "cor" da placa: verde, preta, branca) |
| **Soldas** | Liga de estanho, prata e cobre (sem chumbo, pela diretiva RoHS) |
| **Contatos de slots** | Cobre com banho de **ouro** |
| **Dissipadores do VRM e do chipset** | Alumínio |
| **Capacitores** | Sólidos de polímero de alumínio (os bons, "japoneses") ou eletrolíticos |
| **Chips** | Silício encapsulado |

## Preço médio (Brasil, out/2026)

| Chipset | A partir de (à vista) | Faixa comum |
|---|---|---|
| AMD A620 / Intel H610 | ≈ R$ 400–420 | R$ 400–700 |
| AMD B650 | ≈ R$ 400 | R$ 600–1.200 |
| AMD B850 | ≈ R$ 650 | R$ 800–1.500 |
| AMD X870 / X870E | ≈ R$ 1.600 | R$ 1.800–4.000+ |
| Intel B760 | ≈ R$ 520 | R$ 600–1.200 |
| Intel B860 | ≈ R$ 860 | R$ 900–1.500 |
| Intel Z890 | ≈ R$ 1.550 | R$ 1.700–4.000+ |

*Fonte: menores preços à vista (Pix/boleto) em agregadores como o hardwarebarato.com, out/2026. Modelos Mini-ITX custam bem mais que os ATX do mesmo chipset.*

## Mapa completo da placa-mãe: cada slot e conector

{{img:Placa-mae|Placa-mãe ATX moderna com os principais componentes}}

| Componente | O que é | Para que serve | Como identificar |
|---|---|---|---|
| **Soquete da CPU** | Encaixe do processador | Ligar a CPU à placa | Quadrado grande no centro superior, com alavanca |
| **Slots de memória (DIMM)** | Encaixes longos e finos | Receber os pentes de RAM | 2 ou 4 slots ao lado do soquete, com travas nas pontas |
| **Slots PCI Express (PCIe)** | Slots de expansão | Placa de vídeo, placas de rede, captura, som | O **x16** é o mais longo (≈ 89 mm); x1 é o curtinho; x4 é o intermediário |
| **Slots M.2** | Encaixe pequeno e plano | SSDs NVMe (e Wi-Fi no slot M.2 Key E) | Pequeno conector com um parafuso ou trava, às vezes sob um dissipador |
| **Portas SATA** | Conectores em "L" | HDs, SSDs SATA e drives ópticos | Em grupo, na borda direita, de lado |
| **Conector ATX 24 pinos** | Energia principal | Alimentar a placa | Grande conector na borda direita |
| **Conector EPS 8 pinos (4+4)** | Energia da CPU | Alimentar o processador | No canto superior esquerdo (às vezes 2 deles) |
| **Chipset (PCH)** | Chip controlador | Gerencia USB, SATA e linhas PCIe extras | Sob um dissipador, na parte inferior direita |
| **VRM** | Reguladores de tensão (MOSFETs, bobinas/indutores, capacitores) | Converter 12 V em ≈ 1 V para a CPU | Cubinhos (indutores) ao redor do soquete, sob dissipadores |
| **Chip da BIOS/UEFI** | Memória flash SPI | Guardar o firmware | Pequeno chip de 8 pinos, às vezes em soquete |
| **Bateria CMOS (CR2032)** | Bateria de botão | Manter data, hora e configurações | Moeda prateada de 20 mm |
| **Headers de ventoinha (FAN)** | Conectores de 3 ou 4 pinos | Ligar e controlar coolers (CPU_FAN, SYS_FAN, PUMP) | Pequenos conectores brancos ou pretos espalhados |
| **Headers USB internos** | Conectores | USB do painel frontal | 9 pinos (2.0), 19 pinos (3.0), USB-C (Key-A) |
| **Header de áudio frontal (HD_AUDIO)** | Conector de 9 pinos | Fone e microfone frontais | Canto inferior esquerdo |
| **Painel frontal (F_PANEL)** | Pinos | Botões Power e Reset, LEDs | Canto inferior direito |
| **Headers RGB** | 12 V de 4 pinos (RGB) ou 5 V de 3 pinos (ARGB) | Iluminação | **Cuidado**: ligar ARGB (5 V) no RGB (12 V) **queima** os LEDs |
| **Painel traseiro de I/O** | Conectores externos | USB, rede, áudio, vídeo, antenas Wi-Fi | Parte de trás do gabinete |
| **Jumper Clear CMOS** | Dois pinos (ou botão) | Resetar a BIOS | Marcado "CLR_CMOS" ou "JBAT1" |
| **Debug LEDs / POST code** | LEDs ou display | Mostrar em qual etapa o boot travou | LEDs CPU / DRAM / VGA / BOOT |

## Formatos (fator de forma)

| Formato | Medidas | Slots de RAM | Slots PCIe | Uso | Preço médio (2026) |
|---|---|---|---|---|---|
| **E-ATX** | 305 × 330 mm (varia) | 4–8 | 4–7 | Entusiastas, workstations | R$ 3.000–10.000+ |
| **ATX** (padrão desde 1995, da Intel) | **305 × 244 mm** | 4 | até 7 | PCs gamer e completos | R$ 900–4.000 |
| **Micro-ATX (mATX)** | **244 × 244 mm** | 2–4 | até 4 | Custo-benefício; o mais vendido no Brasil | R$ 500–1.800 |
| **Mini-ITX** | **170 × 170 mm** | 2 | **1** | PCs compactos | R$ 1.000–3.500 |
| **Mini-STX / proprietárias** | Menores | SO-DIMM | — | Mini PCs, PCs de marca (Dell, HP, Lenovo) | — |

:::atencao Placas de computador de marca
Computadores **de marca** (Dell OptiPlex, HP ProDesk, Lenovo ThinkCentre) costumam usar placas com **formato, conectores de fonte e furação proprietários**. Elas nem sempre aceitam fonte ou gabinete padrão, o que é importante para o orçamento de um upgrade.
:::

## Soquete

O **soquete** define **quais processadores a placa aceita**. É o critério de compatibilidade número um.

### Tipos de soquete por tecnologia
| Tipo | Onde ficam os pinos | Exemplo |
|---|---|---|
| **PGA** (*Pin Grid Array*) | **No processador** | AMD **AM4** (Ryzen 1000 a 5000) |
| **LGA** (*Land Grid Array*) | **No soquete da placa** (no processador há só contatos planos) | Intel **LGA1700 / LGA1851**; AMD **AM5** |
| **BGA** (*Ball Grid Array*) | **Soldado** na placa | Notebooks e mini PCs; **não dá para trocar** a CPU |

### Soquetes atuais (out/2026)
| Fabricante | Soquete | Processadores | Memória |
|---|---|---|---|
| **AMD** | **AM4** (2017) | Ryzen 1000 a 5000 (ainda vendidos, ótimo custo) | DDR4 |
| **AMD** | **AM5** (2022) | Ryzen 7000, 8000G, **9000** (Zen 5), 9000X3D | **DDR5** |
| **Intel** | **LGA1700** (2021) | Core de 12ª, 13ª e 14ª geração | DDR4 **ou** DDR5 (depende da placa) |
| **Intel** | **LGA1851** (2024) | **Core Ultra 200S** (Arrow Lake) | DDR5 |

:::dica Longevidade do soquete
A AMD costuma manter o mesmo soquete por **várias gerações** (o AM4 durou de 2017 a 2022, com upgrade possível até o Ryzen 5000; a AMD anunciou na Computex 2026 que o AM5 terá suporte **até pelo menos 2029**, incluindo a futura geração Zen 6). A Intel troca de soquete com mais frequência, geralmente a cada **2 ou 3 gerações**. Isso pesa na escolha de quem pretende trocar só o processador no futuro.
:::

## Chipset

O **chipset** (hoje chamado **PCH**, *Platform Controller Hub*) é o chip que gerencia a comunicação entre a CPU e os periféricos "secundários": portas USB extras, SATA, linhas PCIe adicionais, áudio e rede. Ele determina **os recursos da placa**:

| Fabricante | Topo (overclock completo) | Intermediário (custo-benefício) | Entrada |
|---|---|---|---|
| **AMD (AM5)** | **X870E / X870** | **B850 / B650** | **B840 / A620** |
| **Intel (LGA1851)** | **Z890** (overclock da CPU) | **B860** | **H810** |
| **Intel (LGA1700)** | Z790 / Z690 | B760 / B660 | H610 |

O que muda entre eles: **overclock** (na Intel, só os chipsets "Z" liberam overclock da CPU nos modelos "K"), número de **linhas PCIe**, **PCIe 5.0** para GPU e SSD, quantidade de **USB** e **M.2**, e qualidade média do **VRM**.

## PCI e PCI Express: a evolução dos slots de expansão

| Barramento | Ano | Velocidade | Uso |
|---|---|---|---|
| **ISA** | 1981 | ≈ 8 MB/s | IBM PC, placas de som antigas |
| **PCI** | 1992 (Intel) | 133 MB/s (compartilhado) | Placas de rede, som e modem dos anos 1990 e 2000 |
| **AGP** | 1997 | 266 MB/s – 2,1 GB/s | Exclusivo para placas de vídeo (até ≈ 2006) |
| **PCIe 1.0** | 2003 | 250 MB/s **por linha** | Substituiu PCI e AGP |
| **PCIe 2.0** | 2007 | 500 MB/s por linha | — |
| **PCIe 3.0** | 2010 | ≈ 985 MB/s por linha | x16 ≈ 15,8 GB/s |
| **PCIe 4.0** | 2017 (2019 em PCs) | ≈ 1,97 GB/s por linha | x16 ≈ 31,5 GB/s; SSDs de 7.000 MB/s |
| **PCIe 5.0** | 2019 (2021–22 em PCs) | ≈ 3,94 GB/s por linha | x16 ≈ 63 GB/s; SSDs de 14.000 MB/s |
| **PCIe 6.0** | 2022 (especificação) | ≈ 7,9 GB/s por linha | Data centers |
| **PCIe 7.0** | Junho de 2025 (especificação) | ≈ 15,8 GB/s por linha (x16 ≈ 512 GB/s somando os dois sentidos) | Data centers de IA; o PCIe 8.0 está previsto para ≈ 2028 |

- **Linhas (*lanes*)**: um slot "x16" tem **16 linhas**, que funcionam como **16 faixas de uma rodovia**. x1, x4, x8 e x16 indicam quantas faixas.
- O PCIe é **compatível para frente e para trás**: uma placa PCIe 4.0 funciona num slot 3.0 (na velocidade do 3.0) e vice-versa.
- Um slot pode ser **fisicamente x16** mas **eletricamente x4**. Por isso, sempre veja o manual: só o slot principal costuma ter as 16 linhas ligadas à CPU.

## Onboard × Offboard (explicação detalhada)

Este é um dos conceitos mais importantes para quem vai comprar, vender ou consertar computador.

### Onboard
**Onboard** ("a bordo") é qualquer recurso **integrado à própria placa-mãe** ou ao **processador**, sem precisar de uma placa separada.

| Recurso onboard | Onde fica de verdade | Exemplo |
|---|---|---|
| **Vídeo onboard** (gráfico integrado) | Hoje, **dentro do processador** (iGPU); antigamente, no chipset | Intel UHD/Iris Xe/Arc integrado, AMD Radeon integrado (Ryzen com "G" e Ryzen 7000/9000 desktop) |
| **Áudio onboard** | Chip de áudio na placa (codec Realtek ALC) | Saídas P2 coloridas na traseira |
| **Rede onboard** | Chip de rede na placa (Realtek, Intel) | Porta RJ-45 de 1 ou 2,5 Gbps |
| **Wi-Fi / Bluetooth onboard** | Módulo M.2 já instalado | Placas com "WIFI" no nome |
| **USB, SATA** | Chipset e CPU | — |

### Offboard
**Offboard** ("fora da placa") é um recurso fornecido por uma **placa de expansão separada**, encaixada num slot (geralmente PCIe) ou ligada externamente.

| Recurso offboard | Exemplo |
|---|---|
| **Placa de vídeo dedicada** | NVIDIA GeForce RTX 5060, AMD Radeon RX 9060 XT |
| **Placa de som dedicada** | Creative Sound Blaster, interfaces de áudio USB (Focusrite) |
| **Placa de rede extra** | Placa PCIe de 10 Gbps, placa Wi-Fi PCIe |
| **Placa de captura** | Elgato (para streaming) |
| **Controladora** | Placa com portas SATA ou USB extras |

### Comparativo
| Critério | **Onboard** | **Offboard** |
|---|---|---|
| Custo | Já incluído, mais barato | Custo extra |
| Desempenho | Suficiente para o básico | **Muito superior** (principalmente vídeo) |
| Memória (vídeo) | **Compartilha a RAM** do sistema | Tem **memória própria (VRAM)** |
| Consumo e calor | Baixo | Maior (uma GPU pode consumir de 75 a 575 W) |
| Upgrade | Só trocando a CPU ou a placa | Troca fácil (é só a placa) |
| Manutenção | Defeito pode exigir trocar a placa-mãe inteira | Troca-se só a placa defeituosa |
| Indicado para | Escritório, estudos, internet, vídeo, jogos leves | Jogos, edição pesada, 3D, **IA** |

:::exemplo Exemplo: o caso mais comum de "tela preta" em PC novo
O cliente monta um PC com **placa de vídeo offboard** e liga o cabo HDMI na **saída de vídeo da placa-mãe (onboard)**. Resultado: "sem sinal". Quando há placa de vídeo dedicada, a placa-mãe normalmente **desativa o vídeo onboard** e a imagem sai **só pela placa de vídeo**. A solução é ligar o cabo **nas saídas horizontais, mais baixas, da placa de vídeo**.
:::

:::atencao Vídeo onboard depende do processador
Hoje, quem fornece o vídeo "onboard" é o **processador**. Uma placa-mãe com saída HDMI **não dá imagem** se o processador **não tiver gráfico integrado**:
- Intel com final **"F"** (ex.: Core i5-14400**F**): **sem** vídeo integrado.
- AMD **Ryzen 5000** sem "G" (ex.: Ryzen 5 5600): **sem** vídeo integrado. Os **Ryzen 5 5600G / 8600G** têm.
- AMD **Ryzen 7000 e 9000** desktop: **têm** um gráfico básico (exceto os modelos com final "F").
:::

## BIOS e UEFI

- **BIOS** (*Basic Input/Output System*): firmware criado para o IBM PC (1981). Ele testa o hardware no **POST** (*Power-On Self-Test*), configura as peças e procura o sistema operacional para iniciar.
- **UEFI** (*Unified Extensible Firmware Interface*): o sucessor moderno (adotado em massa a partir de **2011–2012**). Tem interface gráfica com mouse, suporta discos acima de 2 TB (partições **GPT**), **Secure Boot**, inicialização mais rápida e é **obrigatório para o Windows 11** (junto com o **TPM 2.0**).
- Na linguagem do dia a dia, todo mundo continua chamando de "BIOS".
- **Como entrar**: aperte **Del** ou **F2** logo ao ligar (em PCs de marca: F1, F10, F12 ou Esc).
- **CMOS**: a pequena memória onde ficam guardadas as configurações (data, ordem de boot, XMP), mantida pela **bateria CR2032**.

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Causa | Como evitar | Como resolver |
|---|---|---|---|---|
| **Não liga (nada acontece)** | Sem luz, sem ventoinha | Fonte, cabo de 24 ou 8 pinos solto, botão do painel, curto | Conectar tudo com firmeza; espaçadores corretos | Testar a fonte; ligar fora do gabinete (*breadboarding*); dar partida nos pinos PWR_SW |
| **Liga, mas sem imagem** | Ventoinhas girando, monitor sem sinal | RAM mal encaixada, cabo de vídeo na saída errada, CPU sem vídeo integrado, BIOS desatualizada para a CPU | Conferir a compatibilidade da BIOS com a CPU **antes** de comprar | Ver os **LEDs de debug** (CPU/DRAM/VGA/BOOT); reencaixar a RAM; testar 1 pente no slot indicado no manual (geralmente A2); **Clear CMOS** |
| **Bipes ao ligar** | Sequência de bipes | Código do POST indicando falha | — | Consultar a tabela do fabricante da BIOS (AMI, Award, Phoenix) no manual |
| **Perde a data e a hora** | Relógio atrasado, pede para apertar F1 | Bateria CR2032 fraca | Trocar a cada 3–5 anos | Trocar a bateria (≈ R$ 5–15) |
| **Capacitores estufados** | Desliga sozinho, trava, não liga | Calor, capacitores de baixa qualidade, idade | Boa ventilação; placas com capacitores sólidos | Troca dos capacitores (micro-solda) ou troca da placa |
| **VRM superaquecendo** | Perda de desempenho em carga longa (*throttling*) | Placa barata com CPU forte | Escolher placa com VRM compatível com a CPU (ver *reviews*) | Ventilar a região do VRM; limitar a potência da CPU na BIOS |
| **Pinos do soquete tortos (LGA)** | CPU não reconhecida, memória faltando canais | Queda de objeto, instalação errada | Manter a tampa até instalar a CPU; não arrastar a CPU no soquete | Desentortar com lupa e agulha (alto risco) ou assistência |
| **Atualização de BIOS interrompida** | Placa "morta" (*brick*) | Queda de energia durante a atualização | Atualizar com nobreak e arquivo correto | **BIOS Flashback** (botão traseiro em muitas placas), BIOS dual ou regravação do chip com programador (CH341A) |
| **Curto** | Desliga instantaneamente | Espaçador extra, parafuso solto embaixo da placa | Conferir os espaçadores | Desmontar e procurar o objeto ou espaçador |
| **Portas USB queimadas** | Uma porta específica não funciona | Pico, dispositivo em curto | Não usar cabos danificados | Usar outra porta ou um hub; reparo de micro-solda |

:::exemplo Exemplo de bancada: PC novo sem imagem com Ryzen 9000 numa placa B650
Placas B650 fabricadas antes de **agosto de 2024** vêm com uma BIOS que **não reconhece os Ryzen 9000**. O PC liga, as ventoinhas giram e o LED "CPU" fica aceso. Solução: usar o recurso **BIOS Flashback** (pen drive formatado em FAT32 com o arquivo da BIOS nova, renomeado conforme o manual, no USB marcado, apertando o botão traseiro), **sem precisar de processador antigo**. É por isso que verificar a "**CPU Support List**" no site do fabricante é obrigatório.
:::
