A história da computação não começa com eletricidade. Ela começa com uma necessidade muito humana: **contar**. Pastores contavam ovelhas com pedrinhas, comerciantes somavam mercadorias, astrônomos previam eclipses. Cada ferramenta que veio depois tentou fazer a mesma coisa: **contar mais rápido, com menos erro e com menos esforço humano**.

Vamos dividir essa história em sete eras.

## Era 1: contar com objetos (antes de 3000 a.C. até o século XVI)

### Ossos e pedras
O **osso de Ishango** (Congo, cerca de 20.000 anos) tem marcas entalhadas em grupos que muitos pesquisadores interpretam como registros de contagem. A própria palavra **cálculo** vem do latim *calculus*, que quer dizer "pedrinha", porque os romanos calculavam movendo pedrinhas sobre uma mesa.

### O ábaco
- **Origem**: há indícios de tábuas de contagem na **Mesopotâmia (Suméria), por volta de 2700–2300 a.C.**, mas a evidência é indireta. O exemplar mais antigo preservado é a **Tábua de Salamina** (Grécia, c. 300 a.C.).
- **Evolução**: o ábaco romano (com sulcos e contas), o **suanpan** chinês (por volta do século II a.C. em registros, popular no século XIII) e o **soroban** japonês (século XVI), que ainda é ensinado em escolas do Japão.
- **Como funciona**: cada haste representa uma **posição decimal** (unidades, dezenas, centenas...). As contas são movidas para representar algarismos. É o mesmo princípio do **valor posicional** que o computador usa, só que em base 10 em vez de base 2.

:::exemplo Exemplo: 37 + 25 no soroban
Você marca 37 (3 contas na dezena, 7 na unidade). Para somar 25, adiciona 5 nas unidades: 7 + 5 = 12, então deixa 2 nas unidades e **"vai um"** para a dezena. Depois adiciona 2 dezenas: 3 + 1 + 2 = 6. Resultado: **62**. Esse "vai um" (o *carry*) é exatamente o que um circuito somador faz dentro do processador.
:::

### O Mecanismo de Anticítera (c. 200–60 a.C.)
A data exata é debatida: a Britannica indica cerca de 100 a.C., estudos de 2014 e 2022 propõem 205 e 178 a.C., e o naufrágio é de c. 70–60 a.C. Ele foi encontrado em **1901** num naufrágio perto da ilha grega de Anticítera, é considerado o **primeiro computador analógico conhecido**. Ele tinha pelo menos **30 engrenagens de bronze** e previa posições do Sol e da Lua, fases lunares, eclipses e até o calendário dos Jogos Olímpicos. Nada tão sofisticado voltou a aparecer na Europa por mais de mil anos.

## Era 2: as calculadoras mecânicas (1600–1800)

| Ano | Invenção | Inventor | O que fazia |
|---|---|---|---|
| 1614–1617 | Logaritmos e **Ossos de Napier** | John Napier (Escócia) | Bastões numerados que transformavam multiplicação em soma |
| c. 1622 (publicada em 1632) | **Régua de cálculo** | William Oughtred (Inglaterra) | Usava escalas logarítmicas; foi a "calculadora" dos engenheiros até os anos 1970 (foi à Lua com a Apollo) |
| 1623 | **Relógio calculador** | Wilhelm Schickard (Alemanha) | Primeira calculadora mecânica documentada (somava e subtraía) |
| 1642–1645 | **Pascalina** | Blaise Pascal (França), iniciada aos 19 anos | Somava e subtraía com engrenagens; criada para ajudar o pai, cobrador de impostos |
| 1673 (concluída em 1694) | **Stepped Reckoner** | Gottfried Wilhelm Leibniz (Alemanha) | Fazia as quatro operações com o "cilindro de Leibniz" |
| 1703 (impresso em 1705) | **Sistema binário** descrito | Leibniz | Descreveu a aritmética só com 0 e 1, a base de todo computador digital |
| 1820 (patente) / 1851 (produção) | **Aritmômetro** | Thomas de Colmar (França) | Primeira calculadora mecânica fabricada e vendida em série |

:::especialista Leibniz e o binário
Leibniz escreveu em 1703 (e publicou em 1705) o artigo *Explication de l'Arithmétique Binaire*. Ele ficou fascinado ao perceber que **qualquer número pode ser escrito só com 0 e 1**. Quase 250 anos depois, essa ideia virou a linguagem de todos os computadores.
:::

