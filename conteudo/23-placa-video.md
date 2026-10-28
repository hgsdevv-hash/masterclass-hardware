## O que é

A **placa de vídeo** (também chamada de **placa gráfica**, **GPU** ou, no Brasil, de "VGA") é o componente responsável por **gerar as imagens** que aparecem no monitor. O coração dela é a **GPU** (*Graphics Processing Unit*, ou Unidade de Processamento Gráfico), um processador especializado em fazer **milhares de cálculos simples ao mesmo tempo**.

:::dica GPU × placa de vídeo
- **GPU** é o **chip** (o processador gráfico).
- **Placa de vídeo** é a **placa completa**: GPU + memória VRAM + VRM + dissipador + ventoinhas + saídas de vídeo.

Na conversa, os dois termos são usados como sinônimos.
:::

## CPU × GPU: a diferença fundamental

| | **CPU** | **GPU** |
|---|---|---|
| Núcleos | Poucos (6–24 no desktop), **muito poderosos** | **Milhares** (de 2.000 a mais de 20.000), mais simples |
| Especialidade | Tarefas variadas e sequenciais, com muitas decisões | **A mesma operação sobre muitos dados ao mesmo tempo** (paralelismo massivo) |
| Analogia | **Poucos professores de matemática**, que resolvem qualquer problema difícil | **Um estádio cheio de alunos** fazendo continhas simples ao mesmo tempo |
| Ideal para | Sistema operacional, lógica de jogos, Office, navegação | **Gráficos 3D, vídeo, IA, simulações, criptografia** |

:::exemplo Exemplo: por que a GPU é tão boa em imagens
Uma tela 4K tem **8,3 milhões de pixels**. A 60 FPS, a placa de vídeo precisa calcular a cor de **≈ 500 milhões de pixels por segundo**, e cada pixel exige dezenas de operações de luz, sombra e textura. O cálculo de cada pixel é **independente** dos outros: perfeito para milhares de núcleos trabalhando em paralelo.
:::

## Para que serve: sua função no computador

| Atividade | O que a GPU faz | Importância |
|---|---|---|
| **Mostrar a área de trabalho, abrir abas** | Desenha as janelas, o texto e as animações (aceleração por hardware do navegador) | Baixa: o vídeo integrado dá conta |
| **Assistir a vídeos (YouTube, Netflix)** | O **decodificador de hardware** descomprime H.264, H.265 (HEVC) e **AV1** | Baixa a média: o integrado moderno resolve |
| **Editar e exportar vídeo** | Aceleração de efeitos, prévia em tempo real, **codificadores** (NVENC da NVIDIA, AMF/VCN da AMD, Quick Sync da Intel) | **Alta**: exporta muitas vezes mais rápido |
| **Jogos** | Renderiza o 3D: geometria, texturas, iluminação, **ray tracing**, *upscaling* (DLSS, FSR, XeSS) | **Muito alta** |
| **Gerar imagens e vídeos com IA** (Stable Diffusion, Flux) e **rodar modelos de linguagem localmente** | Executa as redes neurais nos **Tensor Cores** (NVIDIA) ou nas unidades de IA (AMD, Intel) | **Muito alta**, e a **VRAM** é o fator decisivo |
| **3D, CAD, renderização (Blender, AutoCAD)** | Viewport e renderização (CUDA, OptiX, HIP) | Alta |
| **Vários monitores** | Cada saída gerencia uma tela | Média |

## Onde fica e como é

- **Onde**: encaixada no **slot PCI Express x16** principal da placa-mãe (o mais próximo do processador), presa por parafusos nos **slots traseiros** do gabinete. As saídas de vídeo ficam **na traseira, na horizontal, mais embaixo** que as saídas da placa-mãe.
- **Como é**: uma placa grande (de 17 cm, nos modelos compactos, a **36 cm** nos topo de linha), com 1 a 3 ventoinhas, uma proteção plástica ou metálica (*shroud*), uma placa traseira (*backplate*) e **conectores de energia** (6+2 pinos ou **12V-2x6**).

