## O que é

A **fonte de alimentação** (*PSU*, *Power Supply Unit*) é o componente que **converte a energia da tomada** (corrente alternada de 127 V ou 220 V) nas **tensões contínuas e baixas** que os componentes usam: **+12 V**, **+5 V** e **+3,3 V** (mais a **+5 VSB**, de *standby*).

Ela é, provavelmente, **a peça mais subestimada do PC**, e uma das mais importantes. Uma fonte ruim pode **levar outras peças junto** quando falha.

:::especialista Ditado de bancada
Entre técnicos e revisores de hardware, repete-se há décadas: **"a fonte é a última peça em que você deve economizar"**. Uma fonte genérica pode custar R$ 100 a menos, mas uma falha pode queimar placa-mãe, SSD e GPU somando milhares de reais.
:::

## Para que serve: sua função no computador

1. **Converter CA em CC** (retificação e filtragem).
2. **Reduzir e estabilizar a tensão** em níveis precisos (variação máxima tolerada pela norma ATX: **±5%** nos trilhos principais).
3. **Fornecer potência suficiente** para todas as peças, inclusive nos **picos de consumo** (as GPUs modernas têm picos de milissegundos muito acima do consumo médio).
4. **Proteger** o computador contra sobretensão, curto, sobrecarga e superaquecimento.
5. **Manter o "standby"** (5 VSB) para que o PC ligue pelo botão, pelo teclado ou pela rede (*Wake-on-LAN*).

:::exemplo Exemplo: a fonte nas tarefas do dia a dia
- **Navegando com 20 abas**: o PC consome ≈ 60–120 W; a fonte trabalha folgada.
- **Exportando vídeo**: a CPU vai a 100%, e o consumo sobe para 200–350 W.
- **Jogando ou gerando imagens com IA**: a GPU puxa de 150 a 575 W, com **picos transitórios** que podem chegar ao **dobro** por milissegundos. Uma fonte fraca ou de má qualidade aciona a proteção, e o **PC desliga de repente**.
:::

## Onde fica e como é

- **Onde**: normalmente na **parte de baixo e traseira** do gabinete (nos gabinetes antigos, no topo), com a **ventoinha virada para baixo** (puxando ar frio pelo filtro inferior) e a tomada saindo pela traseira.
- **Como é**: uma **caixa metálica** (padrão ATX: 150 × 86 mm de frente, com profundidade de 140 a 200 mm), com ventoinha, **interruptor liga/desliga**, **entrada de cabo de força (IEC C14)** e o **feixe de cabos** (ou os conectores, nas modulares).
- **SFX / SFX-L**: fontes menores para PCs compactos.

## Como funciona por dentro (fonte chaveada, ou SMPS)

```
TOMADA ─► [Filtro EMI] ─► [Retificador + PFC ativo] ─► [Capacitor de ≈ 400 V]
 127/220 V CA                                                  │
                                                               ▼
              [Transistores chaveando a ≈ 50–150 kHz] ─► [Transformador]
                                                               │
                                                               ▼
                           [Retificação + filtragem do secundário]
                                                               │
                                          ┌────────────┬───────┴─────┐
                                          ▼            ▼             ▼
                                        +12 V        +5 V         +3,3 V
                                   (CPU, GPU,    (USB, SATA)   (RAM, M.2)
                                    ventoinhas)
```

1. **Filtro EMI**: bloqueia o ruído elétrico de entrar e de sair da fonte.
2. **Retificador + PFC ativo** (*Power Factor Correction*): transforma CA em CC e melhora o aproveitamento da energia. O **PFC ativo** permite trabalhar em **100–240 V automaticamente** (a fonte **bivolt automática**).
3. **Capacitor principal**: armazena energia em **≈ 400 V CC**. É por isso que **nunca se deve abrir uma fonte**: ele pode manter a carga por minutos.
4. **Chaveamento**: transistores (MOSFETs) ligam e desligam dezenas de milhares de vezes por segundo, o que permite usar um **transformador pequeno**.
5. **Transformador**: reduz a tensão e isola o lado da tomada (primário) do lado do PC (secundário).
6. **Secundário**: retifica e filtra para gerar **12 V**. Nas fontes modernas, **conversores DC-DC** geram os 5 V e os 3,3 V a partir dos 12 V, com mais precisão.
7. **Supervisão**: um chip monitora tudo e aciona as **proteções** e o sinal **Power Good**.

### As proteções que uma boa fonte deve ter
| Sigla | Nome | Protege contra |
|---|---|---|
| **OVP** | *Over Voltage Protection* | Tensão de saída alta demais |
| **UVP** | *Under Voltage Protection* | Tensão de saída baixa demais |
| **OCP** | *Over Current Protection* | Corrente excessiva num trilho |
| **OPP / OLP** | *Over Power / Over Load* | Potência total acima do limite |
| **SCP** | *Short Circuit Protection* | Curto-circuito |
| **OTP** | *Over Temperature Protection* | Superaquecimento da fonte |
| **SIP / NLO** | *Surge & Inrush Protection / No Load Operation* | Pico na ligação / funcionar sem carga |

