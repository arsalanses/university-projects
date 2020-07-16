name "Display register in binary & decimal"
include 'emu8086.inc'
ORG 100h

MOV al, 41   ; al = 41
MOV bl, 12 ; bl = 12
ADD al, bl  ; al + bl = 53
     
MOV cx, 8   ; Set loop 8 times
MOV bl, al  ; Take copy of al in bl     
Binary:
MOV dl, bl
SHL bl, 1
AND dl, 10000000b   ; AND value of register dl with 80H
CMP dl, 10000000b   ; Compare value of register dl with 80H
MOV dl, '1'
JE Print         ; If dl equal to 80H program will jump to PrintOne section otherwise PrintZero section
MOV dl, '0'
Print:
MOV ah, 2
INT 21H
DEC cx
JCXZ EndBinary    ; Check if 8 times passed or not
JMP Binary        ; Go back to begging of loop

EndBinary:

GOTOXY 0, 1

MOV al, 41   ; al = 41
MOV bl, 12 ; bl = 12
ADD al, bl  ; al + bl = 53
mov cx, 0

Decimal:
push ax
mov ah, 0
cmp ax, 0
je done
mov dl, 10
div dl
inc cx
jmp Decimal

done:
pop ax
mov al, ah
add al, 30h
mov ah, 0eh
int 10h
loop done

HLT
;RET
;END
