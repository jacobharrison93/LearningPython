try:
    f = open('patrons.csv')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Exception Error')
else:
    while open('patrons.csv','r'):
        for lines[:10] in f:
            print(lines[:10])
finally:
    pass
