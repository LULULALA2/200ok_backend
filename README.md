# 200ok_backend
<p align="center"><img src="https://user-images.githubusercontent.com/104331479/187144287-5f11415c-eff6-4dfa-8ddd-fc704bc4eaa5.png"></p>
<br>

<br>**목차**
<br>[1. 프로젝트 소개](#intro)
<br>[2. 프로젝트 기획 - 시연영상](#프로젝트-기획)
<br>[3. 맡은 역할](#-담당-역할)
<br>[4. 트러블슈팅](#troubleshooting)
<br>[5. 회고](#회고)
<br>

# 🧙‍♂️녹턴앨리 B-street 지하2층 불법 입학 센터 (200ok)
해리포터 컨셉, 사람 사진을 초상화처럼 스타일을 변경하고 움직임을 추가해서 움직이는 초상화를 만들고 기숙사를 분류해주는 웹사이트

<br>

# ⭐Intro
* Style Transfer와 Deepfake를 이용해 사진을 움직이는 초상화로 변형
* 기숙사 배정 테스트와 Chart로 기숙사별 학생수 및 방명록 작성수 시각화
* S.A : [블로그로 이동(☞ﾟヮﾟ)☞](https://cold-charcoal.tistory.com/108)
<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=fff) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=python&logoColor=fff) 

<br>

# 📌Project

### 프로젝트 기획

* 시연영상 : [시연 영상 확인하기(☞ﾟヮﾟ)☞](https://cold-charcoal.tistory.com/117)
* 원본 팀 깃허브 : <a href="https://github.com/cmjcum/200ok_backend">https://github.com/cmjcum/200ok_backend</a>
* Frontend Repository : <a href="https://github.com/cmjcum/200ok_backend">https://github.com/cmjcum/200ok_frontend</a>
* 프로젝트 기간 : 2022.06.28 ~ 2022.07.06

<br>

### 핵심기능

* Style Transfer와 Deepfake를 이용한 이미지 변형
* JWT를 이용한 사용자 인증
* 라운지 페이지에서 방명록 CRUD
* Chart를 이용한 데이터 시각화

<br>

### ✔ 담당 역할
* 기숙사 배정 결과 페이지, 마이페이지, 로그인페이지 제작
* 사용자 정보 표시, sns공유 및 클립보드 링크 복사 기능
* AWS(EC2, Cloud9) 백엔드 배포

<br>

### API
<a href="https://typingmylife.notion.site/MakeMigrations-API-53526cc465344be98ab4e786e487414f">노션 페이지로 이동</a>

<br>

### ERD
![make migrations (6)](https://user-images.githubusercontent.com/104487608/185342143-bfb69da1-2719-4df0-bfa0-fd3353a82036.png)

<br>

# 🧨TroubleShooting

### 1. 사용자가 배정받은 기숙사에 따라 CSS를 변경해야하는 문제
<br>
기숙사는 4개인데 만들어져있는 템플릿은 한개여서 사용자가 배정받은 기숙사에 따라 CSS를 변경해주어야 했습니다. 그래서 미리 각 기숙사에 맞는 알파벳을 붙여서 CSS class를 만들어 놓고 받아오는 기숙사정보에 따라서 적용하는 class의 이름이 바뀌도록 했습니다.
<br>
```javascript
// get data - sorting dormitory
async function change_mydormitory() {

    const response = await fetch(`${backend_base_url}/dorm/sorting/`, {
        method: 'GET',
        headers : { Authorization : "Bearer " + localStorage.getItem("access")},
        withCredentials: true,
    })
    .then(response => response.json())
    .then(data => {      
        dormitory = ["gd", "hf", "sth", "rc"]
        let room_id = data.dormitory_id - 1
        
        // dorm element
        document.getElementById("mybg").classList.toggle(`${dormitory[room_id]}-bg`)
        document.getElementById("mydorm1").innerText = `${data.dormitory}`
		// .. 생략 ..

        // student id card
        admission = getYmd10(data.join_date)
        student_id = admission.slice(2, 4) + String(data.dormitory_id).padStart(2,'0') + String(data.id).padStart(4,'0')

		//.. 생략 ..
        document.getElementById("admission").innerText= `${admission}`
        // document.querySelector(".portrait").attr('style', 'background-image: url("' + image_url +'")')
    })
}
```

<br>

# 🖋회고
프로젝트 기간에 비해서 볼륨이 좀 컸던 것 같다. 그래서 서로 프로젝트에 집중하느라 팀 내 소통이 조금 부족했었다. 가장 큰 문제는 배포를 성공하지 못한 것이었는데, 마감 3일전부터 시작하면 충분히 할 수 있을 거라 생각했는데 배포가 생각보다 오래걸리고 고려해야될 변수가 많았다. 그래서 다음 프로젝트에서는 배포를 미리부터 준비하자는 의견이 나왔다. 그래도 그동안 다른 프로젝트에서는 해보지 못했던 EC2, S3 사용 같은 것도 해볼 수 있어서 좋았고, 멀티프로세싱이라는 새로운 기술도 접할 수 있어서 만족스러웠다. 이번에도 제작한 목업과 기획대로 잘 완성이 되었는데, 특히 프론트쪽은 목업보다 더 잘나와서 뿌듯했다.

<br>

# 실행 화면
![1](https://user-images.githubusercontent.com/104487608/185343990-348d6941-0075-4ab8-9d48-d239e77292b1.png)
![2](https://user-images.githubusercontent.com/104487608/185344475-4786790a-ad6c-4c0e-8ef5-d285059a8376.png)
![3](https://user-images.githubusercontent.com/104487608/185344856-6470e4d1-2423-4441-a477-8bd8cc3d54ac.png)
![4](https://user-images.githubusercontent.com/104487608/185345234-a19afc70-d251-4d6c-941c-941138dd4aa8.png)
![5](https://user-images.githubusercontent.com/104487608/185346135-f155e0a7-9f1b-471e-96a6-bfbe991b1305.png)

<br>

# 👨‍👨‍👧‍👧TEAM Coumi
|이름|역할|깃허브|
|:---:|---|---|
|김동근|메인 페이지|[![github_icon](https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white)](https://github.com/yinmsk)|
|노을|라운지 페이지|[![github_icon](https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white)](https://github.com/minkkky)|
|이정아|메인 페이지, 테스트 페이지 제작|[![github_icon](https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white)](https://github.com/zeonga1102)|
|이현경|테스트 결과 페이지, 마이 페이지 제작|[![github_icon](https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white)](https://github.com/LULULALA2)|

<br>

# ✨Credit
* Style Transfer pre-trained models : <a href="https://github.com/ycjing/Neural-Style-Transfer-Papers"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* 딥페이크 코드 :  <a href="https://github.com/AliaksandrSiarohin/first-order-model"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* 해리포터 모바일게임 "HOGWARTS MYSTERY" - 기숙사 배경
