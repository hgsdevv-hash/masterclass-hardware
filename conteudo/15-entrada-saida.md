Os **dispositivos de entrada e saída (E/S, ou I/O em inglês)** são a **ponte entre o computador e o mundo**. Sem eles, o processador mais rápido do mundo seria uma caixa calculando para ninguém.

## Definições

- **Dispositivo de entrada**: **envia** dados **para dentro** do computador.
- **Dispositivo de saída**: **recebe** dados **do computador** e os apresenta ao mundo (luz, som, papel, movimento).
- **Dispositivo de entrada e saída (misto)**: faz as **duas coisas**.
- **Dispositivo de armazenamento**: costuma ser classificado como **E/S**, porque grava (saída) e lê (entrada).

:::dica Como não errar na prova
Pense sempre **do ponto de vista do computador**: se o dado **entra** no computador, é entrada; se **sai** do computador, é saída. O monitor recebe a imagem que **sai** do PC, por isso é de **saída**.
:::

## Dispositivos de entrada

| Dispositivo | Como funciona | Exemplo de uso | Preço médio (2026) |
|---|---|---|---|
| **Teclado** | Cada tecla fecha um contato numa matriz; o controlador envia um **código de varredura (*scancode*)** | Digitar, atalhos | R$ 40–1.000+ (módulo próprio) |
| **Mouse** | **Óptico**: um LED ilumina a superfície e um minissensor tira **milhares de "fotos" por segundo** para calcular o movimento. **Laser**: funciona até em vidro. A precisão é medida em **DPI/CPI** | Apontar, clicar | R$ 25 (básico) – R$ 800 (gamer sem fio) |
| **Touchpad** | Grade **capacitiva** sente o campo elétrico do dedo | Notebooks | Integrado |
| **Microfone** | Diafragma vibra com o som; o sinal é convertido de analógico para digital (ADC) | Chamadas, gravação | R$ 30–1.500 |
| **Webcam** | Sensor de imagem (CMOS) com lente | Videochamada | R$ 80–1.500 |
| **Scanner** | Sensor CCD ou CIS varre o papel linha a linha | Digitalizar documentos | R$ 400–3.000 |
| **Leitor de código de barras / QR** | Laser ou câmera lê o padrão de barras | Comércio, estoque | R$ 100–600 |
| **Leitor biométrico** | Lê a impressão digital (capacitivo ou óptico) | Login, ponto eletrônico | R$ 60–400 |
| **Joystick / controle** | Botões + sensores analógicos (potenciômetro ou efeito Hall) | Jogos | R$ 80–1.200 |
| **Mesa digitalizadora** | Grade eletromagnética detecta a caneta e a pressão | Desenho, design | R$ 250–10.000+ |
| **Sensores** | Temperatura, movimento, luz, giroscópio | IoT, celulares | Variável |

## Dispositivos de saída

