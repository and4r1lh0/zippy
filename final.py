import logzero
logger = logzero.logger
#packet_size = int(1.5 * 1024**3)   # bytes  ex: 1992294400 = 1900mb
def divide(file,packet_size = 2044723200):
    with open(file, "rb") as output:
        filecount = 0
        while True:
            data = output.read(packet_size)
            #print(len(data))
            logger.info("№ {} | размер файла: {} байт".format(filecount+1, len(data)))
            if not data:
                break   #finish
            with open("{}{:03}".format(file, filecount), "wb") as packet:
                packet.write(data)
            filecount += 1
        print('Всего файлов: ',filecount)
        
def unite(file,numoffiles,desc,packet_size = 2044723200):
    for i in range(numoffiles):
        #with open("{}.rar{:03}".format(file, i), "rb") as packet:
        with open("{}{:03}".format(file+desc, i), "rb") as packet:
            col=packet.read(packet_size)
        with open("{}02{}".format(file,desc), "ab+") as mainpackage:
            mainpackage.write(col)

file = 'H:\WinPE10_8_Sergei_Strelec_x86_x64_2021.10.14_Russian'
desc='.rar'
divide(file+desc) #разделение файла на несколько файлов фиксированного объема
unite(file,3,desc) #слияние нескольких файлов фиксированного объема в один файл