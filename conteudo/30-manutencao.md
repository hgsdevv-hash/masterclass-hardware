## O que é manutenção

**Manutenção** é o conjunto de ações para **manter o computador funcionando** com desempenho, segurança e vida útil máximos. Ela se divide em dois grandes tipos (mais um terceiro, moderno):

| Tipo | Quando é feita | Objetivo | Analogia com o carro |
|---|---|---|---|
| **Preventiva** | **Antes** do problema, em intervalos programados | **Evitar** falhas | Trocar o óleo a cada 10 mil km |
| **Corretiva** | **Depois** que o problema aparece | **Consertar** a falha | Trocar a peça quebrada |
| **Preditiva** | Quando **indicadores** mostram que a falha está próxima | **Antecipar** a falha com dados | O painel avisando que a pastilha de freio está gasta |

:::exemplo Exemplo: preventiva × corretiva × preditiva no mesmo PC
- **Preventiva**: a cada 6 meses, limpar a poeira e conferir as temperaturas.
- **Preditiva**: o **CrystalDiskInfo** mostra o HD em "**Cuidado**", com setores realocados → **trocar o HD antes de ele morrer**, fazendo backup.
- **Corretiva**: o PC não liga mais → diagnóstico → a fonte queimou → trocar a fonte.
:::

## Manutenção preventiva

### Calendário recomendado
| Frequência | O que fazer |
|---|---|
| **Semanal** | Reiniciar o PC (não só suspender); conferir se há atualizações pendentes |
| **Mensal** | Windows Update e drivers da GPU; limpeza de arquivos temporários (**Limpeza de Disco** ou **Sensor de Armazenamento**); verificar o espaço livre (≥ 15–20%); conferir o **backup** |
| **A cada 3–6 meses** | **Limpeza física** dos filtros e da poeira (antes, em ambientes com poeira, pets, fumantes ou obras); conferir as **temperaturas**; ver a saúde dos discos (**CrystalDiskInfo**) |
| **Anual** | Limpeza completa (desmontagem parcial); **trocar a pasta térmica** se as temperaturas subiram; verificar cabos, conectores e a bateria CMOS; atualizar a BIOS se houver correção importante |
| **A cada 2–4 anos** | Trocar a pasta térmica da CPU (e da GPU, em placas de 3–4 anos ou mais); avaliar a bateria do notebook |

### Ferramentas e materiais de limpeza
- Pulseira antiestática
- Chaves Phillips e Torx
- **Pincéis antiestáticos** ou trinchas macias (de cerdas naturais ou específicas para eletrônica)
- **Ar comprimido** em lata ou **soprador elétrico** (o mais econômico para quem faz muitas limpezas)
- **Álcool isopropílico 99%**
- Panos de **microfibra** e hastes flexíveis (cotonetes)
- **Pasta térmica** de qualidade
- Borracha branca (contatos)
- Aspirador **só para o ambiente**, nunca encostado nas placas (gera estática)

:::atencao O que NÃO usar
- **Aspirador de pó** encostado nas placas (gera estática e pode arrancar componentes).
- **Secador de cabelo** (calor e ar úmido).
- **Álcool comum (etílico)** nas placas, **água**, **limpa-vidros**, **solventes**.
- **Compressor de borracharia** sem filtro de umidade e óleo (joga água e óleo nas placas).
- **Sopro com a boca** (umidade e saliva, como vimos no módulo de oxidação).
:::

### Limpeza peça por peça: passo a passo

**Preparação**
1. Desligue pelo sistema, **tire da tomada** e aperte o botão Power por 5 segundos (para descarregar).
2. Leve o PC para um local **ventilado** (de preferência ao ar livre, porque a poeira vai voar).
3. Coloque a **pulseira antiestática**.
4. **Fotografe** o interior antes de mexer.
5. Retire as laterais e os **filtros**.

