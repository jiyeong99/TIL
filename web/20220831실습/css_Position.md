# CSS Position
- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    1. relative : 상대 위치
        - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
        - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 ooffset)
    2. absolute : 절대 위치
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
        - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
    3. fixed : 고정 위치
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 ㅇ낳음 (normal flow에서 벗어남)
        - 부모 요소와 관계없이 viewport를 기준으로 이동
            - 스크롤 시에도 항상 같은 곳에 위치함
    4. sticky : 스크롤에 따라 static -> fixed로 변경
        - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만, 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성
        - 일반적으로 Navigation Bar에서 사용.
## CSS 원칙
- css 원칙 I,II : Normal flow
    - 모든 요소는 네모(박스모델), 좌측상단에 배치
    - display에 따라 크기와 배치가 달라짐
- CSS 원칙 III
    - position으로 위치의 기준을 변경
        - relative : 본인의 원래 위치
        - absolute : 특정 부모의 위치
        - fixed : 화면의 위치
        - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경
# CSS Layout
- 개발자도구...로 볼때?보이는거?
- Display
- Position
- Float (CSS1, 1996)
- Flexbox (2012)
- 기타
    - responsive Web Design(2010), Media Queries (2012)
## Float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrpping 하도록 함
- 요소가 Normal flow를 벗어나도록 함

