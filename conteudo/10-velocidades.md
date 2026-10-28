Se bits e bytes medem **quanto**, hertz e bits por segundo medem **quão rápido**. São as unidades mais citadas nas propagandas (e as mais mal entendidas). Vamos desmontar cada uma.

## Hertz (Hz)

### O que é
**Hertz** é a unidade de **frequência**: o número de **ciclos (repetições) por segundo**.
- 1 Hz = 1 ciclo por segundo
- 1 kHz (quilohertz) = 1.000 Hz
- 1 MHz (megahertz) = 1.000.000 Hz
- 1 GHz (gigahertz) = 1.000.000.000 Hz

Nas frequências, o prefixo é **sempre decimal** (1.000), nunca 1.024.

### De onde veio
O nome homenageia o físico alemão **Heinrich Rudolf Hertz** (1857–1894), que em **1887** provou experimentalmente a existência das **ondas eletromagnéticas** previstas por James Clerk Maxwell, base do rádio, do Wi-Fi e do celular. A unidade foi adotada pela IEC em 1930 e pelo Sistema Internacional (SI) em **1960**, substituindo o antigo "ciclos por segundo" (cps).

### Hertz no computador: o clock
Dentro do computador, um **cristal de quartzo** vibra numa frequência fixa (normalmente 25 MHz ou 100 MHz) e gera um sinal de "batida", o **clock base**. Circuitos chamados **PLL** multiplicam essa frequência para chegar a vários GHz.

Cada "batida" do clock é um **ciclo**. A cada ciclo, a CPU avança uma etapa do seu trabalho. Pense num **metrônomo** ditando o ritmo para uma orquestra inteira.

:::exemplo Exemplo: o que significa um processador de 5 GHz
5 GHz = **5 bilhões de ciclos por segundo**. Cada ciclo dura 1 ÷ 5.000.000.000 = **0,2 nanossegundo**. Nesse tempo, a luz percorre apenas **6 centímetros**. É por isso que as trilhas da placa-mãe precisam ser tão curtas e bem desenhadas.
:::

### MHz: megahertz
- **Valor**: 1 milhão de ciclos por segundo.
- **Onde aparece**:
  - Clock dos processadores antigos: Intel 8088 do IBM PC = **4,77 MHz**; Pentium (1993) = 60–66 MHz; Pentium III (1999) = 450 MHz a 1 GHz.
  - **Memória RAM**: "DDR4-3200" ou "DDR5-6000". Tecnicamente esses números são **MT/s** (megatransferências por segundo), mas o comércio usa "MHz". Na DDR, há **duas transferências por ciclo**, então a DDR5-6000 tem clock real de **3.000 MHz**.
  - **Rádio FM**: 87,5–108 MHz.
  - Placas de vídeo (clock do núcleo): 1.500–2.900 MHz.

### GHz: gigahertz
- **Valor**: 1 bilhão de ciclos por segundo.
- **Onde aparece**:
  - **Processadores modernos**: 3–6 GHz. O primeiro processador comercial a chegar a **1 GHz** foi o **AMD Athlon**, em **março de 2000**, dias antes da Intel.
  - **Wi-Fi**: bandas de **2,4 GHz**, **5 GHz** e **6 GHz**.
  - **Celular 5G**: faixas de 3,5 GHz (a principal no Brasil) e ondas milimétricas acima de 24 GHz.
  - **Forno de micro-ondas**: 2,45 GHz, a mesma faixa do Wi-Fi de 2,4 GHz. Por isso o micro-ondas ligado pode atrapalhar a rede.

### Clock alto ≠ processador mais rápido
Este é um erro clássico. O desempenho de uma CPU depende de:

**Desempenho ≈ Clock (GHz) × IPC × Número de núcleos (conforme o software usa)**

- **IPC** (*Instructions Per Clock*): quantas instruções a CPU executa **por ciclo**. Uma arquitetura nova faz mais trabalho em cada batida.
- **Núcleos e threads**: quantas tarefas em paralelo.
- **Cache**: quanto a CPU espera pela memória.

:::exemplo Exemplo: o caso Pentium 4
Em 2004, o **Pentium 4** chegava a **3,8 GHz**. Em 2006, o **Core 2 Duo** de **2,4 GHz** era **mais rápido** que ele, porque fazia muito mais trabalho por ciclo (IPC maior) e tinha dois núcleos. A Intel abandonou a "corrida dos GHz" justamente por isso. Hoje, um Core i5 de 2026 a 4,5 GHz é **várias vezes** mais rápido que um Core i7 de 2012 também a 4,5 GHz.
:::

### Hz no monitor: taxa de atualização
No monitor, os hertz indicam **quantas vezes por segundo a imagem é redesenhada**:
- **60 Hz**: o padrão de escritório.
- **144–165 Hz**: o padrão gamer de entrada.
- **240–540 Hz**: monitores de e-sports.

Para aproveitar um monitor de 144 Hz, a placa de vídeo precisa entregar **144 FPS** (quadros por segundo). FPS é da GPU; Hz é do monitor.

## Velocidade de dados: bps, kbps, Mbps, Gbps

### O que é
**bps** = **bits por segundo**. É a unidade de **taxa de transmissão** de dados: velocidade de internet, de rede, de cabos e de barramentos seriais.

