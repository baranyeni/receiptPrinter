from whatstk import WhatsAppChat
from escpos.printer import Usb
from unidecode import unidecode

printer = Usb(0x0fe6, 0x811e, 0)
printer.set(bold=True, double_height=2, double_width=2)

chat    = WhatsAppChat.from_source(filepath="chat.txt", hformat='[%H:%M, %d/%m/%y] %name:')
columns = set(chat.df.columns.tolist()) - set(['Id'])
chat_grouped = chat.df.groupby('username')
DELIVERY_ADDRESS = "  MIGROS\n\n"

output = {}
for key, grouped in chat_grouped:
    output[key] = grouped["message"].tolist()


for username in output:
    printer.textln(DELIVERY_ADDRESS)
    for index, message in enumerate(output[username], 1):
        # print(index, "-", unidecode(message.upper()))
        printer.textln("%s-%s" %(index, unidecode(message.upper())))
    
    printer.cut()