### Por dentro de uma placa de vídeo
| Parte | Função |
|---|---|
| **GPU (chip)** | O processador gráfico |
| **VRAM** (GDDR6, GDDR6X, GDDR7) | Memória **própria e ultrarrápida** para texturas, quadros e modelos de IA |
| **VRM** | Regula a energia da GPU e da memória |
| **PCB** | A placa de circuito |
| **Dissipador** (heatpipes ou câmara de vapor) + ventoinhas | Refrigeração |
| **Conector PCIe** | Comunicação com a placa-mãe (e até 75 W de energia) |
| **Conectores de energia extra** | 6, 8 (6+2) pinos ou **12V-2x6 / 12VHPWR (até 600 W)** |
| **Saídas** | **HDMI**, **DisplayPort**, às vezes USB-C |
| **VBIOS** | Firmware da placa |

## Do que é feita (material)

| Parte | Material |
|---|---|
| GPU | **Silício** (fabricado pela **TSMC** para NVIDIA e AMD; a Intel usa TSMC e fábricas próprias) |
| VRAM | Chips de silício (Samsung, SK Hynix, Micron) |
| PCB | Fibra de vidro FR-4 com 8–14 camadas de cobre |
| Dissipador | Base e heatpipes de **cobre**; aletas de **alumínio**; câmara de vapor de cobre |
| Ventoinhas e proteção | Plástico e/ou alumínio |
| Backplate | Alumínio ou aço |
| Pads térmicos | Silicone com partículas cerâmicas |

## Tipos de placa de vídeo

### Integrada (onboard) × dedicada (offboard)
| | **Integrada (iGPU)** | **Dedicada (dGPU)** |
|---|---|---|
| Onde fica | Dentro do processador | Placa separada no slot PCIe |
| Memória | **Usa a RAM do sistema** | **VRAM própria** |
| Desempenho | Básico a moderado (os melhores rodam jogos leves e e-sports em 1080p baixo) | De moderado a extremo |
| Consumo | 5–30 W | 75–575 W |
| Exemplos | Intel UHD / Iris Xe / Arc integrada, AMD Radeon 780M / 890M, Apple M | NVIDIA GeForce RTX, AMD Radeon RX, Intel Arc B |

### Fabricantes de chips (GPU) e marcas de placas
- **Fabricantes de GPU** (quem projeta o chip): **NVIDIA**, **AMD** e **Intel**.
- **Fabricantes de placas** (as *AIBs*, *add-in board partners*, que montam a placa com o chip): **ASUS, MSI, Gigabyte, Zotac, PNY, Galax, Palit, Gainward, Sapphire, PowerColor, XFX, ASRock**... Cada uma tem versões mais simples e versões "premium" (com mais ventoinhas e overclock de fábrica).

### NVIDIA GeForce: como ler o nome
**GeForce RTX 5070 Ti**
- **GeForce**: a linha para **consumidores** (jogos e criação). Para profissionais, há a linha **RTX PRO** (antiga Quadro); para data centers, **H100, H200, B200, GB200**.
- **RTX**: tem **ray tracing** e **Tensor Cores** (IA). As antigas **GTX** não têm.
- **50**: a **geração** (série 50 = arquitetura **Blackwell**, de 2025).
- **70**: a **posição** na linha: 50 (entrada), 60 (intermediária), 70 (intermediária-alta), 80 (alta), 90 (topo).
- **Ti / Super**: versões **mais fortes** do mesmo nível.

| Geração GeForce | Ano | Arquitetura | Destaque |
|---|---|---|---|
| GeForce 256 | **1999** | — | Anunciada como "a **primeira GPU** do mundo" (fazia transformação e iluminação em hardware) |
| GTX 10 | 2016 | Pascal | GTX 1060 foi a GPU mais usada do Steam por anos |
| RTX 20 | 2018 | Turing | Primeiro **ray tracing em tempo real** e **DLSS** |
| RTX 30 | 2020 | Ampere | Grande salto de desempenho |
| RTX 40 | 2022 | Ada Lovelace | **DLSS 3** (geração de quadros) |
| **RTX 50** | **2025** | **Blackwell** | **DLSS 4** com **geração multiquadros**, **GDDR7** |

