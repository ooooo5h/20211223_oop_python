# 동작을 어떻게 해야하는지 정리하는 코드

print('책방 관리 프로그램을 시작합니다.')

def add_two_numbers(num1, num2):
    print('두개의 숫자를 더하는 함수가 실행된다')
    result = num1 + num2
    return result
    
a = add_two_numbers(5, 2)  # 함수에 return이 있다면, 그 결과를 변수에 담거나 / print 등으로 일반변수처럼 활용 가능
print(a)

b = add_two_numbers(10, 4)
print(b)

print(f'11과 15의 합은 {add_two_numbers(11, 15)}입니다.')