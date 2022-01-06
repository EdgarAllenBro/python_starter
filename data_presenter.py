cup_cake = open('CupcakeInvoices.csv')

for line in cup_cake:
    print(line)

for line in cup_cake:
   line_list = line.split(',')
   print(line_list[2])


for line in cup_cake:
    line_list = line.split(',')
    invoice = float(line_list[3]) * float(line_list[4])
    print(invoice)


total = []
for line in cup_cake:
    line_list = line.split(',')
    invoice = float(line_list[3]) * float(line_list[4])
    total.append(invoice)
print(sum(total))

     # finding individual totals
# ordersVN = []
# ordersST = []
# ordersCH = []
# for line in cup_cake:
#     line_list = line.split(',')
#     if line_list[2] == 'Vanilla':
#         invoice = float(line_list[3]) * float(line_list[4])
#         ordersVN.append(invoice)
#     elif line_list[2] == 'Chocolate':
#         invoice = float(line_list[3]) * float(line_list[4])
#         ordersCH.append(invoice)
#     elif line_list[2] == 'Strawberry':
#         invoice = float(line_list[3]) * float(line_list[4])
#         ordersST.append(invoice)

# print(f"total spent on chocolate is {sum(ordersCH)}")
# print(f"total spent on Vanilla is {sum(ordersVN)}")
# print(f"total spent on Strawberry is {sum(ordersST)}")

cup_cake.close()
