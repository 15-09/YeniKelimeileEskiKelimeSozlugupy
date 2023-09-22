meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word], "kelimenin anlamıdır")
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Bu kelimenin karşılığı sözlüğümüzde yoktur")
