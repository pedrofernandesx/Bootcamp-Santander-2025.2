def exibir_poema(data_extenso, *args, **kwargs): # Função que exibe um poema com metadados
    texto = "\n".join(args)                         # Junta os versos do poema, o \n cria quebras de linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # Formata os metadados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # Monta a mensagem final, incluindo data, poema e metadados
    print(mensagem)

exibir_poema(
    "22 de dezembro de 2025",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those.",
    autor="Tim Peters",
    ano=1999
)
