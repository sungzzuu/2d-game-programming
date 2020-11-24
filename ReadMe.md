# 기말 프로젝트 1차 발표

* **High Concept**

    식물과 좀비의 싸움이라는 신박한 디펜스 게임. 본 게임에는 없던 좀비 이동 아이템 추가 예정.
    디펜스 게임으로 좀비의 공격으로부터 기지를 보호해야 한다.

    공격하는 식물인 공격형 식물과 보조역할을 하는 식물인 보조형 식물을 적절히 배치하여 좀비의 공격으로부터 기지를 보호한다.

    각 식물과 좀비의 특성을 달리하여 플레이어가 원하는 플레이를 하도록 한다.

    스테이지 클리어 시 새로운 식물을 추가하여 플레이어의 흥미를 이끈다.


<br>  

* **게임의 핵심 메카닉**  
  1. 스테이지마다 식물 종류 추가됨
  2. 식물을 드래그 앤 드롭하여 배치
  3. 햇살을 클릭하여 섭취
  4. 같은 자리에 식물 놓을 수 있음(같은 식물만)
<br>

## 2. 개발 범위

![Alt text](https://github.com/sungzzuu/2d-game-programming/blob/master/image/2020-10-10%20(47).png?raw=true)

   <br>

  ### <구현할 식물 종류 5종류>

  #### 1.  해바라기: 일정시간마다 햇살 생성
  ![Alt text](https://ww.namu.la/s/0f673158ccacb32d9fa54e6dd5a6684d8ffb2a3d9642bd4d46a3a651f2231d604dff6a5f43f218163d5a2a68ec7cd3e3a3c85639864f3ff204997b0eececc7a95d5a50344be56dcdb35937d4c16be848f952549d47dbd29f0d553ec681925685)
  
  <br>
  
  #### 2. 초록 식물: 초록 총알 쏨
   ![Alt text](https://w.namu.la/s/2b95be7177a577edeadccd2dbd02b50c0e387056588f2c3a3e7fd76d44dc38faf1687f782e12163451476f680144f1faed46936f422383c9dbcdc40c1e81f8ee97bad99a49919f1148a52d2f6393acb842acad2e537a009b00c3ef00258497a5)
  
  <br>
  
  #### 3. 얼음 식물: 얼음 총알 쏨
   ![Alt text](https://w.namu.la/s/2e5897cfcd685ee3d05b4f31e315088efb29cb76cc6239a7a079dc6623a7dcc7a5b1fc3bf9ca13a2497ae30f8ad36a649b7aa72517cd19688ff7ac78a2256998665314372fee1b32d3fca49ba7f4473bf53a857f28a39ae9e291870a6d20cea7)
  
  <br>
  
  #### 4. 체리: 폭탄
   ![Alt text](https://w.namu.la/s/517273ab300d33e9e28b59828ca169fe9bda46e1be00d89fcbbc5f47197ce134559f233819328f9cbcbba1a7ce867efced7c0918d0f8a2cf423806919a8c61db8377c46590175f60317a7497a71e772bb906bd91df9ec8934b36bb390875b8b3)

  <br>
  
  #### 5. 호두: 체력이 큰 방패역할
   ![Alt text](https://w.namu.la/s/aa21f37d8059b8dba920e45fa7115954ab75515988f8a148c1f5ff652f858c1893a0554f0106b33a21fa74b8d4f42abe92b94c2afebd3cb382a0a6a0bc16ee6f7350c6c8f3d238f16f8602ee652626293a1ecc25004e3285a15bdcf3702ba8d5)
  
  <br>
  
  
  ### <구현할 좀비 5종류>
  
  #### 1.  일반 좀비
  ![Alt text](https://w.namu.la/s/4a82173cbd2231249165c7a8386e58a5109605e03b8375195cf6a6be8232c6136f0a61894908fc6db663c19b35a79331712c58cab908c6ed53af7e1a3986c9fca2dab5f6f2a9f3cf4284dcd78be52940ab2fd491a65fcf8143439e0f7f481d9a)
  
  방어력 10
  <br>
  
  #### 2. 깃발 좀비
  ![Alt text](https://ww.namu.la/s/5dfef662a286a62f8e1f8332da18f414759a92e8c091e4d305983db17c0863221fe576833ab6227998f4e58966ad39cc90925a17323c5d993fc714eda2d7a6db846c9e6828d49acec9894b236880838d1a4775432114ff3b0e7005834e4fbd45)
  
  방어력 10
  <br>
  
  
  #### 3. 콘헤드 좀비
  ![Alt text](https://w.namu.la/s/6baeaa686d2d7d2b851382235251e39496fb9cbc5884582845875438d629083269f4b07f701fa9e2feadc69cdaf1fe445f05747cc6dda12b28ae970811b53de0d2a2fdabeab60e543248cb64c17c12e16c24c5fc9a48bc413317ce470f461014)
  
  방어력 28
  <br>
  
  
  #### 4. 장대 좀비
  ![Alt text](https://w.namu.la/s/a74a6c178c7594eb947a7622843772fe8d75ec6047a27b136afd65d0a94312613eb4efbb850c11f5980ae28a426f1006a4d00137ab111affb4091ac7853750c1250c9536a7799c60a66e8d3feb643eca45896fd192cf44e8cbc3e313e01fa105)
  
  방어력 17 식물 통과 1회
  <br>
  
  
  #### 5. 양동이 좀비
 ![Alt text](https://w.namu.la/s/4baf64aff98d2f4a9b69c715952460b73ef0b2dddd91d69a7412f468628ca35b25a22060b0d821523cdd2525817add8beb8212b72c4062f4c3ffd60c11ec485e7fe804d13c022d7f10f656a879576960a2497bdc6788c3d69e6cb2121b6c5e4f)
  
  방어력 65 
  <br>
  
### 구현할 아이템 종류
    1. 삽: 무한으로 사용가능. 식물 파괴 시 사용
    2. 좀비 이동: 좀비 클릭하여 뒤로 보내기-> 일정시간마다 생성
  
  <br>
  
### 구현할 씬 종류
    1. 로고 : 로고를 띄운다.  
    2. 메인 화면 : 게임시작, 도움말 등 메뉴 선택  
    3. 스테이지(5스테이지) : 게임 플레이, 클리어 시 새로운 식물 추가  
    4. 클리어 : 스테이지 클리어 시 나오는 씬  
    5. 게임 오버 : 게임 오버 시 나오는 씬
    6. 스테이지 중간 메뉴 : 스테이지 내에서 menu버튼 클릭 시 뜨는 씬
    7. 스테이지 월드: 스테이지 선택 화면

  <br>



## 3. 예상 게임 실행 흐름

  #### 1. 마우스 피킹을 통한 식물 배치
  #### 2. 햇살의 개수 확인을 통해 식물 배치 여부 판단
  #### 3. 식물마다 각각의 무기(총알, 호박, 얼음 등등) 일정 시간마다 발사
  #### 4. 식물의 무기와 좀비 충돌체크해서 좀비 체력 깎음
  #### 5. 식물과 좀비 충돌체크해서 식물의 체력 깎음 식물이 죽으면 좀비 앞으로 이동
  #### 6. 기지 범위 안에 좀비가 들어오면 차 한 대씩 사라짐
   ![Alt text](https://github.com/sungzzuu/2d-game-programming/blob/master/image/2020-10-10%20(48).png?raw=true)

   <br>

   ![Alt text](https://github.com/sungzzuu/2d-game-programming/blob/master/image/2020-10-10%20(49).png?raw=true)

   <br>

   ![Alt text](https://github.com/sungzzuu/2d-game-programming/blob/master/image/2020-10-10%20(50).png?raw=true)

   <br>


## 4. 개발 일정

   ![Alt text](https://github.com/sungzzuu/2d-game-programming/blob/master/image/2020-10-10%20(51).png?raw=true)

   <br>
