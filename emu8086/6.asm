mov dx, offset msg
mov ah, 9h
int 21h
hlt
;msg db 'salam arsalan', '$'
msg db 'salam arsalan', 0dh, 0ah, '$'