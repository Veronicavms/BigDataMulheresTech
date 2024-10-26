
#ATIVIDADE (github):

#Crie mais duas tabelas (sugestão: 'cursos' e 'filiais') no mesmo banco de dados
#onde você criou 'alunos' e 'professores'. Façam mais características para essas tabelas (ao menos 5)
#e criem, pelo menos, 10 injeções de dados para as novas tabelas e 1 consulta para cada uma delas. 
# No final, peça (no VSCode) para que o Pandas leia cada tabela nova que foi criada.

CREATE TABLE cursos (
  id INTEGER PRIMARY KEY,
  unidade TEXT NOT NULL,
  endereço TEXT NOT NULL,
  modalidade TEXT NOT NULL,
  disciplinas TEXT NOT NULL,
);
-- injeção de dados-teste
INSERT INTO cursos VALUES (01, 'Copacabana', 'Rua Pompeu Loureiro', 'Presencial', 'Big Data');
INSERT INTO cursos VALUES (02, 'Centro', 'Rua Presidente Vargas', 'Presencial', 'Power By');
INSERT INTO cursos VALUES (03, 'Tijuca', 'Barao de Mesquita', 'Semi Presencial', 'Big Data')
INSERT INTO cursos VALUES (04, 'Barra da Tijuca', 'Avenida das Américas', 'Semi Presencial', 'Power By')


SELECT * FROM cursos WHERE genero= 'F'


#

CREATE TABLE unidades (
  id INTEGER PRIMARY KEY,
  unidade TEXT NOT NULL,
  endereço TEXT NOT NULL,
  tipo TEXT NOT NULL, #propria ou filial
);
-- injeção de dados-teste
INSERT INTO unidades VALUES ();
INSERT INTO unidades VALUES ();

SELECT * FROM unidades WHERE genero= 'F'