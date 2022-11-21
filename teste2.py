lista = "NOT", "AND", "NAND", "OR", "NOR", "XOR", "NXOR"

circuitoDigital = input(f"Insira o circuito {lista}: ") #Circuito digital
cd = circuitoDigital.upper()

print(cd)
 
if cd == "NOT":
    print("Aparece a foto com o NOT...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 1:
        print("Led Desligado...")
    else:
        print("Led Ligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ") 
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 1:
        print("Led Desligado...")
      else:
         print("Led Ligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()


elif cd == "AND":
    print("Aparece a foto com o AND...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 1 and y == 1:
        print("Led Ligado...")
    else:
        print("Led DesligadO...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 1 and y == 1:
        print("Led Ligado...")
      else:
        print("Led DesligadO...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()


elif cd == "NAND":
    print("Aparece a foto com o NAND...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 0 and y == 1:
        print("Led Ligado...")
    elif x == 1 and y == 0:
        print("Led Ligado...")
    else:
        print("Led Desligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 0 and y == 1:
        print("Led Ligado...")
      elif x == 1 and y == 0:
        print("Led Ligado...")
      else:
        print("Led Desligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()


elif cd == "OR":
    print("Aparece a foto com o OR...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 1 and y == 0:
        print("Led Ligado...")
    elif x == 0 and y == 1:
        print("Led Ligado...")
    else:
        print("Led Desligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 1 and y == 0:
        print("Led Ligado...")
      elif x == 0 and y == 1:
        print("Led Ligado...")
      else:
        print("Led Desligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()

        
elif cd == "NOR":
    print("Aparece a foto com o NOR...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 0 and y == 0:
        print("Led Ligado...")
    else:
        print("Led Desligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 0 and y == 0:
        print("Led Ligado...")
      else:
        print("Led Desligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()

        
elif cd == "XOR":
    print("Aparece a foto com o XOR...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 1 and y == 0:
        print("Led Ligado...")
    else:
        print("Led Desligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 1 and y == 0:
        print("Led Ligado...")
      else:
        print("Led Desligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()

        
elif cd == "NXOR":
    print("Aparece a foto com o NXOR...")
    x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
    if x == 0 and y == 0:
        print("Led Ligado...")
    else:
        print("Led Desligado...")
    testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
    tn = testarNovamente.upper()
    while tn == "SIM":
      x =int(input("Insira a porta 1 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      y =int(input("Insira a porta 2 para os teste de circuitos (Ligado = 1 ou desligado = 0): "))
      if x == 0 and y == 0:
        print("Led Ligado...")
      else:
        print("Led Desligado...")
      testarNovamente = input("Gostaria de Testar Novamente (sim ou não): ")
      tn = testarNovamente.upper()

        
else:
    print("Valor errado...")

