function parse_data(recruits) {
 let UserRequest =
     {
    "colleges":[],
     
    "years":[],
         
    "ranks":[],
         
    "states":[]
}

 for (let i= 0; i < recruits.length; i++){
     const recruit = String(recruits[i]);
    if (recruit.includes('School_Tab')) {
       const School = recruit.split('&&')[1];
       UserRequest.colleges.push(School);
    }
     
    else if (recruit.includes('Year_Tab')) {
       const Year = recruit.split('&&')[1];
       UserRequest.years.push(parseInt(Year));
    }
     
    else if (recruit.includes('Rank_Tab')) {
       const Rank = recruit.split('&&')[1].split(' ')[0];
       const ConvertedRank = ConvertRank(Rank);
       UserRequest.ranks.push(...ConvertedRank);
    }
     
    else if (recruit.includes('State_Tab')) {
       const State = recruit.split('&&')[1];
       UserRequest.states.push(State);
    }
     else {console.log(recruit)};
 };
    return UserRequest;
};

