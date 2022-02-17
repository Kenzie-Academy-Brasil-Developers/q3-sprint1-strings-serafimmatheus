# Código do dev aqui

# def standardize_names(character_name):
#     new_name = character_name.strip()
#     new_name_split = new_name.split()

#     if len(new_name_split) > 1:
#         new_name_format = "-".join(new_name_split)
#         return new_name_format
#     else:
#         new_name_format = "-".join(new_name_split)
#         return new_name_format

# hero = standardize_names("        Matheus       ")
# print(hero)

# def standardize_title(title):
#     return title.title()

# string = standardize_title("minha namorada é gata.")
# print(string)

#  VERIFICAR O PORQUE NAO ESTA DANDO ESPAÇAMENTOS...

# def standardize_text(text):
#     # use .capitalize()
#     ...
#     list_capitalize = []
#     text_split = text.split(".")
#     for i in text_split:
#         list_capitalize.append(i.strip().capitalize())
    

#     text_format = ".".join(list_capitalize)
#     return text_format.replace(".", ". ")


# text_2 = "a famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma lista com números de telefone de pessoas que morreram recentemente. é uma coisa assustadora, considerando que os nomes das poucas pessoas vivas presentes na lista estão assinalados em vermelho com uma cruz. O da própria Constance é um deles."
# print(standardize_text(text_2))


# def title_creator(text):
#     ...
#     text_title = text.title()

#     return f" {'-' * 20}{text_title}{'-' * 20}"

# print(title_creator("pense num deserto"))

# ------------------------------------------------------------------------------------------------------------------------------------------ #


def text_merge(text_a, text_b):
    ...

    # Formatando texto 1
    text_a_strip = text_a.strip()
    text_a_split = text_a_strip.split(" ")

    list_strip = []

    for i in text_a_split:
        if i == "":
            continue
        else:
            list_strip.append(i)
    
    text_a_join = " ".join(list_strip)
    
    text_a_split_2 = text_a_join.split(".")

    list_capitalize = []

    for i in text_a_split_2:
        text_a_new = i.strip().capitalize()
        list_capitalize.append(text_a_new)

    text_a_formated = ". ".join(list_capitalize)

    # Formatando texto 2
    text_b_strip = text_b.strip()
    text_b_split = text_b_strip.split(" ")

    list_strip_B = []

    for i in text_b_split:
        if i == "":
            continue
        else:
            list_strip_B.append(i)
    
    text_b_join = " ".join(list_strip_B)
    
    text_b_split_2 = text_b_join.split(".")

    list_capitalize_b = []

    for i in text_b_split_2:
        text_b_new = i.strip().capitalize()
        list_capitalize_b.append(text_b_new)

    text_b_formated = ". ".join(list_capitalize_b)
    
    return text_a_formated[:-2] + " " + text_b_formated


text_of_blog_a = ' na Londres do pós-guerra, a escritora     Juliet tenta encontrar uma   trama para seu novo livro. ela recebe ajuda por meio de uma carta de um      desconhecido, um nativo da ilha de Guernsey, em cujas mãos havia chegado um livro    que há tempos tinha pertencido    a Juliet. '
text_of_blog_b = 'O romance "Cinco Quartos de Laranja" é como   um vinho intenso e delicado.    usando metáforas culinárias, personagens peculiares  e acontecimentos sobrenaturais,      Harris cria uma história complexa e      bela ao mesmo tempo.'
text_merge(text_of_blog_a, text_of_blog_b)