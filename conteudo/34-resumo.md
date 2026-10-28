Este é o **resumo geral** da masterclass: tudo o que você precisa lembrar, módulo por módulo, para revisar antes de uma prova, de uma entrevista ou de um atendimento.

## Fundamentos
- **Computar** = transformar entradas em saídas seguindo regras. Ciclo **Entrada → Processamento → Saída**, com **Armazenamento**.
- **Hardware** = a parte física; **software** = as instruções. **Firmware** (BIOS/UEFI) = software gravado no hardware.
- Os 4 pilares: **processar (CPU/GPU)**, **memorizar (RAM)**, **guardar (SSD/HD)**, **comunicar (E/S e rede)**. O resto alimenta, conecta, resfria e protege.

## História
- **Ábaco** (indícios de c. 2700 a.C.) → **Anticítera** (c. 100 a.C.) → **Pascalina** (1642) → **Leibniz e o binário** (1703) → **tear de Jacquard** (1804, cartões perfurados) → **Babbage** (Máquina Analítica, 1837) → **Ada Lovelace** (primeiro programa, 1843) → **Boole** (lógica, 1854) → **Hollerith** (1890, origem da IBM).
- **Turing** (1936, máquina universal) e **Shannon** (1937, lógica em circuitos).
- **Primeiro computador** depende da definição: **Z3** (1941, primeiro programável), **ABC** (1942, primeiro eletrônico digital), **ENIAC** (1945/46, primeiro **eletrônico, digital, programável e de propósito geral**), **Manchester Baby** (1948, primeiro com programa armazenado).
- **ENIAC**: 17.468 válvulas, ≈ 27 t, ≈ 167 m², ≈ 150 kW, 5.000 somas/s, programado por cabos, por seis programadoras pioneiras.
- **Gerações**: válvulas (1946) → **transistor** (1947) → **circuito integrado** (1958) → **microprocessador** (Intel 4004, 1971) → paralelismo e IA → qubits.
- **Lei de Moore** (1965/1975): os transistores dobram a cada ≈ 2 anos.
- **Von Neumann** (1945): **programa e dados na mesma memória**; CPU = **UC + ULA + registradores**; ciclo **buscar → decodificar → executar**; o **gargalo** é resolvido com **cache**.
- **Brasil**: UNIVAC 120 (1957), Zezinho (ITA, 1961–62), Patinho Feio (USP, 1972), reserva de mercado (1984–1992).

## Internet
- **Internet** (infraestrutura e TCP/IP) ≠ **Web** (páginas e links sobre a internet).
- **ARPANET** (29/10/1969, mensagem "LO") → e-mail com @ (1971) → **TCP/IP** (Cerf e Kahn, 1974; adotado em 1º/01/1983) → **DNS** (1983) → **Web** (Tim Berners-Lee, CERN, 1989–1991) → Mosaic (1993) → comercial (1995).
- **Brasil**: Bitnet (LNCC e Fapesp, 1988–1989) → .br (abril de 1989) e **RNP** (setembro de 1989) → TCP/IP (início de 1991) → **Eco-92** → abertura comercial e **CGI.br** (31/05/1995) → banda larga (1999) → Marco Civil (2014) → LGPD (2018/2020).

## Linguagem do computador
- **Bit** = 0 ou 1; **byte** = 8 bits = 256 valores. **b** minúsculo = bit; **B** maiúsculo = byte.
- **KB, MB, GB, TB**: decimal (× 1.000, fabricantes) × binário (× 1.024, Windows; KiB, MiB, GiB). **1 TB aparece como ≈ 931 GB** no Windows: não falta nada.
- **Hertz** = ciclos por segundo; **GHz** da CPU ≠ desempenho (importam IPC, núcleos e cache). **Hz do monitor** = atualizações da tela por segundo.
- **Mbps ÷ 8 = MB/s**: 500 Mbps ≈ 62,5 MB/s. Para jogos, o **ping** importa mais que a velocidade.
- **ASCII** (1963): 7 bits, 128 caracteres; "A" = 65, "a" = 97 (diferença de 32). **UTF-8** (1992) é compatível com ASCII e usado em ≈ 99% dos sites.

## Elétrica e segurança
- **V = R × I** (Lei de Ohm) e **P = V × I**. **kWh = kW × horas**.
- Tomada brasileira: **127 V ou 220 V**, 60 Hz, padrão **NBR 14136** (pino terra!). A fonte converte **CA → CC** (12 / 5 / 3,3 V).
- Fonte de qualidade com **PFC ativo** dispensa estabilizador; prefira **filtro de linha com varistor, nobreak e DPS**.
- **Estática** danifica peças com descargas que você nem sente → **pulseira antiestática**, segurar pelas bordas.
- **Não sopre** contatos: a saliva oxida. Limpe com **borracha branca** e **álcool isopropílico 99%**.

