// 가위 바위 보 선택지 배열
const CHOICE = ['scissors', 'rock', 'paper']

const player1 = document.querySelector('.player1')
const player2 = document.querySelector('.player2')

player1.textContent = '민석'
player2.textContent = '준혁'

// player1, 2 img 접근
// 우클릭 검사 -> copy -> copy selector
const player1Img = document.querySelector('#player1-img')
const player2Img = document.querySelector('#player2-img')

// 개별 가위, 바위, 보 버튼 접근
const scissorsBtn = document.querySelector('#scissors-button')
const rockBtn = document.querySelector('#rock-button')
const paperBtn = document.querySelector('#paper-button')

// 버튼 선택 모음 배열
const BUTTON = [scissorsBtn, rockBtn, paperBtn]

// 승리 횟수 count 접근 - 요소일 뿐이고 계산하지 않아요
// 문자 + 숫자 -> 문자열 1+ '1' = '11
// textContent에다가 값을 바꿔치기해줄 예정
const countA = document.querySelector('.countA') // textContent 문자열
const countB = document.querySelector('.countB') // 

// 모달, 모달컨텐츠 접근
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

// 승리 카운트 변수 let으로 -> countA 랑 countB에 대입 시켜줄 거에요.
let cntA = 0
let cntB = 0


// 승패 판정 메서드, 핸들러 안에서 실행
function playGame(player1, player2) {
  // 반환 0 - 비김
  // 반환 1 - player1 우승
  // 반환 2 - player2 우승
  // cntA 와 cntB는 별개로 활용


  //  비김 - return 0
  // if player1 == player2:
  // if (조건문) {실행문}
  if (player1 === player2) { return 0 }


  // p1.가위
  if (player1 === 'scissors') {
    // p2.보자기 p1+ return 1
    if (player2 === 'paper') { cntA++; return 1 }
    // p2.바위  p2+ return 2
    else if (player2 === 'rock') { cntB++; return 2 }
  }
    
   

  // p1.바위 
  if (player1 === 'rock') {
    // p2.가위  p1+ return 1
    if (player2 === 'scissors') { cntA++; return 1 }
    // p2.보자기 p2+ return 2
    else if (player2 === 'paper') { cntB++; return 2 }
  }
    


  // p1.보자기 
  if (player1 === 'paper') { 
    // p2.바위 p1+ return 1
    if (player2 === 'rock') { cntA++; return 1 }
    // p2.가위 p2+ return 2
    else if (player2 === 'scissors') { cntB++; return 2}
  }

  // 그럴리는 없겠지만 위에 있는 if문을 못들어왔을 때를 대비해서 
  return 0
}

// 버튼 클릭 핸들러 콜백 함수 만들기만 한거라서
// 만드는 것이 끝이 아니고 요소에 붙여줘야해요 ;)
function buttonClickHandler(p1Choice) {
  
  // 1.플레이 버튼 제어 
  // 버튼 비활성화 - 한번 누르면 더 못누르게할려고
  // 힌트 disable = true
  // [scissorsBtn, rockBtn, paperBtn]
  // BUTTON.forEach((btn) => { btn.disabled = true })
  BUTTON.forEach((btn) => btn.disabled = true)

  // 2. 내 선택 이미지 반영
  // setAttribute(key, value)
  player1Img.src = `./img/${p1Choice}.png`

  // 3. 100ms 마다 playerB 무작위 변경 시작
  let p2Choice = '' // 변경하지 않음
  // setInterval(), Math.random 활용 
  const intervalId = setInterval(()=> {
    const randomIdx = Math.floor((Math.random() * CHOICE.length))
    p2Choice = CHOICE[randomIdx]
    player2Img.src = `./img/${p2Choice}.png`
  }, 100)

  // 4. 5초 후 결과 보여주기
  setTimeout(() => {
    // 4.1 intervalId 활용해서 player2의 가위바위보 애니메이션
    // 힌트 clearInterval() 에 위에 만든 setInerval()함수 넘겨주기
    clearInterval(intervalId)

    // 4.2 게임 시작
    const result = playGame(p1Choice, p2Choice)
    
    // 4.3 결과 반영
    countA.textContent = cntA
    countB.textContent = cntB

    // 4.4 모달창 결과
    if (result === 1) {
      modalContent.textContent = `${player1.textContent} win!`
    } 
    else if (result == 2) {
      modalContent.textContent =  `${player2.textContent} win!`
    }
    else {
      modalContent.textContent = "Tie!"
    }
    modal.style.display = 'flex'
    
    // 3초 후에 모달창 닫기
    setTimeout(() => {
      modal.style.display = 'none'
      // 게임 다시 할 수 있게 버튼 활성화 시키기
      BUTTON.forEach((btn) => { btn.disabled = false})
    }, 3000)
  }, 5000 )
}


// 이벤트 핸들러에 등록 
scissorsBtn.addEventListener('click', () => buttonClickHandler('scissors'))
rockBtn.addEventListener('click', () => buttonClickHandler('rock'))
paperBtn.addEventListener('click', () => buttonClickHandler('paper'))