| Componente | Como limpar |
|---|---|
| **Filtros de poeira** | Retire e lave com **água e sabão neutro**, ou aspire. **Seque completamente** antes de recolocar |
| **Gabinete (interno)** | Pincel + ar comprimido, **de cima para baixo** (a poeira cai) e de dentro para fora |
| **Ventoinhas (gabinete, CPU, GPU)** | **Trave as pás com o dedo ou com um palito** antes de soprar (se girarem livres em alta rotação, o motor funciona como gerador e pode danificar o mancal e o circuito); limpe as pás com pincel ou cotonete com isopropílico |
| **Dissipador da CPU** | Jatos de ar **entre as aletas**, no sentido contrário ao fluxo normal; pincel nas aletas. Se for trocar a pasta, veja a seção específica |
| **Radiador do water cooler** | Ar comprimido entre as aletas, pelos dois lados; não amasse as aletas (são frágeis) |
| **Placa de vídeo** | Ar comprimido pelas aberturas do dissipador, travando as ventoinhas; pincel na proteção. Para trocar a pasta e os pads, a desmontagem exige experiência (e pode afetar a garantia) |
| **Placa-mãe** | Pincel antiestático macio nos slots e nos dissipadores do VRM; ar comprimido nos slots PCIe e de memória |
| **Memória RAM** | Retire, limpe os **contatos com borracha** e isopropílico, sopre o slot e reencaixe |
| **Fonte** | **Não abra.** Sopre ar pela grade da ventoinha e pela traseira, travando a ventoinha |
| **HD e SSD** | Só por fora, com pincel; confira os cabos |
| **Conectores e portas** | Ar comprimido; contatos oxidados com isopropílico |
| **Teclado** | Vire de cabeça para baixo, ar comprimido, pano com isopropílico (módulo de Teclado) |
| **Mouse** | Pano com isopropílico; limpe a lente do sensor com cotonete seco; limpe os pés de PTFE |
| **Monitor** | **Desligado e frio**, com pano de **microfibra seco** ou levemente umedecido com **água destilada**; nada de álcool nem limpa-vidros em telas foscas (removem o revestimento antirreflexo) |

### Troca de pasta térmica: passo a passo
1. Retire o cooler (desparafuse **em "X"**). Se ele estiver "colado", **gire levemente** em vez de puxar, principalmente nos AMD AM4 (para não arrancar a CPU do soquete com os pinos).
2. Limpe a pasta antiga da **CPU** e da **base do cooler** com **papel-toalha ou filtro de café** e **álcool isopropílico**, até ficarem espelhadas.
3. Espere secar (segundos).
4. Aplique a pasta nova: **um grão de ervilha** no centro (ou um "X" fino em CPUs grandes).
5. Recoloque o cooler de uma vez, sem arrastar, e aperte **em "X"**, alternando, até o fim.
6. Ligue e confira as temperaturas (HWiNFO64) em repouso e sob carga.

### Manutenção preventiva de software (resumo)
| Ação | Ferramenta |
|---|---|
| Atualizações do sistema | Windows Update |
| Drivers | Site da fabricante da GPU e do chipset |
| Programas que iniciam com o Windows | Gerenciador de Tarefas → **Aplicativos de inicialização** |
| Limpeza de temporários | **Sensor de Armazenamento** / Limpeza de Disco (`cleanmgr`) |
| Segurança | **Microsoft Defender** (já incluso e bem avaliado), atenção a e-mails e downloads |
| Saúde dos discos | **CrystalDiskInfo** |
| Integridade do sistema | `sfc /scannow` e `DISM /Online /Cleanup-Image /RestoreHealth` (no Terminal como administrador) |
| Backup | **Regra 3-2-1** (Histórico de Arquivos, OneDrive, Google Drive, HD externo) |
| Otimização de SSD | Automática (TRIM, em "Otimizar unidades"); **nunca desfragmentar** o SSD |

## Manutenção corretiva

### O método de diagnóstico (passo a passo)
1. **Entreviste o usuário**: o que acontece? Desde quando? O que mudou (atualização, queda de energia, mudança de lugar, líquido, peça nova)? O defeito é **constante** ou **intermitente**?
2. **Reproduza o problema**: veja com os próprios olhos.
3. **Do simples para o complexo**: tomada, cabos, conexões, configurações → só depois as peças.
4. **Isole as variáveis**: troque **uma coisa por vez** e teste.
5. **Use peças de teste** (fonte, memória, GPU e SSD sabidamente bons) para fazer **troca por substituição**.
6. **Registre** o que foi feito (ordem de serviço).
7. **Teste** a solução por tempo suficiente (estresse, uso real).
8. **Explique** ao cliente o que houve e como **prevenir**.