## Do que é feita (material)

| Parte | Material |
|---|---|
| Carcaça | **Aço** galvanizado ou pintado |
| Placa de circuito | Fibra de vidro com cobre |
| Capacitores | Eletrolíticos de alumínio (os melhores são **japoneses**: Nippon Chemi-Con, Rubycon, Nichicon, rated **105 °C**) e de polímero sólido |
| Transformador e bobinas | Núcleo de **ferrite** com fio de **cobre** esmaltado |
| Semicondutores | MOSFETs e diodos de **silício**; nas fontes premium, transistores de **nitreto de gálio (GaN)** |
| Dissipadores internos | Alumínio |
| Ventoinha | Plástico e motor de cobre/ímã |
| Cabos | Cobre com isolamento de PVC, bitola **18 AWG** (16 AWG nos melhores) |

## Tipos de fonte

### Por formato
| Formato | Tamanho | Uso |
|---|---|---|
| **ATX** | 150 × 86 × 140+ mm | O padrão dos desktops |
| **SFX / SFX-L** | 125 × 63,5 × 100 / 130 mm | PCs Mini-ITX |
| **TFX / Flex ATX** | Estreitas e longas | PCs slim e de marca |
| **Fonte externa (adaptador / "carregador")** | — | Notebooks, mini PCs |
| **Proprietárias** | Variável | Dell, HP, Lenovo (às vezes com conector 10 ou 12 pinos, padrão **ATX12VO**) |
| **Redundante (servidor)** | Módulos *hot-swap* | Servidores |

### Por modularidade
| Tipo | Como é | Vantagem |
|---|---|---|
| **Não modular** | Todos os cabos presos | Mais barata |
| **Semimodular** | Cabos principais (24 pinos e CPU) presos; o resto, removível | Bom custo-benefício |
| **Totalmente modular** | Todos os cabos removíveis | Organização máxima |

:::atencao Nunca misture cabos modulares de fontes diferentes
Os conectores do **lado da fonte não têm padrão** entre marcas (nem entre modelos da mesma marca). Usar o cabo de outra fonte pode inverter tensões e **queimar** o SSD, o HD ou a placa-mãe na hora. Esse é um dos piores erros de bancada.
:::

### Por certificação de eficiência: 80 PLUS
A **eficiência** é a porcentagem da energia retirada da tomada que vira energia útil para o PC (o resto vira **calor**). O programa **80 PLUS** (criado em **2004**) certifica fontes por nível. Valores para a rede de **115 V** interna (padrão americano, usado na certificação):

| Selo | 10% de carga | 20% de carga | **50% de carga** | 100% de carga |
|---|---|---|---|---|
| **80 PLUS** (o "Standard", apelidado de "White") | — | 80% | 80% | 80% |
| **Bronze** | — | 82% | **85%** | 82% |
| **Silver** | — | 85% | **88%** | 85% |
| **Gold** | — | 87% | **90%** | 87% |
| **Platinum** | — | 90% | **92%** | 89% |
| **Titanium** | 90% | 92% | **94%** | 90% |
| **Ruby** (novo nível) | 91% | 93% | **95%** | 91% |

Há também o selo **Cybenetics** (ETA para eficiência e LAMBDA para ruído), considerado **mais rigoroso** pelos revisores.

:::exemplo Exemplo: o que a eficiência significa na conta de luz
Um PC precisa de **400 W**:
- Com fonte **80% eficiente**: tira 400 ÷ 0,80 = **500 W** da tomada (100 W viram calor).
- Com fonte **90% eficiente (Gold)**: tira 400 ÷ 0,90 = **444 W** (44 W viram calor).

Diferença de **56 W**. Em 4 h por dia durante um ano: 56 × 4 × 365 = **82 kWh ≈ R$ 82 por ano** de economia (a R$ 1,00/kWh), além de **menos calor e menos ruído**.
:::

:::atencao Selo não é sinônimo de qualidade
O 80 PLUS mede **só a eficiência**. Ele **não** garante proteções, qualidade dos capacitores, estabilidade das tensões nem baixo ruído elétrico (*ripple*). Para escolher uma fonte, consulte **listas de qualidade de fontes** (as *PSU Tier Lists* dos fóruns e *reviews* técnicos com testes de carga), e não só o selo.
:::

### ATX 3.0 / 3.1 e o conector 12V-2x6
- **ATX 3.0 (2022)** e **ATX 3.1 (2023)**: normas da Intel para as GPUs modernas. A fonte precisa aguentar **picos de até 200%** da potência nominal por 100 µs e traz o conector **12VHPWR**, que na revisão 3.1 virou **12V-2x6** (com pinos sensores encurtados, para maior segurança), capaz de entregar **até 600 W** num único cabo.
- Para RTX 4070 e acima, ou RX 9070 e acima, **prefira fontes ATX 3.1**.

## Como calcular a potência necessária

