<%
	username="1480003"
	password="pass@123"
	if request.form("uname")=username AND request.form("password")=password then
		session("status")=1
		response.redirect "index.asp"
	else
		response.redirect "login.asp"
	end if
%>