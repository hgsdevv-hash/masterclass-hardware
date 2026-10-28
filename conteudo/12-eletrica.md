Todo hardware é, antes de tudo, um **circuito elétrico**. Quem entende o básico de eletricidade diagnostica fonte queimada, escolhe estabilizador (ou descobre que não precisa dele), calcula o consumo do PC e, principalmente, **não leva choque nem queima peça**. Esta é a aula de elétrica que todo técnico deveria ter tido no primeiro dia.

## A analogia da caixa-d'água

A forma mais fácil de entender eletricidade é compará-la com **água num cano**:

| Grandeza elétrica | Símbolo / unidade | Analogia com água |
|---|---|---|
| **Tensão** (diferença de potencial) | **V**, volt | A **pressão** da água (a altura da caixa-d'água) |
| **Corrente** | **I**, ampère (A) | A **quantidade** de água passando por segundo |
| **Resistência** | **R**, ohm (Ω) | O **estreitamento** do cano, que dificulta a passagem |
| **Potência** | **P**, watt (W) | O **trabalho** que a água faz (girar uma roda-d'água) |
| **Energia** | watt-hora (Wh), kWh | O **total** de água gasto no mês (o que vem na conta) |

## Volt (V): tensão

### O que é
**Tensão** é a "força" que **empurra** os elétrons por um circuito. Tecnicamente, é a **diferença de potencial elétrico** entre dois pontos. Sem diferença de tensão, não há corrente, assim como sem desnível a água não corre.

### Como surgiu
O nome homenageia o italiano **Alessandro Volta** (1745–1827), que em **1800** inventou a **pilha voltaica**, a primeira fonte de **corrente contínua** da história: discos alternados de zinco e cobre separados por pano molhado em salmoura. A unidade "volt" foi adotada em **1881**.

### Valores do dia a dia
| Fonte | Tensão |
|---|---|
| Pilha AA | 1,5 V |
| Bateria de celular (íon-lítio) | ≈ 3,7–3,85 V (nominal) |
| Porta USB padrão | 5 V (USB-C Power Delivery: até 48 V) |
| Bateria de carro | 12 V |
| Tomada no Brasil | **127 V** ou **220 V**, conforme a região |
| Tensões dentro do PC (fonte ATX) | **+12 V**, **+5 V**, **+3,3 V** |
| Núcleo do processador | ≈ 0,7–1,5 V |
| Memória DDR5 | 1,1 V |

:::atencao 127 V ou 220 V: o Brasil tem as duas
O Brasil **não tem tensão padrão única**. Cidades de SP, RJ, MG, PR e Amazonas, por exemplo, usam majoritariamente **127 V** (chamado popularmente de "110"). DF, SC, GO, CE, PE, RN e outros estados usam **220 V**. Muitas residências têm as duas tensões. **Sempre meça com multímetro** ou confirme com a distribuidora antes de ligar um equipamento que não seja bivolt.
:::

## Ampère (A): corrente

### O que é
**Corrente** é a **quantidade de carga elétrica** (elétrons) que passa por um ponto do circuito **a cada segundo**. 1 ampère = 1 coulomb por segundo ≈ 6,24 × 10¹⁸ elétrons por segundo.

### Como surgiu
Homenagem ao francês **André-Marie Ampère** (1775–1836), que descobriu a relação entre eletricidade e magnetismo em **1820**.

### Corrente contínua (CC/DC) × alternada (CA/AC)
| | **Corrente contínua (CC / DC)** | **Corrente alternada (CA / AC)** |
|---|---|---|
| Como é | Flui sempre no mesmo sentido | Inverte o sentido periodicamente |
| Frequência | 0 Hz | **60 Hz no Brasil** (50 Hz na Europa) |
| Onde está | Pilhas, baterias, **tudo dentro do PC** | Tomada da parede |
| Quem defendeu | Thomas Edison | Nikola Tesla e George Westinghouse ("Guerra das Correntes", 1880–1890) |

A **fonte do computador** existe justamente para **transformar a CA da tomada (127/220 V) em CC de baixa tensão (12, 5 e 3,3 V)**. Veremos isso no módulo da Fonte.

### Por que a corrente é perigosa
**O que mata não é a tensão, é a corrente que passa pelo corpo**, mas é a tensão que empurra essa corrente:
- **1 mA**: formigamento.
- **10–20 mA**: contração muscular; a pessoa pode não conseguir soltar o fio.
- **50–100 mA** passando pelo coração: **fibrilação ventricular**, potencialmente fatal.

Por isso: **nunca abra uma fonte ATX ligada na tomada**, e tenha cuidado mesmo com ela desligada. Os **capacitores do primário** podem guardar mais de **300 V** por minutos depois de desconectados.

## Ohm (Ω): resistência

### O que é
**Resistência** é a **oposição** que um material oferece à passagem da corrente.
- **Condutores** (baixa resistência): cobre, ouro, prata, alumínio.
- **Isolantes** (altíssima resistência): borracha, plástico, vidro, ar seco.
- **Semicondutores** (no meio do caminho, controláveis): **silício** e germânio, a base dos transistores.

### A Lei de Ohm
O físico alemão **Georg Simon Ohm** publicou em **1827** a relação mais importante da eletricidade:

> **V = R × I**   (Tensão = Resistência × Corrente)

Ou, de forma equivalente: **I = V ÷ R** e **R = V ÷ I**.

:::exemplo Exemplo: Lei de Ohm na prática
Um LED de gabinete precisa de 20 mA (0,02 A) e você vai ligá-lo nos 5 V da fonte. O LED "consome" cerca de 2 V; sobram **3 V** para o resistor.
R = V ÷ I = 3 ÷ 0,02 = **150 Ω**. Sem esse resistor, a corrente dispara e o LED queima na hora.
:::

## Watt (W): potência

### O que é
**Potência** é a **velocidade com que a energia é usada ou transformada** (em luz, calor, movimento ou processamento). 1 watt = 1 joule por segundo.

> **P = V × I**   (Potência = Tensão × Corrente)

Combinando com a Lei de Ohm: **P = R × I²** e **P = V² ÷ R**.

### Como surgiu
Homenagem ao escocês **James Watt** (1736–1819), que aperfeiçoou a **máquina a vapor** e motivou a Revolução Industrial. Ele também criou a unidade **"cavalo-vapor"** (HP), para comparar suas máquinas com cavalos (1 HP ≈ 746 W). A unidade watt foi adotada em **1889**.

### Consumo típico dos componentes
| Componente | Consumo típico |
|---|---|
| Processador de entrada (65 W de TDP) | 45–90 W em carga |
| Processador topo de linha | 150–250 W ou mais em carga |
| Placa de vídeo de entrada (RTX 5060) | ≈ 145 W |
| Placa de vídeo topo (RTX 5090) | ≈ 575 W |
| Placa-mãe | 30–80 W |
| Cada pente de memória DDR5 | 3–10 W |
| SSD NVMe | 3–9 W |
| HD 3,5" | 5–10 W (até 25 W na partida) |
| Cada ventoinha | 1–3 W |
| Monitor de 24" | 15–30 W |

:::exemplo Exemplo: calcular a corrente que o PC puxa da tomada
Um PC gamer consome **500 W** da tomada em 127 V:
I = P ÷ V = 500 ÷ 127 ≈ **3,9 A**. Em 220 V: 500 ÷ 220 ≈ **2,3 A**.
Uma tomada padrão brasileira de **10 A** aguenta até ≈ 1.270 W em 127 V, então o PC está bem dentro do limite. Já um **benjamim** com PC, monitor, impressora a laser e aquecedor pode passar de 10 A e **derreter**.
:::

## kWh: quanto o computador custa na conta de luz

**Energia (kWh) = Potência (kW) × Tempo (h)**

:::exemplo Exemplo resolvido: custo mensal de um PC gamer
- Consumo médio jogando: **400 W** = 0,4 kW.
- Uso: **4 horas por dia × 30 dias** = 120 horas.
- Energia: 0,4 × 120 = **48 kWh por mês**.
- Tarifa residencial com impostos: ≈ **R$ 0,95–1,10/kWh** em out/2026, com bandeira verde (varia por distribuidora). Usando **R$ 1,00/kWh**: 48 × 1,00 ≈ **R$ 48 por mês**.

Um PC de escritório (≈ 80 W, 8 h/dia, 22 dias): 0,08 × 176 = 14 kWh ≈ **R$ 14 por mês**.
:::

## Aterramento: o fio que salva vidas e peças

### O que é
O **aterramento** é um condutor ligado a uma **haste metálica enterrada no solo**. Ele oferece um caminho seguro para correntes de fuga e descargas, que vão para a terra em vez de passar por você.

### A tomada brasileira (padrão NBR 14136)
O Brasil criou em **2002** o padrão **NBR 14136**, de **três pinos**, obrigatório desde **2011**:
- **Fase**: o fio "vivo", com tensão.
- **Neutro**: o retorno da corrente.
- **Terra**: o pino central (deslocado), de **proteção**.

Os pinos têm dois diâmetros: **4,0 mm para 10 A** e **4,8 mm para 20 A**. Um plugue de 20 A não entra numa tomada de 10 A, de propósito.

:::atencao Nunca corte o pino terra
Quebrar o terceiro pino para "caber" na tomada velha elimina a proteção. Se o gabinete tiver uma fuga, ele pode dar choque, e a fonte perde o caminho de escoamento do filtro de ruído. O certo é **trocar a tomada** e fazer o aterramento correto (com eletricista).
:::

:::dica Como testar o aterramento com multímetro
Na escala de tensão AC (≈ 750 V):
- Fase × Neutro: ≈ 127 V (ou 220 V).
- Fase × Terra: ≈ o mesmo valor.
- **Neutro × Terra: até ≈ 2–5 V** indica aterramento bom. Se for maior, ou se Fase × Terra der zero, **o terra não está funcionando**.
:::

## Proteções elétricas: o que realmente protege o PC

| Equipamento | O que faz | Protege contra | Vale a pena? |
|---|---|---|---|
| **Filtro de linha (com varistor e fusível)** | Corta picos e protege contra curto | Picos breves, sobrecorrente | ✅ Sim, mas escolha um com **varistor** (MOV); muitos baratos são só "régua" |
| **Estabilizador** | Tenta manter a tensão estável com relés | Variações lentas de tensão | ⚠️ Em geral **não** para PCs modernos: fontes com **PFC ativo** já trabalham de 100 a 240 V. Estabilizadores baratos podem até piorar a energia |
| **Nobreak (UPS)** | Tem bateria e mantém o PC ligado na falta de luz | Queda de energia, picos, oscilações | ✅ Sim, se você não pode perder trabalho. Prefira **senoidal / interativo** para fontes com PFC ativo |
| **DPS (Dispositivo de Proteção contra Surtos)** | Instalado no quadro de energia | Surtos de raio na rede | ✅ Excelente para a casa toda (instalação por eletricista) |

:::especialista O que dizem os especialistas sobre estabilizadores
Sites técnicos brasileiros de referência, como o **Clube do Hardware** (fundado por Gabriel Torres), e diversos engenheiros eletricistas alertam há anos que **fontes ATX de qualidade, com PFC ativo, dispensam estabilizador**. O investimento vai melhor numa **boa fonte** com certificação e proteções (OVP, UVP, OCP, SCP, OTP), num **filtro de linha com varistor** e, se possível, num **nobreak**.
:::

## Multímetro: a ferramenta básica

| Função | Símbolo | Para que serve no hardware |
|---|---|---|
| Tensão contínua | **V⎓** (DCV) | Medir as saídas 12 / 5 / 3,3 V da fonte, a bateria CR2032 (≈ 3 V) |
| Tensão alternada | **V~** (ACV) | Medir a tomada |
| Resistência | **Ω** | Testar fusíveis, cabos, curtos |
| Continuidade | **🔊** (bip) | Ver se um cabo ou trilha está rompido |
| Corrente | **A** | Raramente usado em bancada de PC (exige abrir o circuito) |

:::exemplo Exemplo: testar a bateria da placa-mãe (CR2032)
Uma CR2032 nova mede ≈ **3,0–3,3 V**. Abaixo de ≈ **2,8 V**, ela já pode fazer a BIOS **perder a data e as configurações** toda vez que o PC é tirado da tomada. Troca simples e barata (≈ R$ 5–15).
:::
