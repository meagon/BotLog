
<html>
<head>

<link rel="stylesheet" href="/static/css/login.css" type="text/css" > </link>

<!--
<link rel="stylesheet" href="/static/css/tabzilla-min.css" type="text/css" > </link>
-->
<style type="text/css">

/*
.hidden{
	display:none
}

form .form-group {
    padding: 15px 0;
 }
*/


</style>
</head>

<body>

<!--<div class="main-column" > -->
<div id="main-content" >

<form method="post">
<fieldset>
<legend>
Log in
</legend>

<input type = "hidden" value="http://" name= "refer"> </input>
<input type = "hidden" value="JJJ" name="csrfmiddlewaretoken"> </input>

<div class="form-group input_id_user required">
     <label class="control-label" for="id_username">
        Username / Email Address
     </label>
     <input id="id_username" type="text" value="" required="" name="username" autofocus=""> 
     </input>
</div>

<div class="form-group input_id_passwod required">
    <label class="control-label" for="id_password" >
     PASSWORD
    </label>
        <input id="id_password" type="password" required="" name="password">
    </input>
</div>

<div class="form-actions">
    <button class="primary button button-blue arrow" value="Log in" type="submit">
        <span> 
            Sign In
        </span>
    <button>
</div>

<fieldset>
</form>
</div>

<body>

</html>
