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

# 결과가 없는 함수 예시
def print_my_name(my_name):
    print(f'제 이름은 {my_name}입니다.')
    
print_my_name('전은형')


# 파라미터가 없는 함수 예시
def get_my_age():
    return 31

age = get_my_age()
print(age)

# 뺄셈 수행하는 함수 => 파라미터의 대입 순서가 중요한 함수
def minus_two_numbers(num1, num2):
    return num1 - num2

# 어느 파라미터에 어떤 값 대입할 지 직접 지정
# 파라미터의 순서와 관계 없음!!
result01 = minus_two_numbers(num2=7, num1=10)
print(f'뺄셈 함수 사용 결과 : {result01}')

# bool값에 따라 다른 문구를 출력하는 함수
def print_test(my_bool=True):
    if my_bool:
        print('True가 들어왔습니다.')
    else:
        print('False가 들어왔습니다.')
        
print_test()

# 필요한 만큼 전달인자 (arguments)를 넣으면, 모든 수의 합을 계산
def sum_many_numbers( *args ):
    # args는 목록으로 들어옴( 여러개 담고 있다)
    
    result = 0
    for num in args:
        result += num
        
    return result
    
sum_result1 = sum_many_numbers(1,2,3)
sum_result2 = sum_many_numbers(4,5,6,7,8,9)    

print(sum_result1)
print(sum_result2)