A **computação quântica** é a fronteira mais comentada (e mais mal explicada) da tecnologia. Ela **não é** "um computador comum muito mais rápido". É uma **outra forma de computar**, baseada nas leis da **mecânica quântica**, que é extraordinária para alguns problemas específicos e inútil para a maioria das tarefas do dia a dia.

## O que é

Um **computador quântico** processa informação usando **qubits** (bits quânticos), que exploram três fenômenos da física quântica: **superposição**, **emaranhamento** e **interferência**. Com isso, alguns problemas que levariam milhões de anos num supercomputador clássico podem, em teoria, ser resolvidos em horas ou minutos.

## Bit × qubit

| | **Bit (clássico)** | **Qubit (quântico)** |
|---|---|---|
| Estados | **0 ou 1** | **Superposição** de 0 e 1 ao mesmo tempo (com "pesos", as amplitudes) |
| Leitura | Sempre dá o mesmo valor | A **medição** "colapsa" o qubit em 0 ou 1, com certa **probabilidade** |
| Combinação | n bits guardam **1** de 2ⁿ valores por vez | n qubits descrevem **2ⁿ amplitudes ao mesmo tempo** |
| Cópia | Pode ser copiado | **Não pode ser copiado** (teorema da não clonagem) |
| Estabilidade | Muito estável | **Frágil**: perde a informação com calor, vibração, radiação (a **decoerência**) |
| Exemplo físico | Tensão num transistor | Corrente num circuito supercondutor, um íon preso por laser, um átomo neutro, um fóton |

:::exemplo Exemplo: a moeda girando
Um **bit** é uma moeda **parada** na mesa: ou é cara (0) ou coroa (1).
Um **qubit** é uma moeda **girando**: enquanto gira, ela não é só cara nem só coroa, mas uma combinação das duas. Quando você **bate a mão** na moeda (a **medição**), ela cai em cara ou coroa.
O truque da computação quântica é **inclinar as probabilidades** enquanto as moedas giram, para que, no fim, a resposta certa seja a que tem mais chance de aparecer.
:::

## Os três fenômenos, explicados

1. **Superposição**: o qubit está numa combinação de 0 e 1. Com **50 qubits**, o sistema descreve 2⁵⁰ ≈ **1 quatrilhão** de amplitudes ao mesmo tempo. Para simular isso num computador clássico, seriam necessários petabytes de memória.
2. **Emaranhamento** (*entanglement*): dois ou mais qubits ficam **correlacionados**, de modo que o estado de um não pode ser descrito sem o do outro, mesmo a distância. Einstein chamou isso de **"ação fantasmagórica a distância"**. É o recurso que dá poder ao computador quântico.
3. **Interferência**: assim como ondas de água se somam ou se anulam, os algoritmos quânticos são desenhados para que os caminhos que levam às **respostas erradas se cancelem** e os que levam à **resposta certa se reforcem**.

:::atencao O mito do "testa todas as respostas ao mesmo tempo"
É comum ouvir que o computador quântico "testa todas as possibilidades em paralelo". Isso é **enganoso**: ao medir, você recebe **um único resultado aleatório**. A vantagem só aparece quando um **algoritmo inteligente** usa a **interferência** para aumentar a probabilidade da resposta certa. Por isso existem **poucos problemas** em que o quântico ganha de verdade.
:::

## Quem criou e quando: a história

