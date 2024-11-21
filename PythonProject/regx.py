import re



txt = "Hello, Welcome to Your New World"
# x = re.search("^Hello.*World$",txt)
# x = re.sub("\s","\t",txt)
x = re.findall("\w",txt)
# if x : print("Match found")
# else: print("No")


print(x)


# def validate_reg_no(reg_no):
#     pattern = r"^FUT\d{5}$"
#
#     if re.match(pattern,reg_no):
#         return True
#     else:
#         return False
#
#
# reg_no = input("Enter a Register No")
# # validate_reg_no()
# if validate_reg_no(reg_no):
#     print("Valida Register Number")
# else: print("Invalid register number")


