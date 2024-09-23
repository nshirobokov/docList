import codecs
import datetime
import sys
import turtle

# Ввод первого номера документа и количества документов
turtle.setup(0, 0)
first_num = int(turtle.numinput('Требуются данные', 'Введите начальный номер документа: '))
doc_quantity = int(turtle.numinput('Требуются данные', 'Сколько документов сгенерировать? '))

# Получаем системную дату
current_date = datetime.datetime.now().strftime('%d.%m.%Y')

# Создаем переменную с указанием где и какой файл создать, по умолчанию создаем там, где лежит файл скрипта
myfile = codecs.open(sys.path[0] + '/ufebs.xml', "w+", encoding='cp1251')

# Инициируем цикл записи документов в файл. Первый док с номером, введенным с клавиатуры и количество доков тоже вводим с клавы

# Записываем xml version и тег packetEPD в файл
xml_header = f'''<?xml version="1.0" encoding="WINDOWS-1251"?>\n'''
packetEPD = f'''<PacketEPD xmlns="urn:cbr-ru:ed:v2.0"
EDNo="200" EDDate="2003-04-14" EDAuthor="4525545000"
EDQuantity="2" Sum="2006" SystemCode="01">\n'''

myfile.write(xml_header)
myfile.write(packetEPD)

#Тег ED101
ed101 = f"""<ED101 xmlns="urn:cbr-ru:ed:v2.0" EDNo="1" EDDate="{current_date}" EDAuthor="4525545000" TransKind="01" 
Priority="5" Sum="1003" PaymentPrecedence="60" SystemCode="05" PaymentID="12345123451234512345" PaytKind="4" 
ReceiptDate="{current_date}" ChargeOffDate="{current_date}">\n"""

# Теги от Payer до DepartamentalInfo
paymentInfo = f"""
<Payer PersonalAcc="40701810000000000000" INN="1111111111" KPP="1111111111">
    <Name>ООО "Организация"</Name>
    <Bank BIC="043600000" CorrespAcc="30101810000000000000"/>
</Payer>
<Payee PersonalAcc="40702810000000000000" INN="1111111111" KPP="1111111111">
    <Name>ООО Контрагент</Name>
    <Bank BIC="044000000" CorrespAcc="30101810000000000000"/>
</Payee>
<Purpose>ОПЛАТА ПО ДОГОВОРУ 95456 ОТ 15.01.2018 В ТОМ ЧИСЛЕ НДС 4000 РУБ</Purpose>
<DepartmentalInfo DrawerStatus="01" CBC="18210606032123000110" OKATO="12344321" PaytReason="0" TaxPeriod="МС.03.2024" DocNo="44928" DocDate="06.08.2024" TaxPaytKind="">
</DepartmentalInfo>\n"""

for i in range(first_num, first_num + doc_quantity):
    docnum = str(i)
    accDoc = (f"""    <AccDoc AccDocNo="{docnum}" AccDocDate="{current_date}"/>""")
    myfile.write(ed101)
    myfile.write(accDoc)
    myfile.write(paymentInfo)
    myfile.write(f"</ED101>\n")

myfile.write("</PacketEPD>")  # Записываем финальную строку в файл
myfile.close()  # Останавливаем запись и сохраняем итоговый файл