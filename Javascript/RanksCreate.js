function createRanks() {

let Rank_list = document.getElementById("Rank_Tab");        //ingests list of schools from all_schools.js
                               
                                star_rankings.forEach((star_ranking) => {                 // Setting up process to create buttons for every                                                            schoool listed
                                    
                                let Rank_Button = document.createElement("button");   
                                    Rank_Button.innerText = star_ranking;
                                    Rank_Button.style.color = 'white';
                                    Rank_Button.style.backgroundColor= '#191a1d';
                                    Rank_Button.style.width= "155%";
                                    Rank_Button.style.height= "20vh";
                                 
                            
                                
                                    
                                     
                                    Rank_Button.onclick=function(e) {                 //disables every school button that is not the                                                       //one currently selected. Only 1 school shall be                                                     //run at a time
                                        
                                        
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
                                
                                    Rank_list.append(Rank_Button);
                                
                                });
                                
                                }