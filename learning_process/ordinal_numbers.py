# num = list(range(1,10))
# for nums in num:
#     if nums == 1:
#         print(str(nums)+'st')
#     if nums == 2:
#         print(str(nums) + 'nd')
#     if nums == 3: 
#         print(str(nums) + 'rd')
#     if z
dic = {'points': 4, 'color': 'greeen'}
print(dic)

dic['points'] = 5
print(dic)

dic['name'] = 'JOseph'
dic['passwd'] ='astro'
user = input('Enter username: ')
if dic['name'] == user:
    passwd = input('Enter your passwd: ')
    if dic['passwd'] == passwd:
        print('Welcome ' + dic['name'].upper())
# for key,value in dic.items():
#     if value in dic:
#         print('You have an account with us!')
#     else:
#         dic['newusr'] = input('Sign up with us: ')

print(dic)