# Loja de Meias - Gerador de Estrutura de Pastas

Script em Python que cria a árvore de diretórios de um projeto de loja de meias, com catálogo, estoque, vendas, marketing, site, logística e financeiro.

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa (veja `requirements.txt`)

## Como usar

Cria a estrutura na pasta padrão `loja-de-meias/`:

```bash
python arquivo.py
```

Cria a estrutura em outro destino:

```bash
python arquivo.py minha-pasta
```

O script pode ser executado mais de uma vez: pastas já existentes são mantidas e arquivos já criados não são sobrescritos.

## Estrutura criada

```
loja-de-meias/
├── README.md
├── .gitignore
├── docs/
│   ├── identidade-visual/
│   └── plano-de-negocios.md
├── catalogo/
│   ├── meias-casuais/        (listradas, estampadas, lisas)
│   ├── meias-esportivas/     (cano-curto, cano-alto, compressao)
│   ├── meias-sociais/
│   ├── meias-termicas/
│   ├── meias-infantis/
│   ├── meias-divertidas/     (animais, frutas, edicoes-limitadas)
│   └── kits-presente/
├── estoque/                  (entradas, saidas, inventario)
├── fornecedores/             (contratos, pedidos-de-compra)
├── vendas/                   (pedidos, clientes, devolucoes-trocas, relatorios)
├── marketing/
│   ├── campanhas/            (dia-dos-namorados, black-friday, natal)
│   ├── redes-sociais/
│   ├── fotos-produtos/
│   └── email-newsletter/
├── site/
│   ├── public/               (imagens, fontes)
│   └── src/                  (componentes, paginas, estilos)
├── logistica/                (embalagens, transportadoras, etiquetas-de-envio)
└── financeiro/               (notas-fiscais, contas-a-pagar, contas-a-receber)
```

## Personalização

Para adicionar ou remover pastas, edite a lista `PASTAS` no início do `arquivo.py`. Para criar arquivos iniciais com conteúdo, edite o dicionário `ARQUIVOS`.

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `arquivo.py` | Script que gera a árvore de diretórios |
| `requirements.txt` | Dependências (nenhuma por enquanto) |
| `README.md` | Este documento |
