var host = "172.30.1.78";
var port = 9001;
var mqtt;

// callback함수 - 접속이 완료된 후 호출되는 함수
function onConnect(){
    console.log("접속완료");
}
// callback함수 - 접속 실패하면 호출되는 함수
function onFailure(){
    console.log("접속실패");
}
// publish하는 함수 정의
function sendMsg(msg){
    alert(msg);
    /*
    1. message객체 생성하기
    2. 토픽을 설정
    3. send메소드를 호출
    */
    message = new Paho.MQTT.Message(msg);
    message.destinationName = "iot/led";  // topic 설정
    //mqtt 메시지 보내기 - publish
    mqtt.send(message);
}
//mqtt 통신을 관리하기 위한 사용자 정의 함수
function MQTTConnect(){
    console.log("mqtt 접속:"+host+","+port);
    //mqtt 통신을 위한 클라이언트 객체 생성
    mqtt = new Paho.MQTT.Client(host,port,"javascript_client"); // "javascript_client"는 클라이언트 구분을 위한 id
    // mqtt 통신을 위해 필요한 설정을 명시
    var options = {
        timeout:3,
        onSuccess:onConnect,  // 접속 성공 했을 때 실행될 콜백함수 등록
        onFailure:onFailure,
    }
    mqtt.connect(options);
}