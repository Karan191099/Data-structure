# ****************QUEUE AND STACK*************************
# q - queue
#s - stack
#e - elements
#n - length
#p - pop

q = list()
s = list()

n = int(input('Enter number of elements list should contain: '))

print('Enter elemtents: ')

for i in range(n):
    e = int(input())
    q.append(e)
    s.append(e)

print('Queue: ', q)
print('Stack: ', s)

while True:
    choice = int(input('1. Queue operation\n2. Stack operation '))

    # QUEUE OPERATION
    if choice == 1:
        head = q[0]
        tail = q[n-1]
        print('Head of Queue before pop: ', head)
        #DEQUEUE OPERATION - FIRST IN FIRST OUT
        while True:
            i = 0
            ch = input('Pop element? y/n: ')
            if ch == 'y':
                q.pop(i)
                True
            else:
                break

        head = q[0]
        print('*******************************************************')
        print('New Queue after pop: ', q)
        print('New Head of Queue: ', head)
        print('Tail of Queue: ', tail)
        print('*******************************************************')
        
        ch = int(input('1. Linear queue enqueue\n2. Circular queue enqueue '))
        #ENQUEUE OPERATION - LINEAR QUEUE
        if ch == 1:
            num = int(input('Enter number of elements to append: '))
            for i in range(num):
                e = int(input())
                q.append(e)
            print('Queue after Enqueue: ', q)
        #ENQUEUEU OPERATION - CIRCULAR QUEUE
        if ch == 2:
            num = int(input('Enter number of elements to append: '))
            for i in range(num):
                e = int(input())
                q.insert(i,e)
                i += 1
            
            i=0
            head = q[i+num]
            print('*******************************************************')
            print('New Circular Queue after enqueue: ', q)
            print('New Head of Queue: ', head)
            print('Tail of Queue: ', tail)
            print('*******************************************************')
            

    #STACK OPERATION
    if choice == 2:
        start = s[0]
        end = s[n-1]
        print('End before popping element: ', end)
        #POP OPERATION - LAST IN FIRST OUT
        i = n-1
        while True:
            ch = input('Pop element? y/n: ')
            if ch == 'y':
                s.pop(i)
                i -= 1
                True
            else:
                break
        
        l = len(s)
        end = s[l-1]
        print('*******************************************************')
        print('New Stack after pop: ', s)
        print('New End of Stack: ', end)
        print('Start of Stack: ', start)
        print('*******************************************************')
        #PUSH OPERATION
        num = int(input('Enter number of elements to append: '))
        for i in range(num):
            e = int(input())
            s.append(e)
        print('New Stack after push: ', s)


    c = input('Continue? y/n ')
    if c == 'y':
        True
    else:
        break
