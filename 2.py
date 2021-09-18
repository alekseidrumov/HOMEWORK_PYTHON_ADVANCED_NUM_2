thisdict =	{
  1 : 3,
  3 : 5,
  5 : 7
}
name_of_count_el = 5
spisok = []
for x, y in thisdict.items():
    spisok.append(x)
    spisok.append(y)
print(spisok.count(name_of_count_el))