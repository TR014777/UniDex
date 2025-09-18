# 🌐 UniDex

O **UniDex** é uma aplicação web desenvolvida com **Django** que consome a **PokéAPI** para exibir informações de Pokémons.  
Basta digitar o **nome** ou **ID** de um Pokémon para resgatar dados como **nome, altura, peso e tipos**.

---

## ✨ Funcionalidades
- 🔎 Buscar Pokémon pelo **nome** ou **ID**.  
- 📋 Exibir informações básicas do Pokémon:  
  - Nome  
  - ID  
  - Altura  
  - Peso  
  - Tipos  
- 🎨 Frontend simples e estilizado com HTML/CSS.  
- ⚡ Integração com a [PokéAPI](https://pokeapi.co/).  

---

## 🖼️ Exemplo de tela
![Exemplo do UniDex]
<img width="1351" height="749" alt="image" src="https://github.com/user-attachments/assets/eefdebe7-7598-4f67-9423-017a75df5f5d" />


---

## 🚀 Tecnologias utilizadas
- **Python 3**  
- **Django**  
- **Django REST Framework**  
- **HTML5 + CSS3**  
- **PokéAPI**  

---

## 📂 Estrutura do projeto
```bash
unidex/
├── app/                # App principal
│   ├── migrations/     
│   ├── static/         # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/      # Templates HTML
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── unidex/             # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/               # Ambiente virtual
├── db.sqlite3          # Banco de dados
├── manage.py
├── requirements.txt
└── README.md
```
---
## ⚙️ Como rodar o projeto localmente

Clone este repositório:
```bash
git clone https://github.com/TR014777/unidex.git
cd unidex
```


## Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

## Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execute as migrações:
```bash
python manage.py migrate
```

## Inicie o servidor:
```bash
python manage.py runserver
```

# Acesse no navegador:

*click*👉http://127.0.0.1:8000/

👨‍💻 Autor

Desenvolvido por Juan e Daniel(O bola e o Pika) ✨
