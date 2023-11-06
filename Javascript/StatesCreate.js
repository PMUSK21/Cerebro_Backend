function createStates() {

let State_list = document.getElementById("State_Tab");        //ingests list of schools from all_schools.js
                               
                                state_names.forEach((state_name) => {                 // Setting up process to create buttons for every                                                            schoool listed
                                    
                                let State_Button = document.createElement("button");   
                                    State_Button.innerText = state_name;
                                    State_Button.style.color = 'white';
                                    State_Button.style.backgroundColor= '#191a1d';
                                    State_Button.style.width= "100%";
                                    State_Button.style.height= "35px";
                                     
                                    State_Button.onclick=function(e) {                 //disables every school button that is not the                                                       //one currently selected. Only 1 school shall be                                                     //run at a time
                                        
                                        
                                        if (jQuery(this).hasClass('clicked')) {
                                                (jQuery(this).removeClass('clicked'));
                                                this.style.color = 'white';
                                                this.style.borderStyle = (this.style.borderStyle!=='outset' ? 'outset' : 'inset');
                                                this.style.borderColor = 'grey';
                                        }
                                        
                                        else{
                                        
                                        
                                        (jQuery(this).addClass('clicked'));
                                        this.style.borderStyle = (this.style.borderStyle!=='inset' ? 'inset' : 'outset');
                                        this.style.borderColor = "#89CFF0";
                                        this.style.color = "#89CFF0";
                                        
                                        
                                        };
                                        
                                    };
                                
                                    State_list.append(State_Button);
                                
                                });
                                
                                }