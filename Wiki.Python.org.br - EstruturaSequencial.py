#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercício 01 #

print("Alo Mundo!")


# In[4]:


# Exercício 02 #

numero = input("Diga um número: ")

print("O número informado foi: ", numero)


# In[12]:


# Exercício 03 #

a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
print("A soma de ", a, " e ", b, " é: ", a + b)


# In[16]:


# Exercício 04 #

a = int(input("Qual foi sua nota no 1º bimestre? "))
b = int(input("Qual foi sua nota no 2º bimestre? "))
c = int(input("Qual foi sua nota no 3º bimestre? "))
d = int(input("Qual foi sua nota no 4º bimestre? "))
print("A média de suas notas bimestrais é ", (a + b + c + d) / 4)


# In[22]:


# Exercício 05 #

a = int(input("Diga um valor em metros para converter em centímetros: "))
if a == 1:
    print("1 metro equivale a 100 centímetros")
else:
    print(a, "metros equivalem a", a*100, "centímetros.")


# In[25]:


# Exercício 06 #

import math
a = float(input("Diga o raio do círculo para saber a área: "))
print("Considerando o raio de", a,", a área do círulo é:", math.pi*(a**2))


# In[27]:


# Exercício 07 #

lado = int(input("Diga o valor para os lados de um quadrado: "))
print("O quadrado de lado", lado, "tem área total de", lado**2)
ladoMaior = math.sqrt((lado**2)*2)
print("O dobro da área desse quadrado seria", (lado**2)*2)
print("Cada lado desse novo quadrado teria", ladoMaior)


# In[31]:


# Exercício 08 #

valorHora = float(input("Que valor você recebeu por hora trabalhada esse mês?"))
jornada = int(input("Quantas horas você trabalhou esse mês?"))
salario = valorHora * jornada
salarioMinimo = 1100
if salario > salarioMinimo:
    print("Isso significa que seu salário esse mês será: R$", jornada*valorHora)
else:
    print("Considerando que seu ganho seria de R$", salario, ", você receberá o salário mínimo de R$1.100,00")


# In[ ]:


# Exercício 09 #

tempF = float(input("Qual a temperatura em graus Fahrenheit?"))
tempC = 5 * ((tempF-32) / 9)
print(tempF, "graus Fahrenheit equivalem a", tempC, "graus Celsius.")


# In[36]:


# Exercício 10 #

tempC = float(input("Qual a temperatura em graus Celsius?"))
tempF = (tempC *9/5) + 32
print(tempC, "graus Celsius equivalem a", tempF, "graus Fahrenheit.")


# In[37]:


# Exercício 11 #

a = int(input("Diga um número inteiro: "))
b = int(input("Diga outro número inteiro: "))
c = float(input("Agora diga um número real: "))
print("O produto do dobro do primeiro com metade do segundo é igual a", (a*2)*(b/2))
print("A soma do triplo do primeiro com o terceiro é igual a", (a*3)+c)
print("O terceiro número elevado ao cubo é igual a", c**3)


# In[39]:


# Exercício 12 #

h = float(input("Diga sua altura:"))
pesoIdeal = (72.7*h)-58
print("O seu peso ideal é:", pesoIdeal)


# In[48]:


# Exercício 13 #

h = float(input("Qual sua altura?"))
print("Se você é homem, seu peso ideal é ", (72.7*h) - 58)
print("Se você é mulher, seu peso ideal é ", (62.1*h) - 44.7)


# In[51]:


# Exercício 14 #

peso = float(input("João, quantos quilos você pescou hoje? "))
excesso = peso-50
multa = excesso*4

if peso > 50:
    print("João, com", peso, "quilos de pesca você excedeu o limite em", excesso, "quilos.")
    print("Isso significa uma multa de R$", multa, ".")
else:
    print("Ótimo João, você não excedeu o limite de pesca.")


# In[54]:


# Exercício 15 #

valorHora = float(input("Que valor você recebeu por hora trabalhada esse mês?"))
jornada = int(input("Quantas horas você trabalhou esse mês?"))
salarioBruto = valorHora * jornada
salarioMinimo = 1100
ir = salarioBruto*0.11
inss = salarioBruto*0.08
sind = salarioBruto*0.05
descontos = ir+inss+sind
salarioLiquido = salarioBruto-descontos

print("No referido mês, seu salário bruto é de:", salarioBruto)
print("Você será descontado em 11% de referente ao Imposto de Renda, num total de: R$", ir)
print("Você será descontado em 8% de referente ao INSS, num total de: R$", inss)
print("Você será descontado em 5% de referente ao Imposto Sindical, num total de: R$", sind)
if salarioLiquido < salarioMinimo:
    print("Após os descontos, seu salário liquido seria R$", salarioLiquido, ". Portanto você receberá o salário de R$1.100,00")
else:
    print("Após os descontos, seu salário liquido será R$", salarioLiquido, ".")


# In[67]:


# Exercício 16 #

area = float(input("Qual a área, em m², a ser pintada?"))
litros = float(area/3)
if litros%18 == 0:
    latas = int(litros/18)
else:
    latas = int((litros/18)+1)
gasto = latas*80
print("Você precisará comprar", latas, "latas de tinta.")
print("O preço total dessa compra será de R$", gasto)


# In[84]:


# Exercício 17 #

area = float(input("Qual a área, em m², a ser pintada?"))
litros = area/6

gastoLatas = int(latas*80)
gastoGaloes = int(galoes*25)

if litros%18 == 0:
    latas = int(litros/18)
else:
    latas = int((litros/18)+1)
    
if litros%3.6 == 0:
    galoes = int(litros/3.6)
else:
    galoes = int((litros/3.6)+1)

misturaLatas = int((litros*1.1)//18) 
misturaGaloes = int(((litros*1.1)%18)/3.6)
if litros-(misturaLatas%18)+(misturaGaloes%3.6) != 0:
    misturaGaloes += 1

print("Comprando apenas latas, precisará de", latas, "latas. Isso custará R$", gastoLatas, ".")
print("Comprando apenas galões, precisará de", galoes, "latas. Isso custará R$", gastoGaloes, ".")
print("Misturando e acrescendo 10% para evitar falta, você precisará de", misturaLatas, "latas e", misturaGaloes, "galões. Isso custará R$", misturaLatas*80 + misturaGaloes*25, ".")


# In[71]:


# Exercício 18 #

tamanho = float(input("Qual o tamanho do arquivo para download (em MB?)"))
velocidade = int(input("Qual a velocidade do link de internet (em Mbps)?"))
download = velocidade*8/tamanho

print("O seu download vai demorar aproximadamente:", download/60, "minutos.")

