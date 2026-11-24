목표
학습 주제
Vue를 사용한 양방향 데이터 바인딩


학습 목표
Vue에서의 양방향 데이터 바인딩이란 무엇인지 이해
v-model 디렉티브를 사용하여 폼 입력 요소와 데이터를 양방향으로 바인딩하는 방법
양방향 데이터 바인딩을 통해 사용자 입력에 따라 화면이 업데이트되고 데이터가 변경되는 상황을 다루기


학습 개념

Event Modifiers
Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 합니다.stop, prevent, self 등 다양한 modifiers를 제공합니다.
ex)
<form @submit.prevent="onSubmit">...</form>

위 명령어를 통해 form에서 제출 버튼을 눌러도 기본 동작이 수행되지 않도록 제어하며, onSubmit 메서드가 수행됩니다. • v-modelv-model을 사용하면 사용자 입력 데이터와 반응형 변수를 실시간 동기화할 수 있습니다.단순 text-input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능합니다. - 주의) IME(입력기)가 필요한 언어(한국어, 중국어, 일본어 등)의 경우 v-model이 제대로 업데이트 되지 않으므로, 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용해야 함
const inputText2 = ref('')

<p>{{ inputText2 }}</p>
<input v-model="inputText2">

학습 방향
문제
학습 문제
Vue3의 동적 데이터 바인딩과 이벤트 핸들링을 활용해 사용자 설문조사 양식을 작성하고자 한다. 주어진 코드를 활용하여 요구 사항을 만족하는 코드를 작성하시오.

반응형 변수 formData
속성 5개를 가진 객체이다.
각 속성의 이름은 name, email, age, residence, languages이며, 적절한 HTML의 각 input의 값과 양방향 바인딩된다.
함수 submitForm
HTML form 요소에서 submit 이벤트가 발생하면 호출된다.
반응형 변수 formDate 객체의 각 속성 값을 실행 결과 이미지에 맞춰 console에 출력한다.  
submitForm은 setup()에서 반환된 객체의 메서드이다.