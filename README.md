# 위치 게임

CodeHelp팀의 올해 척 작품, 위치 게임. 라이프 로깅 테크놀로지로 술래잡기를 한다.

## API 사용
``HOST_URL/api/<type\>/`` 이 **API URL**이며, `POST` request으로 데이터를 보낸다.

### TYPE: `UPDATE` (`POST` request)
전달값: <code>{"user":"유저이름", "LAT": 위도(플로트형), "LONG": 경도(플로트형)}</code><br>
반환값: 
```json
{
  "result": "success",
  "protocol": 1, 
  "data": [
    {
      "name": "예제데이터", 
      "lat": 예제데이터의 위도, 
      "long": 예제데이터의 경도,
      "abv": 잡힐수 있는가의 여부,
      "close": 가까이 있는냐 (10m 내외),
      "latAPI": 예제데이터의 정확한 위도,
      "longAPI": 예제데이터의 정확한 경도,
      "distance": 유저와 예제데이터의 거리,
      "direct": 가야하는 방향
    }, 
    {
      "name": "실제 데이터", 
      "lat": 37.72,
      "long": 127.27,
      "abv": "disabled",
      "close": false,
      "latAPI": 37.7189257,
      "longAPI": 127.2650342,
      "distance": "19.62km",
      "direct": "E"
    }
  ]
}
```

### TYPE

## MIT LISCENCE
Copyright (c) 2022 Sarang Park

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
##
- MIT 라이센스 소프트웨어는 누구라도 무상으로 제한없이 취급해도 된다.

- MIT 라이센스 소프트웨어를 취급할 땐 사용한 소프트웨어의 저작권 허가 표시를 모든 복제물이나 중요한 부분에 기재해야한다.

- MIT 라이센스 소프트웨어를 사용해서 발생한 문제는 저작권자가 책임지지 않는다.

