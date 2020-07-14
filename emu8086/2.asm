mov al, 5
mov bl, 0ah
dec bl
add al, bl         
     
mov cx, 8
mov bl, al
     
loop:

mov dl, bl

shl bl, 1

and dl, 10000000b
cmp dl, 10000000b
je one

zero:
mov ah, 2
mov dl, '0'
int 21h

dec cx
jcxz end

jmp    loop

one:
mov ah, 2
mov dl, '1'
int 21h

dec cx
jcxz end

jmp    loop                       

end:
hlt