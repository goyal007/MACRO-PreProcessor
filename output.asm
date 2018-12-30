extern printf
extern atoi
SECTION .data
 integerr:db '%d',20,10 
	
SECTION .bss
		j RESB 64
		n RESB 32
		n RESB 32
		n RESB 32
		n RESB 32
	k RESB 16
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
	mov eax,[Sum]	
	push eax
	push integerr
	call printf	
			mov esp,ebp		
			pop ebp
			ret
				int 80h	
				int 90h	