## Era 3: a programação nasce num tear (1800–1890)

### O tear de Jacquard (demonstrado em 1801, patenteado em 1804)
**Joseph-Marie Jacquard** criou um tear que tecia padrões complexos lendo **cartões perfurados**. Onde havia furo, a agulha passava; onde não havia, ela parava. Na prática, os cartões eram um **programa**: trocando os cartões, o mesmo tear tecia outro desenho. Foi a primeira máquina **programável** de uso industrial, e o furo/não-furo já era um sistema binário.

### Charles Babbage, o "pai do computador"
- **Máquina Diferencial (1822)**: projetada para calcular tabelas matemáticas (polinômios) sem erro humano. Babbage nunca terminou a versão completa por falta de dinheiro e de precisão mecânica. Em **1991**, o Museu de Ciências de Londres construiu a parte de cálculo da **Máquina Diferencial nº 2** com os desenhos originais, e **ela funcionou**. A impressora foi concluída em 2000.
- **Máquina Analítica (projetada a partir de 1834–1837)**: aqui está o grande salto. Ela tinha todos os elementos de um computador moderno:

| Parte da Máquina Analítica | Equivalente moderno |
|---|---|
| *Mill* ("moinho") | **CPU** (unidade de processamento) |
| *Store* ("armazém") | **Memória** |
| Leitor de cartões perfurados | **Dispositivo de entrada** |
| Impressora e perfurador de cartões | **Dispositivo de saída** |
| Desvios condicionais e laços | **Programação** (if, loops) |

### Ada Lovelace, a primeira programadora
**Augusta Ada King, Condessa de Lovelace** (1815–1852), filha do poeta Lord Byron, traduziu em **1843** um artigo sobre a Máquina Analítica e acrescentou **notas três vezes maiores que o original**. Na famosa **Nota G**, ela escreveu um **algoritmo para calcular os números de Bernoulli**, considerado o **primeiro programa de computador publicado**.

Mais importante ainda: Ada percebeu que a máquina poderia manipular **símbolos**, e não só números. Na **Nota A**, ela imaginou que uma máquina assim poderia até **compor peças musicais elaboradas**. E, na própria Nota G, fez uma ressalva que até hoje aparece nos debates sobre IA: a máquina "não tem pretensão alguma de originar coisa alguma", ou seja, só faz o que mandamos. Isso é, em essência, a ideia de computador de propósito geral.

:::curiosidade Curiosidade
A linguagem de programação **Ada**, criada para o Departamento de Defesa dos EUA em 1980, recebeu esse nome em homenagem a ela. E a segunda terça-feira de outubro é o **Ada Lovelace Day**, dedicado às mulheres na ciência.
:::

### George Boole e a lógica (1847–1854)
O matemático inglês **George Boole** publicou *The Mathematical Analysis of Logic* (1847) e *The Laws of Thought* (1854). Ele criou a **álgebra booleana**, em que tudo é **verdadeiro (1)** ou **falso (0)** e as operações são **E (AND)**, **OU (OR)** e **NÃO (NOT)**. Cada transistor do seu processador implementa essas operações.

:::exemplo Exemplo de lógica booleana no dia a dia
"Vou à praia **SE** fizer sol **E** eu estiver de folga."
- Sol = 1, Folga = 1 → Praia = **1** (vai)
- Sol = 1, Folga = 0 → Praia = **0** (não vai)

Dentro da CPU existe uma **porta AND** que faz exatamente isso com sinais elétricos, bilhões de vezes por segundo.
:::

## Era 4: os dados em escala industrial (1890–1930)

### Herman Hollerith e o censo de 1890
O censo dos EUA de 1880 levou **quase oito anos** para ser apurado à mão. **Herman Hollerith** criou uma **máquina tabuladora elétrica** que lia **cartões perfurados** com os dados de cada cidadão: um pino passava pelo furo, fechava um circuito elétrico e avançava um contador. O censo de **1890** teve a contagem principal concluída em cerca de **um ano**.

A empresa de Hollerith (Tabulating Machine Company, 1896) se fundiu com outras em 1911 e, em **1924**, passou a se chamar **IBM (International Business Machines)**.

## Era 5: a teoria e os primeiros computadores (1930–1950)

