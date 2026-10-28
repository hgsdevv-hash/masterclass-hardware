## O que é

A **placa de rede** (também chamada de **NIC**, *Network Interface Card*, ou **adaptador de rede**) é o componente que **conecta o computador a uma rede**, seja ela a rede local de casa ou do escritório, seja a internet (através de um roteador ou modem).

## Para que serve: sua função no computador

- **Enviar e receber dados** pela rede, convertendo os bits do computador em **sinais elétricos** (cabo), **ondas de rádio** (Wi-Fi) ou **luz** (fibra), e vice-versa.
- **Identificar o computador** na rede local pelo **endereço MAC**.
- Trabalhar nas camadas **física** e de **enlace** da rede (as camadas 1 e 2 do modelo OSI).

| Atividade | Papel da placa de rede |
|---|---|
| **Abrir abas e navegar** | Cada página exige dezenas de conexões; a placa recebe os pacotes e os entrega ao sistema |
| **Assistir a vídeos / streaming** | Recebe o fluxo contínuo (vídeo 4K na Netflix usa ≈ 15–25 Mbps) |
| **Jogos online** | Latência baixa e estável é mais importante que a velocidade |
| **Enviar vídeos editados ou backup na nuvem** | O **upload** depende da placa e do plano |
| **Gerar imagens com IA online** | O processamento ocorre no servidor; a placa envia o pedido e recebe a imagem |
| **Baixar jogos de 100 GB** | Uma placa de 2,5 Gbps aproveita planos de fibra acima de 1 Gbps |

## Onde fica e como é

| Tipo | Onde fica | Como é |
|---|---|---|
| **Onboard cabeada (Ethernet)** | Chip na placa-mãe, com porta **RJ-45** no painel traseiro | Porta quadrada com 2 LEDs (link e atividade) |
| **Onboard Wi-Fi** | Módulo **M.2 (Key E)** na placa-mãe, com antenas parafusadas atrás | Pequena placa de 22 × 30 mm |
| **Offboard PCIe** | Slot **PCIe x1 ou x4** | Placa com porta RJ-45 ou com antenas |
| **Adaptador USB** | Porta USB | Um "pen drive" com ou sem antena |
| **Notebooks** | Módulo M.2 Wi-Fi sob a tampa inferior | Placa pequena com dois cabinhos de antena (os fios preto e branco) |

### Por dentro
| Parte | Função |
|---|---|
| **Controlador MAC** | Monta os quadros (*frames*) de dados e cuida do endereço MAC |
| **PHY (transceptor físico)** | Converte os bits em sinal elétrico ou de rádio |
| **Transformador de isolamento (*magnetics*)** | Isola eletricamente o PC do cabo (proteção) |
| **Porta RJ-45** | Conector do cabo |
| **Rádio e antenas** (Wi-Fi) | Transmitem e recebem em 2,4, 5 e 6 GHz |
| **Memória de buffer** | Armazena pacotes temporariamente |

## Do que é feita (material)

Chips de **silício**, PCB de fibra de vidro com **cobre**, conector RJ-45 com contatos de cobre banhados a **ouro**, antenas de **cobre ou latão**, e invólucro plástico nas antenas.

## O endereço MAC

O **MAC** (*Media Access Control*) é um endereço de **48 bits** gravado na placa de rede, escrito em hexadecimal: `3C-52-82-1A-9F-04`.
- Os **3 primeiros bytes** (o **OUI**) identificam o **fabricante** (Intel, Realtek, TP-Link...).
- Os **3 últimos** identificam a **placa**.
- Para ver o seu: **`ipconfig /all`** no Prompt de Comando ("Endereço Físico").

:::dica MAC × IP
- **MAC**: o "**CPF**" da placa, fixo, que vale **dentro da rede local**.
- **IP**: o "**endereço da casa**", que muda conforme a rede em que você está e serve para **chegar até você** pela internet.
:::

## Tipos de placa de rede

### Cabeada: Ethernet
A **Ethernet** foi inventada por **Bob Metcalfe** e equipe no **Xerox PARC** em **1973** e padronizada como **IEEE 802.3** em **1983**.

| Padrão | Velocidade | Cabo mínimo | Uso |
|---|---|---|---|
| Ethernet (10BASE-T) | 10 Mbps | Cat3 | Antigo |
| **Fast Ethernet** | 100 Mbps | Cat5 | Ainda comum em roteadores baratos (**um gargalo para planos de fibra acima de 100 Mbps!**) |
| **Gigabit Ethernet** | 1 Gbps | **Cat5e** | O padrão atual |
| **2.5GbE** | 2,5 Gbps | Cat5e | Placas-mãe intermediárias e altas de 2026 |
| **5GbE / 10GbE** | 5 / 10 Gbps | Cat6 / **Cat6a** | Entusiastas, NAS, escritórios |

### Sem fio: Wi-Fi
| Geração | Padrão IEEE | Ano | Bandas | Velocidade máxima teórica |
|---|---|---|---|---|
| Wi-Fi 4 | 802.11n | 2009 | 2,4 / 5 GHz | 600 Mbps |
| Wi-Fi 5 | 802.11ac | 2013 | 5 GHz | ≈ 3,5 Gbps |
| **Wi-Fi 6** | 802.11ax | 2019 | 2,4 / 5 GHz | ≈ 9,6 Gbps |
| **Wi-Fi 6E** | 802.11ax | 2020 | + **6 GHz** | ≈ 9,6 Gbps |
| **Wi-Fi 7** | 802.11be | 2024 | 2,4 / 5 / 6 GHz, canais de 320 MHz, **MLO** (várias bandas ao mesmo tempo) | ≈ 46 Gbps |

