#Challenge 1
word = input("Enter a word: ")
letter_indices = {}
index = 0

for letter in word:
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]
    index += 1

print(letter_indices)


#Challenge 2
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
print (items_purchase)

wallet = "$300"

print(wallet)

wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= clean_price 

if not basket:
    print("Nothing")
else:
    print(sorted(basket))

