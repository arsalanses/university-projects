MOV al, 5   ; al = 5
MOV bl, 0Ah ; bl = A
DEC bl      ; bl - 1
ADD al, bl  ; al + bl
     
MOV cx, 8   ; Loop 8 times
MOV bl, al  ; Take copy of al in bl
     
Loop:
MOV dl, bl
SHL bl, 1
AND dl, 10000000b   ; AND value of register dl with 10H
CMP dl, 10000000b   ; Compare value of register dl with 10H
JE PrintOne         ; If dl equal to 10H program will jump to PrintOne section otherwise PrintZero section

; PrintZero:
MOV ah, 2
MOV dl, '0'
INT 21H

DEC cx
JCXZ EndLoop    ; Check if 8 times passed or not
JMP Loop        ; Go back to begging of loop 

PrintOne:
MOV ah, 2
MOV dl, '1'
INT 21H

DEC cx
JCXZ EndLoop    ; Check if 8 times passed or not
JMP Loop        ; Go back to begging of loop

EndLoop:
HLT
