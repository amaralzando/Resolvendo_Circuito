import math

tensaoGerador =  127#int(input("Insira o valor do Tensao gerador: "))
frequenciaGerador = 60 #int(input("Insira o valor do Frequencia do gerador: "))

R1 =  100#int(input("Insira o valor do resitor 1: "))
R2 =  100#int(input("Insira o valor do resitor 2: "))
R3 =  100#int(input("Insira o valor do resitor 3: "))
R4 =  100#int(input("Insira o valor do resitor 4: "))
R5 =  100#int(input("Insira o valor do resitor 5: "))
R6 =  100#int(input("Insira o valor do resitor 6: "))
retificadorL =  100#int(input("Insira o valor do retificador: "))

print(f"tensão : {tensaoGerador}v e frequencia: {frequenciaGerador}hz")
print(f"R1 {R1}Ω, R2 {R2}Ω, R3 {R3}Ω, R4 {R4}Ω, R5 {R5}Ω, R6 {R6}Ω")


##Corrente Total Circuito = Tensão /  ## Resitencia Total
paraleloR1 = 1/(1/R1)
paraleloR6 = 1/(1/R6)
resistenciaTotal =(paraleloR1+paraleloR6+R2+R3+R4+R5)
correnteTotal = round(tensaoGerador/resistenciaTotal,2)
print(f"Corrente Total: {correnteTotal}i")

#A corrente que percorre cada  resistor do circuito
#Paralelo
correnteR1 = round(tensaoGerador/(paraleloR1+paraleloR6),2)#certo?
correnteR6 = round(tensaoGerador/(paraleloR1+paraleloR6),2)#certo?
#Serie
correnteR2 = round(correnteTotal,2)
correnteR3 = round(correnteTotal,2)
correnteR4 = round(correnteTotal,2)
correnteR5 = round(correnteTotal,2)

print(f"Corrente paralela: R1 {correnteR1}i, R6 {correnteR6}i, Corrente Serie: R2 {correnteR2}i, R3 {correnteR3}i, R4 {correnteR4}i, R5 {correnteR5}i")

#A potência consumida em cada elemento do circuito e produzida pelo gerador
potenciaR1 = round(tensaoGerador*correnteR1,2)#certo?128
potenciaR6 = round(tensaoGerador*correnteR6,2)#certo?
potenciaR2 = round(tensaoGerador*correnteR2,2)
potenciaR3 = round(tensaoGerador*correnteR3,2)
potenciaR4 = round(tensaoGerador*correnteR4,2)
potenciaR5 = round(tensaoGerador*correnteR5,2)

print(f"Ptencial paralela: R1 {potenciaR1}w, R6 {potenciaR6}w,  Potencia Serie: R2 {potenciaR2}w, R3 {potenciaR3}w, R4 {potenciaR4}w, R5 {potenciaR5}w")


####Parte22222222222222222222222222222
##Usarei os mesmo input

##tensão de pico no capacitor, a tensão de ripple e a tensão média na carga
V1 = 200 #Não sei o que é
N2 = 200 #Não sei o que é
N1 = 1000 #Não sei o que é

tensaoEficazSecundario = round(((V1*N2)/N1),2)
print(f"Tensaão Eficaz Secundário: {tensaoEficazSecundario}i")

tensaoPicoSecundaria = round(math.sqrt(2)*tensaoEficazSecundario,2)
print(f"Tensão Pico Secundário: {tensaoPicoSecundaria}i")

Vd = 0.7 #Não sei o que é
tensaoPicoCapacitor = round((tensaoPicoSecundaria/2) - Vd,2)
print(f"Tensão Pico Capacitor: {tensaoPicoCapacitor}i")

RL = retificadorL
tensaCorrenteMedia = round(tensaoPicoCapacitor/RL,2)
print(f"Tensão Corrente média: {tensaCorrenteMedia}i")

C = resistenciaTotal #Não sei se é isso
F = frequenciaGerador
tensaoRipple = round(tensaCorrenteMedia/(C*F),2)
print(f"Tensão Ripple: {tensaoRipple}i")

Vmax = tensaoPicoCapacitor
Vmin = tensaoPicoCapacitor-tensaoRipple
tensaoMediaCarga = round((Vmax+Vmin)/2,2)
print(f"Tensão Média Carga: {tensaoMediaCarga}i")

