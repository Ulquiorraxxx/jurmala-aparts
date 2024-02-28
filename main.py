
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)
def sorting_kv(apartment):
    return int(apartment[-4])
def sorting(apartment):
    return int(apartment[-1])

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. 20 tems more than m2")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        for x in apartments:
            print(apartments.index(x) , ": " , x)
    elif choice == '2':
        apartments.sort(key=sorting , reverse=True)
        print(apartments[0:10])
        
        
    elif choice == '3':
        apartments.sort(key=sorting )
        print(apartments[0:10])
    elif choice == '4':
        super_mega_number=0
        summa=int(input("summa: "))
        apartments.sort(key=sorting , reverse=True)
        for element in apartments:
            if int(element[-1]) <= summa:
                if super_mega_number<20:
                    print(element)
                    super_mega_number=super_mega_number+1
        
    elif choice == '5':
       super_mega_number=0
       summa=int(input("Summa: "))
       apartments.sort(key=sorting)
       for element in apartments:
           if int(element[-1]) >= summa:
               if super_mega_number<20:
                   print(element)
                   super_mega_number=super_mega_number+1
        

    elif choice == '6':
        super_mega_number=0
        m_kv=int(input("Platība: "))
        apartments.sort(key=sorting_kv)
        for element in apartments:
            if int(element[-4]) >= m_kv:
                if super_mega_number<20:
                    print(element)
                    super_mega_number=super_mega_number+1
        
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")


    print("==========================")