### AMD Radeon: como ler o nome
**Radeon RX 9070 XT**
- **RX**: linha para consumidores.
- **9**: a geração (série 9000 = arquitetura **RDNA 4**, de **março de 2025**).
- **070**: a posição na linha (060 intermediária, 070 alta).
- **XT / XTX**: versões mais fortes.
- Tecnologias: **FSR** (*upscaling*; o **FSR 4**, da série 9000, usa IA), **AFMF** (geração de quadros) e **Radeon Anti-Lag**.

### Intel Arc
**Arc B580 / B570** (arquitetura **Battlemage**, de dezembro de 2024): placas de entrada com bom custo-benefício, **12 GB de VRAM** na B580 e *upscaling* **XeSS**.

### Por perfil de uso (2026)
| Perfil | Exemplos | VRAM recomendada |
|---|---|---|
| Escritório, vídeo, internet | Integrada | — |
| E-sports e jogos leves em 1080p | Integrada forte, RTX 3050, RX 6600 | 6–8 GB |
| Jogos em 1080p no alto | **RTX 5060**, **RX 9060 XT**, Arc B580 | **8–16 GB** (prefira 12–16 GB em 2026) |
| Jogos em 1440p | RTX 5060 Ti 16 GB, **RTX 5070**, **RX 9070 / 9070 XT** | 12–16 GB |
| 4K e criação pesada | **RTX 5080**, **RTX 5090** | 16–32 GB |
| IA local (imagens, LLMs) | RTX 5060 Ti 16 GB (entrada), RTX 5090 (32 GB) | **Quanto mais, melhor** (16 GB no mínimo) |

## Preço médio (Brasil, out/2026)

| Placa | Menor preço à vista (out/2026) |
|---|---|
| Intel Arc B580 12 GB | ≈ R$ 2.400 |
| **RTX 5060 8 GB** | **≈ R$ 2.400–2.700** |
| RX 9060 XT 8 GB | ≈ R$ 2.830 |
| **RX 9060 XT 16 GB** | **≈ R$ 2.800–3.700** |
| RTX 5060 Ti 16 GB | ≈ R$ 4.100–4.300 |
| RTX 5070 12 GB | ≈ R$ 5.100 |
| RX 9070 XT 16 GB | ≈ R$ 5.400 |
| RTX 5080 16 GB | ≈ R$ 11.400 |
| RTX 5090 32 GB | ≈ R$ 29.000 |

*Fontes: Pichau, no Pix, em 08/10/2026 (RTX 5060 a R$ 2.399 e RX 9060 XT 16 GB a R$ 2.799) e hardwarebarato.com em 28/10/2026. Os valores oscilam muito: a RX 9060 XT 16 GB variou de R$ 2.800 a R$ 3.700 no mesmo mês, e a RTX 5060 estava ≈ 48% acima da mínima de novembro de 2025. As versões **RTX 50 Super** foram adiadas por tempo indeterminado por causa da falta de memória.*

## Como saber se a placa de vídeo é compatível