:::atencao A velocidade "da caixa" não é a real
Os valores máximos teóricos somam todas as antenas e bandas em condições ideais. Na prática, um notebook com Wi-Fi 6 perto do roteador alcança **600–1.200 Mbps**; atrás de duas paredes, talvez **100–300 Mbps**.
:::

| Banda | Alcance | Velocidade | Interferência |
|---|---|---|---|
| **2,4 GHz** | **Maior** (atravessa paredes) | Menor | **Alta** (vizinhos, Bluetooth, micro-ondas) |
| **5 GHz** | Médio | Alta | Média |
| **6 GHz** | Menor | **Muito alta** | **Baixíssima** (faixa nova, liberada pela Anatel no Brasil em 2021) |

### Outros tipos
| Tipo | Uso |
|---|---|
| **Placa de fibra (SFP / SFP+)** | Servidores e redes corporativas |
| **Adaptador USB-Ethernet** | Notebooks finos sem porta RJ-45 |
| **Adaptador USB Wi-Fi** | PCs sem Wi-Fi (os modelos com antena externa são melhores) |
| **Placa 4G/5G (modem celular)** | Notebooks corporativos |
| **Bluetooth** | Normalmente vem **junto** com o Wi-Fi no mesmo módulo |

## Cabeado × Wi-Fi: qual usar

| Critério | **Cabo (Ethernet)** | **Wi-Fi** |
|---|---|---|
| Estabilidade | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Latência (ping) | **Menor e constante** | Maior, com variações (jitter) |
| Velocidade real | Plena | Depende da distância, das paredes e da interferência |
| Mobilidade | Nenhuma | Total |
| Indicado para | **PC de mesa, jogos, TV, videogame, home office** | Celulares, notebooks, onde não chega cabo |

:::exemplo Exemplo: "minha fibra de 600 mega só chega a 94 no PC"
Diagnóstico clássico: **94 Mbps** é o teto real de uma conexão **Fast Ethernet (100 Mbps)**. As causas possíveis:
1. A placa de rede ou a porta do roteador é de 100 Mbps.
2. O **cabo** é Cat5 antigo ou tem um dos 4 pares rompido (o Gigabit usa **os 4 pares**; o Fast Ethernet, só 2).
3. O conector RJ-45 foi mal crimpado.

Solução: cabo **Cat5e ou Cat6** bem crimpado e portas Gigabit. Para conferir, veja a velocidade do link no Windows (**Configurações → Rede → Propriedades do adaptador**): o certo é "1 Gbps", e não "100 Mbps".
:::

## Preço médio (Brasil, out/2026)

| Produto | Faixa de preço |
|---|---|
| Adaptador USB Wi-Fi 4/5 simples | R$ 40–120 |
| Adaptador USB Wi-Fi 6 | R$ 120–300 |
| Placa PCIe Wi-Fi 6E / 7 com Bluetooth | R$ 180–600 |
| Módulo M.2 Wi-Fi 6E / 7 (Intel AX210 / BE200) | R$ 100–300 |
| Placa PCIe Gigabit | R$ 50–120 |
| Placa PCIe 2.5GbE | R$ 120–250 |
| Placa PCIe 10GbE | R$ 400–1.200 |
| Adaptador USB-C para Ethernet Gigabit | R$ 60–200 |

## Problemas mais comuns, como evitar e como resolver

| Problema | Sintoma | Como evitar | Como resolver |
|---|---|---|---|
| **"Sem internet" / "Rede não identificada"** | Ícone com X ou globo | — | Reiniciar o roteador; **`ipconfig /release`** e **`ipconfig /renew`**; **`ipconfig /flushdns`**; **`netsh winsock reset`** e reiniciar |
| **Driver ausente** (Windows recém-instalado) | Nenhuma rede aparece | Ter o driver da placa-mãe num pen drive | Baixar o driver em outro PC (ou usar o **ancoramento USB** do celular) |
| **Link de 100 Mbps** | Velocidade limitada a ≈ 94 Mbps | Cabos Cat5e/Cat6 de qualidade | Trocar o cabo; refazer o conector; verificar a porta do roteador |
| **Wi-Fi fraco e instável** | Quedas, lentidão | Roteador central e elevado; Wi-Fi 5/6 GHz | Aproximar; usar **rede mesh** ou **repetidor**; mudar o canal (apps de análise de Wi-Fi); recolocar as **antenas** do PC |
| **Conflito de IP** | "Outro dispositivo está usando este IP" | DHCP automático | Liberar e renovar o IP; configurar **reserva de DHCP** no roteador |
| **DNS lento** | Sites demorando a "começar" a abrir | — | Usar DNS públicos rápidos (ex.: **1.1.1.1** da Cloudflare, **8.8.8.8** do Google) |
| **Porta RJ-45 queimada** | Nada funciona no cabo, LEDs apagados | Usar **DPS** e filtro de linha (raios chegam pela rede elétrica e também pelo cabo de rede ou do modem) | Usar uma placa PCIe ou um adaptador USB |
| **Wi-Fi desconecta ao economizar energia** | Quedas no notebook | — | Gerenciador de Dispositivos → adaptador → Gerenciamento de Energia → desmarcar "Permitir que o computador desligue este dispositivo" |

:::dica Comandos de rede essenciais (Prompt de Comando)
- `ipconfig /all`: mostra IP, MAC, gateway e DNS.
- `ping 8.8.8.8`: testa se há internet (sem depender do DNS).
- `ping google.com`: testa a internet **e** o DNS.
- `tracert google.com`: mostra o caminho (os saltos) até o destino.
- `nslookup site.com.br`: consulta o DNS.
- `netstat -an`: lista as conexões abertas.
:::
