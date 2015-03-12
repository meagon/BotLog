
<!DOCTYPE html> 
<html  lang="zh-CN">
<head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <link rel="stylesheet"  href="/static/css/final.css" type="text/css" >
        <script src="/static/js/lib/jquery.min.js"></script>
    {% block head %}
    {% endblock %}
</head>

<header>
    <div class="avatar"> </div>
    <div class="title">
    </div>
    <nav>
        <ul class="nav">
            <li><a class="category" href="/blogs">blogs</a></li>
            <li><a class="category" href="/about">About </a> </li>
            <li><a class="category" href="/archives">Archives</a></li>
            <li><a class="category" href="/links">Links</a></li>
        </ul>
    </nav>
</header>

<div class="wrapper">
    {% block body %}
    {% endblock %}
</div>


<footer>
    <div class="wrapper">
        <div id="copyright">
            <p> {{local.user}} space © 2014 . All Rights Reserved </p>
        <div> <!--/#copyright-->
        <p class="footer">Powered By <a href="http://github.com/meagon/botlog"> BotLog </a></small></p>
        <p class="email"> <small>    
            <a href="mailto: meagon@localhost "> {{local.user}}
            </a>
        </p>    
    </div>
<footer>

</body>
</html>