| Ano | Marco | Quem |
|---|---|---|
| **1900–1930** | Nasce a **mecânica quântica** | Planck, Einstein, Bohr, Heisenberg, Schrödinger, Dirac |
| **1980** | Primeiro modelo de **máquina de Turing quântica** | **Paul Benioff** (EUA); **Yuri Manin** (URSS) propõe a ideia de forma independente |
| **1981–1982** | Palestra no MIT (1981, publicada em 1982): "*Simulating Physics with Computers*". Para simular a natureza, é preciso um computador **quântico** | **Richard Feynman** (Nobel de Física, 1965) |
| **1985** | **Computador quântico universal** (o equivalente quântico da máquina de Turing) | **David Deutsch** (Oxford) |
| **1992** | **Algoritmo de Deutsch–Jozsa**: primeiro exemplo de vantagem exponencial (num problema artificial) | Deutsch e Richard Jozsa |
| **1994** | **Algoritmo de Shor**: fatora números grandes de forma eficiente, o que **ameaça a criptografia RSA** | **Peter Shor** (Bell Labs) |
| **1995** | Primeiros esquemas de **correção de erros quânticos** | Peter Shor; Andrew Steane |
| **1996** | **Algoritmo de Grover**: busca em base de dados não ordenada com ganho **quadrático** | **Lov Grover** (Bell Labs) |
| **1998** | Primeiros algoritmos executados em computadores quânticos de 2–3 qubits (por ressonância magnética nuclear, RMN) | Oxford, IBM, MIT, Stanford |
| **2001** | A IBM **fatora o número 15** (= 3 × 5) com **7 qubits** usando o algoritmo de Shor (RMN) | IBM e Stanford |
| **2011** | **D-Wave One**: primeiro computador quântico **comercial** (do tipo *annealing*, especializado em otimização) | D-Wave (Canadá) |
| **2016** | **IBM Quantum Experience**: primeiro computador quântico acessível **pela nuvem**, gratuitamente | IBM |
| **2019** | **Sycamore** (53 qubits) anuncia a **"supremacia quântica"**: um cálculo em ≈ 200 s que levaria, segundo o Google, 10 mil anos num supercomputador. A IBM contestou, estimando ≈ 2,5 dias | Google |
| **2021–2023** | IBM **Eagle** (127 qubits, 2021), **Osprey** (433, 2022), **Condor** (1.121, 2023) e **Heron** (2023, menos qubits e muito menos erros) | IBM |
| **2023** | Demonstrações de **qubits lógicos** com átomos neutros | Harvard, QuEra e MIT |
| **Dez. 2024** | **Willow** (105 qubits): primeira demonstração convincente de **correção de erros "abaixo do limiar"** (quanto mais qubits na correção, **menos** erros) | Google Quantum AI |
| **Fev. 2025** | **Majorana 1**: chip com qubits **topológicos**; recebido com **ceticismo** pela comunidade científica | Microsoft |
| **Out. 2025** | **Nobel de Física de 2025**: **John Clarke, Michel Devoret e John Martinis**, pelo tunelamento quântico macroscópico em circuitos elétricos (anos 1980), a base dos qubits supercondutores | Academia Sueca |
| **22/10/2025** | **Quantum Echoes** (artigo na *Nature*): algoritmo no Willow ≈ **13.000 vezes mais rápido** que o melhor método clássico, com resultado **verificável** (outro computador quântico de qualidade semelhante pode reproduzi-lo) | Google |
| **Nov. 2025** | **IBM Nighthawk** (120 qubits) e **Loon** (demonstra os elementos de hardware para tolerância a falhas); decodificação de erros em tempo real em menos de 480 ns. Meta: o **Starling**, tolerante a falhas, em **2029** | IBM |
| **Nov. 2025** | **Helios**: 98 qubits de íons de bário, com fidelidades anunciadas de 99,92% em portas de 2 qubits | Quantinuum |
| **Jun. 2026** | **Majorana 2** anunciado, com promessa de confiabilidade 1.000 vezes maior; críticos dizem que o artigo ainda não demonstra um qubit completo | Microsoft |

:::especialista Feynman
A frase de **Richard Feynman** que fundou a área, no fim do artigo de 1982, em tradução livre: *"Se você quer fazer uma simulação da natureza, é melhor que ela seja quântica."*
:::

## Como funciona na prática

### O hardware
| Tecnologia | Como funciona | Empresas | Temperatura |
|---|---|---|---|
| **Supercondutores** | Circuitos de alumínio e nióbio com **junções Josephson**, resfriados até a supercondutividade | **IBM, Google**, Rigetti, IQM | ≈ **10–15 milikelvin** (−273,14 °C, mais frio que o espaço sideral) |
| **Íons aprisionados** | Átomos com carga elétrica presos por campos eletromagnéticos e controlados por **laser** | **Quantinuum, IonQ** | Íons a temperaturas ultrabaixas, numa câmara de vácuo |
| **Átomos neutros** | Átomos presos por "pinças ópticas" (lasers) | **QuEra, Pasqal, Atom Computing**, Infleqtion | Ultrafrios (microkelvin) |
| **Fotônica** | Qubits feitos de **fótons** (luz) | **PsiQuantum, Xanadu** | Em geral, perto da temperatura ambiente (os detectores são resfriados) |
| **Topológicos** | Quasipartículas de **Majorana**, teoricamente mais protegidas contra erros | **Microsoft** | Ultrafrio; ainda experimental e controverso |
| **Spin em silício** | Elétrons em pontos quânticos de silício (parecido com chips atuais) | **Intel**, Diraq | Ultrafrio |

:::curiosidade O "lustre dourado"
A imagem clássica de um computador quântico supercondutor é um **"lustre" dourado** pendurado: na verdade é o **refrigerador por diluição**, com vários estágios que vão esfriando até os milikelvin. O chip quântico fica **na ponta de baixo**, e é minúsculo (alguns centímetros).
:::

### Portas e circuitos quânticos
Assim como o computador clássico usa portas lógicas (AND, OR, NOT), o quântico usa **portas quânticas**:
- **X**: o "NOT" quântico (troca 0 por 1).
- **H (Hadamard)**: coloca o qubit em **superposição** igual de 0 e 1.
- **CNOT**: porta de 2 qubits que cria **emaranhamento**.
- **Medição**: lê o resultado (0 ou 1).

