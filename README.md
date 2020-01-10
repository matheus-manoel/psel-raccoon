---
layout: post
title: Trabalhando com fluxo de dados: resolvendo o desafio do processo seletivo da Raccoon
---

## 10.1.2020

Aqui vamos nós: mais um desafio em um processo seletivo a ser resolvido.

O processo de escrever meus pensamentos e minhas tomadas de decisão me agrada, pois ele próprio me ajuda a pensar e a tomar decisões. Além disso,

- pode servir como guia para alguém resolvendo um problema similar ao meu,
- será útil caso eu passe para a fase de entrevista e precise explicar minhas decisões,
- pode ser útil para os trabalhadores que estão conduzindo meu processo seletivo entenderem como penso os problemas e como modelo e codifico suas soluções.

Lo-fi no talo, cafeína e sem mais digressões, vamos ao problema:

#### Resumo Abstrato do Problema

Tratar dados recebidos através de uma requisição e enviá-los, de acordo com as especificações, à outro serviço.

#### Especificações da Solução Desejada 

a) IDs dos produtos que contém "promoção" no título e seus respectivos preços para todas as mídias. O
resultado deve estar ordenado por preço e depois ID, de forma CRESCENTE. OBS: Não pode conter IDs de
produtos repetidos.

b) IDs dos posts e preços dos produtos para as postagens com mais de 700 likes na mídia
"instagram_cpc". O resultado deve estar ordenado por preço e depois ID de forma CRESCENTE.

c) Somatório de likes no mês de maio de 2019 para todas as mídias pagas (google_cpc, facebook_cpc,
instagram_cpc).

d) Todos os IDs de produtos devem ter o mesmo preço nas postagens. Eventualmente poderá ocorrer
postagens com o mesmo produto e diferentes preços, causando problemas para o cliente.

Sua tarefa é verificar se existe alguma inconsistência nos produtos que a API retorna pela rota https://us-
central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get_error.

Caso seja encontrado algum erro, envie em uma lista todos os IDs de produtos com erro de forma ordenada
e crescente.
Atenção: A rota para o exercício d é diferente dos exercícios a, b e c.

#### Documentação da API

- Rota de a, b e c: https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get

- Exemplo de resposta:

```json
{
    "report_info": {
        "trace_id": "dd628806-d804-45f1-8d26-9ef604328874",
        "begin_date": "23/09/2019",
        "end_date": "28/11/2019",
        "response": 200,
        "extraction_duration": "260 seconds",
        "extraction_size": "16.25 Mb"
    },
    "posts": [
        {
            "media": "MEDIA_A",
            "post_id": "928981fb-77ed-48ef-8aa2-026207731121",
            "title": "product_0_padrao",
            "product_id": "b755a6f1-d34a-433b-b6c9-bf87a67c459f",
            "price": 20,
            "date": "18/10/2019",
            "likes": 828
        },
        {
            "media": "MEDIA_A",
            "post_id": "ad5ae35c-b3cd-4422-aef5-37e30500c8a3",
            "title": "product_1_lancamento_promocao",
            "product_id": "2e370229-750b-4dc7-91c9-ae63cd5e154e",
            "price": 261,
            "date": "24/07/2019",
            "likes": 520
        }
    ]
}
```

- Rota de d: https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get_error

- Exemplo de Resposta:

```json
{
    "report_info": {
        "trace_id": "dd628806-d804-45f1-8d26-9ef604328874",
        "begin_date": "23/09/2019",
        "end_date": "28/11/2019",
        "response": 200,
        "extraction_duration": "260 seconds",
        "extraction_size": "16.25 Mb"
    },
    "posts": [
        {
            "media": "MEDIA_A",
            "post_id": "928981fb-77ed-48ef-8aa2-026207731121",
            "title": "product_0_padrao",
            "product_id": "b755a6f1-d34a-433b-b6c9-bf87a67c459f",
            "price": 20,
            "date": "18/10/2019",
            "likes": 828
        },
        {
            "media": "MEDIA_A",
            "post_id": "ad5ae35c-b3cd-4422-aef5-37e30500c8a3",
            "title": "product_1_lancamento_promocao",
            "product_id": "2e370229-750b-4dc7-91c9-

            ae63cd5e154e",

            "price": 261,
            "date": "24/07/2019",
            "likes": 520
        }
    ]
}
```

- Rota de Envio: https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_post

- Formato Esperado de dados no POST

```json
{
    'full_name': "nome completo",
    'email': "email@pessoal.com",
    'code_link': "www.github.com/name/psel-raccoon",
    'response_a': [
        {"product_id": "prod_id_example", "price_field": 10},
        {"product_id": "prod_id_example2", "price_field": 50}
    ],
    'response_b': [
        {"post_id": "post_id_example3", "price_field": 20},
        {"post_id": "post_id_example3", "price_field": 100}
    ],
    'response_c': 1365,
    'response_d': ["prod_id_example7", "prod_id_example8"]
}
```

- Exemplo de Resposta POST

```json
{
    "success": true,
    "msg": "Thank you for sending your answer. Results: Response A: true Response B: true: Response C: true Response D: true"
}
```
