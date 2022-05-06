let numbers1 =[4, 1, 2, 1];


function solution(numbers, target) {
    var answer = 0;
    n = numbers.length;
    function dfs(lv, total) {
        if(lv === n){
            if(total === target){
                answer += 1;
            }
            return;
        } else{
            dfs(lv+1,total+numbers[lv]);
            dfs(lv+1,total-numbers[lv]);
        }
    }
    dfs(0,0);
    return answer;
}

console.log(solution(numbers1,4));