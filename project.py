# Program koji pretvara valute

a = input('Enter a currency: ')
b = input('Enter a currency to convert to: ')
c = int(input('Enter the amount: '))
if a == 'BAM' and b == 'EUR':
    print(c, a, 'is equal to', c * 0.51, b)
elif a == 'EUR' and b == 'BAM':
    print(c, a, 'is equal to', c * 1.96, b)
elif a == 'EUR' and b == 'USD':
    print(c, a, 'is equal to', c * 1.17, b)
elif a ==  'USD' and b == 'EUR':
    print(c, a, 'is equal to', c * 0.86, b)
elif a == 'GBP' and b == 'USD':
    print(c, a, 'is equal to', c * 1.32, b)
elif a == 'USD' and b == 'GBP':
    print(c, a, 'is equal to', c * 0.76, b)
elif a == 'EUR' and b == 'GBP':
    print(c, a, 'is equal to', c * 0.89, b)
elif a == 'GBP' and b == 'EUR':
    print(c, a, 'is equal to', c * 1.13, b)
elif a == 'CHF' and b == 'USD':
    print(c, a, 'is equal to', c, b)
elif a == 'USD' and b == 'CHF':
	print(c, a, 'is equal to', c, b)
elif a == 'CHF' and b == 'EUR':
	print(c, a 'is equal to', c * 0.85)
else:
    print('You did not enter the appropriate currency and/or amount')
