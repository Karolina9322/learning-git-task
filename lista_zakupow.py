shopping_list = {

"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]
}
print("Lista zakupionych  produktów")

for keys, products in shopping_list.items():  
      print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(products).title()}")
      products_1= len(shopping_list["piekarnia"])
      products_2 = len(shopping_list["warzywniak"])
print(f"W sumie kupuję: {products_1 + products_2} produktów.")