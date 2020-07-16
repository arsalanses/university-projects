mov al, 5
mov bl, 0ah
add bl, al
sub bl, 1

mov cx, 8
print:
mov ah, 2
mov dl, '0'
test bl, 10000000b
jz zero
mov dl, '1'

zero:
int 21h
shl bl, 1

loop print

mov dl, 'b'
int 21h

mov ah, 0
int 16h

ret