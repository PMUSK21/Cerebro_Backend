function createYears() {

let Year_list = document.getElementById("Year_Tab");        //ingests list of schools from all_schools.js
                               
                                year_names.forEach((year_name) => {                 // Setting up process to create buttons for every                                                            schoool listed
                                    
                                let Year_Button = document.createElement("button");   
                                    Year_Button.innerText = year_name;
                                    Year_Button.style.color = 'white';
                                    Year_Button.style.backgroundColor= '#191a1d';
                                    Year_Button.style.width= "100%";
                                    Year_Button.style.height= "35px";
                                     
                                    Year_Button.onclick=function(e) {                 //disables every school button that is not the                                                       //one currently selected. Only 1 school shall be                                                     //run at a time
                                        
                                        
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
                                
                                    Year_list.append(Year_Button);
                                
                                });
                                
                                }
                                        