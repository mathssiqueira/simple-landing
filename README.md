Template simples de uma Landing Page

- Python 3.9
- Flask 2.0
- Jinja 2
- Bootstrap 5

Configurações:
  - Criando Ambiente Virtual
    - python3 -m venv simple-landing
    - source simple-landing/bin/activate
    - pip install -r requeriments.txt
 
 Execução (dentro do venv):
  - python simple-landing/run.py

A execução do APP encontra-se configurado para: http://IP_Servidor:5000, para alteação da porta (Ex: 80) efetuar alteração dentro do arquivo run.py 
  - De:
    - app.run(host="0.0.0.0", debug=False)
  - Para:
    - app.run(host="0.0.0.0", port="80", debug=False)