| Verificação | Como conferir | Exemplo de problema |
|---|---|---|
| **1. Slot PCIe x16** | Praticamente toda placa-mãe moderna tem. PCIe 3.0, 4.0 e 5.0 são compatíveis entre si | Placas com **PCIe x8** (RTX 5060, RX 9060 XT) perdem um pouco de desempenho em placas-mãe **PCIe 3.0** |
| **2. Tamanho no gabinete** | Comparar o **comprimento** da GPU (ex.: 300 mm) com o **"max GPU length"** do gabinete, mais a **espessura em slots** (2, 2,5, 3 ou 3,5 slots) | Uma placa de 340 mm não cabe num gabinete que aceita só 300 mm |
| **3. Fonte (potência)** | Seguir a **fonte recomendada** pelo fabricante (ex.: RTX 5070 → 650 W; RTX 5090 → 1.000 W) | Fonte fraca → PC desliga em jogo |
| **4. Conectores de energia** | Ver se a fonte tem os cabos **PCIe 6+2 pinos** necessários ou o **12V-2x6** (nativo ou adaptador) | Placa que pede 3 × 8 pinos numa fonte com só dois cabos |
| **5. Processador (gargalo)** | Equilibrar: uma RTX 5080 com um processador de entrada antigo desperdiça a GPU | GPU trabalhando a 60% em jogo |
| **6. Monitor e cabos** | Para 1440p/4K em alta taxa, use **DisplayPort 1.4/2.1** ou **HDMI 2.1** | Monitor de 165 Hz preso a 60 Hz com cabo HDMI antigo |
| **7. BIOS em UEFI** | GPUs novas podem exigir boot em **UEFI** (sem o modo legado/CSM) | Tela preta em placas-mãe muito antigas |
| **8. Resizable BAR** | Ativar na BIOS (**Above 4G Decoding + ReBAR**); essencial para a Intel Arc | Arc com desempenho muito baixo sem ReBAR |

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **Superaquecimento** | GPU acima de 85–90 °C (ou *hotspot* acima de 100–105 °C), ventoinhas a toda, queda de FPS | Bom fluxo de ar no gabinete; limpeza | Limpar; ajustar a curva das ventoinhas; trocar a pasta e os pads térmicos (placas com mais de 3–4 anos) |
| **Artefatos na tela** | Quadrados, linhas, cores estranhas, "chuvisco" | Não exagerar no overclock; temperatura sob controle | Remover o overclock; testar em outro PC; se persistir em vários jogos e na área de trabalho, pode ser defeito de **VRAM** ou da GPU (garantia ou reparo especializado) |
| **Tela preta ou "sem sinal"** | Monitor não liga | Cabo ligado **na placa de vídeo**; conectores de energia encaixados | Conferir o cabo, a entrada do monitor e a energia da GPU; reencaixar no slot; atualizar a BIOS da placa-mãe |
| **Driver travando** | "O driver de vídeo parou de responder", tela piscando | Usar drivers estáveis | **Desinstalação limpa com DDU** (*Display Driver Uninstaller*) em modo de segurança e reinstalação do driver oficial |
| **Conector 12VHPWR derretido** | Cheiro de queimado, conector deformado (casos reais com RTX 4090 e 5090) | Encaixar **até o fim**, sem dobrar o cabo perto do conector (≥ 35 mm reto), usar o cabo nativo de uma boa fonte ATX 3.1 | **Desligar imediatamente**; trocar o cabo; verificar o conector da placa (acionar a garantia) |
| **PC desliga em jogo** | Reinício sob carga | Fonte com boa margem e de qualidade | Testar com outra fonte; usar **cabos separados** para cada conector PCIe (não use o "rabicho" *daisy chain* em placas de alto consumo) |
| **Placa "envergando" (*GPU sag*)** | Placa caída no lado oposto ao slot | Usar o **suporte** que acompanha a placa | Instalar suporte; verificar trincas no slot |
| **Coil whine** | Chiado agudo em FPS muito alto | — | É normal em alguns casos (as bobinas vibram); limitar o FPS reduz bastante |
| **Desempenho baixo** | FPS abaixo do esperado | Cabo de vídeo na GPU; slot x16 correto | Conferir se o slot está em x16; se o perfil de energia está em "desempenho"; se o notebook está usando a GPU dedicada (e não a integrada) |

:::exemplo Exemplo de bancada: "comprei uma placa de vídeo e o jogo continua igual"
O cliente instalou uma RTX nova, mas o FPS não mudou. Diagnóstico: o **cabo HDMI estava ligado na placa-mãe**. Como o processador tinha vídeo integrado, o Windows desenhava tudo pela **iGPU** e a placa nova ficava ociosa. Trocar o cabo para a GPU resolveu e multiplicou o FPS por **cinco**.
:::

:::dica Ferramentas para placa de vídeo
**GPU-Z** (identifica a placa e mostra clocks, temperatura e se o slot está em x16), **MSI Afterburner** + **RivaTuner** (monitorar e ajustar), **HWiNFO64**, **DDU** (limpar drivers), **3DMark** e **FurMark** (testes de estresse).
:::
