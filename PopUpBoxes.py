def solution(n, w, num):
    
    answer = 1
    height = n // w
    floorsLeft = height - ((num + w - 1) // w) #위로 남은 만큼의 층수
    lastFloor = (n + w - 1) // w # 마지막 층수
    
    current = num
    min = num % w
    add = w - min
    sum = w + 1


    current += (floorsLeft // 2) * 2 * w
    answer += (floorsLeft // 2) * 2
    if (current + add*2 + 1) <= n: #짝을 이루지 못한 층의 경우
        answer += 1
        current += add*2 + 1

    if current == n:
        return answer
    
    currentFloor = (current + w - 1) // w # 꺼내야 하는 상자의 층수
    if currentFloor == lastFloor:
        return answer


        
    # #층이 짝수, 홀수인 경우(나머지와 동일)
    # if lastFloor % 2 == 1:
    #     if current % w <= n % w:
    #         answer += 1

    # #층이 홀수, 짝수인 경우
    # elif lastFloor % 2 == 0:
    cmod = current % w #current mod,
    if cmod == 0:
        cmod = w
    lmod = n % w
    if lmod == 0:
        lmod = w
    
    if cmod + lmod >= w + 1:
        answer += 1
     
    
    return answer