### Alan Turing e a máquina universal (1936)
O britânico **Alan Turing** publicou em **1936** o artigo *On Computable Numbers*. Nele descreveu uma máquina teórica (a **Máquina de Turing**) com uma fita infinita, uma cabeça que lê e escreve símbolos e uma tabela de regras. Ele provou que uma **máquina universal** poderia simular **qualquer outra máquina**, desde que recebesse a descrição dela como dados. Isso é a definição teórica do computador moderno: **uma única máquina, infinitos programas**.

Durante a Segunda Guerra, Turing trabalhou em **Bletchley Park** quebrando a cifra alemã **Enigma** com a máquina eletromecânica **Bombe**. Em **1950**, propôs o **Teste de Turing** para a inteligência das máquinas.

:::curiosidade Curiosidade
Turing foi perseguido por ser homossexual e morreu em 1954. Recebeu perdão real póstumo em 2013 e, desde 2021, estampa a nota de **50 libras** do Reino Unido. O filme *O Jogo da Imitação* (2014) conta parte da sua história.
:::

### Claude Shannon une Boole e eletricidade (1937)
Na sua dissertação de mestrado no MIT, escrita em **1937** e publicada em 1938, **Claude Shannon** mostrou que **circuitos de relés elétricos podiam implementar a álgebra booleana**. Muitos a consideram a dissertação de mestrado mais importante do século XX. Em **1948**, Shannon publicou *A Mathematical Theory of Communication*, fundando a **Teoria da Informação** e popularizando a palavra **bit**.

### A corrida dos primeiros computadores

| Ano | Máquina | Onde | Tecnologia | Destaque |
|---|---|---|---|---|
| 1938 | **Z1** | Alemanha (Konrad Zuse) | Mecânica, binária | Montada na sala dos pais de Zuse |
| 1941 | **Z3** | Alemanha (Zuse) | Eletromecânica (≈ 2.000–2.600 relés, conforme a fonte) | **Primeiro computador programável e automático funcional** |
| 1937–1942 | **ABC (Atanasoff-Berry)** | EUA (Iowa State) | Eletrônico (válvulas), binário | Primeiro computador **eletrônico digital**, mas não programável |
| 1944 | **Colossus** | Reino Unido (Tommy Flowers) | Eletrônico (Mark 1: ≈ 1.500–1.600 válvulas; Mark 2: 2.400) | Quebrava cifras nazistas (Lorenz); ficou em segredo até os anos 1970 |
| 1944 | **Harvard Mark I** | EUA (Howard Aiken + IBM) | Eletromecânico | 15 m de comprimento, ≈4,3 toneladas |
| 1945–1946 | **ENIAC** | EUA (Mauchly e Eckert) | Eletrônico (17.468 válvulas) | Primeiro **eletrônico, digital, programável e de propósito geral** |
| 1948 | **Manchester Baby** | Reino Unido | Eletrônico | **Primeiro programa armazenado na memória** (21/06/1948) |
| 1949 | **EDSAC** | Reino Unido (Maurice Wilkes) | Eletrônico | Primeiro com programa armazenado em uso regular |
| 1951 | **UNIVAC I** | EUA | Eletrônico | Primeiro computador comercial de sucesso nos EUA; previu a eleição de Eisenhower em 1952 |

O ENIAC e o debate sobre "qual foi o primeiro computador" ganham um módulo próprio, a seguir.

## Era 6: transistores, chips e computadores pessoais (1947–2000)

### O transistor (1947)
Em **dezembro de 1947**, **John Bardeen, Walter Brattain e William Shockley**, do **Bell Labs**, criaram o **transistor**, um interruptor eletrônico minúsculo feito de **semicondutor** (germânio e, depois, silício). Ele substituiu a válvula: era menor, mais barato, esquentava menos e quase não queimava. Os três ganharam o **Nobel de Física em 1956**.

### O circuito integrado (1958–1959)
- **Jack Kilby** (Texas Instruments, **1958**) colocou vários componentes num único pedaço de germânio. Ganhou o **Nobel em 2000**.
- **Robert Noyce** (Fairchild, **1959**) criou o CI **planar de silício**, que permitiu a produção em massa. Noyce depois cofundou a **Intel**.

### A Lei de Moore (1965)
**Gordon Moore** (cofundador da Intel) observou em **1965** que o número de transistores num chip dobrava a cada ano. Em **1975**, ajustou a previsão para **a cada dois anos**. Essa "lei" (na verdade uma observação econômica) guiou a indústria por mais de 50 anos.

