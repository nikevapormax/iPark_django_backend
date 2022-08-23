# iPark Project
> https://www.ilovepark.net <br>
> [frontend repo](https://github.com/2JYK/iPark_frontend)

## 📌 프로젝트 개요
- 공원을 중심으로 한 지역의 커뮤니티 구성
- 커뮤니티를 통해 친목 도모 및 나눔마켓 활성화
- 공원 옵션 또는 선호 지역을 선택해 원하는 공원 찾기

<br>

## 📌 개발환경
### back-end : <img src="https://img.shields.io/badge/python-3.9.10-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-4.0.6-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/django rest framework-4.0.6-red?style=for-the-badge&logo=django-rest-framework&logoColor=white"> <img src="https://img.shields.io/badge/postgreSQL-4169E1?style=for-the-badge&logo=postgreSQL&logoColor=white">

### front-end : <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">

### deploy : <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">

<br>

## 📌 역할
- **Django의 기본 user model을 커스텀**해 사용자 관련 기능 구현
    - **회원가입**, **로그인**, **계정관리**, **아이디 찾기**, **비밀번호 변경**
- **query parameter를 활용**한 공원 검색 기능 구현
    - **이름**을 통한 공원 검색
    - **옵션 및 지역**을 통한 공원 검색
- **인기 있는 공원** 또는 **공원 이름의 초성을 활용**한 공원 목록 나열
- **geopy 모듈**을 사용해 공원 근처 공영 주차장을 거리순으로 추천

<br>

## 📌 ERD

<img width="1242" alt="ipark" src="https://user-images.githubusercontent.com/104303285/185301146-12508b43-dd0f-4bd1-afa1-5666f2fab8ea.png">

<br>

## 📌 사용자 피드백
- 프로젝트의 방향이나 여건 상 맞지 않는 피드백은 필터링하고 **7일의 기간동안 마무리할 수 있을 것 같은 피드백을 선별**해 아래와 같이 해결
- 공원과 공영 주차장 공공 데이터들은 인터넷으로는 추가적으로 조사해 퀄리티를 높일 수 없다 판단해 보류

<img width="530" alt="스크린샷 2022-08-22 오후 6 45 13" src="https://user-images.githubusercontent.com/99387514/185892052-7cecef17-bb12-4cf0-ab2a-f6d28a736bda.png">

<br>

## 📌 트러블슈팅
<details>
<summary>회원정보 수정을 시도하면 새로운 사용자가 생성됨</summary>
&nbsp;&nbsp;&nbsp;&nbsp;- <code style="white-space:nowrap;">partial=True</code>로 인해 입력한 정보만 가진 사용자가 생성됨 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- serializer에 로그인한 사용자의 데이터를 추가해 아래와 같이 보내주어 사용자의 정보를 수정할 수 있도록 조치 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code style="white-space:nowrap;">serializer = UserSerializer(user, data=request.data, partial=True)</code> <br>
    <br>
&nbsp;&nbsp;&nbsp;&nbsp; > github issue : https://github.com/2JYK/iPark_django_backend/issues/29 <br>
</details>

<details>
<summary>TypeError: expected string or bytes-like object 발생</summary>
&nbsp;&nbsp;&nbsp;&nbsp;- 정규표현식을 사용할 떄 해당 에러 발생 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- <code style="white-space:nowrap;">birthday_input = correct_birthday.match(data.get("birthday", ""))</code>에서 에러가 발생하였고, 정규표현식을 사용할때는 생년월일의 값이 str로 들어와야 유효성을 검증할 수 있음 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- <code style="white-space:nowrap;">birthday_input = correct_birthday.match(str(data.get("birthday", "")))</code>로 수정해 에러 해결 <br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp; > github issue : https://github.com/2JYK/iPark_django_backend/issues/34 <br>
</details>

<details>
<summary>through 테이블 사용 시 에러 발생</summary>
&nbsp;&nbsp;&nbsp;&nbsp;- 애초에 모델 생성 시 같이 작성하였다면 에러가 나지 않았을 것이지만 한참 뒤에 생성하게 되어 에러 발생 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- runserver에서는 에러가 나지 않지만, 테스트 코드 작성 시 에러 발생 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code style="white-space:nowrap;">django.db.utils.OperationalError: table "park_park_option" already exists</code> <br>
&nbsp;&nbsp;&nbsp;&nbsp;- migrate를 지웠다가 다시 생성하는 방법을 통해 에러 해결 <br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp; > github issue : https://github.com/2JYK/iPark_django_backend/issues/57 <br>
</details>

<details>
<summary>사용자 관련 기능 사용 시 에러 처리에 대한 고민</summary>
&nbsp;&nbsp;&nbsp;&nbsp;- 맨 처음 기능 구현 시에는 기본 validator와 serializer의 custom validator의 정규표현식을 사용해 틀린 부분에 대한 에러 메세지를 사용자에게 alert를 통해 제시하도록 작성 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- model 생성 시 각 항목에 맞는 field를 사용했기에 기본 validator의 에러 메세지가 사용자에게 제시되고, 대다수의 항목은 정규표현식을 바탕으로 한 에러메세지가 반영되지 않음 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- 서비스를 사용하면서 필요없는 부분을 삭제하고 정규표현식이 불필요한 항목들을 수정 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- 추가적으로 에러 메세지가 반영되지 않았던 부분들이 많고 틀린 부분을 다 보여주는 것이 보안에 좋지 않을수도 있다는 피드백이 있어 에러 메세지를 하나로 통일 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- 사용자의 피드백을 반영하기 위해 다시 항목에 맞는 에러 메세지를 사용자에게 제시하였으며, alert창이 아닌 틀린 부분에 표시되도록 수정 <br>
    https://github.com/nikevapormax/iPark_django_backend/blob/942a473ba96c7aadaeb19ac6b3900b91042fcf8d/user/views.py#L34
    https://github.com/nikevapormax/iPark_django_backend/blob/942a473ba96c7aadaeb19ac6b3900b91042fcf8d/user/serializers.py#L22
    https://github.com/nikevapormax/iPark_frontend/blob/1145041a5c36d3e4e6fbe5ee520914ff86d2a565/static/js/api_user.js#L47
</details>

<details>
<summary>회원의 비밀번호 수정 코드 오류 해결</summary>
&nbsp;&nbsp;&nbsp;&nbsp;- 회원의 비밀번호를 수정하는 코드 작성 시 <code style="white-space:nowrap;">validated_data</code>에 포함된 비밀번호를 서로 비교하도록 코드 작성 <br>
&nbsp;&nbsp;&nbsp;&nbsp;- 프론트엔드와 연동해 비밀번호를 수정하고, 포스트맨을 통해 비밀번호를 수정할 때는 문제가 없었으나 <code style="white-space:nowrap;">테스트 코드</code> 작성 시 에러 발생 <br>
    https://github.com/nikevapormax/iPark_django_backend/blob/531ab77844a2fefb2a38878bca05d4b43ede7172/user/tests.py#L330
&nbsp;&nbsp;&nbsp;&nbsp;- serializer의 코드에 문제가 있다는 것을 발견하고 아래와 같이 수정 (100번줄 ~)
https://github.com/nikevapormax/iPark_django_backend/blob/531ab77844a2fefb2a38878bca05d4b43ede7172/user/serializers.py#L100
</details>
<br>

