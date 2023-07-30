# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#
#     #Check input
#     try:
#         value = int(num)
#     except:
#         print('Invalid input')
#         continue
#     #print(num)
#
#     # Find largest
#     if largest is None:
#         largest = value
#     elif value > largest:
#         largest = value
#
#     #Find smallest
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#
# print("Maximum", largest)
# print("Minimum", smallest)

# text = "X-DSPAM-Confidence:    0.8475"
# post = text.find(':')
# newText = text[post+1:]
# numText = newText.strip()
# num = float(numText)
# print(num)