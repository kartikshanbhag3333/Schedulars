var item_added=false;
    	$("#rquao").click(function(e){
    		alert("here");
    		{% if range == 1 %}
    		{% else %}
    			var current_bold=$("a.bolds").text();
    			var next_bold=parseInt(current_bold)+1;
    			
    			if(next_bold > {{ range }})
    			{
    			 	next_bold=1;
    			}
    			var data_required=(parseInt(next_bold)-1)*10;
    			//document.getElementById("todo"+current_bold).class="";
    			//document.getElementById("todo"+next_bold).class="bolds";
    			//alert(document.getElementById("todo"+next_bold).text);
    			$("#todo"+current_bold).removeClass("bolds");
    			$("#todo"+next_bold).addClass("bolds");
    			$(".todo-list").empty();
    			$.ajax({
        type:"post",
        url:"/temp/gettask/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		data:data_required},
        cache :false,
        async :true,
        success : function(res) {
        	
              $(".todo-list").html(res);
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        e.preventDefault();
    			 
    		{% endif %}
    	});
    	
    	$("#lquao").click(function(e){
    		{% if range	== 1 %}
    		{% else %}
    			var current_bold=$("a.bolds").text();
    			var next_bold=parseInt(current_bold)-1;
    			
    			if(next_bold < 1)
    			{
    			 	next_bold={{ range }};
    			}
    			var data_required=(parseInt(next_bold)-1)*10;
    			$("#todo"+current_bold).removeClass("bolds");
    			$("#todo"+next_bold).addClass("bolds");
    			$(".todo-list").empty();
    			$.ajax({
        type:"post",
        url:"/temp/gettask/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		data:data_required},
        cache :false,
        async :true,
        success : function(res) {
        	
              $(".todo-list").html(res);
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        e.preventDefault();
    		{% endif %}
    	});
    	
    	$("#add-task").click(function(e){
    		//alert($(".form-control option:selected").text());
    		item_added=true;
    		if(!$("#task-name").val() || !$("#task-time").val())
				{
					
					$(".user-result").hide();
					
					$(".user-result").text("Please Enter Task Details First");
					$( ".user-result" ).toggle( "slide" );
						
				}
				else
				{
					//alert('username='+$("#user").val()+'&password='+$("#pass").val());
					  $(".user-result").hide();
					$.ajax({
        type:"post",
        url:"/temp/addtask/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		taskname:$("#task-name").val(),
        		tasktime:$("#task-time").val(),
        		timepara:$("#time-para option:selected").text(),
        		tasktype:$("#task-para option:selected").text()},
        cache :false,
        async :true,
        success : function(res) {
        	
              $(".user-result").html(res);
              
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        e.preventDefault(); 
					  $( ".user-result" ).toggle( "slide" );
				}
				
    	});
    	
    	$("[id^=todo]").click(function(e){
    		var current_bold=$("a.bolds").text();
    		var clicked_bold=$(this).text();
    		$("#todo"+current_bold).removeClass("bolds");
    		$("#todo"+clicked_bold).addClass("bolds")
    		var data_required=(parseInt(clicked_bold)-1)*10;
    		
    		$.ajax({
        type:"post",
        url:"/temp/gettask/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		data:data_required},
        cache :false,
        async :true,
        success : function(res) {
        	
              $(".todo-list").html(res);
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        e.preventDefault();
    		
    	});
    	
    	
    $("#close-button").click(function(e){
    	
    	if(item_added)
    	{
    	var last_element=parseInt({{ range }});
    	var current_bold=$("a.bolds").text();
    	$("#todo"+current_bold).removeClass("bolds");
    	$("#todo"+last_element).addClass("bolds");
    	$(".todo-list").empty();
    	var data_required=(parseInt(last_element)-1)*10;
    	$.ajax({
        type:"post",
        url:"/temp/getLastCount/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		count:data_required},
        cache :false,
        async :true,
        success : function(res) {
        	
              //alert(res);
              data_required=parseInt(res);
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        //e.preventDefault();
    	item_added=false;
    	//alert(data_required);
    	var data;
    	if(data_required<10)
    	{
    		data_required=(parseInt(last_element)-1)*10;
    		data="false";
    	}
    	else
    	{
    		data_required=(parseInt(last_element))*10;
    		data="true";
    	}
    		
    			$.ajax({
        type:"post",
        url:"/temp/gettask/",
        //name:'username='+$("#user").val()+'&password='+$("#pass").val(),
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        		data:data_required,
        		newtask:data},
        cache :false,
        async :true,
        success : function(res) {
        	//alert(res);
        	alert(data);
        	if(data=="true")
        	{
        		//alert("here");
        		$("#counter").empty();
        		var html="<li><a href=# id=lquao>&laquo;</a></li>";
        		for(var i=1;i<={{ range|add:1 }};i++)
        		{
        			html+="<li><a href=# id=todo"+i+">"+i+"</a></li>"
        		}
        		html+="<li><a href=# id=rquao>&raquo;</a></li>"
        		$("#counter").html(html);
        	
        		
        	}
        	
              $(".todo-list").html(res);
              if(res=="Session Expired")
              {
              	window.location.href="/temp/"
              }
              
              return this;
             
            }  	
        });
        e.preventDefault();
    	}
    	
    });