1. **Some o consumo** da CPU (use o consumo máximo, PPT/PL2) + a GPU (TGP/TBP) + ≈ **50–100 W** para placa-mãe, RAM, SSDs e ventoinhas.
2. **Acrescente 30–50% de margem**: a fonte trabalha mais **eficiente e silenciosa** entre 40% e 70% de carga, e a margem absorve picos e o envelhecimento dos capacitores.
3. Confira a **fonte recomendada pelo fabricante da GPU**.

:::exemplo Exemplo resolvido: PC com Ryzen 5 7600 + RTX 5070
- CPU (Ryzen 5 7600, PPT): ≈ **88 W**
- GPU (RTX 5070, TGP): ≈ **250 W**
- Restante do sistema: ≈ **75 W**
- **Total**: ≈ **413 W**
- Com 40% de margem: 413 × 1,4 ≈ **580 W**
- **Recomendação**: fonte de **650 W**, **80 PLUS Gold** (ou Bronze de boa linha), **ATX 3.1** (a NVIDIA recomenda **650 W** para a RTX 5070).
:::

| Perfil de PC | Fonte recomendada (2026) |
|---|---|
| Escritório (vídeo integrado) | 350–450 W, 80 PLUS (marca confiável) |
| Gamer de entrada (RTX 5060 / RX 9060 XT) | 550–650 W, Bronze ou Gold |
| Gamer intermediário (RTX 5070 / RX 9070 XT) | 650–750 W, **Gold**, ATX 3.1 |
| Gamer alto (RTX 5080) | 850 W, Gold, ATX 3.1 |
| Topo (RTX 5090 + Ryzen 9 / Core Ultra 9) | **1.000–1.200 W**, Gold ou Platinum, ATX 3.1 |

## Preço médio (Brasil, out/2026)

| Categoria | Faixa de preço (out/2026) |
|---|---|
| Fonte "genérica" (sem certificação, potência "de etiqueta") | R$ 60–150 (**evite**) |
| 500 W de entrada (marcas populares) | R$ 115–250 |
| 500–650 W, 80 PLUS Bronze, boa linha | R$ 250–500 |
| 750 W **Gold** | a partir de ≈ R$ 340–390 em promoção; R$ 450–800 o comum |
| 850 W Gold, ATX 3.1 (ex.: XPG Kyber II 850 W) | a partir de ≈ R$ 470; R$ 600–1.000 o comum |
| 1.000–1.200 W Gold/Platinum, ATX 3.1 | R$ 560–2.200 |

*Fonte: menores preços à vista em agregadores, out/2026. Fontes boas em promoção estão baratas em relação a RAM e SSD, o que é mais um motivo para não economizar nelas.*

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **PC não liga** | Nada acontece | Fonte de qualidade; interruptor traseiro em "I" | Conferir a tomada, o cabo e o interruptor; **teste do clipe** (*paperclip test*): com a fonte **desligada da tomada**, ligue o fio **verde (PS_ON)** a um fio **preto (GND)** no conector de 24 pinos, ligue a fonte na tomada; se a ventoinha girar, a fonte "liga" (mas isso **não prova** que as tensões estão corretas). Use um **testador de fonte** ou multímetro |
| **PC desliga ou reinicia em jogo** | Desligamento sob carga | Potência adequada e ATX 3.x | Testar com outra fonte; verificar se a GPU está ligada com cabos separados |
| **Cheiro de queimado / estalo** | — | Não usar fontes genéricas; DPS e filtro de linha | **Desligar da tomada imediatamente**; não religar; trocar a fonte e testar as outras peças |
| **Fonte "chiando" ou zumbindo** | Ruído de bobina ou de ventoinha | Fonte de qualidade | Se for a ventoinha, limpar; se for ruído elétrico forte, trocar |
| **Ventoinha da fonte parada** | Superaquecimento | Muitas fontes têm **modo semipassivo** (a ventoinha fica parada em carga baixa, o que é **normal**) | Verificar sob carga; se não girar quando esquenta, trocar a fonte |
| **Fonte superaquecendo** | Desligamentos | Ventoinha virada para o filtro inferior, com o gabinete **elevado do chão** (não sobre carpete) | Limpar o filtro; reposicionar |
| **Chave 127/220 V errada** (fontes antigas, sem PFC ativo) | Em 220 V com a chave em 127 V: a fonte **queima na hora** | Preferir fontes **bivolt automáticas** (PFC ativo) | Trocar a fonte (e torcer para ter levado só ela) |
| **Tensões fora do padrão** | Instabilidade, HDs desconectando, USB falhando | Fonte de qualidade | Medir no HWiNFO (estimativa) ou com multímetro (12 V deve ficar entre 11,4 e 12,6 V) |

:::atencao Nunca abra uma fonte
Mesmo desligada da tomada, o **capacitor do primário pode guardar cerca de 400 V por minutos**. Conserto de fonte é trabalho para **técnico de eletrônica especializado**, com descarga controlada dos capacitores. Para o técnico de PC, fonte com defeito **se troca**, não se abre.
:::
