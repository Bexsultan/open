# #1

# with open('/home/beksultan/Desktop/directories.txt','r') as d:
#     print(d.read())

# #2
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# with open('users.txt', 'w') as v:
#     v.write('login: '+login+'\n')
#     v.write('password: '+password+'\n')

# print()
# print()

# #3
# with open('text.txt','r') as f:
#     if 'w' in f.read():
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')
# print()
# print()

# #4
# t_words = []
# with open('python.txt','r') as p:
#     for word in p.read().split():
#         if 't' in word or 'T' in word:
#             t_words.append(word)
# print(t_words)
# print()
# print()

# #5
# while True:
#     akkaunt = input('Введите логин: ')
#     with open('database.txt','r') as db:
#         login = "Логин:"+akkaunt
#         l = ''.join(db.readlines()).split()
#         if login in l:
#             print('Данный аккаунт уже зарегестрирован')
#         else:
#             password = input('Создайте пароль: ')
#             check_ps = input('Введите пароль ещё раз: ')
#             if password != check_ps:
#                 print('Пароль неверный')
#             else:
#                 break
# with open('database.txt','a') as db:
#     db.write('\n')
#     db.write(login+'\n')
#     db.write('Пароль:'+password+'\n')
#     print('Аккаунт успешно зарегестрирован')
# #6
# def check_rashirenie(p):
#     rashirenie = ['jpeg','jpg','png']
#     if "."not in p:
#         return False
#     i = p.index('.')
#     if p[i+1:] in rashirenie:
#         return True
#     return False

# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# picture = input("Путь к изображению: ")
# try:
#     with open(picture,'r') as p:
#         with open('registration.txt','w') as file:
#             if check_rashirenie(picture) == True:
#                 file.write('Логин: '+login+'\n')
#                 file.write('Пароль: '+password+'\n')
#                 file.write('Фото: '+picture)
#                 print('Аккаунт успешно сделан')
# except Exception:
#     print('Путь не найден')

# #7
# a = input('Путь до картинки которую нужно изменить: ')
# b = input('Путь до картинки НА которую нужно изменить: ')
# try:
#     with open(a,'rb') as p:
#         p.read()
#         with open(a,'w') as w:
#             w.write(b)
# except Exception as e:
#     print("Фото или путь не найден",e)


# #8
# month = ['May', 'July', 'September', 'November']
# moneys = []
# with open('text2.txt','r') as text:
#     for line in text.readlines():
#         l = line.split()
#         if len(l)>1:
#             if l[0] in month:
#                 moneys.append(int(l[1]))
# srednee = sum(moneys)//len(moneys)
# print(srednee)

# #9
# lst = []
# with open('chisla.txt', 'r') as ch:
#     for i in ch.read().split():
#         lst.append(int(i))
# with open('vyvod.txt','w') as vy:
#     vy.write(str(min(lst))+'\n')
#     vy.write(str(max(lst)))

# #10
# t = input('Введите текст: ')
# t = t.split()
# with open('txt_file.txt','w') as f:
#     for i in t:
#         f.write(i)
#         f.write('\n')