| Unidade | Valor | Exemplo |
|---|---|---|
| **bps** | 1 bit/s | — |
| **kbps** | 1.000 bits/s | Modem discado: 56 kbps; MP3: 128–320 kbps |
| **Mbps** | 1.000.000 bits/s | Internet residencial: 100–1.000 Mbps |
| **Gbps** | 1.000.000.000 bits/s | Fibra de 1 Gbps, rede Gigabit, USB 3.2 (5–20 Gbps) |

Aqui também os prefixos são **decimais** (1.000).

### A confusão nº 1: Mbps × MB/s
O provedor vende em **megabits por segundo (Mbps)**. O navegador, a Steam e o Windows mostram o download em **megabytes por segundo (MB/s)**. Como 1 byte = 8 bits:

> **MB/s = Mbps ÷ 8**

| Plano contratado | Velocidade máxima de download real (≈) |
|---|---|
| 50 Mbps | 6,25 MB/s |
| 100 Mbps | 12,5 MB/s |
| 300 Mbps | 37,5 MB/s |
| 500 Mbps | 62,5 MB/s |
| 1 Gbps | 125 MB/s |

Na prática, tire mais **5% a 10%** pelo "custo" dos protocolos (cabeçalhos dos pacotes TCP/IP).

:::exemplo Exemplo resolvido: quanto tempo para baixar um jogo de 100 GB com fibra de 500 Mbps?
1. Converta o plano: 500 Mbps ÷ 8 = **62,5 MB/s**.
2. Considere ≈ 90% de eficiência: ≈ **56 MB/s**.
3. Converta o jogo: 100 GB = **100.000 MB**.
4. Tempo: 100.000 ÷ 56 ≈ **1.786 segundos ≈ 30 minutos**.

Se o cliente reclamar que "a internet de 500 está baixando a 60", ela está **perfeita**: são 60 MB/s, não 60 Mbps.
:::

### Outras medidas de rede que importam
| Medida | O que é | Valor bom | Afeta |
|---|---|---|---|
| **Download** | Velocidade de receber dados | Conforme o plano | Streaming, downloads |
| **Upload** | Velocidade de enviar dados | ≥ 50% do download na fibra | Videochamada, backup, live |
| **Latência (ping)** | Tempo de ida e volta de um pacote, em **ms** | < 20 ms (fibra); < 50 ms (jogos ok) | Jogos online, chamadas |
| **Jitter** | Variação da latência | < 5–10 ms | Chamadas travando, áudio robótico |
| **Perda de pacotes** | % de pacotes que não chegam | 0% | Travadas, desconexões |

:::exemplo Exemplo: por que a internet "rápida" trava no jogo
Uma conexão via satélite geoestacionário pode ter 100 Mbps de download e **600 ms de ping**: ótima para Netflix e péssima para jogo online. Já uma fibra de 100 Mbps com **8 ms de ping** é excelente para jogar. **Para jogos, o ping importa mais que os megas.**
:::

## Velocidades de armazenamento e barramentos (MB/s e GB/s)

Dentro do PC, a velocidade costuma ser medida em **bytes** por segundo:

| Dispositivo ou barramento | Velocidade típica |
|---|---|
| HD 7.200 rpm | 80–250 MB/s (sequencial) |
| SSD SATA | até ≈ 550 MB/s |
| SSD NVMe PCIe 3.0 | até ≈ 3.500 MB/s |
| SSD NVMe PCIe 4.0 | até ≈ 7.500 MB/s |
| SSD NVMe PCIe 5.0 | até ≈ 14.000–15.000 MB/s |
| Memória DDR5-6000 (dual channel) | ≈ 96 GB/s (teórico) |
| VRAM GDDR7 de uma GPU de ponta | > 1.500 GB/s |

:::dica Fórmula de bolso para memória
**Largura de banda (GB/s) = MT/s × 8 bytes × número de canais ÷ 1.000**
DDR5-6000 em dual channel: 6.000 × 8 × 2 ÷ 1.000 = **96 GB/s**.
:::

## Outras unidades que aparecem em fichas técnicas

| Unidade | O que mede | Onde aparece |
|---|---|---|
| **FPS** | Quadros por segundo | Jogos, vídeo (24, 30, 60 FPS) |
| **ms** (milissegundo) | Tempo (milésimo de segundo) | Ping, tempo de resposta de monitor (1–5 ms) |
| **ns** (nanossegundo) | Tempo (bilionésimo de segundo) | Latência da RAM (≈ 10–15 ns) |
| **rpm** | Rotações por minuto | HD (5.400 / 7.200 rpm), cooler (500–3.000 rpm) |
| **IOPS** | Operações de entrada e saída por segundo | SSD (de centenas de milhares a mais de 1 milhão) |
| **FLOPS** | Operações de ponto flutuante por segundo | GPUs e supercomputadores (TFLOPS, PFLOPS, EFLOPS) |
| **TOPS** | Trilhões de operações por segundo (normalmente em inteiros de 8 bits) | NPUs de notebooks "Copilot+ PC" (≥ 40 TOPS) |
| **dB / dBA** | Nível de ruído | Coolers e fontes (20–40 dBA) |
| **CFM** | Vazão de ar (pés cúbicos por minuto) | Ventoinhas |
| **mm H₂O** | Pressão estática | Ventoinhas de radiador |
| **nits (cd/m²)** | Brilho | Monitores (250–1.000+ nits) |
| **PPI** | Pixels por polegada | Nitidez de telas |
