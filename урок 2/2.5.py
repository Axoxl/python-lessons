rating = [9, 5, 1, 2]
new_element = int(input('Пожалуйста введите новый элемент рейтинга: '))
counter = rating.count(new_element)
if counter:
    index = rating.index(new_element)
    rating.insert(index + counter, new_element)
else:
    rating.append(new_element)
    rating.sort(reverse=True)
print(rating)
