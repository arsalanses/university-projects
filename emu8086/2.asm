name "Display register in binary"
include 'emu8086.inc'
ORG 100h

;CALL SCAN_NUM
;MOV ax, cx
MOV al, 5   ; al = 5
MOV bl, 0Ah ; bl = A
DEC bl      ; bl - 1
ADD al, bl  ; al + bl
     
MOV cx, 8   ; Set loop 8 times
MOV bl, al  ; Take copy of al in bl
     
Loop:
MOV dl, bl
SHL bl, 1
AND dl, 10000000b   ; AND value of register dl with 80H
CMP dl, 10000000b   ; Compare value of register dl with 80H
JE PrintOne         ; If dl equal to 80H program will jump to PrintOne section otherwise PrintZero section

; PrintZero:
;PRINT '0'
MOV ah, 2
MOV dl, '0'
INT 21H

DEC cx
JCXZ EndLoop    ; Check if 8 times passed or not
JMP Loop        ; Go back to begging of loop 

PrintOne:
;PRINT '1'
MOV ah, 2
MOV dl, '1'
INT 21H

DEC cx
JCXZ EndLoop    ; Check if 8 times passed or not
JMP Loop        ; Go back to begging of loop

EndLoop:
;HLT
RET

;Print_Zero   PROC
;PRINT '0'
;MOV ah, 2
;MOV dl, '0'
;INT 21H
;Print_Zero   ENDP

;DEFINE_SCAN_NUM

END
