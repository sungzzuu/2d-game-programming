# 기말 프로젝트 기획

## 1. 게임의 소개

* **게임 제목**

  플랜츠 vs. 좀비          
<br>  
  
* **플랜츠 vs. 좀비 게임은 어떤 게임인가?**  

  식물을 설치하여 좀비를 무찌르는 게임이다.  
  식물은 태양을 얻어야 심을 수 있으며  
  좀비가 기지로 넘어오기 전에 좀비를 무찔러야 한다.  

<br>

* **이 게임의 목적**  

  태양(마나)를 사용하여 기지로 들어오는 좀비를 무찌른다.  
  좀비의 공격으로 부터 식물을 설치하여  
  기지를 보호해야 한다.  


  <br>

* **게임 플레이 방법**  

  1. 태양을 일정시간 제공해주는 식물인 해바라기를 일정 개수 설치하여 태양을 얻는다.
  2. 식물마다 주어진 태양의 개수를 달성하면 식물을 설치할 수 있다.
  3. 좀비가 습격하기전에 공격 식물을 설치해두어야 한다.
  4. 태양을 제공하는 식물과 공격하는 식물을 합리적으로 배치하여 좀비를 공격한다.
  5. 좀비는 식물을 먹는 행동을 하는데, 감자같은 섭취가 오래걸리는 식물을 앞쪽에 배치하여  
     좀비가 기지에 들어오지 못하게 한다.
  6. 좀비를 모두 무찌르면 다음 스테이지로 넘어간다.

<br>

## 2. GameState(Scene)의 수 및 각각의 이름

  ### 총 Scene의 수 : 5 씬

  1. 로고 : 로고를 띄운다.  
  2. 메인 화면 : 게임시작, 도움말 등 메뉴 선택  
  3. 스테이지 : 게임 플레이  
  4. 클리어 : 스테이지 클리어 시 나오는 씬  
  5. 게임 오버 : 게임 오버 시 나오는 씬  
  
  <br>
  
## 3. 각 GameState 별 다음 항목
  1. 로고
  - 로고를 띄운다.
  - 객체 없음
  - 일정시간 후 알아서 다음 씬으로 넘어감
  - 자동으로 다음 State로 이동
  <br>
  
  2. 메인 화면
  - 게임 시작, 도움말 등 메뉴
  - 버튼 3개(게임시작, 도움말, 종료)
  - 마우스로 버튼 클릭
  - 마우스의 LBUTTON클릭 시 그 버튼에 해당하는 씬으로 이동
  <br>
  
  3. 스테이지
  - 본 게임을 하는 씬.
  - 게임 오브젝트들(좀비, 식물, 버튼, 공격체 등등)
  - 마우스 클릭으로 모든 조작. 식물 심기. 태양 습득 등등
  - 메인 메뉴로 넘어가기 위해 키보드 입력을 받음
   <br>
  
  
  4. 클리어
  - 스테이지 클리어 시 나오는 씬
  - 클리어 글씨를 객체로 만들어 띄운다.
  - 자동으로 넘어간다.
  - 다음 State인 스테이지로 자동으로 넘어간다.
   <br>
  
  
  5. 게임 오버
  - 스테이지 도중 게임 오버 시 나오는 씬
  - 다시하기, 메인화면 버튼 2개 생성
  - 마우스로 버튼 클릭
  - 다시하기 클릭 시 해당 스테이지 처음부터 다시 실행,
    메인화면 클릭 시 메인화면으로 돌아감.
    
    <br>
   
## 4. 필요한 기술
  - c++ 프로그래밍에서 배운 클래스를 생각하며 모듈을 분리하여 객체를 효율적으로 생성하여 사용하도록 한다.
  - 직선이동, 곡선 이동, 중력 값 적용 등 물리적인 요소 구현
  - 충돌 체크, 이펙트, 랜덤값을 알맞게 사용하기(100프로 랜덤이 아닌 내가 지정하는 수 중에 랜덤처리),
    스크롤 이동, 씬이동 자연스럽게, 페이드 인 아웃, 시간값 조절(게임 느려졌다 빨라졌다 하는 것)
