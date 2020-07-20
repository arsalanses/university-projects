org 100h

mov ax, 3
int 10h

mov ax, 0b800h
mov ds, ax

mov [00h], 'H'
mov [02h], 'e'
mov [04h], 'y'
mov [06h], 'F'
mov [08h], 'r'
mov [0ah], 'i'
mov [0ch], 'e'
mov [0eh], 'n'
mov [10h], 'd'

mov cx, 9
mov di, 01h

c:
mov [di], 11110001b ; color
add di, 2
loop c

mov ah, 0
int 16h

ret
end

; hex    bin        color
; 
; 0      0000      black
; 1      0001      blue
; 2      0010      green
; 3      0011      cyan
; 4      0100      red
; 5      0101      magenta
; 6      0110      brown
; 7      0111      light gray
; 8      1000      dark gray
; 9      1001      light blue
; a      1010      light green
; b      1011      light cyan
; c      1100      light red
; d      1101      light magenta
; e      1110      yellow
; f      1111      white

