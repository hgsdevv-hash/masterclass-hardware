# Masterclass de Hardware

Masterclass completa de TI com foco em hardware: história da computação, internet no mundo e no Brasil, bits e bytes, elétrica básica e cada componente do PC, até compatibilidade, manutenção, notebooks, computação quântica e IA.

- **Site interativo:** https://hgsdevv-hash.github.io/masterclass-hardware/
- **Apresentação:** https://hgsdevv-hash.github.io/masterclass-hardware/apresentacao.html
- Apostila em PDF e Word e PowerPoint na pasta `docs/`.

## Como gerar

```
python ferramentas/baixar_imagens.py
python ferramentas/build.py
python ferramentas/pdf.py        # precisa de um servidor local na porta 5750 servindo saida/
python ferramentas/docx_build.py
python ferramentas/slides_build.py
```

O conteúdo fica em `conteudo/` (um arquivo Markdown por módulo).

Produzido por [HGS Dev](https://hgsdev.com.br).
