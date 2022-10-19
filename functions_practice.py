
def hello():
    print('greetings')
hello()

item1 = 'apple'
item2 = 'banana' 
item3 = 'cherry' 
def pack():
    return [item1, item2, item3]

print(pack())
print(item1, item2)

def eat_lunch(list):
    if len(list) == 0:
        print('lunchbox is empty today')
    else:
        for index in range(len(list)):
            if index == 0:
                print(f'first i eat {list[0]}')
            else:
                print(f'next i eat {list[index]}')

eat_lunch([])
eat_lunch(pack())
