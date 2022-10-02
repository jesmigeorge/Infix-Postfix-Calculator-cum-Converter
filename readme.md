# Expression evaluator and converter

## Infix to Postfix Converter

Allows user to input an infix expression and converts it to a postfix expression by using the stack data structure and its push and pop operations.

Eg:-

- Format 1 : 
    - Input : 2+4/5*(5-3)^5^4
    - Output : 245/53-5^4^*+
- Format 2 :
    - Input : A+B/C*(D-A)^F^H
    - Output : ABC/DA-F^H^*+

---

## Postfix Expression Evaluator

Allows user to input a postfix expression and evaluates it using the stack data structure and its push and pop operations.

Eg:-

- Format 1 :
    
    - Input : 231*+9-
    - Output : -4
  
---

## Algorithm for Infix to Postfix Conversion

- Step 1 : Scan the Infix Expression from left to right.
- Step 2 : If the scanned character is an operand, append it with final Infix to Postfix string.
- Step 3 : Else,
    - Step 3.1 : If the precedence order of the scanned(incoming) operator is greater than the precedence order of the operator in the stack (or the stack is empty or the stack contains a ‘(‘ or ‘[‘ or ‘{‘), push it on stack.
    - Step 3.2 : Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
- Step 4 : If the scanned character is an ‘(‘ or ‘[‘ or ‘{‘, push it to the stack.
- Step 5 : If the scanned character is an ‘)’or ‘]’ or ‘}’, pop the stack and and output it until a ‘(‘ or ‘[‘ or ‘{‘ respectively is encountered, and discard both the parenthesis.
- Step 6 : Repeat steps 2-6 until infix expression is scanned.
- Step 7 : Print the output
- Step 8 : Pop and output from the stack until it is not empty.

---

## Algorithm for Postfix Expression Evaluation

- Step 1 : Create a stack to store operands.
- Step 2 : Scan the given expression from left to right.
- Step 3:
    - Step 3.1 : If the scanned character is an operand, push it into the stack.
    - Step 3.2 : If the scanned character is an operator, POP 2 operands from stack and perform operation and PUSH the result back to the stack.
- Step 4 : Repeat step 3 till all the characters are scanned.
- Step 5 : When the expression is ended, the number in the stack is the final result.