function ConvertRank(input){
    const num = parseInt(input);
    if (num == 2) {
        return  [0,0.75]
    };
    if (num == 3) {
        return [0.750000001, .85]
    };
    if (num == 4) {
        return [.8500000001, .95]
    }
    if (num == 5) {
        return [.9500000001, 1.1]
        
    }
};
