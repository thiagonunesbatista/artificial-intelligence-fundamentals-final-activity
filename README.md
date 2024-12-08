# Visão de Cores para Deuteranopia

Projeto criado para disciplina Fundamentos de Inteligência Artificial (FIA) - Graduação, pelos alunos Thiago Nunes Batista e Eduardo Gonçalves Souza.

---

## 📘 Sobre o Projeto

Este projeto utiliza Inteligência Artificial com Visão Computacional para identificar cores em tempo real e exibi-las de duas formas:

1. Cor Detectada — Como a cor é vista por pessoas sem daltonismo.
2. Simulação de Deuteranopia — Como a cor é vista por pessoas com deuteranopia (um tipo de daltonismo que afeta a percepção das cores verde e vermelho).

A ideia para este projeto surgiu a partir de uma experiência pessoal: um familiar próximo possui deuteranopia. A solução visa promover a inclusão e acessibilidade, além de sensibilizar as pessoas sobre como é a visão de quem tem essa condição.

O código detecta tons de verde em uma imagem no formato HSV (Hue, Saturation, Value) e simula a visão de deuteranopia, mudando a percepção de verde para como uma pessoa com essa condição enxerga.

Importante salientar que para o código funcionar corretamente é necessário estar em um ambiente com boa iluminação.

---

## 🎯 Objetivos do Projeto

- Identificação de cores em tempo real por meio de uma webcam ou câmera integrada.
- Simulação da visão de deuteranopia para ajudar pessoas sem daltonismo a compreenderem as diferenças perceptivas.
- Educação e Sensibilização — Mostrar, de forma prática e visual, como a deuteranopia impacta a percepção de cores.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — Linguagem principal, incluindo o uso de tipos de dados da biblioteca padrão (`typing`, `List`, `Tuple`, etc.).
- **OpenCV** — Para captura de imagem e manipulação de cores.
- **NumPy** — Para operações de matriz e cálculo de cores.

---

## Instalação de Dependências

Instale as dependências listadas no arquivo `requirements.txt` com o comando abaixo:

```bash
pip install -r requirements.txt
```

## Execução do projeto

Execute o comando abaixo para executar o projeto:

```bash
python main.py
```
