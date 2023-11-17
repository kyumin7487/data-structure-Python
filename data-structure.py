import random

S = 1 # 퀵정열 하는데 문제가 자꾸 생겨서 여기에다가 S 잡았어요

def selection_sort(A): 
    # 선택 정렬 알고리즘 구현
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("단계", i + 1, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def insertion_sort(A): 
    # 삽입 정렬 알고리즘 구현
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print("단계", i + 1, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def bubble_sort(A): 
    # 버블 정렬 알고리즘 구현
    n = len(A)
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True
        if not bChanged:
            break
        print("단계", n - i, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def quick_sort(A, left, right):
    # 퀵 정렬 알고리즘 구현
    global S
    print("quick_sort(A,", left, right, ")")
    if left < right:  
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                print_qs(A)
        A[left], A[j] = A[j], A[left]
        print_qs(A)
        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)

def print_qs(A):
    global S
    print("단계", S, "=", A)
    S += 1
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def main():
    while True:
        print("""
        ***********************************
        *** 여러가지 정렬 프로그램 구현 ***
        ***                             ***
        *** 1. 선택(selection)정렬      ***
        *** 2. 삽입(insertion) 정렬     ***
        *** 3. 버블(bubble) 정렬        ***
        *** 4. 퀵(quick) 정렬           ***
        *** 5. 합병(merge) 정렬         ***
        *** 6. 힙(heap) 정렬            ***
        *** 7. 종료(quit)               ***
        ***********************************
        """)

        n = int(input("원하시는 정렬의 번호를 선택해 주세요 (종료하려면 7을 입력하세요): "))

        if n == 7:
            print("프로그램을 종료합니다.")
            break

        elif n == 1:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("선택정렬을 실행합니다")
            print("원본 리스트:", random_list) # 원본 리스트 출력
            selection_sort(random_list) # 선택정렬 함수 호출

        elif n == 2:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("삽입정렬을 실행합니다")
            print("원본 리스트:", random_list) # 원본 리스트 출력
            insertion_sort(random_list) # 삽입정렬 함수 호출

        elif n == 3:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("버블정렬을 실행합니다")
            print("원본 리스트:", random_list)# 원본 리스트 출력
            bubble_sort(random_list) # 버블정렬 함수 호출

        elif n == 4:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("퀵정렬을 실행합니다")
            print("원본 리스트:", random_list)# 원본 리스트 출력
            quick_sort(random_list, 0, len(random_list) - 1) # 퀵정렬 함수 호출

if __name__ == "__main__":
    main()
