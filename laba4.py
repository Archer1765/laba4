import numpy as np

colors = ["Белый", "Черный", "Фиолетовый", "Оранжевый", "Зеленый"]
abc = ["Алена", "Аня", "Настя", "Арина", "Ирина"]
#print(colors)
#print(abc,"\n")

n = int(input("Введите количество кандидатов голосования: "))
m = int(input("Введите количество голосующих: "))
print()
a = [[0] * n for i in range(m)]

new_colors = colors[0:n]
print("Кандидаты голосования")
print(new_colors)
new_abc = abc[0:m]
print("Голосующие")
print(new_abc,"\n")

#num = [[int(input()) for i in range(n)] for j in range(m)]
#print(np.matrix(num))

for i in range(m):
    print(f"{new_abc[i]} голосует так: ")
    for j in range(n):
        a[i][j] = int(input(f"приоритет для '{new_colors[j]}': "))
        #print('\n',np.matrix(a),'\n')
    print()

print("Полученная матрица:")
#a2 = np.matrix(a)
print(np.matrix(a),"\n")

print("МЕТОД БОРДА")
bord = [0] * n
for k in range(n):
    for i in range(m):
        for j in range(n):
            if a[i][j] == k + 1:
                bord[k] += n - 1 - j
                #print(f"{k} =",bord[k])

print("Результаты:")
for i in range(n):
    print(f"'{new_colors[i]}' набрал {bord[i]} баллов")

#bord2 = np.matrix(bord)
print(bord)
#print(bord2)
max_bord = np.matrix(bord).max()
#print(max_bord)
ind_bord = 0
c_bord = 0
for i in range(n):
    if bord[i] == max_bord:
        ind_bord = i
        c_bord +=1
    if c_bord > 1:
        print(f"несколько кандидатов набрали {max_bord} баллов")
        print("с помощью метода Борда голосование не проведено\n")
        break
    if i == n - 1:
        print(f"победил '{new_colors[ind_bord + 1]}', его балл - {max_bord}\n")
    
print("МЕТОД ОТНОСИТЕЛЬНОГО БОЛЬШИНСТВА")
rel_maj = [0] * n
for k in range(n):
    for i in range(m):
        w = a[i][0]
        #print(w)
        if w == k + 1:
            rel_maj[k] += 1

print("Результаты:")
for i in range(n):
    print(f"'{new_colors[i]}' набрал {rel_maj[i]} баллов")

#rel_maj2 = np.matrix(rel_maj)
print(rel_maj)
#print(rel_maj2)
max_rel_maj = np.matrix(rel_maj).max()
#print(max_rel_maj)
ind_rel_maj = 0
c_rel_maj = 0
for i in range(n):
    if rel_maj[i] == max_rel_maj:
        ind_rel_maj = i
        c_rel_maj +=1
    if c_rel_maj > 1:
        print(f"несколько кандидатов набрали {max_rel_maj} баллов")
        print("с помощью метода относительного большинства голосование не проведено\n")
        break
    if i == n - 1:
        print(f"победил '{new_colors[ind_rel_maj + 1]}', его балл - {max_rel_maj}\n")
        
