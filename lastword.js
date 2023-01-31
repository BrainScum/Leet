/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const regexp = /\w+$|(\w+\s+$)/gi;
    let word = (String(s.match(regexp)).trim());

    return word.length;
};

console.log((lengthOfLastWord("b   a    ")));