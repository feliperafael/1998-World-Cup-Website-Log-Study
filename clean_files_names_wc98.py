#esse arquivo le o nome dos arquivos de log
#removendo somente a parte de interesse
file_names = []

with open('ita_public_tools/input/all_98WC_files.txt') as f:
	for line in f.readlines():
		file_names.append(line[:13])

print file_names
