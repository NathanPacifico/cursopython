terca = False
quinta = False

sorvete = terca or quinta
tv32 = terca != quinta
tv50 = terca and quinta
saude = not terca and not quinta

# print("sorvete: " + sorvete + "tv32: " + tv32 + "tv50: " + tv50 + "saude: " + saude)
# print(sorvete, tv32, tv50, saude)
print("sorvete={} tv32={} tv50={} saude={}"
	.format(sorvete, tv32, tv50, saude))

print("{1} {0} {2}".format(1, 2, 3))
print("{0} {1} {2}".format(1, 2, "string tb pode"))