function createSchools() {
                                var a  = Math.random()*100;
                               
                                var list = document.getElementById("School_Tab");          //ingests list of schools from all_schools.js
                               
                               
                                school_names.forEach((school_name) => {                 // Setting up process to create buttons for every                                                            schoool listed
                                    
                                var School_Button = document.createElement("button");  
                                    School_Button.id = "Each_School" + a;
                                    School_Button.innerText = school_name;
                                    School_Button.style.color = 'white';
                                    School_Button.style.backgroundColor= '#191a1d';
                                    School_Button.style.width= "100%";
                                    School_Button.style.height= "35px";
                                    
                                 
                               School_Button.onclick=function(e) {                 //disables every school button that is not the                                                               //one currently selected. Only 1 school shall be                                                             //run at a time
                               
                                   
                                   this.classList.add('clicked')
                                   
                                   var elems = document.querySelectorAll('[id^="Each_"]');
                                    
                                   for (var i = 0; i < elems.length; i++) {
                                        elems[i].disabled = true;
                                            } 
                                       
                                    
                                        this.style.borderStyle = (this.style.borderStyle!=='inset' ? 'inset' : 'outset');
                                        this.style.borderColor = "#89CFF0";
                                        this.style.color = "#89CFF0";
                                        
                                   
                                 
                                        
                                        setTimeout(function() {                             //Pushes user to next "class" tab after                                                           //selecting school
                                            $("#mate").removeClass('active');
                                            $("#school_content").removeClass('active');
                                            $("#jumpHere").addClass('active');
                                            $("#class_buttons").addClass('active');
                                          
                                            }, 1000);
                                    };
                                          
                                    list.append(School_Button);
                                        ;});
                                   
                                       
                                    list.addEventListener('click', function onClick() {
                                            btn.style.backgroundColor = '#5cbdea';
                                            btn.style.borderColor = 'white';
                                            btn.onclick = function() {
                                                const recruits = document.querySelectorAll("[class='clicked']");
                                                //queryData
                                                let recruitsstring = [];
                                                recruits.forEach(recruit => recruitsstring.push(recruit.parentNode.id +'&&'+ recruit.innerHTML));
                                                const returnData = parse_data(recruitsstring);
                                                const headers = {
                                                    headers: {
                                                        "content-type": "application/json; charset=UTF-8", 
                                                        "Access-Control-Allow-Origin": '*',
                                                        "Access-Control-Allow-Headers": 'Origin, X-Requested-With, Content-Type, Accept',
                                                    }, 
                                                    body: JSON.stringify(returnData), 
                                                    method: "POST"
                                                };
                                                
                                                fetch('http://127.0.0.1:1130/recruit_data', headers)   
                                                .then(data=>{return(data.json())})
                                                .then(res=>{console.log(res)})
                                                .catch(error=>console.log(error))
                                                //const DB_Data = makeHttpRequest('http://127.0.0.1:1130/recruit_data', 'POST', returnData);
                                                //console.log(DB_Data);
                    
                                                                     }
                                                                }           
                                                         
                                                         )
                                                                      
                                                                      
                                                    }
                                        
                                     

                                   