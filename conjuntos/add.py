#{}.add                       —> é possivel passar um elemento e se não existir,			 	
    #                          ele passa a existir com add. se ja existir, é ignorado.

sorteio= {1, 23}

sorteio.add(25) #>> {1, 23, 25}
sorteio.add(42) #>> {1, 23, 25, 42}
sorteio.add(25) # >> {1, 23, 25, 42}