## Componentes (fichas rápidas)
| Peça | Função em uma frase | Ponto de atenção |
|---|---|---|
| **Gabinete** | Abriga, protege e organiza o fluxo de ar | Não é "CPU"; frente e base com entrada de ar, topo e traseira com saída |
| **Placa-mãe** | Conecta e alimenta todas as peças | **Soquete**, chipset, formato (ATX, mATX, ITX), DDR4 ou DDR5; onboard × offboard |
| **CPU** | Executa as instruções | Intel (i3–i9 / Ultra 5–9) × AMD (Ryzen 3–9); sufixos **K, F, X, X3D, G** |
| **Dissipador** | Metal que retira o calor | Cobre e alumínio, heatpipes, **pasta térmica** |
| **Cooler** | Ventoinha ou sistema ativo de refrigeração | Ar × water cooler AIO; PWM de 4 pinos; sentido do ar |
| **RAM** | Memória de trabalho, volátil | DDR1→DDR5; **dual channel**; ativar **XMP/EXPO**; 16–32 GB em 2026 |
| **ROM** | Memória do firmware (BIOS/UEFI) | ROM → PROM → EPROM → EEPROM → **flash** |
| **Placa de vídeo** | Gera as imagens; acelera vídeo e IA | **VRAM**; NVIDIA GeForce RTX × AMD Radeon RX × Intel Arc; cabo **na GPU** |
| **Placa de rede** | Conecta à rede | Ethernet (Gigabit, 2.5G) × Wi-Fi (6/6E/7); **MAC**; cabo Cat5e/Cat6 |
| **Fonte** | Converte CA em CC | Potência + **30–50% de margem**; **80 PLUS**; ATX 3.1; **nunca abrir** |
| **Cabos** | Levam energia e dados | 24 pinos, EPS 8, PCIe/12V-2x6, SATA; HDMI 2.1 / DP; USB-C varia muito |
| **HD** | Armazenamento magnético barato | Lento (partes móveis); ótimo para **backup**; SMART no CrystalDiskInfo |
| **SSD** | Armazenamento flash rápido | SATA (550 MB/s) × **NVMe** (3.500–15.000 MB/s); TLC/QLC; **não desfragmentar** |

## Prática
- **Compatibilidade**: comece pela **CPU e pela placa-mãe** (soquete + chipset + BIOS), depois RAM (DDR), GPU (tamanho e fonte), SSD (tipo de M.2), fonte (potência e conectores), cooler (soquete e altura) e gabinete.
- **Montagem**: CPU → M.2 → RAM → cooler → teste fora do gabinete → fonte → placa → cabos → GPU → BIOS (XMP) → sistema → drivers → testes.
- **Manutenção preventiva** (antes: limpeza, pasta, atualizações, backup **3-2-1**) × **corretiva** (depois: diagnosticar do simples para o complexo, trocando uma coisa por vez) × **preditiva** (pelos indicadores, como o SMART).
- **Notebooks**: CPU e GPU soldadas; o upgrade é de SSD e (às vezes) RAM; bateria de lítio na faixa de 20–80%, longe do calor; **bateria estufada = perigo**.

## Fronteira
- **Computação quântica**: **qubits** com superposição, emaranhamento e interferência; ótima para simulação de moléculas e fatoração (Shor), inútil para o uso comum; o desafio é o **erro** (Willow, 2024: correção abaixo do limiar). Já existe **criptografia pós-quântica** (NIST, 2024).
- **IA**: redes neurais = multiplicação de matrizes → **GPUs** (CUDA, Tensor Cores), TPUs, **NPUs**, **HBM**. A demanda dos data centers de IA **encareceu RAM e SSD** em 2025–2026.

:::dica As 10 frases para nunca esquecer
1. "Gabinete não é CPU."
2. "A fonte é a última peça em que se economiza."
3. "Cabo de vídeo vai na placa de vídeo."
4. "Dois pentes de memória (dual channel) são melhores que um."
5. "Ative o XMP/EXPO."
6. "SSD é o upgrade que mais muda a sensação de velocidade."
7. "Mbps ÷ 8 = MB/s."
8. "1 TB = 931 GB no Windows, e não falta nada."
9. "Não sopre os contatos; não abra a fonte; use a pulseira."
10. "Backup 3-2-1: todo disco um dia falha."
:::
