var obj_api = {
	

     call_login: function(VueObj, data, fn_return ){


                var url =  window.URL_API + "login" ; 

                 $.ajax({
                              type: "POST",
                              url: url,
                              contentType: "application/x-www-form-urlencoded",
                              processData: true,
                              data: data,
                              success: function (retorno) {
                                  
                                  console.log(retorno);

                                  var str = "Login realizado.<br> <b>Token Recebido:</b> " + retorno.token+
                                  "<br><b>CSRF TOKEN:</b> " + retorno.csfrtoken;

                                  VueObj.msg_retorno =str;
                                   if (fn_return != null ){
                                      	fn_return(retorno)
                                   }

                                 
                              },
                              error: function (xhr, status, p3, p4) {
                                  var err = "Error " + " " + status + " " + p3 + " " + p4;
                                  if (xhr.responseText && xhr.responseText[0] == "{")
                                      err = JSON.parse(xhr.responseText).Message;


                                  console.error(err);

                                  VueObj.msg_retorno ="Problema na comunicação com a Api";
                                  if ( document.getElementById("div_error_api") != null ){


                                        $("#div_error_api").html( xhr.responseTex ) ;
                                   } 

                              }
                          }).fail(function (response) {
                                console.log("Falha ao tentar obter dados");
                                console.log(response);   

                                  
                                  VueObj.msg_retorno ="Problema na comunicação com a Api";
                                if ( document.getElementById("div_error_api") != null ){
                                        $("#div_error_api").html( response.responseText );
                                }  
                          });


     },
      call: function(tipo, method, data , fn_return ){

              
                var url =  window.URL_API +  tipo; 
                console.log("URL enviada: " + url );
            
                var auth = "Bearer " + window.USER_TOKEN;
                var csfrtoken = window.USER_CSRFTOKEN ;    

                 $.ajax({
                              type: method,
                              url: url,
                              contentType:  "application/x-www-form-urlencoded", //"text/plain" 
                              processData: false,
                              data: data,
                              headers: {
                                Authorization: auth,
                                "Content-Type": "application/json", //"text/plain" , 
                                 Accept: "application/json",
                              //  "X-CSRF-TOKEN": csfrtoken,
                              //  "X-Requested-With": "XMLHttpRequest"
                              },
                              success: function (retorno) {
                                  
                                  console.log(retorno);
                                  console.log( fn_return );
								  
								  
                                  $("#div_error_api").html( "Sucesso: <pre>" +  JSON.stringify(retorno)+"</pre>" ) ;
                                 
                                   if (fn_return != null ){
                                        fn_return(retorno, tipo)
                                   }

                                 
                              },
                              error: function (xhr, status, p3, p4) {
                                  var err = "Error " + " " + status + " " + p3 + " " + p4;
                                  if (xhr.responseText && xhr.responseText[0] == "{"){
                                      
                                        console.log("Erro ao disparar mensagem");
                                        console.log(xhr.responseTex); 
                                        
                                          
                                   if ( document.getElementById("div_error_api") != null ){


                                        $("#div_error_api").html( xhr.responseTex ) ;
                                   }  
                                  }
                                    //  err = JSON.parse(xhr.responseText).Message;


                                  console.log(err);
                                
                                  //console.error(err);

                              }
                          }).fail(function (response) {
                                console.log("Falha ao tentar obter dados");
                                console.log(response); 

                                if ( document.getElementById("div_error_api") != null ){


                                        $("#div_error_api").html( "Falha ao tentar obter dados:" + 
                                           response.responseText );
                                }  

                          });


     },
	     call_upload: function(tipo, method, data , fn_return ){

              
                var url =  window.URL_API +  tipo; 
                console.log("URL enviada: " + url );
            
              //  var auth = "Bearer " + window.USER_TOKEN;
              //  var csfrtoken = window.USER_CSRFTOKEN ;    

                 $.ajax({
                              type: method,
                              url: url,
                              contentType:  "multipart/form-data", //"text/plain" 
                              processData: false,
                              data: data,
                              headers: {
                               // Authorization: auth,
                                "Content-Type": "application/json", //"text/plain" , 
                               //  Accept: "application/json",
                              //  "X-CSRF-TOKEN": csfrtoken,
                              //  "X-Requested-With": "XMLHttpRequest"
                              },
                              success: function (retorno) {
                                  
                                  console.log(retorno);
                                  console.log( fn_return );
								  
								  
                                  $("#div_error_api").html( "Sucesso: <pre>" +  JSON.stringify(retorno)+"</pre>" ) ;
                                 
                                   if (fn_return != null ){
                                        fn_return(retorno, tipo)
                                   }

                                 
                              },
                              error: function (xhr, status, p3, p4) {
                                  var err = "Error " + " " + status + " " + p3 + " " + p4;
                                  if (xhr.responseText && xhr.responseText[0] == "{"){
                                      
                                        console.log("Erro ao disparar mensagem");
                                        console.log(xhr.responseTex); 
                                        
                                          
                                   if ( document.getElementById("div_error_api") != null ){


                                        $("#div_error_api").html( xhr.responseTex ) ;
                                   }  
                                  }
                                    //  err = JSON.parse(xhr.responseText).Message;


                                  console.log(err);
                                
                                  //console.error(err);

                              }
                          }).fail(function (response) {
                                console.log("Falha ao tentar obter dados");
                                console.log(response); 

                                if ( document.getElementById("div_error_api") != null ){


                                        $("#div_error_api").html( "Falha ao tentar obter dados:" + 
                                           response.responseText );
                                }  

                          });


     }



}

//window.obj_api = obj_api;