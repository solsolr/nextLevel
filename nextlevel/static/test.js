function test() {
  var p1 = document.getElementById('user_pwd').value;
  var p2 = document.getElementById('user_pwd2').value;
  if( p1 != p2 ) {
    alert("비밀번호가 일치하지 않습니다.");
    return false;
  } else{
    return true;
  }

}
