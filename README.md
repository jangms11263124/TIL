## Git 설정

### 저장소 만들기

```
git init
```

### global 설정하기

```
git config --global user.email "your email"
git config --global user.name "your name"
삭제 시 unset 옵션 사용
ex) git config --global --unset user.name

이름 삭제: git config --global --unset user.name
이메일 삭제: git config --global --unset user.email
삭제 확인: git config --global --list 

```

### git 상태보기

```
git status
git log --oneline
```

### 변경사항 저장(add & commit)

```
전체파일 추가
git add {file_name}  ex) git add .    
변경사항 저장
git commit -m {commit message}
```

### 기타

```
reset : 완전히 없던일로 치는거....(시계를 되돌리기)
revert : 그 변경사항 취소!
```