:::exemplo Exemplo: a Lei de Moore em números
- Intel 4004 (1971): **2.300** transistores.
- Intel Pentium (1993): **3,1 milhões**.
- Apple M1 (2020): **16 bilhões**.
- NVIDIA Blackwell B200 (2024): **208 bilhões** (dois chips num mesmo pacote).

De 2.300 para 208 bilhões são cerca de **26 dobras** em pouco mais de 50 anos, quase exatamente o que Moore previu.
:::

### O microprocessador (1971)
O **Intel 4004**, anunciado em **15 de novembro de 1971**, foi o primeiro **microprocessador comercial**: uma CPU inteira num único chip. Tinha **cerca de 2.300 transistores** (algumas fontes dizem 2.250), **4 bits**, clock de **740 kHz** e foi feito para uma calculadora da empresa japonesa **Busicom**. A equipe tinha **Federico Faggin**, **Ted Hoff**, **Stan Mazor** e o japonês **Masatoshi Shima**.

### O computador chega em casa

| Ano | Marco |
|---|---|
| 1973 | **Xerox Alto**: primeiro computador com interface gráfica, janelas e mouse (nunca vendido ao público) |
| 1975 | **Altair 8800**, primeiro microcomputador popular (kit). Bill Gates e Paul Allen fundam a **Microsoft** |
| 1976 | **Steve Jobs e Steve Wozniak** fundam a **Apple**; lançam o Apple I |
| 1977 | **Apple II**, Commodore PET e TRS-80, a "trindade" dos micros prontos para uso |
| 1981 | **IBM PC 5150** (12 de agosto de 1981): processador Intel 8088 a 4,77 MHz e sistema MS-DOS. Nasce o padrão **PC** |
| 1984 | **Apple Macintosh** populariza a interface gráfica e o mouse |
| 1985 | **Windows 1.0** |
| 1991 | **Linux** (Linus Torvalds) |
| 1995 | **Windows 95**, com menu Iniciar e plug-and-play |

## Era 7: internet, mobilidade, nuvem, IA e quântica (1990 até hoje)

| Ano | Marco |
|---|---|
| 1991 | Primeiro site da **World Wide Web** (CERN) |
| 1998 | Fundação do **Google** |
| 2006 | **Amazon Web Services**: começa a era da **computação em nuvem** |
| 2007 | **iPhone**; em 2008, o primeiro celular **Android** |
| 2012 | **AlexNet**: redes neurais treinadas em **GPUs** vencem o desafio ImageNet e começa o boom do *deep learning* |
| 2016 | **AlphaGo** (DeepMind) vence Lee Sedol no Go |
| 2017 | Artigo *Attention Is All You Need* (Google) cria a arquitetura **Transformer**, base do ChatGPT, do Claude e do Gemini |
| 2019 | **Google Sycamore** (53 qubits) faz um cálculo que alegadamente levaria milhares de anos num supercomputador |
| 2022 | **ChatGPT** (30 de novembro) leva a IA generativa ao grande público |
| 2024 | **Google Willow** (105 qubits) demonstra correção de erros quânticos abaixo do limiar |
| 2025–2026 | IA generativa em escala global; data centers de IA disparam a demanda por **GPU, RAM e SSD**, e os preços sobem para o consumidor |

## O Brasil nessa história

- **1957**: o governo do Estado de São Paulo compra um **UNIVAC 120**, considerado o primeiro computador do Brasil, para calcular o consumo de água na capital.
- **1961–1962**: alunos do **ITA** constroem o **"Zezinho"**, o primeiro computador feito no Brasil (transistorizado e apenas didático).
- **Julho de 1972**: a **USP** inaugura o **"Patinho Feio"**, primeiro computador projetado e construído no Brasil com fins práticos. O nome brinca com o "Cisne Branco", um projeto da Marinha.
- **18 de julho de 1974**: nasce a **Cobra (Computadores e Sistemas Brasileiros)**, estatal de informática.
- **1984–1992**: a **Lei de Informática (Lei 7.232, de 29/10/1984)** cria a **reserva de mercado** por oito anos, limitando a importação de computadores. Ela estimulou empresas nacionais, mas deixou o país tecnologicamente atrasado e com máquinas caras. Terminou em **outubro de 1992**.

:::especialista Para aprofundar
O **Computer History Museum** (Mountain View, Califórnia) tem a maior coleção do mundo e uma linha do tempo online gratuita. O livro *Os Inovadores*, de Walter Isaacson, conta essa história a partir das pessoas, de Ada Lovelace a Larry Page.
:::
