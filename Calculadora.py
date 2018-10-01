
#-*- coding: utf-8 -*-
ope=""
total = 0.0
while(True):

	num = input("introducir numero: ")
	num = num * 1.0
	if ope == "":
		
		total = num
	else:
		if (ope == "+"):
			total = total + num
		elif(ope == "-"):
			total = total - num
		elif(ope == "*"):
			total = total * num
		elif(ope == "/"):
			total = total / num
		elif(ope == "**"):
			total = total ** num
		elif(ope == "%"):
			total = total % num
		else:
			print("Error. Operación no implementada")

	print(total)
	ope = raw_input("Introduccir operación: ")

	