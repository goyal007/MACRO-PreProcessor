@@BEGINN ...SINGLE... (&d1_=1,&d2_=1,&d3_=1,&d4_=1,&d5_=1,&d6_=1,&d7_=1,&d8_=1,&d8_=1,&d9=1,&d10_=1) integerr:db '%d',&d1_,&d2_ @@ENDD
@@BEGIN ...MULTI... (&d1_=1,&d2_=2,&d3_=1,&d4_=1,&d5_=1,&d6_=1,&d7_=1,&d8_=1,&d8_=1,&d9=1,&d10_=16)
	iff(&d1_ EQUAL &d2_)
		i RESB &d1_
	elsee
		j RESB &d2_
	endif
	WHILEE (&d4_ LESS &d5_)
		INRR &d4_		<#use INRR and DCRR according to the condition in WHILEE such that it will remain valid#>
		n RESB &d3_
	ENDWHIL
	k RESB &d10_
@@END
@@BEGIN ...PRINT... (&d10_=1,&d2_=1,&d3_=1,&d4_=1,&d5_=1,&d6_=1,&d7_=1,&d8_=1,&d8_=1,&d9=1,&d1_=1)
	mov eax,[Sum]	
	push &d10_
	push integerr
	call printf	
		@@BEGIN ...QUIT... (&d1_=1,&d2_=1,&d3_=1,&d4_=1,&d5_=1,&d6_=1,&d7_=1,&d8_=1,&d8_=1,&d9=1,&d10_=1)
			mov esp,ebp		
			pop ebp
			ret
			@@BEGIN ...FINISH... (&d1_=80h,&d2_=1,&d3_=1,&d4_=1,&d5_=1,&d6_=1,&d7_=1,&d8_=1,&d8_=1,&d9=1,&d10_=1)
				<# BYE BYE#>int &d1_	
			@@END
		@@END
@@END

extern printf
extern atoi
SECTION .data
	...SINGLE... (20,10)
	
SECTION .bss
	...MULTI... (62,64,32,1,5)
SECTION .text
	global main
main:
	push ebp
	mov ebp,esp
	mov ebx,dword[esp+12]	
	mov ecx,[ebx+4]			
	push ecx
	call atoi
	mov [i],eax
	mov edx,[ebx+8]			
	push edx
	call atoi
	mov [n],eax
	
	mov eax,1
	mov [Sum],eax			

loop: 
	mov eax,[n]
	inc eax
	cmp eax,[i]
	jz end
	mov eax,[i]
	mov edx,[i]
	mul edx
	mov edx,[Sum]
	mul edx
	mov [Sum],eax
	mov eax,[i]
	inc eax
	mov [i],eax
	jmp loop
end:
	...PRINT... (eax)
	...FINISH... (90h)
