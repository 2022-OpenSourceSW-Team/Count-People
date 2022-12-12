# Count-People

## 개요

2022년 10월 29일 이태원에서 압사 사고 발생하였으며 좁은 이태원 골목에 핼러윈을 즐기려는 수많은 인파가 몰렸다. 특히 사고가 발생한 골목은 보행로 폭이 4ｍ 안팎으로 매우 좁은 구역임에도 현장 통제 및 통행
관리가 전혀 이뤄지지 않으면서 대형 참사로 이어졌다. 이 사고로 158명이 사망하는 등 300명이 넘는 사상자가 발생했는데, 사망자 성별은 102명이 여성, 56명이 남성으로 확인됐다. 이 가운데 외국인 사망자는
중국·이란·미국·우즈베키스탄·노르웨이·일본·러시아·호주·스리랑카 등 14개국 26명으로 파악됐다.

[관련 자료 Link](https://terms.naver.com/entry.naver?docId=6637399&cid=43667&categoryId=43667, "관련 자료")

## 목표

우리는 openCV를 활용하여 사람들의 수를 Counting하고 일정 임계값을 넘어가게 되면 관리자에게 TTS 및 경보를 통해 위험성을 전달할 예정이다. 이를 통해 기존의 인구 밀집으로 인한 사망자 및 사상자를
줄이는 것이 목표이다.

## 특징

- 설치 및 사용이 쉬움
- 비교적 높은 정확도
- 다양한 사용자 위험 인지 도움 (현재 인원 출력 & TTS & 경보음)

## 프로그램 Flow

1. oepnCV를 활용한 카메라 사용
2. haarcascade_eye.xml & haarcascade_frontalface_default.xml을 통해 얼굴 인식 진행
3. 인식된 얼굴을 Counting하여 현재 카메라 프레임내의 인원 수 파악
4. TTS(Text-to-Speech)을 화용하여 관리자에게 현재 인원 수 전달
5. 지정된 인원의 threshold를 초과하여 인원 수 발생시 경보 발생

## 라이브러리

자세한 라이브러리 버전을 확인하고 싶은 경우 requirements.txt를 참고해주시기를 바랍니다.
<pre>
<code>
pip install -r requirements.txt
</code>
</pre>

## 실행

<pre>
<code>
cd workspace <br>
python3 workspace/test.py
</code>
</pre>

## 시연

추후 추가 예정

## 라이센스

Apache License 2.0   
A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.    

[Apache License 2.0 Link](https://www.apache.org/licenses/LICENSE-2.0, "홈페이지")
