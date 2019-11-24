
function findOdds(arr){
    let result = [];
    function helper(inputArray) {
        if (inputArray.length === 0) {
        return;
        }

        if (inputArray[0] % 2 !== 0) {
        result.push(inputArray[0]);
        }
        helper(inputArray.slice(1));
    }
    helper(arr)
    return result;
}
const arr = [1, 2, 3, 4, 1, 1, 5, 2]

const result = findOdds(arr);
console.log(result)