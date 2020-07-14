mov al, 5
mov bl, 0ah
dec bl ; sub bl, 1
add al, bl         
     
mov cx, 9     
loop:

mov bl, al

shr al, 1

and bl, 00000001b
cmp bl, 1

dec cx
jcxz end

je one

zero:
mov ah, 2
mov dl, '0'
int 21h

jmp    loop

one:
mov ah, 2
mov dl, '1'
int 21h

jmp    loop                       

end:
hlt