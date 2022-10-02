def precedence(ch):
    if ch=='^':
        return 4;
    elif ch=='*' or ch=='/':
        return 3;
    elif ch=='+' or ch=='-':
        return 2;
    else:
        return 0;

exp=input("Enter : ")
exp+=")"
n=len(exp)
stack=[0 for i in range(n)]
postfix=[0 for i in range(n)]
top,index=0,0
stack[top]="("
for i in range(0,n):
    ch=exp[i]
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9'):
        postfix[index]=ch
        index+=1
    elif ch==")":
        while stack[top]!="(" and index<n:
            postfix[index]=stack[top]
            index+=1
            top-=1
        if ((top-1)>=0):
            top-=1
    elif ch=="(":
        top+=1
        stack[top]=ch
    elif ch in '*+-/^':
        if precedence(stack[top])<precedence(ch):
            top+=1
            stack[top]=ch
        else:
            while precedence(stack[top])>=precedence(ch):
                postfix[index]=stack[top]
                index+=1
                top-=1
            top+=1
            stack[top]=ch
            
print("POSTFIX EXPRESSION : ")
for ele in postfix:
    if ele!=0:
        print(ele,end='')
