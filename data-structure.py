import random

def selection_sort(A): # 선택정렬
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step", i + 1, "=", A)

    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def main(): # 시작할때마다 이화면 띄우기 
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

        # 사용자에게 정렬 방법을 선택하도록 함
        n = int(input("원하시는 정렬의 번호를 선택해 주세요 (종료하려면 7을 입력하세요): "))

        # 7을 선택하면 프로그램 종료
        if n == 7:
            print("프로그램을 종료합니다.")
            break
        elif n == 1:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("원본 리스트:", random_list)
            
            # 선택 정렬 함수 호출
            selection_sort(random_list)

if __name__ == "__main__":
    main()
