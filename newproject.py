from rapidfuzz import fuzz
import json
dic={}
dic_2={}
dic1={}
ans={}
with open('dialog.json','r', encoding='utf-8') as f: 
    dialog = json.load(f)
    
    for x in range(len(dialog)):
        message = dialog[x]['dialogue'] #все сообщения в этом списке
        pic = dialog[x]['photo_url'] #ссылка на фото
        
    
        for i in range(len(message)):
         for j in message[i]:
                if  message[i][j] is True: #находим сообщение с картинкой
                    replika = message[i-3]['message']+ ' ' +(message[i-2]['message'])+ ' ' +(message[i-1]['message']) # 3 реплики перед картинкой
                    replika = str(replika.split())
                    dic[replika] = pic #словарь с репликами и ссылками на картинки
 
        
        
 #для входных данных в виде такого же файла с большим кол-вом диалогов  
 #                                         |
 #                                         V
file = input('введите название файла: ' )       
with open(file,'r', encoding='utf-8') as g: 
        dialog_2 = json.load(g)
        
        message_2 = dialog_2[0]['dialogue'] #вместо нуля можно поставить порядковый номер диалога из файла (начиная с 0)
        
        for q in range(len(message_2)):
         for w in message_2[q]:
                if  message_2[q][w] is True: #находим сообщение с картинкой
                    replika_2 = message_2[q-3]['message']+ ' ' +(message_2[q-2]['message'])+ ' ' +(message_2[q-1]['message']) # 3 предыдущих предложения 
                    replika_2 = str(replika_2.split())


#для входных данных, где диалог (записанный так же, как в тестовых файлах) заканчивается на [Share the photo]
 #                                         |
 #                                         V
#file = input('введите название файла: ' )   
#with open(file,'r', encoding='utf-8') as k:
    #message_2 = dialog_2[0]['dialogue']
    #print(message_2)
    #replika_2 = message_2[len(message_2)-3]['message']+ ' ' + message_2[len(message_2)-2]['message']+ ' ' + message_2[len(message_2)-1]['message'] # 3 реплики перед [Share the photo] 
    #replika_2 = str(replika_2.split())
    
    
                   
for c in dic:
    ans[dic[c]] = fuzz.ratio(c, replika_2) #сравнение
    
ans= dict(sorted(ans.items(), key=lambda x: x[1])) #сортируем по возрастанию

ans =  list(ans.keys())[-10:]
count=1
for p in ans[::-1]:
    print(count, p, sep='. ') 
    count+=1  
