let numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];

function solution(numbers, hand) {
    var answer = '';

    // 키패드의 위치를 미리 저장 
    let pad = {
        1:[1,1],2:[1,2],3:[1,3],
        4:[2,1],5:[2,2],6:[2,3],
        7:[3,1],8:[3,2],9:[3,3],
        '*':[4,1],0:[4,2],'#':[4,3]
    };

    // 왼손과 오른손의 위치
    let cur_L = [4,1];
    let cur_R = [4,3];
    numbers.forEach(number =>{
        let target = pad[number];   // 누르고자 하는 버튼
        
        if(target[1] === 1){ // 무조건 왼손일 때
            cur_L = target;
            answer += "L";
        } else if(target[1] === 3){ //무조건 오른손
            cur_R = target;
            answer += "R";
        } else{
            // 거리 비교가 필요
            let dist_L = Math.abs(target[0]-cur_L[0]) + Math.abs(target[1]-cur_L[1]);
            let dist_R = Math.abs(target[0]-cur_R[0]) + Math.abs(target[1]-cur_R[1]);
            if(dist_L<dist_R){
                cur_L = target;
                answer += "L"
            }else if(dist_L>dist_R){
                cur_R = target;
                answer += "R"
            }else {
                if(hand==="right"){
                    cur_R = target;
                    answer += "R";
                }else{
                    cur_L = target;
                    answer += "L";
                }
            }
        }
    }
    );
    return answer;
};

console.log(solution(numbers1,"right"));