Um **algoritmo quântico** é uma sequência dessas portas (um **circuito quântico**), executada **muitas vezes** (os *shots*), porque o resultado é probabilístico.

### O grande desafio: erros e qubits lógicos
- Os qubits **físicos** erram muito: as melhores portas de 2 qubits de 2025–2026 erram de 1 em 1.000 a 1 em 100 vezes.
- Para fazer cálculos úteis, é preciso **correção de erros quânticos**: juntar **dezenas, centenas ou milhares de qubits físicos** para formar **um qubit lógico** confiável.
- O **limiar** (*threshold*) é o ponto a partir do qual adicionar mais qubits **reduz** os erros, em vez de aumentá-los. O **Willow (2024)** foi o primeiro a mostrar isso de forma convincente.
- Estimativas indicam que quebrar o RSA-2048 exigiria cerca de **1 milhão de qubits físicos** de boa qualidade (estimativa de Craig Gidney, do Google, em 2025, revisando para baixo as de 20 milhões de 2019). Ainda estamos **muito longe** disso.

## Para que serve (e para que não serve)

| Aplicação | Por que o quântico ajuda | Situação em 2026 |
|---|---|---|
| **Simulação de moléculas e materiais** (remédios, baterias, fertilizantes, supercondutores) | A natureza **é** quântica (era a ideia de Feynman) | A aplicação mais promissora; primeiros resultados científicos |
| **Criptografia** (algoritmo de Shor) | Fatoração rápida quebraria **RSA** e **ECC** | Ainda impossível na prática, mas motiva a criptografia pós-quântica |
| **Otimização** (logística, finanças, rotas) | Algoritmos variacionais e *annealing* | Vantagem real ainda **não comprovada** de forma clara |
| **Aprendizado de máquina quântico** | Pesquisa | Especulativo |
| **Busca (Grover)** | Ganho quadrático | Limitado na prática |
| **Planilhas, jogos, internet, vídeos** | **Nenhum** ganho | **Nunca** vai substituir o seu PC |

:::dica Resposta de prova
"O computador quântico **não substitui** o computador clássico. Ele é um **acelerador especializado** para certos problemas (simulação quântica, fatoração, alguns tipos de otimização), e no futuro deve funcionar **ao lado** dos supercomputadores e das GPUs, acessado pela nuvem."
:::

## Criptografia pós-quântica: por que isso já importa hoje

- **"Colher agora, decifrar depois"** (*harvest now, decrypt later*): agentes mal-intencionados podem **gravar hoje** dados criptografados (diplomáticos, médicos, financeiros) para **decifrá-los no futuro**, quando houver computadores quânticos grandes.
- Em **agosto de 2024**, o **NIST** (EUA) publicou os **primeiros padrões de criptografia pós-quântica**:
  - **FIPS 203 (ML-KEM)**, baseado no CRYSTALS-Kyber, para troca de chaves.
  - **FIPS 204 (ML-DSA)**, baseado no CRYSTALS-Dilithium, para assinaturas digitais.
  - **FIPS 205 (SLH-DSA)**, baseado no SPHINCS+, para assinaturas.
- Em **março de 2025**, o NIST escolheu o **HQC** como algoritmo reserva para troca de chaves (padrão final previsto para 2027).
- Navegadores (Chrome, Edge, Firefox), o Signal, o iMessage e a Cloudflare **já usam** troca de chaves híbrida pós-quântica.

## E no Brasil?

- O **SENAI CIMATEC** (Salvador) coordena uma rede nacional de computação quântica ligada ao **MCTI** e à Softex. O **Kuatomu**, desenvolvido com a Atos, é um **simulador** quântico de 35 qubits que roda em hardware clássico, e não um computador quântico.
- O **MCTI** abriu em 2024 um grupo de trabalho para diretrizes nacionais e lançou em **junho de 2026** um programa de residência em tecnologias quânticas.
- A **Paraíba** anunciou o primeiro centro com computadores quânticos operacionais do país (**CIQUANTA-PB**, com máquinas de 20 e 100 qubits). A instalação foi noticiada para **agosto de 2026**, e a conclusão ainda deve ser confirmada em fontes oficiais.
- Universidades como **USP, Unicamp, UFRJ, UFPE, UFRN** e o **CBPF** têm grupos fortes de pesquisa em informação quântica.

## Problemas e limitações

| Limitação | Por quê |
|---|---|
| **Decoerência** | Qubits perdem a informação em micro a milissegundos |
| **Taxa de erros alta** | Exige correção de erros, que multiplica o número de qubits necessários |
| **Refrigeração extrema** | Equipamentos caros e grandes, que consomem muita energia |
| **Escala** | Ir de centenas para milhões de qubits é um enorme desafio de engenharia |
| **Poucos algoritmos com vantagem comprovada** | Para a maioria dos problemas, o computador clássico continua melhor |
| **Exagero de marketing** | Muitos anúncios de "vantagem quântica" são questionados depois; é preciso ler com espírito crítico |