### Tabela de diagnóstico rápido
| Sintoma | Causas mais prováveis (em ordem) | Teste e solução |
|---|---|---|
| **Não liga (nenhum sinal de vida)** | Tomada ou filtro de linha; interruptor da fonte; cabo de força; cabo do botão Power; fonte; curto; placa-mãe | Testar a tomada; dar partida pelos pinos PWR_SW; testar a fonte (testador ou outra fonte); ligar fora do gabinete |
| **Liga, gira e desliga em seguida** | Curto (espaçador), cabo de 8 pinos (CPU) desconectado, cooler da CPU não detectado, fonte | Conferir o EPS de 8 pinos; espaçadores; ligar com o mínimo de peças |
| **Liga, mas sem imagem** | Cabo de vídeo na saída errada; memória; GPU sem energia; BIOS incompatível; CPU sem vídeo integrado | LEDs de debug; reencaixar a RAM; 1 pente; outro cabo e outra entrada; Clear CMOS |
| **Bipes ao ligar** | Código de erro do POST (memória, vídeo, CPU) | Consultar o manual da placa ou do fabricante da BIOS |
| **Tela azul (BSOD)** | Driver; memória; overclock ou XMP instável; disco com defeito; superaquecimento | Anotar o **código de parada** (ex.: MEMORY_MANAGEMENT); MemTest86; desativar overclock; atualizar drivers; ver o **Visualizador de Eventos** e os arquivos de despejo (WhoCrashed, BlueScreenView) |
| **Desliga sozinho sob carga** | Superaquecimento; fonte fraca ou defeituosa | HWiNFO64 (temperaturas); testar outra fonte |
| **Travamentos aleatórios** | RAM; disco; temperatura; driver; fonte | MemTest86; CrystalDiskInfo; HWiNFO; Visualizador de Eventos |
| **Lentidão geral** | HD (trocar por SSD); pouca RAM; disco cheio; muitos programas na inicialização; malware; *throttling* térmico | Gerenciador de Tarefas (o que está em 100%?); limpeza; upgrades |
| **Ruído anormal** | Ventoinha com rolamento gasto; HD com defeito ("cliques"); *coil whine* | Identificar a origem parando as ventoinhas uma por vez (com cuidado); **backup imediato** em caso de cliques no HD |
| **Sem internet** | Roteador; cabo; driver; configuração IP/DNS | `ping`, `ipconfig`, reset de rede (Configurações → Rede → Redefinição de rede) |
| **Sem som** | Dispositivo padrão errado; driver; cabo na porta errada | Configurações de som; reinstalar o driver |
| **Data e hora sempre erradas** | Bateria CMOS | Trocar a CR2032 |
| **Cheiro de queimado** | Fonte, conector derretido, componente em curto | **Desligar e tirar da tomada imediatamente**; inspeção visual (capacitores estufados, marcas pretas) |

### Códigos de bipe mais comuns (BIOS AMI, a mais usada)
| Bipes | Significado comum |
|---|---|
| 1 curto | POST concluído com sucesso (em muitas placas) |
| 1 longo + 2 curtos / 1 longo + 3 curtos | Problema de **vídeo** |
| 3 curtos (ou bipes longos contínuos) | Problema de **memória** |
| Bipes contínuos rápidos | Memória ou energia |
| 5 curtos | Processador |

*Os códigos variam por fabricante (AMI, Award, Phoenix) e por placa; **consulte sempre o manual**. Placas modernas preferem **LEDs de diagnóstico** (CPU, DRAM, VGA, BOOT) ou um **display de POST** (código hexadecimal).*

:::exemplo Exemplo completo de manutenção corretiva
**Queixa**: "O PC desliga sozinho quando jogo há uns 20 minutos."
1. **Entrevista**: começou no verão; o PC tem 3 anos; nunca foi limpo.
2. **Reprodução**: com o HWiNFO64 aberto, um jogo leva a GPU a **92 °C** e a CPU a **98 °C** antes de desligar.
3. **Hipótese**: superaquecimento (poeira e pasta seca).
4. **Ação**: limpeza completa, **troca da pasta** da CPU e **ventoinha traseira** que estava travada substituída.
5. **Teste**: 1 hora de jogo: GPU a **74 °C** e CPU a **79 °C**, sem desligamentos.
6. **Orientação**: limpar a cada 6 meses e não deixar o gabinete encostado na parede.
:::
