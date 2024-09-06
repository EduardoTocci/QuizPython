import streamlit as st

with open("style.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Armazena o estado do quiz selecionado
if "quiz_selecionado" not in st.session_state:
    st.session_state.quiz_selecionado = None

quiz = [
    {
        "Pergunta": "Qual o Maior clube do Mundo?",
        "Opções":["A) Santos" , "B) Real Madrid" , "C) Íbis" , "D)Jumentus"],
        "resposta": "A) Santos"
    },
    {
        "Pergunta": "Qual a Maior seleção do Mundo?",
        "Opções":["A) Itália" , "B) EUA" , "C) Alemanha" , "D)Brasil"],
        "resposta": "D)Brasil"
    },
    {
        "Pergunta": "Quantos jogadores tem em um time de futebol?",
        "Opções":["A)13" , "B)12" , "C)10" , "D)11"],
        "resposta": "D)11"
    },
    {
        "Pergunta": "Qual país venceu a Copa do Mundo de 2018?",
        "Opções": ["A) Brasil", "B) Alemanha", "C) França", "D) Argentina"],
        "resposta": "C) França"
    },
    {
        "Pergunta": "Quem é o maior artilheiro da história da Liga dos Campeões da UEFA?",
        "Opções": ["A) Lionel Messi", "B) Robert Lewandowski", "C) Raúl González", "D) Cristiano Ronaldo"],
        "resposta": "D) Cristiano Ronaldo"
    },
    {
        "Pergunta": "Qual clube tem o maior número de títulos da Premier League?",
        "Opções": ["A) Chelsea", "B) Arsenal", "C) Manchester United", "D) Liverpool"],
        "resposta": "C) Manchester United"
    },
    {
        "Pergunta": "Qual foi o único jogador a vencer três Copas do Mundo?",
        "Opções": ["A) Diego Maradona", "B) Pelé", "C) Zinedine Zidane", "D) Ronaldo Fenômeno"],
        "resposta": "B) Pelé"
    },
    {
        "Pergunta": "Qual seleção tem o maior número de títulos da Copa América?",
        "Opções": ["A) Argentina", "B) Brasil", "C) Uruguai", "D) Chile"],
        "resposta": "C) Uruguai"
    },
      {
        "Pergunta": "Qual jogador marcou o gol decisivo para o Brasil na final da Copa do Mundo de 2002?",
        "Opções": ["A) Ronaldo", "B) Rivaldo", "C) Ronaldinho Gaúcho", "D) Cafu"],
        "resposta": "A) Ronaldo"
    },
    {
        "Pergunta": "Em que ano Pelé marcou seu milésimo gol?",
        "Opções": ["A) 1971", "B) 1969", "C) 1968", "D) 1970"],
        "resposta": "B) 1969"
    }
]

perguntas_mitologia = [
    # Seu quiz de mitologia aqui
    {
        "Pergunta": "Quem é o deus do submundo na mitologia grega?",
        "Opções": ["A) Hades", "B) Zeus", "C) Poseidon", "D) Apolo"],
        "resposta": "A) Hades"
    },
    {
        "Pergunta": "Qual é o nome do martelo mágico de Thor na mitologia nórdica?",
        "Opções": ["A) Excalibur", "B) Gungnir", "C) Mjölnir", "D) Aegis"],
        "resposta": "C) Mjölnir"
    },
    {
        "Pergunta": "Quem matou o Minotauro no labirinto de Creta?",
        "Opções": ["A) Perseu", "B) Teseu", "C) Hércules", "D) Aquiles"],
        "resposta": "B) Teseu"
    },
    {
        "Pergunta": "Quem é a deusa do amor e da beleza na mitologia romana?",
        "Opções": ["A) Vênus", "B) Minerva", "C) Juno", "D) Diana"],
        "resposta": "A) Vênus"
    },
    {
        "Pergunta": "Qual deus egípcio é conhecido como o deus dos mortos e da mumificação?",
        "Opções": ["A) Hórus", "B) Rá", "C) Osíris", "D) Anúbis"],
        "resposta": "D) Anúbis"
    },
    {
        "Pergunta": "Quem é o rei dos deuses na mitologia grega?",
        "Opções": ["A) Apolo", "B) Zeus", "C) Ares", "D) Dionísio"],
        "resposta": "B) Zeus"
    },
    {
        "Pergunta": "Qual herói grego é conhecido por sua força e pelos Doze Trabalhos?",
        "Opções": ["A) Aquiles", "B) Hércules", "C) Odisseu", "D) Perseu"],
        "resposta": "B) Hércules"
    },
    {
        "Pergunta": "Qual era o nome do cavalo alado na mitologia grega?",
        "Opções": ["A) Quimera", "B) Centauro", "C) Hipogrifo", "D) Pégaso"],
        "resposta": "D) Pégaso"
    },
    {
        "Pergunta": "Quem é a deusa da sabedoria e da guerra na mitologia grega?",
        "Opções": ["A) Atena", "B) Afrodite", "C) Hera", "D) Deméter"],
        "resposta": "A) Atena"
    },
    {
        "Pergunta": "Qual herói grego era conhecido por sua jornada de volta para casa após a Guerra de Troia?",
        "Opções": ["A) Páris", "B) Aquiles", "C)  Odisseu", "D) Heitor"],
        "resposta": "C) Odisseu"
    },
]

perguntas_geografia = [
    # Seu quiz de geografia aqui
    {
        "Pergunta": "Qual a capital da Noruega?",
        "Opções":["A) Oslo" , "B) Berna" , "C) Estocolmo" , "D) Kiev"],
        "resposta": "A) Oslo"
    },
    {
        "Pergunta": "Qual o maior país em extensão territorial?",
        "Opções": ["A) Canadá", "B) China", "C) Rússia", "D) Estados Unidos"],
        "resposta": "C) Rússia"
    },
    {
        "Pergunta": "Qual o deserto mais seco do mundo?",
        "Opções": ["A) Deserto do Saara", "B) Deserto do Atacama", "C) Deserto de Gobi", "D) Deserto da Arábia"],
        "resposta": "B) Deserto do Atacama"
    },
    {
        "Pergunta": "Qual é o rio mais longo do mundo?",
        "Opções": ["A) Rio Amazonas", "B) Rio Nilo", "C) Rio Yangtzé", "D) Rio Mississipi"],
        "resposta": "B) Rio Nilo"
    },
    {
        "Pergunta": "Qual é a montanha mais alta do mundo?",
        "Opções": ["A) Lhotse", "B) K2", "C) Kangchenjunga", "D) Monte Everest"],
        "resposta": "D) Monte Everest"
    },
    {
        "Pergunta": "Qual país tem a maior população do mundo?",
        "Opções": ["A) Estados Unidos", "B) Índia", "C) China", "D) Indonésia"],
        "resposta": "C) China"
    },
    {
        "Pergunta": "Qual é a capital do Canadá?",
        "Opções": ["A) Ottawa", "B) Toronto", "C) Vancouver", "D) Montreal"],
        "resposta": "A) Ottawa"
    },
    {
        "Pergunta": "Qual é a principal cadeia de montanhas da América do Sul?",
        "Opções": ["A) Montes Apalaches", "B) Cordilheira dos Andes", "C) Montanhas Rochosas", "D) Alpes"],
        "resposta": "B) Cordilheira dos Andes"
    },
    {
        "Pergunta": "Qual país possui o maior número de ilhas no mundo?",
        "Opções": ["A) Suécia", "B) Indonésia", "C) Canadá", "D) Noruega"],
        "resposta": "C) Canadá"
    },
    {
        "Pergunta": "Qual é o maior lago da África em termos de área?",
        "Opções": ["A) Lago Vitória", "B) Lago Tanganica", "C) Lago Malaui", "D) Lago Chad"],
        "resposta": "A) Lago Vitória"
    }
]

perguntas_historia = [
      {
        "Pergunta": "Qual foi o primeiro presidente dos Estados Unidos?",
        "Opções": ["A) John Adams", "B) Thomas Jefferson", "C) Abraham Lincoln", "D) George Washington"],
        "resposta": "D) George Washington"
    },
    {
        "Pergunta": "Em que ano começou a Segunda Guerra Mundial?",
        "Opções": ["A) 1945", "B) 1941", "C) 1939", "D) 1935"],
        "resposta": "C) 1939"
    },
    {
        "Pergunta": "Quem foi o líder revolucionário que iniciou a Revolução Cubana?",
        "Opções": ["A) Fidel Castro", "B) Che Guevara", "C) Hugo Chávez", "D) Simón Bolívar"],
        "resposta": "A) Fidel Castro"
    },
    {
        "Pergunta": "Qual era o nome da rainha que governou o Reino Unido durante o século XIX?",
        "Opções": ["A) Rainha Ana", "B) Rainha Elizabeth I", "C) Rainha Vitória", "D) Rainha Mary"],
        "resposta": "C) Rainha Vitória"
    },
    {
        "Pergunta": "Qual foi o evento que marcou o início da Revolução Francesa?",
        "Opções": ["A) Declaração dos Direitos do Homem", "B) Queda da Bastilha", "C) Morte de Luís XVI", "D) Fuga de Varennes"],
        "resposta": "B) Queda da Bastilha"
    },
    {
        "Pergunta": "Quem foi o primeiro imperador romano?",
        "Opções": ["A) Calígula", "B) Júlio César", "C) Nero", "D) Augusto"],
        "resposta": "D) Augusto"
    },
    {
        "Pergunta": "Em que ano ocorreu a independência dos Estados Unidos?",
        "Opções": ["A) 1776", "B) 1789", "C) 1804", "D) 1812"],
        "resposta": "A) 1776"
    },
    {
        "Pergunta": "Qual tratado encerrou a Primeira Guerra Mundial?",
        "Opções": ["A) Tratado de Utrecht", "B) Tratado de Tordesilhas", "C) Tratado de Paris", "D) Tratado de Versalhes"],
        "resposta": "D) Tratado de Versalhes"
    },
    {
        "Pergunta": "Quem foi o explorador que liderou a primeira viagem ao redor do mundo?",
        "Opções": ["A) Vasco da Gama", "B) Cristóvão Colombo", "C) Fernão de Magalhães", "D) Américo Vespúcio"],
        "resposta": "C) Fernão de Magalhães"
    },
    {
        "Pergunta": "Qual civilização antiga construiu as pirâmides de Gizé?",
        "Opções": ["A) Egípcia", "B) Maia", "C) Inca", "D) Mesopotâmica"],
        "resposta": "A) Egípcia"
    }
]

st.header(f"Quiz de Conhecimento")

st.title("Escolha o Tema do Quiz")

coluna1, coluna2, coluna3, coluna4 = st.columns(4)

with coluna1:
    if st.button("Futebol"):
        st.session_state.quiz_selecionado = "futebol"
  
with coluna2:
    if st.button("Mitologia"):
        st.session_state.quiz_selecionado = "mitologia"

with coluna3:
    if st.button("Geografia"):
        st.session_state.quiz_selecionado = "geografia"

with coluna4:
    if st.button("História"):
        st.session_state.quiz_selecionado = "historia"

# Função para exibir as perguntas
def exibir_perguntas(quiz):
    score = 0
    respostas_selecionadas = []

    for cont, pergunta in enumerate(quiz):
        st.subheader(f"{cont + 1}° Pergunta: {pergunta['Pergunta']}")
        respostas = st.radio("Selecione sua resposta", pergunta["Opções"], key=f"radio_{cont}")
        respostas_selecionadas.append(respostas)

    if st.button("Confirmar respostas"):
        for cont, pergunta in enumerate(quiz):
            if respostas_selecionadas[cont] == pergunta["resposta"]:
                st.success(f"Pergunta {cont + 1}: Acertou")
                score += 1
            else:
                st.error(f"Pergunta {cont + 1}: Errou. Resposta correta: {pergunta['resposta']}")
                
        st.write(f"Pontuação final: {score} de {len(quiz)}")

# Exibe o quiz de acordo com o tema selecionado
if st.session_state.quiz_selecionado == "futebol":
    exibir_perguntas(quiz)

elif st.session_state.quiz_selecionado == "mitologia":
    exibir_perguntas(perguntas_mitologia)

elif st.session_state.quiz_selecionado == "geografia":
    exibir_perguntas(perguntas_geografia)

elif st.session_state.quiz_selecionado == "historia":
    exibir_perguntas(perguntas_historia)
