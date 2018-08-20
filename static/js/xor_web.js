 
 
  $('body').on('click',"button",function()
  {
  
    $('#inf').modal("show") ; 
  }) ; 
  
 $('body').on('click',"#cnfg",function()
  {
      var epochs = $('#epochs').val() 
      var rate = $('#rate').val() 
      
      
      $.ajax({
            type : 'post' , 
            url : "/cnfg" , 
            data : { "epochs" : epochs ,
                     "rate" : rate } , 
            success : function(result) 
            {
               $("#alert").fadeTo(2000, 500).slideUp(500, function(){
               $("#alert").slideUp(500);
            });
            }
      }) ; 
  }) ;
   
  $('body').on('click',"#ok",function()
  {
      var a = $('#input_a').val() 
      var b = $('#input_b').val() 
      
      $("#gf").show() ; 
      
      $.ajax({
            type : 'post' , 
            url : "/xor" , 
            data : { "a" : a ,
                     "b" : b } , 
            success : function(result) 
            {
               
               
               $("#gf").hide() ; 
                
               $("#alert2").fadeTo(2000, 500).slideUp(500, function(){
               $("#alert2").slideUp(500);
               }) ; 
               
               s = result.split(",") ; 
               
               
               $('#result').html(s[0]) ;
               $('#cost').html(s[1]) ; 
            }
      }) ; 
  }) ; 
  