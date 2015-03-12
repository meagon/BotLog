<!DOCTYPE html> 
<html  lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<link rel="stylesheet"  href="/static/final.css" type="text/css" >
</head>

<body class="home blog col-3cm full-width topbar-enabled gecko">

<div id="wrapper">
  <div class="container" id="page">
    <div class="container-inner">
      <div class="main">
	<div class="main-inner group">
	  <section class="content">
	    <div class="page-title pad group">
	      <h2>Meagon space*</h2>
	    </div><!--/.page-title-->	
	    <div class="pad group">
	      <div class="featured">

{% for blog in blogs %}
		<article id="{{blog.post_id}}" class="post post type-post status-publish format-standard has-post-thumbnail hentry category-stationery-zakka tag group">
		  <div class="post-inner post-hover">		
		    <div class="post-thumbnail">
			<a href="{{ blog.url}}" title="{{blog.title}}">
				<img width="720" height="340" src="{{blog.thumbnial_url}}" class="attachment-thumb-large wp-post-image" alt="图片描述" />
			</a>
			<a class="post-comments" href="{{blog.url + "/#comments"}}">
			  <span><i class="fa fa-comments-o"></i>	{{ blog.comments_len }}  </span>
			</a>
		    </div><!--/.post-thumbnail-->		
		    <!--- blog meta information -->
		    <div class="post-meta group">
		      <p class="post-category">
			<a href="{{blog.category}}" title=" 查看分类「{{blog.category}}」的全部文章" rel="category tag">
			  {{  blog.category.url }} 分类  
			</a>
		      </p>
		      <p class="post-date">   {{ blog.date }}   24 /7/2014</p>
		    </div><!--/.post-meta-->
		    <h2 class="post-title">
		      <a href="{{ blog.url }}" rel="bookmark" title="{{ blog.title }}"> {{ blog.title }}</a>
		    </h2>  <!--/.post-title-->
		    <!-- 
		    <div class="entry excerpt">	 <p> {{blog.content[:50]+ "..."}}   </p>
            -->
		    <div class="entry excerpt">	 <p> {{ blog.content+ "..."}}   </p>
		    </div><!--/.entry-->
		  </div><!--/.post-inner-->	
		</article><!--/.post-->	
		{% endfor %}
		
	     </div><!--/.featured-->
	      <nav class="pagination group">
		      <div class='wp-pagenavi'>
		      <span class='pages'>Page 1 of 55</span>
              <span class='current'>1</span>
              <a class="page larger" href="blog.com/page/2/">2</a>
              <a class="page larger" href="blog.com/page/3/">3</a>
              <span class='extend'>...</span>
              <a class="nextpostslink" href="blog.com/page/2/">下一页</a>
              <a class="last" href="blog.com/page/{{blogs.count()}}/"> »</a>
	          </div>	
          </nav><!--/.pagination-->
	    </div><!--/.pad-->
	  </section><!--/.content-->
	  
	</div><!--/.main-inner-->
      </div><!--/.main-->
    </div><!--/.container-inner-->
  </div><!--/.container-->
</body>
</html>
