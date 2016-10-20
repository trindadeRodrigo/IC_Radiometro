import matplotlib.pyplot as plt
import serial
import xlwt


#Th = 35.185

ser = 0
count = 0
i = 0
x = []
y = []
z = []
k = []

#Criando planilha
wb = xlwt.Workbook()
ws = wb.add_sheet('Sec_Temp')

#Título das colunas
titles = ['7815', 'Rc', 'Heater', 'Volts Base']

#Escreve títulos na primeira linha do arquivo
for i in range(len(titles)):
    ws.col(i).width = 3500
    ws.write(0, i, titles[i])


#Function to Initialize the Serial Port
def init_serial():
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = "/dev/ttyUSB0"   #COM Port Name Start from 0
    

    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.timeout = None
    ser.open()          #Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print ('Open: ' + ser.portstr)
#Function Ends Here
        

#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

try:
    valor = ser.readline()  #Read from Serial Port

    sep = valor.split() #Separa a string
    x.insert(count, float(sep[3]))
    y.insert(count, float(sep[0]))
    z.insert(count, float(sep[1]))
    k.insert(count, float(sep[2]))
    count += 1

    #Escreve os dados na planilha
    for i in range(len(titles)):
        ws.write(count, i, float(sep[i]))
    
    while 1:
        
        valor = ser.readline()  #Read from Serial Port
        sep = valor.split()
            
        x.insert(count, float(sep[3]))
        y.insert(count, float(sep[0]))
        z.insert(count, float(sep[1]))
        k.insert(count, float(sep[2]))
        count += 1
        for i in range(len(titles)):
            ws.write(count, i, float(sep[i]))
            
        print (sep)
        
        if float(sep[3])>=4095:
            break

    wb.save('Sec_Temp.xls') #Salva planilha
    
    plt.plot(x, y, 'r', label = "7815")
    plt.plot(x,z, 'g', label = "Rc")
    plt.plot(x,k, 'b', label = "Heater")
    plt.ylabel("Temperatura (ºC)")
    plt.xlabel("Volts (v)")
    plt.title("TEMPERATURA PELO ACRESCIMO DE TENSÃO")
    plt.legend(loc=4, borderaxespad=0.8)

    plt.ylim([0, 90])

    plt.show()
    print ("Programa encerrado!")

except KeyboardInterrupt:
    wb.save('Sec_Temp.xls') #Salva planilha
    
    plt.plot(x, y, 'r', label = "7815")
    plt.plot(x,z, 'g', label = "Rc")
    plt.plot(x,k, 'b', label = "Heater")
    plt.ylabel("Temperatura (ºC)")
    plt.xlabel("Volts (v)")
    plt.title("TEMPERATURA PELO ACRESCIMO DE TENSÃO")
    plt.legend(loc=4, borderaxespad=0.8)

    plt.ylim([0, 90])

    plt.show()
    print ("Programa encerrado!")



    
    
    

