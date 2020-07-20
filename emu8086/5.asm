mov si, 0

next:
mov al, msg[si]
cmp al, 0
je stop

mov ah, 0eh
int 10h

inc si

jmp next

stop:
hlt

msg db 'hello arsalan', 0

end
