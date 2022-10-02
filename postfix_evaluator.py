
exp=input("Enter the expression : ")
n=len(exp)
stack=[0 for i in range(n)]
top=-1
for i in range(n):
    ch=exp[i]
    if '0'<=ch<='9':
        top+=1
        stack[top]=int(ch)
    elif ch in '+-*/^':
        b=stack[top]
        top-=1
        a=stack[top]
        if ch=='+':
            stack[top]=a+b
        elif ch=='-':
            stack[top]=a-b
        elif ch=='*':
            stack[top]=a*b
        elif ch=='/':
            stack[top]=a/b
        elif ch=='^':
            stack[top]=a^b
print(stack[0])
            
            
        