| Dispositivo | Como funciona | Exemplo de uso | Preço médio (2026) |
|---|---|---|---|
| **Monitor** | Matriz de pixels: **LCD (IPS, VA, TN)** com luz de fundo LED, **OLED** (cada pixel emite a própria luz) ou **Mini-LED** | Ver tudo | R$ 500 (21,5" Full HD) – R$ 8.000+ (OLED 4K) |
| **Impressora jato de tinta** | Gotas microscópicas de tinta (térmica ou piezoelétrica) | Casa, fotos | R$ 400–2.000 (as "tanque de tinta" têm custo por página muito menor) |
| **Impressora laser** | Um laser "desenha" com carga elétrica num cilindro; o toner (pó) gruda e é fundido no papel pelo calor | Escritório, volume | R$ 900–5.000 |
| **Impressora térmica** | Aquece papel termossensível | Cupom fiscal, etiquetas | R$ 300–1.500 |
| **Caixas de som / fones** | Bobina e ímã movem um cone que vibra o ar (DAC → amplificador → alto-falante) | Áudio | R$ 30–3.000+ |
| **Projetor** | Lâmpada, LED ou laser + painel LCD/DLP projeta a imagem | Aulas, cinema | R$ 400–15.000 |
| **Plotter** | Impressora de grande formato | Plantas, banners | R$ 8.000+ |
| **Óculos de RV (saída visual)** | Duas telas próximas aos olhos | Realidade virtual | R$ 2.500–30.000 |

## Dispositivos de entrada e saída (mistos)

| Dispositivo | Entrada | Saída |
|---|---|---|
| **Tela touch** | Toque | Imagem |
| **Headset** | Microfone | Fones |
| **Multifuncional** | Scanner | Impressora |
| **Placa de rede / modem / roteador** | Recebe dados | Envia dados |
| **Pen drive, SSD externo, HD externo** | Leitura | Gravação |
| **Controle com vibração (force feedback)** | Botões | Vibração |
| **Óculos de realidade virtual** | Sensores de movimento da cabeça e das mãos | Telas e áudio |

## Como os dispositivos se comunicam: interfaces

| Interface | Tipo | Velocidade | Exemplos |
|---|---|---|---|
| **USB 2.0** | Cabo | 480 Mbps | Teclado, mouse, impressora |
| **USB 3.2 / USB-C** | Cabo | 5–20 Gbps | SSD externo, webcam 4K, *docks* |
| **USB4 / Thunderbolt 4–5** | Cabo (USB-C) | 40–120 Gbps | Monitores, GPUs externas, *docks* |
| **HDMI / DisplayPort** | Cabo | Até 48–96 Gbps (HDMI) e 80 Gbps (DP) | Monitores e TVs |
| **P2 (3,5 mm)** | Cabo analógico | — | Fone, microfone, caixa de som |
| **Bluetooth** | Sem fio | Até ≈ 2–3 Mbps (versões 5.x) | Fone, mouse, controle |
| **Rádio 2,4 GHz (receptor USB)** | Sem fio | Latência muito baixa (≈ 1 ms) | Mouse e teclado gamer |
| **Wi-Fi** | Sem fio | Centenas de Mbps a vários Gbps | Impressoras de rede |
| **Ethernet (RJ-45)** | Cabo | 100 Mbps – 10 Gbps | Rede |
| **PS/2 (antigo)** | Cabo | — | Teclados e mouses antigos; algumas placas ainda têm |

:::exemplo Exemplo: a "taxa de sondagem" (polling rate) do mouse gamer
Um mouse comum envia sua posição ao computador **125 vezes por segundo (125 Hz)**, ou seja, a cada 8 ms. Um mouse gamer envia **1.000 Hz** (a cada 1 ms), e os mais novos, **4.000–8.000 Hz**. Na prática, isso deixa o ponteiro mais "colado" na mão em jogos competitivos. Para trabalho de escritório, 125 Hz é mais que suficiente.
:::

## Problemas comuns de E/S e como resolver

| Sintoma | Causa provável | Solução |
|---|---|---|
| Dispositivo USB não reconhecido | Driver, porta com mau contato, falta de energia na porta, cabo ruim | Trocar de porta (de preferência a traseira, direto na placa-mãe), trocar o cabo, reinstalar o driver no Gerenciador de Dispositivos |
| Mouse "pulando" | Superfície reflexiva ou irregular, sujeira no sensor, pilha fraca, interferência de 2,4 GHz | Usar mousepad, limpar a lente, trocar a pilha, aproximar o receptor (use extensor USB) |
| Monitor "sem sinal" | Cabo ligado na **placa-mãe** quando há placa de vídeo dedicada, entrada errada no monitor, RAM mal encaixada | Ligar o cabo **na placa de vídeo**, selecionar a entrada (*source*) correta, reencaixar a memória |
| Fone ou microfone sem som | Dispositivo padrão errado no Windows, conector P2 na porta errada (verde = fone, rosa = microfone) | Configurações → Sistema → Som → escolher o dispositivo correto |
| Impressora "offline" | Fila travada, IP mudou na rede, driver | Reiniciar o spooler de impressão, fixar o IP da impressora, reinstalar o driver |
| Bluetooth desconectando | Interferência de Wi-Fi 2,4 GHz, gerenciamento de energia | Usar Wi-Fi de 5 GHz, desativar "permitir que o computador desligue este dispositivo" |
