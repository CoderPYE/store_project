# 함수를 사용한 프로그램 설계
# 1. 요구사항이 들어오면 철저하게 분석을 해야된다. (요구사항 명세서, 사규, 데이터 등)
# 2. 문제를 한 번에 해결하려고 하지말고 더 작은 크기의 문제들로 분해한다. 문제가 충분히 작아질 때까지 지속적으로 분해를 하도록 해야한다.
# 3. 더 이상 분해가 되지 않는 그러한 부분에 도달을 했을 때, 비로소 해당하는 기능을 함수로 만들어서 조립해서 최종적인 프로그램을 완성을 한다.
# 4. 솔루션(solution)을 단위테스트 및 통합테스트까지 완료하고, 비로소 회사에 배포를 하고 안정화를 시켜줘야 한다.

# grade.py 모듈을 ex14.py 파일에서 사용하겠다라고 인터프리터에게 알리고 있다.
import grade
def main():
    score_list = grade.readList()
    score_list = grade.sortingList(score_list)
    grade.show_score(score_list)

if __name__ == "__main__":      # 프로그램의 시작점
    main()
