mov al, 24
mov cx, 0

cmp al, 0
jne print

mov al, '0'
mov ah, 0eh
int 10h

jmp lbl

print:
push ax
mov ah, 0
cmp ax, 0
je done
mov dl, 10
div dl
inc cx
jmp print

done:
pop ax
mov al, ah
add al, 30h
mov ah, 0eh
int 10h
loop done

lbl:
hlt