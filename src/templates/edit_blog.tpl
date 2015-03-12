{% extends "layout.tpl" %} 
{% block body %} 
  <form method="post"  action="/user/edit/add"> 
    <div class="write-blog">
      
    <div class="section"> 
      <strong> 博客标题</strong> 

      <div class="blog-title"> 
	<input class="input" size="80" maxlength="50" name="title" value="blog title" placeholder="博客标题" type="text">
	  </input> 
      </div>
      
      <div class="catalog"> 
	<p>
	  <label class="setting-title">博客类b</label> 
	</p>
	<select class="select_box" name="classification" > 
	  <option value="article" > post </option>
	  <option value="private" > private </option> 
	</select> 
      </div>
      
    </div>
    
    
     <div class="section"> 
      <p>博客摘要  </p>
	  <textarea class="input" name="abstracts" placeholder="摘要，一段好的摘要"> </textarea>  
     </div>
	 
 
      <div class="section" id="content"> 
        <p><strong>博客正文  </strong>
	</p>
	<textarea class="input" name="blog-content"  style="padding: 5px 1% 3px 1%;width:80%;">

	  ![在此输入图片描述][1] [1]: http://static.oschina.net/uploads/space/2014/1230/154252_UkpX_1016427.png 
	  
	</textarea>
      </div>

      
       <div class="section" id="tag"> 
        <strong> 关键字</strong> 
        <input class="input" name="blog-tags" placeholder="设置Tag，用逗号隔开" size="80" type="text" /> 
       </div> 
	   
       <div class="section"  id="setting-password" style="margin-top:8px;"> 
         
          <p>设置密码 </p>
	    <input name="privacy" id="blog-password" value="0" /> 
		  
       </div>

       <div class="section" id="save">
	 
	   
	 <input type="submit" class="button" value="save"> </input>

	 <div class="section"> 
           <button type="button" class="s-button" id="save-bt"> 保存修改 
	   </button>
         </div> 
       </div>

       </div>
  </form>
  
{% endblock %}
